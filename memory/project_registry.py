#!/usr/bin/env python3
"""Route Codex Hindsight processes to a unique local bank per project root."""

import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

VERSION = "0.8.6"
SCRIPTS = {
    "start": "codex-sessionstart-hook.js",
    "prompt": "codex-hook.js",
    "stop": "codex-stop-hook.js",
    "mcp": "mcp-server.js",
}


def identify_project(directory):
    root = Path(directory).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Workspace is not a directory")
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env["LC_ALL"] = "C"
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--path-format=absolute", "--show-toplevel", "--git-common-dir", "--is-bare-repository"],
        capture_output=True, text=True, env=env, timeout=10,
    )
    if result.returncode:
        if "not a git repository" in result.stderr.lower():
            for directory in (root, *root.parents):
                marker = directory / ".git"
                if marker.exists() or marker.is_symlink():
                    raise ValueError("Git metadata exists but could not be read; memory was skipped")
            return root, False
        raise ValueError("Git could not identify the project; memory was skipped")
    lines = result.stdout.splitlines()
    if len(lines) != 3:
        raise ValueError("Unexpected Git project identity")
    worktrees = subprocess.run(
        ["git", "-C", str(root), "worktree", "list", "--porcelain", "-z"],
        capture_output=True, env=env, timeout=10,
    )
    first = worktrees.stdout.split(b"\0", 1)[0]
    if worktrees.returncode or not first.startswith(b"worktree "):
        raise ValueError("Git could not identify the main project directory")
    return Path(os.fsdecode(first[len(b"worktree "):])).resolve(strict=True), True


def project_root(directory):
    return identify_project(directory)[0]


def hook_root(event):
    cwd = event.get("cwd")
    if not isinstance(cwd, str) or not cwd:
        raise ValueError("Hook event has no workspace directory")
    root, is_git = identify_project(cwd)
    session_id = event.get("session_id")
    if not isinstance(session_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", session_id):
        raise ValueError("Hook event has no valid session ID")
    root_file = Path(tempfile.gettempdir()) / "hindsight-codex" / (session_id + ".root")
    if root_file.is_file():
        session_dir = Path(root_file.read_text(encoding="utf-8").strip()).resolve(strict=True)
        session_root, session_is_git = identify_project(session_dir)
        if is_git or session_is_git:
            if is_git and session_is_git and root == session_root:
                return root
        elif root == session_root or session_root in root.parents:
            return session_root
        raise ValueError("Project changed during the session; start a new session for memory")
    if event.get("hook_event_name") == "SessionStart":
        return root
    raise ValueError("Cannot establish the session root; memory was skipped")


def check_config(config, version):
    if version != VERSION:
        raise ValueError(f"Unsupported Hindsight runtime version: {version}")
    codex = config.get("harnesses", {}).get("codex", {})
    if not isinstance(codex, dict) or codex.get("mapPathToBank") != {} or codex.get("autoUpdate") is not False:
        raise ValueError("Codex directory isolation is not configured or runtime updates are not pinned")
    if any(key in source for source in (config, codex) for key in ("bankId", "dynamicBankId")):
        raise ValueError("Conflicting Hindsight bank settings")
    for source in (config, codex):
        for group in (source.get("banks", {}), source.get("paths", {})):
            if not isinstance(group, dict) or any(isinstance(value, dict) and "bank" in value for value in group.values()):
                raise ValueError("Hindsight bank alias may redirect project memory")


def register(state_dir, root, mappings):
    state_dir = Path(state_dir)
    state_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    if state_dir.is_symlink():
        raise ValueError("Registry directory cannot be a symlink")
    lock_path = state_dir / "projects.lock"
    fd = os.open(str(lock_path), os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
    with os.fdopen(fd, "a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        path = state_dir / "projects.json"
        if path.is_symlink():
            raise ValueError("Registry cannot be a symlink")
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, OSError) as exc:
                raise ValueError("Cannot safely read project registry") from exc
            if not isinstance(data, dict) or data.get("version") != 1 or not isinstance(data.get("projects"), dict):
                raise ValueError("Invalid project registry")
            projects = data["projects"]
        else:
            projects = {}
        for directory, bank in mappings.items():
            key = str(Path(directory).expanduser().resolve())
            if not isinstance(bank, str) or not bank or (key in projects and projects[key] != bank):
                raise ValueError("Conflicting legacy project mapping")
            projects[key] = bank
        if any(not isinstance(k, str) or not isinstance(v, str) or not v for k, v in projects.items()):
            raise ValueError("Invalid project registry entries")
        if len(set(projects.values())) != len(projects):
            raise ValueError("One bank is assigned to multiple project directories")
        key = str(Path(root).resolve(strict=True))
        if key not in projects:
            projects[key] = "coding-agent::project-" + hashlib.sha256(os.fsencode(key)).hexdigest()
        if len(set(projects.values())) != len(projects):
            raise ValueError("One bank is assigned to multiple project directories")
        fd, name = tempfile.mkstemp(prefix=".projects-", dir=state_dir)
        try:
            os.fchmod(fd, 0o600)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump({"version": 1, "projects": projects}, f, indent=2)
                f.write("\n")
            os.replace(name, path)
        finally:
            if os.path.exists(name):
                os.unlink(name)
        return projects[key]


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in SCRIPTS:
        raise ValueError("Expected one of: start, prompt, stop, mcp")
    mode = sys.argv[1]
    root = Path.home() / ".hindsight"
    runtime = root / "coding-agents"
    version = json.loads((runtime / "package.json").read_text(encoding="utf-8")).get("version")
    if os.environ.get("HINDSIGHT_CONFIG"):
        raise ValueError("Alternate Hindsight config is not supported by project isolation")
    config = json.loads((root / "coding-agent.json").read_text(encoding="utf-8"))
    check_config(config, version)
    if mode == "mcp":
        if os.environ.get("HINDSIGHT_MCP_HARNESS") != "codex":
            raise ValueError("Expected the Codex MCP harness")
        cwd = os.environ.get("HINDSIGHT_MCP_PROJECT_CWD") or os.getcwd()
        project = project_root(cwd)
    else:
        raw = sys.stdin.buffer.read()
        event = json.loads(raw)
        project = hook_root(event)
        # An anonymous file forwards exactly the original bytes without pipe-buffer deadlocks.
        temp = tempfile.TemporaryFile()
        temp.write(raw)
        temp.seek(0)
        os.dup2(temp.fileno(), 0)
    bank = register(root / "mirket", project, config.get("mapPathToBank", {}))
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(HINDSIGHT_BANK_ID=bank, HINDSIGHT_DYNAMIC_BANK_ID="false")
    node = shutil.which("node")
    if not node:
        raise ValueError("Node is unavailable to the Hindsight registry")
    os.execvpe(node, [node, str(runtime / "dist" / SCRIPTS[mode])], env)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print("Hindsight project isolation skipped: " + str(exc), file=sys.stderr)
        sys.exit(1)
