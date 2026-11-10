#!/usr/bin/env python3
"""Read-only checks for the Mirket registry and local Hindsight daemon."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

from install import HOOKS, codex_mcp
import project_registry as registry


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def request(base, path, body=None):
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(base + path, data=data, headers={"Content-Type": "application/json"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    with opener.open(request, timeout=12) as response:
        return json.load(response)


def walk_pages(nodes):
    for page in nodes:
        if page.get("kind") == "page":
            yield page
        yield from walk_pages(page.get("children", []))


def primary_session_ids(codex_home, project):
    """Count only primary interactive sessions; inspect their metadata, not their messages."""
    found, roots = set(), {}
    for folder in ("sessions", "archived_sessions"):
        for path in (codex_home / folder).rglob("*.jsonl"):
            try:
                with path.open(encoding="utf-8") as stream:
                    record = json.loads(stream.readline(1024 * 1024))
                if record.get("type") != "session_meta":
                    continue
                meta = record["payload"]
                if meta.get("source") not in ("vscode", "cli") or not isinstance(meta.get("id"), str):
                    continue
                cwd = meta.get("cwd")
                if not isinstance(cwd, str) or not cwd:
                    continue
                if cwd not in roots:
                    try:
                        roots[cwd] = registry.project_root(cwd)
                    except (ValueError, OSError, subprocess.SubprocessError):
                        roots[cwd] = None
                if roots[cwd] == project:
                    found.add(meta["id"])
            except (ValueError, OSError, TypeError, AttributeError, KeyError):
                continue
    return found


def document_ids(base, path, tag):
    offset = 0
    while True:
        params = urllib.parse.urlencode({"tags": tag, "limit": 100, "offset": offset})
        response = request(base, path + "/documents?" + params)
        rows = response["items"]
        yield from (row["id"] for row in rows)
        offset += len(rows)
        if not rows or offset >= response["total"]:
            break


def inspect(home, directory, query=None):
    root = home / ".hindsight"
    managed = root / "mirket/project_registry.py"
    runtime = root / "coding-agents"
    config = json.loads((root / "coding-agent.json").read_text())
    version = json.loads((runtime / "package.json").read_text())["version"]
    registry.check_config(config, version)
    overrides = config["harnesses"]["codex"]
    effective = {**config, **overrides}
    project = registry.project_root(directory)
    state = root / "mirket/projects.json"
    projects = json.loads(state.read_text())["projects"] if state.exists() else {}
    mappings = {str(Path(path).expanduser().resolve()): value for path, value in config.get("mapPathToBank", {}).items()}
    if str(project) in mappings and str(project) in projects and mappings[str(project)] != projects[str(project)]:
        raise ValueError("Project registry conflicts with the explicit map.")
    bank = projects.get(str(project), mappings.get(str(project))) or "coding-agent::project-" + hashlib.sha256(os.fsencode(project)).hexdigest()
    connection = {"serverMode", "apiUrl", "apiPort", "apiToken"}
    if effective.get("serverMode") != "daemon" or effective.get("apiUrl") or effective.get("apiToken") or any(
        connection.intersection(value)
        for source in (config, overrides) for group in ("paths", "banks") for value in source.get(group, {}).values()
        if isinstance(value, dict)
    ):
        raise ValueError("This doctor only probes the default unauthenticated local daemon; check overridden endpoints separately.")
    port = int(effective.get("apiPort", 9077))
    base = f"http://127.0.0.1:{port}"
    path = "/v1/default/banks/" + urllib.parse.quote(bank, safe="")
    if query:
        return request(base, path + "/memories/recall", {
            "query": query, "budget": "low", "max_tokens": 2000,
            "tags": ["source:chat"], "tags_match": "all_strict",
        })["results"]
    hooks = json.loads((home / ".codex/hooks.json").read_text())["hooks"]
    wired = {event: any(
        shlex.split(item.get("command", ""))[-2:] == [str(managed), mode]
        for group in hooks.get(event, []) for item in group.get("hooks", [])
    ) for event, mode in HOOKS.items()}
    server = codex_mcp() or {}
    mcp = server.get("transport", {})
    env = mcp.get("env") or {}
    mcp_wired = (server.get("enabled") is True and mcp.get("args") == [str(managed), "mcp"] and
                 env.get("HINDSIGHT_MCP_HARNESS") == "codex")
    dist = runtime / "dist"
    patched = all((dist / name).is_file() and (dist / name).read_text() == value
                  for name, value in registry.adapters(dist).items())
    source_current = managed.is_file() and managed.read_bytes() == Path(registry.__file__).read_bytes()
    health = request(base, "/health")
    stats = request(base, path + "/stats")
    pages = list(walk_pages(request(base, path + "/knowledge-base/tree").get("roots", [])))
    tags = ("source:chat", "source:git-log", "source:git-diff", "source:survey-baseline")
    counts = {tag: request(base, path + "/documents?" + urllib.parse.urlencode({"tags": tag, "limit": 1}))["total"] for tag in tags}
    surveys = {doc["id"] for doc in request(base, path + "/documents?limit=100&q=repository-")["items"]
               if doc["id"] in {"repository-component-map", "repository-core-concepts",
                                "repository-conventions-and-patterns", "repository-tech-stack-and-features"}}
    primary = primary_session_ids(home / ".codex", project)
    retained = {doc.partition(":")[2] for doc in document_ids(base, path, "source:chat")
                if doc.startswith(("conversation:", "chat:"))}
    return {
        "bank": bank, "workspace": str(project), "runtime": version,
        "hooks_wired": wired, "mcp_wired": mcp_wired, "survey_adapter_current": patched,
        "installed_registry_current": source_current, "daemon_reachable": health.get("status") == "healthy",
        "auto_inject": effective.get("autoInject", "reflect"),
        "git_ingestion": effective.get("gitIngest", "message"),
        "opt_in_only": effective.get("optInOnly", False),
        "documents": stats["total_documents"], "source_counts": counts, "survey_findings": len(surveys),
        "local_primary_sessions": len(primary), "primary_sessions_missing_from_bank": len(primary - retained),
        "page_count": len(pages), "stale_pages": sum(bool(p.get("is_stale")) for p in pages),
        "pages_with_refresh_failure": sum(bool(p.get("last_refresh_failed_at")) for p in pages),
        "pending_operations": stats["pending_operations"],
        "historical_failed_operations": stats["failed_operations"],
        "last_memory_write": stats.get("last_memory_write_at"),
        "live_host_capture_verified_by_doctor": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", default=".")
    parser.add_argument("--recall-chat", help="retrieve matching raw chat evidence from the resolved bank")
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(Path.home(), args.directory, args.recall_chat), indent=2))
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as exc:
        print(f"Hindsight doctor: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
