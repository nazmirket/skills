#!/usr/bin/env python3
"""Install Hindsight's Codex integration in its normal user-level locations."""

import argparse
import json
import os
from pathlib import Path
import platform
import re
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


def launcher(command):
    """Read a literal executable and environment; refuse shell behavior we cannot preserve."""
    if not isinstance(command, str) or any(char in command for char in "\n\r$`"):
        raise ValueError("Ambiguous Hindsight hook command; preserve and review it before wiring")
    tokens = shlex.split(command)
    values = {}
    if tokens and tokens[0] in ("env", "/usr/bin/env", "/bin/env"):
        tokens.pop(0)
        if tokens and tokens[0] == "--":
            tokens.pop(0)
    while tokens and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tokens[0]):
        key, value = tokens.pop(0).split("=", 1)
        values[key] = value
    if not tokens or any(token in {";", "&&", "||", "|", ">", "<", "&"} for token in tokens):
        raise ValueError("Unsupported Hindsight hook wrapper or compound command")
    return tokens, values


def validate_environment(values):
    if not isinstance(values, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in values.items()):
        raise ValueError("Hindsight environment must contain string values")
    if any(key in values for key in ("HINDSIGHT_CONFIG", "HINDSIGHT_BANK_ID", "HINDSIGHT_DYNAMIC_BANK_ID", "HINDSIGHT_MCP_PROJECT_CWD")):
        raise ValueError("Review custom Hindsight configuration or routing overrides before wiring")


def runtime_toml(text, dist):
    """Python 3.8 fallback: reuse the parser bundled in the pinned installer."""
    source = (dist / "installer.js").read_text()
    markers = ('function parse2(toml, options = {})', 'if (isMain || mainPath?.endsWith("installer.js"))')
    if any(source.count(marker) != 1 for marker in markers):
        raise ValueError("Unsupported bundled TOML parser; configuration was not changed")
    with tempfile.TemporaryDirectory(prefix="mirket-toml-") as temporary:
        module = Path(temporary) / "parser.mjs"
        module.write_text(source + "\nexport {parse2 as parseMirketToml};\n")
        script = ('const {parseMirketToml}=await import(process.argv[1]); '
                  'const {readFileSync}=await import("node:fs"); '
                  'console.log(JSON.stringify(parseMirketToml(readFileSync(0,"utf8"))));')
        result = subprocess.run(["node", "--input-type=module", "-e", script, module.as_uri()],
                                input=text, capture_output=True, text=True, check=True, timeout=10)
        return json.loads(result.stdout)


def plain_upstream_mcp(home, dist, transport):
    """The CLI's list projection omits restrictions: inspect raw TOML before replacement."""
    try:
        text = (home / ".codex/config.toml").read_text()
        try:
            import tomllib
        except ImportError:
            parsed = runtime_toml(text, dist)
        else:
            parsed = tomllib.loads(text)
        entry = parsed.get("mcp_servers", {}).get("hindsight")
    except (ValueError, OSError, subprocess.SubprocessError):
        raise ValueError("Cannot safely inspect the raw Codex MCP configuration; no settings were changed") from None
    if not isinstance(entry, dict) or set(entry) - {"command", "args", "env", "enabled"}:
        raise ValueError("Custom Hindsight MCP options require review; automatic conversion would drop tool restrictions, timeouts or other fields")
    if entry.get("enabled", True) is not True:
        raise ValueError("The raw Hindsight MCP entry is disabled; preserve that choice")
    if any(entry.get(key) != transport.get(key) for key in ("command", "args")) or (entry.get("env") or {}) != (transport.get("env") or {}):
        raise ValueError("Raw and effective MCP settings differ; review configuration layers before wiring")


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
        tokens, existing_env = launcher(entry["command"])
        validate_environment(existing_env)
        if tokens[1:] == [str(dist / registry.SCRIPTS[mode])] and Path(tokens[0]).name in ("node", "nodejs"):
            hook_env = {k: v for k, v in env.items() if k != "HINDSIGHT_MCP_HARNESS"}
            hook_env.update(existing_env)
            entry["command"] = shlex.join(
                ["/usr/bin/env", *(f"{k}={v}" for k, v in hook_env.items()),
                 sys.executable, str(managed), mode]
            )
        elif tokens[1:] != [str(managed), mode] or not Path(tokens[0]).name.startswith("python"):
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
    if already_wired and not Path(transport.get("command") or "").name.startswith("python"):
        raise ValueError("Unexpected executable for the registry MCP entry")
    if server.get("enabled") is False:
        raise ValueError("The existing Hindsight MCP entry is disabled; preserve that choice")
    if not already_wired and (Path(transport.get("command") or "").name not in ("node", "nodejs") or
                              transport.get("env_vars") or transport.get("cwd")):
        raise ValueError("Review customized upstream MCP launch settings before wiring")
    existing_env = transport.get("env") or {}
    validate_environment(existing_env)
    env.update(existing_env)
    env["HINDSIGHT_MCP_HARNESS"] = "codex"
    if not already_wired:
        plain_upstream_mcp(home, dist, transport)
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
            subprocess.run(cmd + ["--", sys.executable, str(managed), "mcp"], check=True, capture_output=True, text=True)
    except (OSError, subprocess.SubprocessError):
        for path, old in originals.items():
            if old is None:
                path.unlink(missing_ok=True)
            else:
                registry.atomic_text(path, old)
        raise
    return backup


