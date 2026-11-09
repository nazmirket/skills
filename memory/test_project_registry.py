"""Verify project isolation without executing Codex or catalog skills."""

import importlib.util
import concurrent.futures
import json
import os
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("project_registry", Path(__file__).with_name("project_registry.py"))
registry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registry)


class ProjectRegistryTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.state = self.base / "state"

    def git_init(self, path):
        path.mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(path)], check=True)
        return path.resolve()

    def test_equal_named_projects_have_distinct_stable_banks(self):
        a = self.git_init(self.base / "one" / "same")
        b = self.git_init(self.base / "two" / "same")
        sub = a / "child"
        sub.mkdir()
        self.assertEqual(registry.project_root(sub), a)
        first = registry.register(self.state, a, {})
        self.assertEqual(first, registry.register(self.state, registry.project_root(sub), {}))
        self.assertNotEqual(first, registry.register(self.state, b, {}))

    def test_nested_git_project_is_separate_and_alias_matches(self):
        parent = self.git_init(self.base / "parent")
        nested = self.git_init(parent / "nested")
        alias = self.base / "alias"
        alias.symlink_to(parent, target_is_directory=True)
        self.assertEqual(registry.project_root(alias), parent)
        self.assertEqual(registry.project_root(alias / "nested"), nested)
        a = registry.register(self.state, parent, {str(parent): "existing-parent"})
        b = registry.register(self.state, nested, {str(parent): "existing-parent"})
        self.assertEqual(a, "existing-parent")
        self.assertNotEqual(a, b)

    def test_linked_worktree_uses_main_project_bank(self):
        main = self.git_init(self.base / "main")
        subprocess.run(["git", "-C", str(main), "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "--allow-empty", "-qm", "test"], check=True)
        linked = self.base / "linked"
        subprocess.run(["git", "-C", str(main), "worktree", "add", "-qb", "work", str(linked)], check=True)
        self.assertEqual(registry.project_root(linked), main)

    def test_linked_worktree_with_separate_git_directory(self):
        main = self.base / "main"
        metadata = self.base / "metadata"
        subprocess.run(["git", "init", "-q", "--separate-git-dir", str(metadata), str(main)], check=True)
        subprocess.run(["git", "-C", str(main), "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "--allow-empty", "-qm", "test"], check=True)
        linked = self.base / "linked"
        subprocess.run(["git", "-C", str(main), "worktree", "add", "-qb", "work", str(linked)], check=True)
        self.assertEqual(registry.project_root(main), metadata.resolve())
        self.assertEqual(registry.project_root(linked), metadata.resolve())

    def test_broken_git_marker_fails_closed(self):
        root = self.base / "broken"
        root.mkdir()
        (root / ".git").write_text("gitdir: /nonexistent/mirket-setup-gitdir\n")
        with self.assertRaisesRegex(ValueError, "Git"):
            registry.project_root(root)

    def test_concurrent_projects_preserve_all_registry_entries(self):
        roots = [self.base / str(i) for i in range(12)]
        for root in roots:
            root.mkdir()
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            ids = list(pool.map(lambda root: registry.register(self.state, root, {}), roots))
        data = json.loads((self.state / "projects.json").read_text())
        self.assertEqual(len(data["projects"]), len(roots))
        self.assertEqual(len(set(ids)), len(roots))

    @patch.object(registry.subprocess, "run")
    def test_git_error_does_not_become_non_git_directory(self, run):
        run.return_value.returncode = 128
        run.return_value.stderr = "fatal: permission denied"
        with self.assertRaisesRegex(ValueError, "Git"):
            registry.project_root(self.base)

    def test_inherited_git_environment_cannot_redirect_project(self):
        a = self.git_init(self.base / "a")
        b = self.git_init(self.base / "b")
        with patch.dict(os.environ, {"GIT_DIR": str(a / ".git"), "GIT_WORK_TREE": str(a)}):
            self.assertEqual(registry.project_root(b), b)

    def test_hook_forwards_input_and_sets_project_bank(self):
        project = self.git_init(self.base / "project")
        fake_home = self.base / "fake-home"
        runtime = fake_home / ".hindsight/coding-agents"
        runtime.mkdir(parents=True)
        (runtime / "package.json").write_text('{"version":"0.8.6"}')
        (fake_home / ".hindsight/coding-agent.json").write_text(json.dumps({
            "harnesses": {"codex": {"mapPathToBank": {}, "autoUpdate": False}}
        }))
        bin_dir = self.base / "bin"
        bin_dir.mkdir()
        node = bin_dir / "node"
        node.write_text("#!" + sys.executable + "\nimport hashlib,json,os,sys\nprint(json.dumps({'sha': hashlib.sha256(sys.stdin.buffer.read()).hexdigest(), 'bank': os.environ['HINDSIGHT_BANK_ID'], 'dynamic': os.environ['HINDSIGHT_DYNAMIC_BANK_ID'], 'git_dir': os.environ.get('GIT_DIR')}))\n")
        node.chmod(0o755)
        payload = json.dumps({"hook_event_name": "SessionStart", "cwd": str(project), "session_id": "test-session"}).encode()
        code = (
            "import importlib.util,sys,pathlib; "
            "s=importlib.util.spec_from_file_location('r',sys.argv[1]); "
            "r=importlib.util.module_from_spec(s);s.loader.exec_module(r); "
            "home=pathlib.Path(sys.argv[2]);r.Path.home=lambda:home;sys.argv=['registry','start'];r.main()"
        )
        env = dict(os.environ, PATH=str(bin_dir) + os.pathsep + os.environ.get("PATH", ""), GIT_DIR="/elsewhere/.git")
        env.pop("HINDSIGHT_CONFIG", None)
        result = subprocess.run([sys.executable, "-B", "-c", code, registry.__file__, str(fake_home)], input=payload, capture_output=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        output = json.loads(result.stdout)
        self.assertEqual(output["sha"], hashlib.sha256(payload).hexdigest())
        self.assertEqual(output["bank"], "coding-agent::project-" + hashlib.sha256(os.fsencode(project)).hexdigest())
        self.assertEqual(output["dynamic"], "false")
        self.assertIsNone(output["git_dir"])

    def test_duplicate_legacy_banks_are_rejected(self):
        a = self.base / "a"
        b = self.base / "b"
        a.mkdir(); b.mkdir()
        with self.assertRaisesRegex(ValueError, "multiple"):
            registry.register(self.state, a, {str(a): "same", str(b): "same"})

    def test_corrupt_registry_is_preserved(self):
        self.state.mkdir()
        p = self.state / "projects.json"
        p.write_text("invalid json")
        with self.assertRaises(ValueError):
            registry.register(self.state, self.base, {})
        self.assertEqual(p.read_text(), "invalid json")

    def test_new_conflicting_mapping_is_not_ignored(self):
        self.assertTrue(registry.register(self.state, self.base, {}))
        with self.assertRaisesRegex(ValueError, "mapping"):
            registry.register(self.state, self.base, {str(self.base): "different-bank"})

    def test_non_git_session_uses_recorded_root(self):
        root = self.base / "plain"
        root.mkdir()
        sub = root / "sub"
        sub.mkdir()
        tmp = self.base / "tmp"
        (tmp / "hindsight-codex").mkdir(parents=True)
        (tmp / "hindsight-codex/session-123.root").write_text(str(root))
        with patch.object(registry.tempfile, "gettempdir", return_value=str(tmp)):
            self.assertEqual(registry.hook_root({"cwd": str(sub), "session_id": "session-123", "hook_event_name": "Stop"}), root.resolve())

    def test_nested_git_project_does_not_reuse_parent_session_bank(self):
        parent = self.git_init(self.base / "parent")
        nested = self.git_init(parent / "nested")
        tmp = self.base / "tmp"
        (tmp / "hindsight-codex").mkdir(parents=True)
        (tmp / "hindsight-codex/session-123.root").write_text(str(parent))
        with patch.object(registry.tempfile, "gettempdir", return_value=str(tmp)):
            with self.assertRaisesRegex(ValueError, "session"):
                registry.hook_root({"cwd": str(nested), "session_id": "session-123", "hook_event_name": "Stop"})

    def test_rejects_alias_routing_or_changed_runtime(self):
        with self.assertRaisesRegex(ValueError, "alias"):
            registry.check_config({"harnesses": {"codex": {"mapPathToBank": {}, "autoUpdate": False}}, "banks": {"a": {"bank": "b"}}}, "0.8.6")
        with self.assertRaisesRegex(ValueError, "version"):
            registry.check_config({"harnesses": {"codex": {"mapPathToBank": {}, "autoUpdate": False}}}, "0.9.0")
        with self.assertRaisesRegex(ValueError, "alias"):
            registry.check_config({"harnesses": {"codex": {"mapPathToBank": {}, "autoUpdate": False, "banks": {"a": {"bank": "b"}}}}}, "0.8.6")


if __name__ == "__main__":
    unittest.main()
