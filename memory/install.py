#!/usr/bin/env python3
"""Install Hindsight's Codex integration in its normal user-level locations."""

import argparse
import json
import os
from pathlib import Path
import platform
import shlex
import shutil
import socket
import subprocess
import sys
import tempfile

try:
    from . import project_registry as registry
except ImportError:
    # Also support direct script invocation and the isolated installer tests.
    import importlib.util
    spec = importlib.util.spec_from_file_location("mirket_project_registry", Path(__file__).with_name("project_registry.py"))
    registry = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(registry)

PACKAGE = "@vectorize-io/hindsight-coding-agents@0.8.6"


def check_requirements():
    required = ["npx", "node", "codex", "uvx"]
    if platform.system() == "Darwin":
        required.append("rustc")
    missing = [name for name in required if not shutil.which(name)]
    if missing:
        raise ValueError("Missing prerequisites: " + ", ".join(missing) + ". See memory/README.md.")


def check_existing(home):
    if os.environ.get("HINDSIGHT_CONFIG"):
        raise ValueError("HINDSIGHT_CONFIG is set; review the alternate Hindsight configuration before installation.")
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home and Path(codex_home).expanduser().resolve() != (home / ".codex").resolve():
        raise ValueError("A custom CODEX_HOME is set; verify upstream installer support before continuing.")
    for path in (home / ".agents/skills/hindsight-coding-agent", home / ".hindsight/coding-agents"):
        if path.exists() or path.is_symlink():
            raise ValueError(f"Existing Hindsight installation already exists: {path}. Review it before continuing.")
    for name in ("coding-agent.json", "codex.json", "claude-code.json", "profiles/coding-agent.env"):
        path = home / ".hindsight" / name
        if path.exists() or path.is_symlink():
            raise ValueError(f"Existing Hindsight configuration already exists: {path}. Review it before using the upstream installer.")
    hooks = home / ".codex/hooks.json"
    if hooks.exists():
        try:
            content = json.loads(hooks.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"Cannot safely read {hooks}: {exc}") from exc
        if not isinstance(content, dict):
            raise ValueError(f"{hooks} must contain a JSON object; preserve and repair it before installation.")
        hook_map = content.get("hooks", {})
        if not isinstance(hook_map, dict) or any(not isinstance(value, list) for value in hook_map.values()):
            raise ValueError(f"{hooks} must contain a hooks object with arrays for events; preserve and repair it before installation.")
    try:
        with socket.create_connection(("127.0.0.1", 9077), timeout=0.5):
            raise ValueError("A service is already listening on 127.0.0.1:9077; inspect it before installation.")
    except OSError:
        pass


def codex_mcp():
    result = subprocess.run(["codex", "mcp", "list", "--json"], check=True, capture_output=True, text=True)
    try:
        servers = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError("Could not inspect the existing Codex MCP configuration.") from exc
    if not isinstance(servers, list) or any(not isinstance(item, dict) or "name" not in item for item in servers):
        raise ValueError("Could not inspect the existing Codex MCP configuration.")
    return next((item for item in servers if item["name"] == "hindsight"), None)


def check_codex_mcp():
    if codex_mcp() is not None:
        raise ValueError("A Hindsight MCP server is already configured in Codex; review it before installation.")


HOOKS = {"SessionStart": "start", "UserPromptSubmit": "prompt", "Stop": "stop"}
FRESHNESS_GUIDE = ("For recent status, decisions or corrections, check the source transcript and current project files "
                   "when a knowledge page is older than the evidence. Use explicit reflection only when it adds value.")
GUIDE = FRESHNESS_GUIDE + " A synced seed does not establish conversation coverage, survey coverage, or page freshness."


def wiring(home, provider=None):
    """Prepare only recognized upstream or Mirket wiring; preserve unrelated settings."""
    root = home / ".hindsight"
    dist = root / "coding-agents/dist"
    managed = root / "mirket/project_registry.py"
    version = json.loads((dist.parent / "package.json").read_text())["version"]
    config_path = root / "coding-agent.json"
    config = json.loads(config_path.read_text())
    codex = config.setdefault("harnesses", {}).setdefault("codex", {})
    if codex.get("mapPathToBank", {}) != {}:
        raise ValueError("Review existing Codex path mappings before enabling the registry.")
    codex.update(mapPathToBank={}, autoUpdate=False, autoInject="pages")
    prior = codex.get("toolGuideExtra", "").strip().split("\n\n")
    codex["toolGuideExtra"] = "\n\n".join(
        [line for line in prior if line and line not in (GUIDE, FRESHNESS_GUIDE)] + [GUIDE]
    )
    registry.check_config(config, version)
    patched = registry.adapters(dist)
    hooks_path = home / ".codex/hooks.json"
    hooks = json.loads(hooks_path.read_text())
    host_path = os.environ.get("PATH", os.defpath)
    env = {"PATH": host_path, "HINDSIGHT_MCP_HARNESS": "codex"}
    if provider:
        env["HINDSIGHT_API_LLM_PROVIDER"] = provider
    for event, mode in HOOKS.items():
        records = [entry for group in hooks["hooks"].get(event, []) for entry in group.get("hooks", [])
                   if str(managed) in shlex.split(entry.get("command", "")) or
                   str(dist / registry.SCRIPTS[mode]) in shlex.split(entry.get("command", ""))]
        if len(records) != 1:
            raise ValueError(f"Expected one recognized Hindsight hook for {event}")
        entry = records[0]
        tokens = shlex.split(entry["command"])
        if str(managed) not in tokens:
            entry["command"] = shlex.join(
                ["/usr/bin/env", *(f"{k}={v}" for k, v in env.items() if k != "HINDSIGHT_MCP_HARNESS"),
                 sys.executable, str(managed), mode]
            )
        elif tokens[-2:] != [str(managed), mode]:
            raise ValueError(f"Unexpected registry command for {event}")
    return config, hooks, patched, env


