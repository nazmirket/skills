"""Check evaluation fixtures, not whether a model follows their expectations."""

import hashlib
import json
from pathlib import Path
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
            for case in load_cases():
                with self.subTest(case=case["id"]):
                    destination = prepare(case, root / case["id"])
                    result = json.loads((destination / "Result.json").read_text())
                    self.assertEqual(result["status"], "unverified")
                    self.assertTrue(all(item["status"] == "unverified" for item in result["criteria"].values()))
                    self.assertIsNone(result["observed"]["primary_owner"])
                    self.assertEqual(result["observed"]["writes"], [])
                    self.assertIn(case["prompt"], (destination / "Prompt.md").read_text())
                    for relative, digest in result["fixture_sha256"].items():
                        self.assertEqual(hashlib.sha256((destination / relative).read_bytes()).hexdigest(), digest)

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
        with self.assertRaisesRegex(ValueError, "absolute"):
            prepare(case, Path("relative"))


if __name__ == "__main__":
    unittest.main()
