"""Check evaluation fixtures, not whether a model follows their expectations."""

import doctest
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from prepare_host_smoke import load_cases, prepare
from test_package_wiring import EXPECTED_SKILLS


class HostSmokeFixtureTest(unittest.TestCase):
    def test_scenarios_cover_the_catalog_with_reviewable_expectations(self):
        cases = load_cases()
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertEqual({case["primary_owner"] for case in cases}, EXPECTED_SKILLS)
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertRegex(case["id"], r"^[a-z][a-z0-9-]*$")
                for key in ("prompt", "context", "stopping_condition", "evidence_reuse"):
                    self.assertTrue(case[key].strip(), key)
                self.assertTrue(case["expected_actions"])
                self.assertIn(case.get("invocation", "implicit"), {"implicit", "explicit"})
                self.assertTrue(case["prohibited_writes"])
                self.assertIsInstance(case["allowed_writes"], list)
                self.assertLessEqual(set(case["supporting_skills"]), EXPECTED_SKILLS)
                for relative in case["files"]:
                    self.assertNotIn(relative, {"Prompt.md", "Result.json"})
                    self.assertFalse(Path(relative).is_absolute())
                    self.assertNotIn("..", Path(relative).parts)

    def test_prepared_cases_start_unverified_and_record_the_input_snapshot(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root).resolve()
            for index, case in enumerate(load_cases()):
                with self.subTest(case=case["id"]):
                    destination = prepare(case, root / f"trial-{index}")
                    result = json.loads((root / f"trial-{index}.result.json").read_text())
                    self.assertEqual(result["case_id"], case["id"])
                    self.assertEqual(result["invocation"], case.get("invocation", "implicit"))
                    self.assertEqual(result["rubric_exposure"], "unverified")
                    self.assertIsNone(result["host"]["global_mirket_instructions"])
                    visible = {f.relative_to(destination).as_posix() for f in destination.rglob("*") if f.is_file()}
                    self.assertEqual(visible, set(result["fixture_sha256"]))
                    self.assertNotIn("Result.json", visible)
                    self.assertEqual(result["status"], "unverified")
                    self.assertTrue(all(item["status"] == "unverified" for item in result["criteria"].values()))
                    self.assertLessEqual({"owner", "support_selection", "announcement", "outcome", "write_scope", "stopping_condition"}, result["criteria"].keys())
                    self.assertIsNone(result["observed"]["primary_owner"])
                    self.assertEqual(result["observed"]["writes"], [])
                    self.assertEqual(result["observed"]["references_loaded"], [])
                    self.assertIn(case["prompt"], (destination / "Prompt.md").read_text())
                    for relative, digest in result["fixture_sha256"].items():
                        self.assertEqual(hashlib.sha256((destination / relative).read_bytes()).hexdigest(), digest)

    def test_cli_accepts_an_unpublished_catalog_and_keeps_its_label_outside_workspace(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root).resolve()
            case = dict(load_cases()[0], id="reviewer-only-label", prompt="Explain the result.", files={}, include_sample_app=False)
            catalog = root / "private.json"
            catalog.write_text(json.dumps({"cases": [case]}))
            workspace = root / "trial-01"
            workspace.mkdir()
            results = root / "evaluator"
            subprocess.run([sys.executable, str(Path(__file__).with_name("prepare_host_smoke.py")),
                            "--cases", str(catalog), "--case", case["id"], "--output", str(workspace),
                            "--results-dir", str(results)],
                           capture_output=True, check=True)
            record = json.loads((results / "trial-01.result.json").read_text())
            self.assertEqual(record["case_id"], case["id"])
            self.assertEqual({p.name for p in workspace.iterdir()}, {".gitignore", "README.md", "Context.md", "Prompt.md"})
            self.assertFalse((root / "trial-01.result.json").exists())
            for path in workspace.rglob("*"):
                if path.is_file():
                    self.assertNotIn(case["id"], path.read_text())

    def test_failed_preparation_preserves_previous_results_and_removes_its_partial_files(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root).resolve()
            workspace = root / "trial-02"
            record = root / "trial-02.result.json"
            case = load_cases()[0]
            record.write_text("earlier verdict")
            with self.assertRaisesRegex(ValueError, "existing work is preserved"):
                prepare(case, workspace)
            self.assertFalse(workspace.exists())
            self.assertEqual(record.read_text(), "earlier verdict")
            broken = dict(case, files={"a": "file", "a/b": "conflicting entry"})
            with self.assertRaises(OSError):
                prepare(broken, root / "trial-03")
            self.assertFalse((root / "trial-03").exists())
            self.assertFalse((root / "trial-03.result.json").exists())

    def test_preparer_preserves_existing_work_and_rejects_indirect_paths(self):
        case = load_cases()[0]
        with tempfile.TemporaryDirectory() as root:
            root = Path(root).resolve()
            destination = root / "existing"
            destination.mkdir()
            important = destination / "important.txt"
            important.write_text("preserve")
            with self.assertRaisesRegex(ValueError, "existing work is preserved"):
                prepare(case, destination)
            self.assertEqual(important.read_text(), "preserve")
            link = root / "linked"
            link.symlink_to(destination, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink"):
                prepare(case, link / "new")
            empty = root / "empty"
            with self.assertRaisesRegex(ValueError, "outside the agent workspace"):
                prepare(case, empty, results_dir=empty / "review")
            self.assertFalse(empty.exists())
        with self.assertRaisesRegex(ValueError, "absolute"):
            prepare(case, Path("relative"))

    def test_release_fixture_example_runs_with_only_the_shipped_files(self):
        case = next(case for case in load_cases() if case["id"] == "release-prepare-only")
        with tempfile.TemporaryDirectory() as root:
            root = Path(root).resolve()
            source = prepare(case, root / "source")
            consumer = root / "consumer"
            consumer.mkdir()
            for name in ("app.py", "README.md"):
                shutil.copyfile(source / name, consumer / name)
            readme = (consumer / "README.md").read_text(encoding="utf-8")
            examples = doctest.DocTestParser().get_examples(readme)
            self.assertTrue(any(example.want for example in examples), "The shipped example must check a result")
            result = subprocess.run(
                [sys.executable, "-E", "-s", "-B", "-m", "doctest", "README.md"],
                cwd=consumer, text=True, capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
