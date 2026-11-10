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
SURVEY_ENTRY = "mirket-codex-sessionstart-hook.js"
PROMPT_ENTRY = "mirket-codex-hook.js"
DEEPEN_ENTRY = "mirket-deepen.js"
SURVEY_COMMAND = '`mcp_servers.hindsight.command="node"`'
SURVEY_ARGS = '`mcp_servers.hindsight.args=${tomlValue([opts.mcpServerPath])}`'
SURVEY_RECEIPT = "SURVEY_DOC_IDS.some((id) => uploads.has(id))"
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


def atomic_text(path, text):
    fd, name = tempfile.mkstemp(prefix=".mirket-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def survey_source(source):
    """Adapt only the audited Codex survey recipe, failing on runtime drift."""
    if source.count(SURVEY_COMMAND) != 1 or source.count(SURVEY_ARGS) != 1:
        raise ValueError("Unsupported Hindsight Codex survey recipe")
    return deepen_launcher(survey_receipts(source)).replace(
        SURVEY_COMMAND, '`mcp_servers.hindsight.command=${tomlValue(process.env.MIRKET_HINDSIGHT_PYTHON)}`'
    ).replace(
        SURVEY_ARGS, '`mcp_servers.hindsight.args=${tomlValue([process.env.MIRKET_HINDSIGHT_REGISTRY, "mcp"])}`,\n'
        '          "-c",\n'
        '          `mcp_servers.hindsight.env.MIRKET_HINDSIGHT_EXPECTED_BANK=${tomlValue(process.env.HINDSIGHT_BANK_ID)}`,\n'
        '          "-c",\n'
        '          `mcp_servers.hindsight.env.PATH=${tomlValue(process.env.PATH)}`'
    )


def survey_receipts(source):
    if source.count(SURVEY_RECEIPT) != 1:
        raise ValueError("Unsupported Hindsight survey receipt check")
    return source.replace(SURVEY_RECEIPT, SURVEY_RECEIPT.replace(".some(", ".every("))


def deepen_launcher(source):
    marker = 'join5(dirname4(fileURLToPath(import.meta.url)), "deepen.js")'
    if source.count(marker) != 1:
        raise ValueError("Unsupported Hindsight background worker launcher")
    return source.replace(marker, marker.replace("deepen.js", DEEPEN_ENTRY))


def adapters(dist):
    return {
        SURVEY_ENTRY: survey_source((dist / SCRIPTS["start"]).read_text()),
        PROMPT_ENTRY: deepen_launcher((dist / SCRIPTS["prompt"]).read_text()),
        DEEPEN_ENTRY: survey_receipts((dist / "deepen.js").read_text()),
    }


def transcript_root(event, session_id, codex_home):
    supplied = event.get("transcript_path")
    if not isinstance(supplied, str) or not supplied:
        return None
    path = Path(supplied).resolve()
    if path.suffix != ".jsonl" or not any(
        (codex_home / folder).resolve() in path.parents for folder in ("sessions", "archived_sessions")
    ):
        raise ValueError("Cannot verify the Codex transcript location")
    if not path.is_file():
        return None
    with path.open(encoding="utf-8") as stream:
        line = stream.readline(1024 * 1024)
    if not line:
        return None
    meta = json.loads(line)
    payload = meta.get("payload") if isinstance(meta, dict) and meta.get("type") == "session_meta" else None
    if not isinstance(payload, dict) or payload.get("id") != session_id or not isinstance(payload.get("cwd"), str):
        raise ValueError("Transcript does not match the Codex session")
    return identify_project(payload["cwd"])


def hook_root(event, state_dir=None, codex_home=None):
    cwd = event.get("cwd")
    if not isinstance(cwd, str) or not cwd:
        raise ValueError("Hook event has no workspace directory")
    root, is_git = identify_project(cwd)
    session_id = event.get("session_id")
    if not isinstance(session_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", session_id):
        raise ValueError("Hook event has no valid session ID")
    root_file = Path(tempfile.gettempdir()) / "hindsight-codex" / (session_id + ".root")
    def resolve(binding):
        if binding and binding.is_file():
            recorded = json.loads(binding.read_text(encoding="utf-8"))
            if not isinstance(recorded, dict) or not isinstance(recorded.get("root"), str) or not isinstance(recorded.get("git"), bool):
                raise ValueError("Invalid persisted Codex session binding")
            original = Path(recorded["root"]), recorded["git"]
        elif codex_home and (original := transcript_root(event, session_id, codex_home)):
            pass
        elif root_file.is_file() and not root_file.is_symlink() and root_file.stat().st_uid == os.getuid():
            original = identify_project(root_file.read_text(encoding="utf-8").strip())
        elif event.get("hook_event_name") == "SessionStart":
            original = root, is_git
        else:
            raise ValueError("Cannot establish the session root; memory was skipped")
        session_root, session_is_git = original
        if (is_git or session_is_git) and not (is_git and session_is_git and root == session_root):
            raise ValueError("Project changed during the session; start a new session for memory")
        if not (is_git or session_is_git) and not (root == session_root or session_root in root.parents):
            raise ValueError("Project changed during the session; start a new session for memory")
        if binding and not binding.exists():
            atomic_text(binding, json.dumps({"root": str(session_root), "git": session_is_git}) + "\n")
        return session_root

    if state_dir is None:
        return resolve(None)
    sessions = state_dir / "sessions"
    sessions.mkdir(mode=0o700, parents=True, exist_ok=True)
    if state_dir.is_symlink() or sessions.is_symlink():
        raise ValueError("Session binding directory cannot be a symlink")
    binding = sessions / (session_id + ".json")
    lock = os.open(sessions / "bindings.lock", os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    with os.fdopen(lock, "r+") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        if binding.is_symlink():
            raise ValueError("Session binding cannot be a symlink")
        return resolve(binding)


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


def register(state_dir, root, mappings, expected_bank=None):
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
        if expected_bank and projects[key] != expected_bank:
            raise ValueError("Survey MCP resolved a different bank; no memory was written")
        updated = {"version": 1, "projects": projects}
        if not path.exists() or json.loads(path.read_text(encoding="utf-8")) != updated:
            atomic_text(path, json.dumps(updated, indent=2) + "\n")
        return projects[key]


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in SCRIPTS:
        raise ValueError("Expected one of: start, prompt, stop, mcp")
    mode = sys.argv[1]
    if mode != "mcp" and os.environ.get("HINDSIGHT_DISABLE_HOOKS"):
        return
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
        project = hook_root(event, root / "mirket", Path.home() / ".codex")
        # An anonymous file forwards exactly the original bytes without pipe-buffer deadlocks.
        temp = tempfile.TemporaryFile()
        temp.write(raw)
        temp.seek(0)
        os.dup2(temp.fileno(), 0)
    bank = register(root / "mirket", project, config.get("mapPathToBank", {}),
                    os.environ.get("MIRKET_HINDSIGHT_EXPECTED_BANK"))
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(HINDSIGHT_BANK_ID=bank, HINDSIGHT_DYNAMIC_BANK_ID="false")
    node = shutil.which("node")
    if not node:
        raise ValueError("Node is unavailable to the Hindsight registry")
    entry = SCRIPTS[mode]
    if mode == "start":
        entry = SURVEY_ENTRY
        env.update(MIRKET_HINDSIGHT_PYTHON=sys.executable, MIRKET_HINDSIGHT_REGISTRY=str(Path(__file__).resolve()))
    elif mode == "prompt":
        entry = PROMPT_ENTRY
    os.execvpe(node, [node, str(runtime / "dist" / entry)], env)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print("Hindsight project isolation skipped: " + str(exc), file=sys.stderr)
        sys.exit(1)
