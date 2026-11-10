import json
from pathlib import Path
import tempfile
import unittest

import doctor


class DoctorTest(unittest.TestCase):
    def test_coverage_counts_primary_session_metadata_for_only_the_project(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            project, other = root / "one/same", root / "two/same"
            project.mkdir(parents=True)
            other.mkdir(parents=True)
            home = root / "codex"
            for folder, sid, cwd, source in (
                ("sessions", "live", project, "vscode"),
                ("archived_sessions", "archived", project, "vscode"),
                ("archived_sessions", "unrelated", other, "vscode"),
                ("archived_sessions", "worker", project, {"subagent": {}}),
                ("sessions", "survey", project, "exec"),
            ):
                path = home / folder / (sid + ".jsonl")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps({"type": "session_meta",
                                            "payload": {"id": sid, "cwd": str(cwd), "source": source}}) + "\n")
            self.assertEqual(doctor.primary_session_ids(home, project), {"live", "archived"})


if __name__ == "__main__":
    unittest.main()
