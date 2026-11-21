#!/usr/bin/env python3
"""Prepare one isolated behavioral case. Never launch an agent or mark it passed."""

import argparse
from contextlib import ExitStack
import hashlib
import json
from pathlib import Path

CASES = Path(__file__).with_name("behavior_cases.json")


def load_cases(path=CASES):
    return json.loads(path.read_text(encoding="utf-8"))["cases"]


def evaluator_path(destination, results_dir=None):
    directory = destination.parent if results_dir is None else Path(results_dir)
    if not directory.is_absolute() or ".." in directory.parts:
        raise ValueError("--results-dir must be an absolute path")
    if directory == destination or destination in directory.parents:
        raise ValueError("--results-dir must be outside the agent workspace")
    if directory.is_symlink() or any(parent.is_symlink() for parent in directory.parents):
        raise ValueError("--results-dir must not pass through a symlink")
    return directory / (destination.name + ".result.json")


def prepare(case, destination, *, results_dir=None):
    destination = Path(destination)
    if not destination.is_absolute() or not destination.name or ".." in destination.parts:
        raise ValueError("--output must be an absolute path")
    if destination.is_symlink() or any(parent.is_symlink() for parent in destination.parents):
        raise ValueError("--output must not pass through a symlink")
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError("--output must be a new or empty directory; existing work is preserved")
    result_path = evaluator_path(destination, results_dir)
    if result_path.is_symlink() or result_path.exists():
        raise ValueError("the evaluator result already exists; existing work is preserved")
    files = {
        ".gitignore": "/.work/temp/\n/.work/recover/\n/.work/stashes/\n/.work/routines/\n/__pycache__/\n",
        "README.md": "# Local project\n\nSee Context.md for the task and its scope.\n",
        "Context.md": case["context"] + "\n",
    }
    if case.get("include_sample_app", True):
        files["app.py"] = "def total(items):\n    return sum(items)\n"
        files["test_app.py"] = "import unittest\nfrom app import total\n\nclass TotalTest(unittest.TestCase):\n    def test_all_items_contribute(self):\n        self.assertEqual(total([2, 3]), 5)\n\n    def test_empty_total_is_zero(self):\n        self.assertEqual(total([]), 0)\n"
    files.update(case.get("files", {}))
    for relative in files:
        path = Path(relative)
        if path.is_absolute() or not path.parts or ".." in path.parts or path.parts[0].casefold() in {"prompt.md", "result.json"}:
            raise ValueError(f"Unsafe fixture path: {relative}")
    files["Prompt.md"] = "Read Context.md and relevant fixture files first. " + case["prompt"] + "\n"
    result = {
        "case_id": case["id"],
        "invocation": case.get("invocation", "implicit"),
        "rubric_exposure": "unverified",
        "status": "unverified",
        "host": {"name": None, "version": None, "model": None, "model_driver": None, "catalog_condition": None,
                 "plugin_revision": None, "hook_trust": None, "hooks_enabled": None, "global_mirket_instructions": None},
        "observed": {"primary_owner": None, "skills_loaded": [], "unnecessary_reads": [], "announcement": None,
                     "writes": [], "commands": [], "evidence_reused": [], "stop_reason": None},
        "criteria": {key: {"status": "unverified", "evidence": []} for key in (
            "owner", "support_selection", "announcement", "actions", "outcome", "write_scope", "stopping_condition", "evidence_reuse"
        )},
        "transcript": None,
        "limits": [],
        "fixture_sha256": {relative: hashlib.sha256(content.encode("utf-8")).hexdigest() for relative, content in files.items()},
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation preserves earlier trials. Roll back only this attempt's files.
    directories = {parent for name in files for parent in Path(name).parents if parent.parts}
    with ExitStack() as rollback:
        with result_path.open("x", encoding="utf-8") as record:
            rollback.callback(result_path.unlink)
            if not destination.exists():
                destination.mkdir()
                rollback.callback(destination.rmdir)
            for relative in sorted(directories, key=lambda path: len(path.parts)):
                directory = destination / relative
                directory.mkdir()
                rollback.callback(directory.rmdir)
            for relative, content in files.items():
                path = destination / relative
                with path.open("x", encoding="utf-8", newline="") as output:
                    rollback.callback(path.unlink)
                    output.write(content)
            record.write(json.dumps(result, indent=2) + "\n")
        rollback.pop_all()
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="list case IDs and expected owners")
    parser.add_argument("--case", help="case ID to prepare")
    parser.add_argument("--cases", type=Path, default=CASES, help="case catalog; use an evaluator-only file for blind trials")
    parser.add_argument("--output", type=Path, help="new or empty absolute fixture directory")
    parser.add_argument("--results-dir", type=Path, help="absolute evaluator-only directory for the result (default: workspace parent)")
    args = parser.parse_args()
    cases = load_cases(args.cases)
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
        destination = prepare(case, args.output, results_dir=args.results_dir)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(f"Workspace: {destination}\nEvaluator result: {evaluator_path(destination, args.results_dir)}")


if __name__ == "__main__":
    main()