def freshness_profile(home, directory):
    """Opt one already-authorized project into prompt freshness; never widen capture."""
    root = home / ".hindsight"
    config_path = root / "coding-agent.json"
    if config_path.is_symlink():
        raise ValueError("Cannot replace a symlinked Hindsight configuration")
    config = json.loads(config_path.read_text())
    registry.check_config(config, json.loads((root / "coding-agents/package.json").read_text())["version"])
    project = registry.project_root(directory)
    bank, _ = registry.resolve_bank(project, config.get("mapPathToBank", {}), registry.read_projects(root / "mirket"))
    server = codex_mcp() or {}
    transport = server.get("transport", {})
    if server.get("enabled") is False or transport.get("args") != [str(root / "mirket/project_registry.py"), "mcp"]:
        raise ValueError("Wire and enable the recognized registry before setting project freshness")
    environment = dict(os.environ, **(transport.get("env") or {}))
    effective = registry.effective_config(home, Path(directory).resolve(), bank, environment)
    if effective["disabled"]:
        raise ValueError("This project is not enabled by the current capture policy; freshness does not opt it in")
    codex = config["harnesses"]["codex"]
    # Upstream merges bank names, not each bank's fields. Preserve the complete
    # inherited section before adding a Codex-specific override.
    section = codex.setdefault("banks", {}).setdefault(bank, dict(config.get("banks", {}).get(bank, {})))
    desired = {"surveyRefreshCommits": 1, "pageTriggerType": "auto-refresh", "pageRefreshEveryTurns": 1}
    if all(section.get(key) == value for key, value in desired.items()):
        return {"bank": bank, "changed": False}
    section.update(desired)
    backups = root / "mirket/backups"
    backups.mkdir(mode=0o700, parents=True, exist_ok=True)
    if backups.is_symlink() or backups.parent.is_symlink():
        raise ValueError("Mirket backup directory cannot be a symlink")
    backup = Path(tempfile.mkdtemp(prefix="freshness-", dir=backups))
    registry.atomic_text(backup / config_path.name, config_path.read_text())
    registry.atomic_text(config_path, json.dumps(config, indent=2) + "\n")
    return {"bank": bank, "changed": True, "backup": str(backup), "settings": desired,
            "capture_policy_changed": False, "next_step": "Start a fresh trusted host session, then run the doctor and host capture check."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check prerequisites and existing settings without installing")
    parser.add_argument("--wire", action="store_true", help="wire or update a recognized installed Hindsight runtime without reinstalling it")
    parser.add_argument("--freshness", action="store_true", help="set bounded automatic freshness for one already-enabled project")
    parser.add_argument("--directory", default=".", help="project for --freshness")
    args = parser.parse_args()
    try:
        provider = os.environ.get("HINDSIGHT_API_LLM_PROVIDER")
        if args.freshness:
            if args.check or args.wire:
                parser.error("--freshness, --check and --wire are separate operations")
            if os.environ.get("HINDSIGHT_CONFIG") or os.environ.get("CODEX_HOME") and Path(os.environ["CODEX_HOME"]).resolve() != (Path.home() / ".codex").resolve():
                raise ValueError("Alternate configuration is not supported by the freshness profile")
            print(json.dumps(freshness_profile(Path.home(), args.directory), indent=2))
            return 0
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
    except subprocess.CalledProcessError as exc:
        # argv can contain preserved credential-bearing --env values. Neither it
        # nor the subprocess's output belongs in a user-facing failure message.
        print(f"Hindsight setup stopped: a setup command failed (exit {exc.returncode}); sensitive command details withheld.", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"Hindsight setup stopped: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
