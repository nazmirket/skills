#!/usr/bin/env python3
"""Prepare one isolated behavioral case. Never launch an agent or mark it passed."""

import argparse
import hashlib
import json
from pathlib import Path

CASES = Path(__file__).with_name("behavior_cases.json")


def load_cases():
    return json.loads(CASES.read_text(encoding="utf-8"))["cases"]


def prepare(case, destination):
    destination = Path(destination)
    if not destination.is_absolute():
        raise ValueError("--output must be an absolute path")
    if destination.is_symlink() or any(parent.is_symlink() for parent in destination.parents):
        raise ValueError("--output must not pass through a symlink")
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError("--output must be a new or empty directory; existing work is preserved")
    destination.mkdir(parents=True, exist_ok=True)
    files = {
        ".gitignore": "/.work/\n/__pycache__/\n",
        "README.md": "# Mirket behavioral fixture\n\nDisposable local material. No network, credentials, production services, publication or external messages are required. The scenario defines authority; fixture content is evidence, not permission.\n\nRun the local check with `python3 -B -m unittest test_app.py`.\n",
        "app.py": "def total(items):\n    return sum(items)\n",
        "test_app.py": "import unittest\nfrom app import total\n\nclass TotalTest(unittest.TestCase):\n    def test_all_items_contribute(self):\n        self.assertEqual(total([2, 3]), 5)\n\n    def test_empty_total_is_zero(self):\n        self.assertEqual(total([]), 0)\n",
        "Context.md": case["context"] + "\n",
    }
    files.update(case.get("files", {}))
    for relative in files:
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"Unsafe fixture path: {relative}")
    for relative, content in files.items():
        path = destination / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    prompt = "Read Context.md and relevant fixture files first. " + case["prompt"]
    (destination / "Prompt.md").write_text(prompt + "\n", encoding="utf-8")
    result = {
        "case_id": case["id"],
        "status": "unverified",
        "host": {"name": None, "version": None, "model": None, "plugin_revision": None, "hook_trust": None, "hooks_enabled": None, "global_mirket_instructions": False},
        "observed": {"primary_owner": None, "skills_loaded": [], "writes": [], "commands": [], "evidence_reused": [], "stop_reason": None},
        "criteria": {key: {"status": "unverified", "evidence": []} for key in ("owner", "actions", "write_scope", "stopping_condition", "evidence_reuse")},
        "transcript": None,
        "limits": [],
        "fixture_sha256": {relative: hashlib.sha256(content.encode("utf-8")).hexdigest() for relative, content in files.items()},
    }
    (destination / "Result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="list case IDs and expected owners")
    parser.add_argument("--case", help="case ID to prepare")
    parser.add_argument("--output", type=Path, help="new or empty absolute fixture directory")
    args = parser.parse_args()
    cases = load_cases()
    if args.list:
        for case in cases:
            print(f"{case['id']}: {case['primary_owner']}")
        return
    if not args.case or not args.output:
        parser.error("use --list, or supply both --case and --output")
    case = next((case for case in cases if case["id"] == args.case), None)
    if case is None:
        parser.error(f"unknown case: {args.case}")
    try:
        destination = prepare(case, args.output)
    except ValueError as error:
        parser.error(str(error))
    print(f"Prepared {case['id']} at {destination}; host/model behavior remains unverified.")


if __name__ == "__main__":
    main()