def wire(home, provider=None):
    if os.environ.get("HINDSIGHT_CONFIG") or (
        os.environ.get("CODEX_HOME") and Path(os.environ["CODEX_HOME"]).resolve() != (home / ".codex").resolve()
    ):
        raise ValueError("Alternate Codex or Hindsight config is not supported by this installer.")
    config, hooks, patched, env = wiring(home, provider)
    root = home / ".hindsight"
    dist = root / "coding-agents/dist"
    managed = root / "mirket/project_registry.py"
    server = codex_mcp()
    transport = (server or {}).get("transport", {})
    args = transport.get("args") or []
    if args not in ([str(managed), "mcp"], [str(dist / registry.SCRIPTS["mcp"])]):
        raise ValueError("Expected the upstream Hindsight or Mirket MCP registration.")
    already_wired = args == [str(managed), "mcp"]
    if already_wired and (server.get("enabled") is False or (transport.get("env") or {}).get("HINDSIGHT_MCP_HARNESS") != "codex"):
        raise ValueError("The existing registry MCP entry is disabled or lacks the Codex harness.")
    managed.parent.mkdir(mode=0o700, exist_ok=True)
    if managed.parent.is_symlink():
        raise ValueError("Mirket installation directory cannot be a symlink.")
    paths = {
        managed: Path(registry.__file__).read_text(),
        **{dist / name: value for name, value in patched.items()},
        root / "coding-agent.json": json.dumps(config, indent=2) + "\n",
        home / ".codex/hooks.json": json.dumps(hooks, indent=2) + "\n",
    }
    changed = {}
    for path, desired in paths.items():
        if path.is_symlink():
            raise ValueError(f"Cannot replace symlink: {path}")
        current = path.read_text() if path.exists() else None
        if path.suffix == ".json" and current is not None and json.loads(current) == json.loads(desired):
            continue
        if current != desired:
            changed[path] = desired
    if not changed and already_wired:
        return None
    if any(path.suffix == ".js" for path in changed):
        for path, content in changed.items():
            if path.suffix == ".js":
                subprocess.run(["node", "--check", "--input-type=module"], input=content, text=True, check=True)
    backups = managed.parent / "backups"
    backups.mkdir(mode=0o700, exist_ok=True)
    if backups.is_symlink():
        raise ValueError("Mirket backup directory cannot be a symlink.")
    backup = Path(tempfile.mkdtemp(prefix="wire-", dir=backups))
    originals = {}
    for path in [*changed, *([] if already_wired else [home / ".codex/config.toml"])]:
        originals[path] = path.read_text() if path.exists() else None
        if originals[path] is not None:
            registry.atomic_text(backup / path.name, originals[path])
    try:
        for path, value in changed.items():
            registry.atomic_text(path, value)
        if not already_wired:
            cmd = ["codex", "mcp", "add", "hindsight"]
            for key, val in env.items():
                cmd += ["--env", f"{key}={val}"]
            subprocess.run(cmd + ["--", sys.executable, str(managed), "mcp"], check=True)
    except (OSError, subprocess.SubprocessError):
        for path, old in originals.items():
            if old is None:
                path.unlink(missing_ok=True)
            else:
                registry.atomic_text(path, old)
        raise
    return backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check prerequisites and existing settings without installing")
    parser.add_argument("--wire", action="store_true", help="wire or update a recognized installed Hindsight runtime without reinstalling it")
    args = parser.parse_args()
    try:
        provider = os.environ.get("HINDSIGHT_API_LLM_PROVIDER")
        if args.wire:
            if args.check:
                parser.error("--check and --wire are mutually exclusive")
            backup = wire(Path.home(), provider)
            print(f"Mirket Hindsight wiring updated; recovery copies: {backup}" if backup else "Mirket Hindsight wiring is current.")
            return 0
        check_requirements()
        check_existing(Path.home())
        check_codex_mcp()
        if not provider:
            raise ValueError("Set HINDSIGHT_API_LLM_PROVIDER explicitly before continuing; see memory/README.md.")
        if args.check:
            print("Preflight passed. This does not verify authentication, provider persistence, hook trust, or recall.")
            return 0
        print("Installing the Codex integration with a local Hindsight daemon; user-level Codex and Hindsight settings will change.", flush=True)
        subprocess.run(["npx", "-y", PACKAGE, "install", "codex", "--server", "daemon"], check=True)
        wire(Path.home(), provider)
        print("Installer finished. Follow memory/README.md to make your provider available to the host, review hooks, and verify capture and recall.")
        return 0
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"Hindsight setup stopped: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
