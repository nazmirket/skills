import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import doctor


class DoctorTest(unittest.TestCase):
    def settings_home(self, base):
        home = Path(base)
        runtime = home / ".hindsight/coding-agents"
        runtime.mkdir(parents=True)
        (runtime / "package.json").write_text('{"version":"0.8.6"}')
        (home / ".hindsight/coding-agent.json").write_text(json.dumps({"serverMode": "daemon", "harnesses": {
            "codex": {"mapPathToBank": {}, "autoUpdate": False}}}))
        project = home / "project"
        project.mkdir()
        return home, project, runtime

    def test_connection_uses_effective_upstream_port_and_stops_for_disabled_policy(self):
        with tempfile.TemporaryDirectory() as temp:
            home, project, _ = self.settings_home(temp)
            settings = {"disabled": False, "serverMode": "daemon", "apiUrl": "http://127.0.0.1:9999", "apiPort": 9999, "apiTokenConfigured": False}
            with patch.object(doctor, "codex_mcp", return_value={}), patch.object(doctor.registry, "effective_config", return_value=settings):
                result = doctor.connection(home, project)
                self.assertEqual(result[4], "http://127.0.0.1:9999")
                settings["disabled"] = True
                with self.assertRaisesRegex(ValueError, "disabled"):
                    doctor.connection(home, project)

    def test_completed_survey_and_dirty_source_are_separate(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def git(*args):
                return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True).stdout.strip()
            git("init", "-q")
            for message in ("one", "two"):
                git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "--allow-empty", "-qm", message)
                if message == "one":
                    old = git("rev-parse", "HEAD")
            head = git("rev-parse", "HEAD")
            (root / "dirty").write_text("not in the survey")
            result = doctor.git_state(root, [{"id": "survey-baseline:" + old, "tags": ["survey-state:done"]},
                                             {"id": "survey-baseline:" + head, "tags": []}])
            self.assertEqual(result["survey_commits_behind"], 1)
            self.assertEqual(result["completed_survey_baseline"], old)
            self.assertTrue(result["dirty_worktree"])

    def test_page_recovery_is_bounded_and_preserves_source_and_policy(self):
        pages = [{"id": f"page-{i}", "mental_model_id": f"model-{i}", "kind": "page", "is_stale": True} for i in range(7)]
        def request(base, path, body=None):
            if path.endswith("/stats"):
                return {"pending_operations": 0}
            if "/operations?" in path:
                return {"total": 0, "operations": []}
            if path.endswith("/knowledge-base/tree"):
                return {"roots": pages}
            self.assertTrue(path.endswith("/refresh"))
            self.assertEqual(body, {})
            return {"operation_id": path, "status": "queued"}
        with patch.object(doctor, "connection", return_value=(None, "bank", {}, {}, "base", "/bank", "0.8.6")), patch.object(doctor, "request", side_effect=request) as calls:
            result = doctor.refresh_pages(Path("/unused"), "/unused", limit=2, wait_seconds=0)
            self.assertEqual(result["submitted"], 2)
            self.assertEqual(result["remaining_pages"], 5)
            self.assertFalse(result["source_ingestion_verified"])
            self.assertEqual(len(calls.call_args_list), 6)

    def test_page_recovery_refuses_more_work_when_operations_are_pending(self):
        with patch.object(doctor, "connection", return_value=(None, "bank", {}, {}, "base", "/bank", "0.8.6")), patch.object(doctor, "request", return_value={"pending_operations": 1}) as calls:
            with self.assertRaisesRegex(ValueError, "pending"):
                doctor.refresh_pages(Path("/unused"), "/unused")
            calls.assert_called_once()

    def test_page_recovery_refuses_processing_with_no_pending_operations(self):
        def request(base, path, body=None):
            if path.endswith("/stats"):
                return {"pending_operations": 0}
            if "status=processing" in path:
                return {"total": 1, "operations": [{"id": "consolidation", "status": "processing"}]}
            if "status=pending" in path:
                return {"total": 0, "operations": []}
            if path.endswith("/knowledge-base/tree"):
                return {"roots": [{"id": "page", "kind": "page", "mental_model_id": "model", "is_stale": True}]}
            return {"operation_id": "unexpected-refresh", "status": "queued"}
        with patch.object(doctor, "connection", return_value=(None, "bank", {}, {}, "base", "/bank", "0.8.6")), patch.object(doctor, "request", side_effect=request) as calls:
            with self.assertRaisesRegex(ValueError, "processing"):
                doctor.refresh_pages(Path("/unused"), "/unused", wait_seconds=0)
            self.assertFalse(any(call.args[1].endswith("/refresh") for call in calls.call_args_list))

    def test_page_recovery_refuses_unknown_operation_state_before_writes(self):
        for response in ({}, {"total": None, "operations": []}, {"total": "0", "operations": []},
                         {"total": False, "operations": []}, {"total": -1, "operations": []},
                         {"total": 0}, {"total": 0, "operations": [{"id": "contradiction"}]}):
            with self.subTest(response=response):
                def request(base, path, body=None):
                    if path.endswith("/stats"):
                        return {"pending_operations": 0}
                    if "status=pending" in path:
                        return {"total": 0, "operations": []}
                    return response
                with patch.object(doctor, "connection", return_value=(None, "bank", {}, {}, "base", "/bank", "0.8.6")), patch.object(doctor, "request", side_effect=request) as calls:
                    with self.assertRaisesRegex(ValueError, "Cannot establish processing"):
                        doctor.refresh_pages(Path("/unused"), "/unused", wait_seconds=0)
                    self.assertFalse(any(len(call.args) > 2 for call in calls.call_args_list))

    def test_inspection_flags_processing_when_stats_pending_is_zero(self):
        with tempfile.TemporaryDirectory() as temp:
            home, project, _ = self.settings_home(temp)
            hooks = home / ".codex/hooks.json"
            hooks.parent.mkdir()
            hooks.write_text('{"hooks":{}}')
            stats = {"pending_operations": 0, "failed_operations": 0, "total_documents": 0}
            def request(base, path, body=None):
                if path.endswith("/stats"):
                    return stats
                if path.endswith("/health"):
                    return {"status": "healthy"}
                if path.endswith("/knowledge-base/tree"):
                    return {"roots": []}
                if "/documents?" in path:
                    return {"total": 0, "items": []}
                if "status=processing" in path:
                    return {"total": 1, "operations": [{"id": "consolidation", "status": "processing"}]}
                return {"total": 0, "operations": []}
            with patch.object(doctor, "connection", return_value=(project, "bank", {}, {}, "base", "/bank", "0.8.6")), patch.object(doctor, "request", side_effect=request), patch.object(doctor.registry, "adapters", return_value={}), patch.object(doctor, "git_state", return_value={"head": None, "dirty_worktree": False}):
                result = doctor.inspect(home, project)
            self.assertIn("operations_processing", result["attention"])
            self.assertNotIn("operations_pending", result["attention"])
            self.assertEqual(result["operation_health"]["totals"]["processing"], 1)

    def test_operation_health_does_not_infer_failure_time_from_creation(self):
        def request(base, path):
            if "status=failed" in path:
                return {"total": 1, "operations": [{"id": "old-job", "created_at": "2000-01-01T00:00:00Z",
                    "updated_at": "2099-01-01T00:00:00Z", "status": "failed"}]}
            return {"total": 0, "operations": []}
        with patch.object(doctor, "request", side_effect=request):
            result = doctor.operation_health("base", "/bank")
        sample = result["samples"]["failed"][0]
        self.assertGreater(sample["created_age_seconds"], 300)
        self.assertNotIn("failed_at", sample)
        self.assertNotIn("recent_failure", result)

    @unittest.skipUnless(os.environ.get("MIRKET_TEST_RUNTIME") and shutil.which("node"), "Set MIRKET_TEST_RUNTIME to the pinned runtime for real resolver parity")
    def test_pinned_runtime_config_adapter_matches_layering_without_starting_mcp(self):
        source = Path(os.environ["MIRKET_TEST_RUNTIME"]) / "dist/mcp-server.js"
        with tempfile.TemporaryDirectory() as temp:
            home, project, runtime = self.settings_home(temp)
            dist = runtime / "dist"
            dist.mkdir()
            # The disposable package is ESM, like the pinned runtime.
            (runtime / "package.json").write_text('{"version":"0.8.6","type":"module"}')
            (dist / doctor.registry.CONFIG_ENTRY).write_text(doctor.registry.config_source(source.read_text()))
            config = home / ".hindsight/coding-agent.json"
            raw = json.loads(config.read_text())
            raw.update(paths={str(project): {"pageTriggerType": "manual"}}, banks={"bank": {"surveyRefreshCommits": 2}})
            config.write_text(json.dumps(raw))
            env = dict(os.environ, HINDSIGHT_API_PORT="9999", HINDSIGHT_OPT_IN_ONLY="true", HINDSIGHT_OPT_IN_PATHS=str(project), HINDSIGHT_API_TOKEN="do-not-output")
            value = doctor.registry.effective_config(home, project, "bank", env)
            self.assertEqual(value["apiUrl"], "http://127.0.0.1:9999")
            self.assertTrue(value["optInOnly"])
            self.assertFalse(value["disabled"])
            self.assertTrue(value["apiTokenConfigured"])
            self.assertNotIn("do-not-output", json.dumps(value))
            self.assertEqual(value["pageTriggerType"], "manual")
            self.assertEqual(value["surveyRefreshCommits"], 2)
            raw["harnesses"]["codex"]["apiPort"] = 9998
            config.write_text(json.dumps(raw))
            self.assertEqual(doctor.registry.effective_config(home, project, "bank", env)["apiPort"], 9998)
            raw["disabled"] = True
            raw["banks"]["bank"]["disabled"] = False
            config.write_text(json.dumps(raw))
            self.assertTrue(doctor.registry.effective_config(home, project, "bank", env)["disabled"])
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
