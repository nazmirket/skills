#!/usr/bin/env python3
"""Install Hindsight's Codex integration in its normal user-level locations."""

import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import socket
import subprocess
import sys

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


def check_codex_mcp():
    result = subprocess.run(["codex", "mcp", "list", "--json"], check=True, capture_output=True, text=True)
    try:
        servers = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError("Could not inspect the existing Codex MCP configuration.") from exc
    if not isinstance(servers, list) or any(not isinstance(item, dict) or "name" not in item for item in servers):
        raise ValueError("Could not inspect the existing Codex MCP configuration.")
    if any(item["name"] == "hindsight" for item in servers):
        raise ValueError("A Hindsight MCP server is already configured in Codex; review it before installation.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check prerequisites and existing settings without installing")
    args = parser.parse_args()
    try:
        check_requirements()
        check_existing(Path.home())
        check_codex_mcp()
        if not os.environ.get("HINDSIGHT_API_LLM_PROVIDER"):
            raise ValueError("Set HINDSIGHT_API_LLM_PROVIDER explicitly before continuing; see memory/README.md.")
        if args.check:
            print("Preflight passed. This does not verify authentication, provider persistence, hook trust, or recall.")
            return 0
        print("Installing the Codex integration with a local Hindsight daemon; user-level Codex and Hindsight settings will change.", flush=True)
        subprocess.run(["npx", "-y", PACKAGE, "install", "codex", "--server", "daemon"], check=True)
        print("Installer finished. Follow memory/README.md to make your provider available to the host, review hooks, and verify capture and recall.")
        return 0
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f"Hindsight setup stopped: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
