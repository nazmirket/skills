#!/usr/bin/env python3
"""Inspect project memory; explicitly request bounded page refresh when needed."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from install import HOOKS, codex_mcp, launcher
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


def documents(base, path, tag):
    offset = 0
    while True:
        params = urllib.parse.urlencode({"tags": tag, "limit": 100, "offset": offset})
        response = request(base, path + "/documents?" + params)
        rows = response["items"]
        yield from rows
        offset += len(rows)
        if not rows or offset >= response["total"]:
            break


def document_ids(base, path, tag):
    return (row["id"] for row in documents(base, path, tag))


def connection(home, directory):
    root = home / ".hindsight"
    managed = root / "mirket/project_registry.py"
    runtime = root / "coding-agents"
    config = json.loads((root / "coding-agent.json").read_text())
    version = json.loads((runtime / "package.json").read_text())["version"]
    registry.check_config(config, version)
    project = registry.project_root(directory)
    bank, _ = registry.resolve_bank(project, config.get("mapPathToBank", {}), registry.read_projects(root / "mirket"))
    server = codex_mcp() or {}
    env = dict(os.environ, **(server.get("transport", {}).get("env") or {}))
    effective = registry.effective_config(home, Path(directory).resolve(), bank, env)
    if effective["disabled"]:
        raise ValueError("This project's memory is disabled by its effective policy; no bank was queried")
    base = effective["apiUrl"]
    if effective["serverMode"] != "daemon" or effective["apiTokenConfigured"] or base != f"http://127.0.0.1:{effective['apiPort']}":
        raise ValueError("This doctor supports an unauthenticated local daemon only; effective endpoint/auth settings require another check")
    path = "/v1/default/banks/" + urllib.parse.quote(bank, safe="")
    return project, bank, effective, server, base, path, version


def git_state(directory, baselines):
    """Compare completed survey receipts with committed source; dirty work is separate."""
    def git(*args):
        env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        result = subprocess.run(["git", "-C", str(directory), *args], env=env, capture_output=True, text=True, timeout=10)
        return result.stdout.strip() if result.returncode == 0 else None
    head = git("rev-parse", "HEAD")
    state = git("status", "--porcelain")
    best = None
    for row in baselines:
        sha = row.get("id", "").partition("survey-baseline:")[2]
        if "survey-state:done" not in row.get("tags", []) or not re.fullmatch(r"[0-9a-f]{40,64}", sha):
            continue
        if git("merge-base", "--is-ancestor", sha, "HEAD") is None:
            continue
        behind = git("rev-list", "--count", sha + "..HEAD")
        if behind is not None and (best is None or int(behind) < best[1]):
            metadata = row.get("document_metadata") or {}
            evidence = "generation_timestamps" if metadata.get("mirket_survey_revision") == sha and metadata.get("mirket_survey_started_at") and metadata.get("mirket_survey_finding_updates") else "legacy_receipt_only"
            best = sha, int(behind), evidence
    return {"head": head, "dirty_worktree": None if state is None else bool(state),
            "completed_survey_baseline": best[0] if best else None,
            "survey_commits_behind": best[1] if best else None,
            "survey_receipt_evidence": best[2] if best else None}


def operation_health(base, path, statuses=("pending", "processing", "failed")):
    """Bounded samples, with totals kept separate from sampled age/failure evidence."""
    now = datetime.now(timezone.utc)
    samples, totals = {}, {}
    for status in statuses:
        data = request(base, path + "/operations?" + urllib.parse.urlencode({"status": status, "limit": 100}))
        total = data.get("total") if isinstance(data, dict) else None
        items = data.get("operations") if isinstance(data, dict) else None
        if type(total) is not int or total < 0 or not isinstance(items, list) or total < len(items):
            raise ValueError(f"Cannot establish {status} operation status from the daemon response")
        totals[status] = total
        rows = []
        for item in items:
            created = item.get("created_at")
            try:
                age = max(0, int((now - datetime.fromisoformat(created.replace("Z", "+00:00"))).total_seconds()))
            except (ValueError, TypeError, AttributeError):
                age = None
            rows.append({"id": item["id"], "status": status, "created_age_seconds": age,
                         "next_retry_at": item.get("next_retry_at"), "operation_type": item.get("operation_type", item.get("task_type"))})
        samples[status] = rows
    return {"totals": totals, "samples": samples,
            "samples_complete": all(totals[status] == len(samples[status]) for status in totals)}


def inspect(home, directory, query=None):
    project, bank, effective, server, base, path, version = connection(home, directory)
    root = home / ".hindsight"
    managed = root / "mirket/project_registry.py"
    runtime = root / "coding-agents"
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
    mcp = server.get("transport", {})
    env = mcp.get("env") or {}
    mcp_wired = (server.get("enabled") is True and mcp.get("args") == [str(managed), "mcp"] and
                 env.get("HINDSIGHT_MCP_HARNESS") == "codex")
    hook_settings, hook_errors = {}, {}
    for event, mode in HOOKS.items():
        commands = [item.get("command", "") for group in hooks.get(event, []) for item in group.get("hooks", [])
                    if str(managed) in shlex.split(item.get("command", ""))]
        try:
            if len(commands) != 1:
                raise ValueError("Expected one registered hook")
            tokens, extra = launcher(commands[0])
            if tokens[1:] != [str(managed), mode]:
                raise ValueError("Unexpected launcher")
            hook_settings[event] = registry.effective_config(home, Path(directory).resolve(), bank, dict(os.environ, **extra))
        except (ValueError, OSError, subprocess.SubprocessError):
            hook_errors[event] = "Cannot resolve the registered hook safely"
    dist = runtime / "dist"
    patched = all((dist / name).is_file() and (dist / name).read_text() == value
                  for name, value in registry.adapters(dist).items())
    source_current = managed.is_file() and managed.read_bytes() == Path(registry.__file__).read_bytes()
    health = request(base, "/health")
    stats = request(base, path + "/stats")
    pages = list(walk_pages(request(base, path + "/knowledge-base/tree").get("roots", [])))
    tags = ("source:chat", "source:git-log", "source:git-diff", "source:survey-baseline")
    counts = {tag: request(base, path + "/documents?" + urllib.parse.urlencode({"tags": tag, "limit": 1}))["total"] for tag in tags}
    surveys = {doc["id"] for doc in documents(base, path, "source:upload")
               if doc["id"] in {"repository-component-map", "repository-core-concepts",
                                "repository-conventions-and-patterns", "repository-tech-stack-and-features"}}
    primary = primary_session_ids(home / ".codex", project)
    retained = {doc.partition(":")[2] for doc in document_ids(base, path, "source:chat")
                if doc.startswith(("conversation:", "chat:"))}
    git = git_state(directory, documents(base, path, "source:survey-baseline"))
    operations = operation_health(base, path)
    differences = {event: [key for key in effective if settings.get(key) != effective[key]]
                   for event, settings in hook_settings.items() if settings != effective}
    findings = []
    if not all(wired.values()) or not mcp_wired or not patched or not source_current or hook_errors:
        findings.append("wiring_incomplete_or_stale")
    if differences:
        findings.append("hook_and_mcp_configuration_differ")
    if primary - retained:
        findings.append("primary_sessions_not_retained_or_still_active")
    if git["head"] and (git["survey_commits_behind"] is None or git["survey_commits_behind"] > 0):
        findings.append("committed_source_newer_than_completed_survey")
    if git["dirty_worktree"]:
        findings.append("uncommitted_source_not_proven_by_survey")
    if len(surveys) < 4:
        findings.append("survey_findings_incomplete")
    if any(p.get("is_stale") for p in pages):
        findings.append("knowledge_pages_stale")
    if any(p.get("last_refresh_failed_at") for p in pages):
        findings.append("knowledge_page_refresh_failed")
    if stats["pending_operations"] or operations["totals"]["pending"]:
        findings.append("operations_pending")
    if operations["totals"]["processing"]:
        findings.append("operations_processing")
    return {
        "bank": bank, "workspace": str(project), "runtime": version,
        "configuration_scope": "Current shell plus explicit registered launcher settings; inherited desktop environment and hook trust require host verification",
        "effective_mcp_settings": effective, "effective_hook_settings": hook_settings,
        "hook_configuration_errors": hook_errors, "hook_mcp_differences": differences,
        "source_freshness": git, "attention": findings,
        "operation_health": operations,
        "hooks_wired": wired, "mcp_wired": mcp_wired, "survey_adapter_current": patched,
        "installed_registry_current": source_current, "daemon_reachable": health.get("status") == "healthy",
        "auto_inject": effective.get("autoInject", "reflect"),
        "git_ingestion": effective.get("gitIngest", "message"),
        "opt_in_only": effective.get("optInOnly", False),
        "documents": stats["total_documents"], "source_counts": counts, "survey_findings": len(surveys),
        "local_primary_sessions": len(primary), "primary_sessions_missing_from_bank": len(primary - retained),
        "missing_primary_session_ids": sorted(primary - retained),
        "page_count": len(pages), "stale_pages": sum(bool(p.get("is_stale")) for p in pages),
        "pages_with_refresh_failure": sum(bool(p.get("last_refresh_failed_at")) for p in pages),
        "pending_operations": stats["pending_operations"],
        "historical_failed_operations": stats["failed_operations"],
        "last_memory_write": stats.get("last_memory_write_at"),
        "live_host_capture_verified_by_doctor": False,
        "source_capture_complete_verified": False,
    }


def refresh_pages(home, directory, limit=3, wait_seconds=45):
    """Explicit, bounded retry of stale/failed pages. Never change triggers or source data."""
    if not 1 <= limit <= 5 or not 0 <= wait_seconds <= 55:
        raise ValueError("Refresh limit must be 1–5 and wait must be 0–55 seconds")
    _, bank, _, _, base, path, _ = connection(home, directory)
    stats = request(base, path + "/stats")
    if stats["pending_operations"]:
        raise ValueError("Wait for pending source/refresh operations before submitting more page refreshes")
    active = operation_health(base, path, statuses=("pending", "processing"))
    if any(active["totals"].values()):
        raise ValueError("Wait for pending or processing source/refresh operations before submitting more page refreshes")
    pages = list(walk_pages(request(base, path + "/knowledge-base/tree").get("roots", [])))
    eligible = [page for page in pages if page.get("mental_model_id") and
                (page.get("is_stale") or page.get("last_refresh_failed_at"))]
    operations = []
    for page in eligible[:limit]:
        response = request(base, path + "/mental-models/" + urllib.parse.quote(page["mental_model_id"], safe="") + "/refresh", {})
        operations.append({"page_id": page["id"], "operation_id": response["operation_id"], "status": response["status"]})
    deadline = time.monotonic() + wait_seconds
    while operations and time.monotonic() < deadline:
        pending = [op for op in operations if op["status"] not in {"completed", "failed", "cancelled"}]
        if not pending:
            break
        for op in pending:
            result = request(base, path + "/operations/" + urllib.parse.quote(op["operation_id"], safe=""))
            op["status"] = result.get("status", "unknown").lower()
            details = result.get("details") or {}
            op["details"] = details
            outcome = details.get("outcome") if isinstance(details, dict) else None
            op["refresh_outcome"] = outcome or "not_reported"
            op["refresh_failed"] = op["status"] in {"failed", "cancelled"} or bool(outcome and outcome.startswith("refresh_failed"))
        if any(op["status"] not in {"completed", "failed", "cancelled"} for op in operations):
            time.sleep(min(1, max(0, deadline - time.monotonic())))
    return {"bank": bank, "submitted": len(operations), "remaining_pages": max(0, len(eligible) - limit),
            "operations": operations, "source_ingestion_verified": False,
            "next_step": "Run the doctor again; refresh completion does not establish source capture or live-host recall."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", default=".")
    parser.add_argument("--recall-chat", help="retrieve matching raw chat evidence from the resolved bank")
    parser.add_argument("--refresh-pages", action="store_true", help="explicitly refresh up to --limit stale/failed pages")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--wait", type=int, default=45)
    args = parser.parse_args()
    try:
        if args.refresh_pages and args.recall_chat:
            parser.error("Choose either refresh or recall")
        result = (refresh_pages(Path.home(), args.directory, args.limit, args.wait) if args.refresh_pages else
                  inspect(Path.home(), args.directory, args.recall_chat))
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as exc:
        print(f"Hindsight doctor: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
