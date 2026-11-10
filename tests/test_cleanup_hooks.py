"""Exercise cleanup hook messages without executing any supplied shell command."""

import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile
import unittest

HOOK = Path(__file__).resolve().parents[1] / "plugins/mirket/hooks/cleanup.py"
CLEAN = HOOK.parent.parent / "skills/clean/SKILL.md"


def invoke(payload, *, env=None):
    text = payload if isinstance(payload, str) else json.dumps(payload)
    result = subprocess.run(
        [sys.executable, "-I", str(HOOK)],
        input=text,
        text=True,
        capture_output=True,
        env=env,
        check=True,
    )
    return json.loads(result.stdout)


def before_shell(command):
    return invoke({"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command}})


def denied(output):
    return output.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"


class CleanupHooksTest(unittest.TestCase):
    def test_stop_requests_one_continuation(self):
        first = invoke({"hook_event_name": "Stop", "stop_hook_active": False})
        self.assertEqual(first.get("decision"), "block")
        self.assertIn(str(CLEAN), first.get("reason", ""))
        self.assertTrue(CLEAN.is_file())
        self.assertEqual(invoke({"hook_event_name": "Stop", "stop_hook_active": True}), {})

    def test_missing_or_invalid_stop_flag_does_not_loop(self):
        for payload in ({"hook_event_name": "Stop"}, {"hook_event_name": "Stop", "stop_hook_active": "false"}):
            with self.subTest(payload=payload):
                result = invoke(payload)
                self.assertNotIn("decision", result)
                self.assertIn("systemMessage", result)

    def test_malformed_payload_reports_gap_without_loop(self):
        for payload in ("{invalid", "[]", "null"):
            with self.subTest(payload=payload):
                result = invoke(payload)
                self.assertIn("systemMessage", result)
                self.assertNotIn("decision", result)

    def test_unacknowledged_commits_are_blocked(self):
        commands = (
            "git commit -m first",
            "git -C /tmp commit -m first",
            "git -c user.name=x commit -m first",
            "env X=1 git commit -m first",
            "command git commit -m first",
            "git commit -m 'MIRKET_CLEANUP_DONE=1'",
            "echo MIRKET_CLEANUP_DONE=1; git commit -m first",
            "export MIRKET_CLEANUP_DONE=1; git commit -m first",
            "MIRKET_CLEANUP_DONE=1 git commit -m first && git commit -m second",
            "git status\ngit commit -m first",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assertTrue(denied(before_shell(command)))

    def test_acknowledged_commits_are_neutral_not_allowed(self):
        commands = (
            "MIRKET_CLEANUP_DONE=1 git commit -m first",
            "env MIRKET_CLEANUP_DONE=1 git -C . commit -m first",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assertEqual(before_shell(command), {})

    def test_quoted_and_escaped_operators_are_commit_arguments(self):
        for message in ("'|'", r"\;", '"("'):
            with self.subTest(message=message):
                self.assertEqual(before_shell(f"MIRKET_CLEANUP_DONE=1 git commit -m {message} --allow-empty"), {})

    def test_does_not_execute_command_selected_git(self):
        with tempfile.TemporaryDirectory() as root:
            sentinel = Path(root) / "executed"
            git = Path(root) / "git"
            git.write_text(f"#!/bin/sh\ntouch {shlex.quote(str(sentinel))}\n")
            git.chmod(0o700)
            payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "cwd": root}
            for command in ("./git commit -m x", "PATH=. git commit -m x"):
                with self.subTest(command=command):
                    result = invoke({**payload, "tool_input": {"command": f"MIRKET_CLEANUP_DONE=1 {command}"}})
                    self.assertTrue(denied(result))
                    self.assertFalse(sentinel.exists())
            result = invoke({**payload, "tool_input": {"command": "MIRKET_CLEANUP_DONE=1 git commit -m x"}},
                            env={**os.environ, "PATH": "." + os.pathsep + os.defpath})
            self.assertTrue(denied(result))
            self.assertFalse(sentinel.exists())

    def test_does_not_execute_fsmonitor_during_index_probe(self):
        with tempfile.TemporaryDirectory() as root:
            subprocess.run(["git", "init", "-q", root], check=True)
            path = Path(root)
            (path / "tracked").write_text("x")
            subprocess.run(["git", "-C", root, "add", "tracked"], check=True)
            index = (path / ".git/index").read_bytes()
            sentinel = path / "executed"
            helper = path / "fsmonitor"
            helper.write_text(f"#!/bin/sh\ntouch {shlex.quote(str(sentinel))}\nprintf 'token\\000'\n")
            helper.chmod(0o700)
            payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "cwd": root}
            command = f"git -c {shlex.quote('core.fsmonitor=' + str(helper))} commit -m x"
            result = invoke({**payload, "tool_input": {"command": f"MIRKET_CLEANUP_DONE=1 {command}"}})
            self.assertFalse(sentinel.exists())
            self.assertTrue(denied(result))
            subprocess.run(["git", "-C", root, "config", "core.fsmonitor", str(helper)], check=True)
            result = invoke({**payload, "tool_input": {"command": "MIRKET_CLEANUP_DONE=1 git commit -m x"}})
            self.assertEqual(result, {})
            self.assertFalse(sentinel.exists())
            self.assertEqual((path / ".git/index").read_bytes(), index)

    def test_commit_modes_that_change_index_inputs_are_not_probed(self):
        for args in ("-am x", "--all -m x", "--include tracked -m x", "--only -m x", "--interactive", "-m x -- tracked", "-m x tracked"):
            with self.subTest(args=args):
                result = before_shell(f"MIRKET_CLEANUP_DONE=1 git commit {args}")
                self.assertTrue(denied(result))
                self.assertIn("stage", result["hookSpecificOutput"]["permissionDecisionReason"])

    def test_precommit_requests_installed_clean_skill_and_preserves_marker(self):
        output = before_shell("git commit -m first")
        self.assertTrue(denied(output))
        reason = output["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn(str(CLEAN), reason)
        self.assertIn("MIRKET_CLEANUP_DONE=1 git commit", reason)

    def test_noncommit_commands_are_neutral(self):
        for command in ("git status", "echo git commit", "echo 'git commit'", "git show --format=commit"):
            with self.subTest(command=command):
                self.assertEqual(before_shell(command), {})

    def test_hash_inside_word_does_not_hide_a_following_commit(self):
        for command in ("echo x#note; git commit -m first", "echo x\\ #note; git commit -m first", "echo 'x'#note; git commit -m first"):
            with self.subTest(command=command):
                self.assertTrue(denied(before_shell(command)))

    def test_shell_comments_are_not_executed_commands(self):
        for command in ("echo ok # git commit -m first", "# git commit -m first\ngit status"):
            with self.subTest(command=command):
                self.assertEqual(before_shell(command), {})
        self.assertTrue(denied(before_shell("echo ok # note\ngit commit -m first")))

    def test_heredoc_is_reported_not_treated_as_executed_commands(self):
        for command in ("cat <<EOF\ngit commit -m example\nEOF",):
            with self.subTest(command=command):
                result = before_shell(command)
                self.assertIn("systemMessage", result)
                self.assertFalse(denied(result))

    def test_commit_before_heredoc_is_blocked(self):
        self.assertTrue(denied(before_shell("git commit -F - <<'EOF'\nmessage\nEOF")))
        self.assertTrue(denied(before_shell("echo x\\ #word; git commit -F - <<EOF\nmessage\nEOF")))

    def test_quoted_heredoc_text_is_not_an_operator(self):
        self.assertEqual(before_shell("echo '<<EOF'"), {})
        self.assertTrue(denied(before_shell("git commit -m '<< note'")))

    def test_unparseable_shell_reports_gap(self):
        result = before_shell("git commit -m 'unclosed")
        self.assertIn("systemMessage", result)
        self.assertFalse(denied(result))

    def test_wrapped_commits_report_uncertain_coverage(self):
        for command in ("if git commit -m x; then true; fi", "env -i git commit -m x", "time git commit -m x"):
            with self.subTest(command=command):
                self.assertIn("systemMessage", before_shell(command))

    def test_staged_work_is_blocked_even_after_cleanup_acknowledgment(self):
        with tempfile.TemporaryDirectory() as root:
            subprocess.run(["git", "init", "-q", root], check=True)
            work = Path(root) / ".work"
            work.mkdir()
            (work / "private.txt").write_text("private")
            subprocess.run(["git", "-C", root, "add", ".work/private.txt"], check=True)
            def request(command):
                return invoke({"hook_event_name": "PreToolUse", "tool_name": "Bash", "cwd": root, "tool_input": {"command": command}})
            result = request("MIRKET_CLEANUP_DONE=1 git commit -m x")
            self.assertTrue(denied(result))
            self.assertIn(".work/private.txt", result["hookSpecificOutput"]["permissionDecisionReason"])
            self.assertEqual(request("MIRKET_CLEANUP_DONE=1 MIRKET_WORK_EXCEPTION=.work/private.txt git commit -m x"), {})
            self.assertTrue(denied(request("MIRKET_CLEANUP_DONE=1 MIRKET_WORK_EXCEPTION=.work/other.txt git commit -m x")))
            (work / "other.txt").write_text("other")
            subprocess.run(["git", "-C", root, "add", ".work/other.txt"], check=True)
            self.assertTrue(denied(request("MIRKET_CLEANUP_DONE=1 MIRKET_WORK_EXCEPTION=.work/private.txt git commit -m x")))

    def test_staged_work_targets_git_c_directory(self):
        with tempfile.TemporaryDirectory() as root:
            target = Path(root) / "target"
            subprocess.run(["git", "init", "-q", str(target)], check=True)
            subprocess.run(["git", "-C", str(target), "config", "diff.relative", "true"], check=True)
            (target / "nested").mkdir()
            work = target / ".work"
            work.mkdir()
            (work / "secret").write_text("x")
            subprocess.run(["git", "-C", str(target), "add", ".work/secret"], check=True)
            payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "cwd": root, "tool_input": {"command": "MIRKET_CLEANUP_DONE=1 git -C target -C nested commit -m x"}}
            result = invoke(payload)
            self.assertTrue(denied(result))
            self.assertIn(".work/secret", result["hookSpecificOutput"]["permissionDecisionReason"])
            result = invoke(payload, env={**os.environ, "GIT_INDEX_FILE": str(target / "alternate-index")})
            self.assertTrue(denied(result))
            self.assertIn("inherited GIT_*", result["hookSpecificOutput"]["permissionDecisionReason"])

    def test_index_inspection_failure_blocks_an_acknowledged_commit(self):
        with tempfile.TemporaryDirectory() as root:
            payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "cwd": root, "tool_input": {"command": "MIRKET_CLEANUP_DONE=1 git commit -m x"}}
            self.assertTrue(denied(invoke(payload)))

    def test_compound_commands_cannot_change_index_before_inspection(self):
        for command in ("git add -f .work/a && MIRKET_CLEANUP_DONE=1 git commit -m x", "cd other && MIRKET_CLEANUP_DONE=1 git commit -m x", "MIRKET_CLEANUP_DONE=1 git commit -m x && MIRKET_CLEANUP_DONE=1 git commit -m y"):
            with self.subTest(command=command):
                self.assertTrue(denied(before_shell(command)))


if __name__ == "__main__":
    unittest.main()
