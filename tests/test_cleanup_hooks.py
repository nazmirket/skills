"""Exercise cleanup hook messages without executing any supplied shell command."""

import json
import os
from pathlib import Path
import runpy
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

HOOK = Path(__file__).resolve().parents[1] / "hooks/cleanup.py"
CLEAN = HOOK.parent.parent / "skills/clean/SKILL.md"
REPOSITORY = shlex.quote(str(HOOK.parents[1]))


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


def before_shell(command, *, cwd=None, env=None):
    payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command}}
    if cwd is not None:
        payload["cwd"] = str(cwd)
    return invoke(payload, env=env)


def denied(output):
    return output.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"


def transport_environment():
    env = {name: value for name, value in os.environ.items() if not name.startswith("GIT_")}
    url = "https://example.invalid:443/team/a%20repository.git"
    entries = [
        (f"credential.{url}.helper", ""),
        (f"credential.{url}.helper", "example-helper"),
        (f"credential.{url}.useHttpPath", "true"),
        (f"http.{url}.proactiveAuth", "basic"),
        (f"http.{url}.followRedirects", "false"),
    ]
    env["GIT_CONFIG_COUNT"] = str(len(entries))
    for index, (key, value) in enumerate(entries):
        env[f"GIT_CONFIG_KEY_{index}"] = key
        env[f"GIT_CONFIG_VALUE_{index}"] = value
    return env


class CleanupHooksTest(unittest.TestCase):
    def test_package_does_not_register_a_stop_hook(self):
        hooks = json.loads((HOOK.parent / "hooks.json").read_text())["hooks"]
        self.assertNotIn("Stop", hooks)
        bash_commands = [hook["command"] for group in hooks["PreToolUse"]
                         if group["matcher"] == "^Bash$" for hook in group["hooks"]]
        self.assertTrue(any("/hooks/cleanup.py" in command for command in bash_commands))

    def test_stale_stop_event_with_old_opt_in_cannot_continue(self):
        self.assertEqual(invoke({"hook_event_name": "Stop", "stop_hook_active": False},
                                env={**os.environ, "MIRKET_FINAL_REVIEW": "1"}), {})

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
            f"MIRKET_CLEANUP_DONE=1 git -C {REPOSITORY} commit -m first",
            f"env MIRKET_CLEANUP_DONE=1 git -C {REPOSITORY} -C . commit -m first",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assertEqual(before_shell(command), {})

    def test_https_transport_settings_preserve_the_staged_work_check(self):
        with tempfile.TemporaryDirectory() as root:
            subprocess.run(["git", "init", "-q", root], check=True)
            env = transport_environment()
            command = f"MIRKET_CLEANUP_DONE=1 git -C {shlex.quote(root)} commit -m first"
            (Path(root) / "reviewed.md").write_text("reviewed")
            subprocess.run(["git", "-C", root, "add", "reviewed.md"], check=True)
            self.assertEqual(before_shell(command, env=env), {})
            private = Path(root) / ".work" / "temp" / "local.md"
            private.parent.mkdir(parents=True)
            private.write_text("test fixture")
            subprocess.run(["git", "-C", root, "add", "-f", ".work/temp/local.md"], check=True)
            result = before_shell(command, env=env)
            self.assertTrue(denied(result))
            self.assertIn(".work/temp/local.md", result["hookSpecificOutput"]["permissionDecisionReason"])

    def test_transport_settings_cannot_hide_other_git_overrides(self):
        base = transport_environment()
        command = f"MIRKET_CLEANUP_DONE=1 git -C {REPOSITORY} commit -m first"
        for name, value in (
            ("GIT_INDEX_FILE", "other-index"),
            ("GIT_DIR", "other-repository"),
            ("GIT_CONFIG_PARAMETERS", ""),
            ("GIT_CONFIG_KEY_0", "core.worktree"),
            ("GIT_CONFIG_KEY_0", "include.path"),
            ("GIT_CONFIG_KEY_0", "credential.helper"),
            ("GIT_CONFIG_KEY_0", "http.https://example.invalid/repo.proxy"),
            ("GIT_CONFIG_KEY_0", "credential.https://example.invalid:65536/repo.helper"),
            ("GIT_CONFIG_KEY_0", "credential.https://example.invalid/re%2.helper"),
            ("GIT_CONFIG_COUNT", "50000000"),
            ("GIT_CONFIG_COUNT", "1"),
            ("GIT_CONFIG_KEY_7", "credential.https://example.invalid/repo.helper"),
        ):
            with self.subTest(name=name, value=value):
                self.assertTrue(denied(before_shell(command, env={**base, name: value})))
        for missing in ("GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_1", "GIT_CONFIG_VALUE_1"):
            with self.subTest(missing=missing):
                self.assertTrue(denied(before_shell(command, env={k: v for k, v in base.items() if k != missing})))

    def test_explicit_system_git_and_identity_still_check_the_intended_index(self):
        system_git = shutil.which("git", path="/usr/bin:/bin")
        with tempfile.TemporaryDirectory() as root:
            subprocess.run([system_git, "init", "-q", root], check=True)
            # Bare git could resolve to a workspace executable here.
            env = {**transport_environment(), "PATH": ".", "GIT_COMMITTER_NAME": "Tester"}
            command = (f"GIT_AUTHOR_NAME=Tester MIRKET_CLEANUP_DONE=1 {system_git}"
                       f" -C {shlex.quote(root)} commit -m reviewed")
            self.assertEqual(before_shell(command, env=env), {})
            self.assertTrue(denied(before_shell(command.replace("MIRKET_CLEANUP_DONE=1 ", ""), env=env)))
            self.assertTrue(denied(before_shell(command, env={**env, "GIT_INDEX_FILE": "other"})))
            work = Path(root) / ".work" / "recover"
            work.mkdir(parents=True)
            (work / "private").touch()
            subprocess.run([system_git, "-C", root, "add", "-f", ".work/recover/private"], check=True)
            result = before_shell(command, env=env)
            self.assertIn(".work/recover/private", result["hookSpecificOutput"]["permissionDecisionReason"])

    def test_transport_values_stay_out_of_probes_and_errors(self):
        hook = runpy.run_path(str(HOOK))
        env = transport_environment()
        marker = "inert-test-helper-value"
        env["GIT_CONFIG_VALUE_1"] = marker
        env["PATH"] = os.defpath
        command = f"MIRKET_CLEANUP_DONE=1 git -C {REPOSITORY} commit -m first"
        payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command}}
        with patch.dict(os.environ, env, clear=True), patch("subprocess.run") as run:
            run.side_effect = [
                subprocess.CompletedProcess([], 0),
                subprocess.CalledProcessError(1, ["git"], stderr=marker.encode()),
            ]
            result = hook["handle"](payload)
        self.assertTrue(denied(result))
        self.assertIn("target Git index", result["hookSpecificOutput"]["permissionDecisionReason"])
        self.assertNotIn(marker, json.dumps(result))
        self.assertEqual(run.call_count, 2)
        for call in run.call_args_list:
            child_env = call.kwargs["env"]
            self.assertFalse(any(name.startswith("GIT_CONFIG_") for name in child_env))
            self.assertNotIn(marker, child_env.values())
            self.assertEqual(child_env["GIT_ALLOW_PROTOCOL"], "")
            self.assertIn("--no-lazy-fetch", call.args[0])

    def test_quoted_and_escaped_operators_are_commit_arguments(self):
        for message in ("'|'", r"\;", '"("'):
            with self.subTest(message=message):
                self.assertEqual(before_shell(f"MIRKET_CLEANUP_DONE=1 git -C {REPOSITORY} commit -m {message} --allow-empty"), {})

    def test_supported_commit_previews_do_not_need_cleanup_or_a_target(self):
        for command in (
            "git commit --dry-run",
            "MIRKET_CLEANUP_DONE=1 git commit --dry-run",
            "git commit --dry-run -a",
            "git commit --dry-run -- path/to/file",
            "git commit --short -- path/to/file",
            "env git -C . commit -m 'Preview only' --dry-run",
            "command git commit --no-dry-run --dry-run",
            "git commit -h",
            "git commit --help",
        ):
            with self.subTest(command=command):
                self.assertEqual(before_shell(command), {})

    def test_status_output_options_are_native_previews(self):
        with tempfile.TemporaryDirectory() as root:
            subprocess.run(["git", "init", "-q", root], check=True)
            (Path(root) / "staged").touch()
            subprocess.run(["git", "-C", root, "add", "staged"], check=True)
            for option in ("--short", "--porcelain", "--long", "-z", "--null"):
                with self.subTest(option=option):
                    args = ["git", "commit", option, "--no-dry-run", "-m", "preview"]
                    subprocess.run(args, cwd=root, check=True, capture_output=True)
                    head = subprocess.run(["git", "rev-parse", "--verify", "HEAD"], cwd=root, capture_output=True)
                    self.assertNotEqual(head.returncode, 0)
                    self.assertEqual(before_shell(" ".join(args)), {})

    def test_commit_options_and_messages_do_not_accidentally_enable_preview(self):
        for args in ("--dry-run --no-dry-run", "-m --dry-run", "--message=--dry-run", "-- --dry-run",
                     "-m --short", "-F -z", "--message=--help", "-- --porcelain"):
            with self.subTest(args=args):
                self.assertTrue(denied(before_shell(f"git commit {args}")))

    def test_unsupported_preview_guidance_keeps_the_operation_read_only(self):
        result = before_shell("git commit --dry-run | cat")
        self.assertTrue(denied(result))
        self.assertIn("--dry-run", result["hookSpecificOutput"]["permissionDecisionReason"])

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
            result = invoke({**payload, "tool_input": {"command": f"MIRKET_CLEANUP_DONE=1 git -C {shlex.quote(root)} commit -m x"}},
                            env={**os.environ, "PATH": "." + os.pathsep + os.defpath})
            self.assertTrue(denied(result))
            self.assertIn("PATH", result["hookSpecificOutput"]["permissionDecisionReason"])
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
            result = invoke({**payload, "tool_input": {"command": f"MIRKET_CLEANUP_DONE=1 git -C {shlex.quote(root)} commit -m x"}})
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
        self.assertIn("MIRKET_CLEANUP_DONE=1 git -C", reason)

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

    def test_ordinary_heredocs_are_quiet(self):
        self.assertEqual(before_shell("python3 - <<'PY'\nprint('ready')\nPY"), {})

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

    def test_workspace_records_can_be_committed_without_an_exception(self):
        with tempfile.TemporaryDirectory() as root:
            subprocess.run(["git", "init", "-q", root], check=True)
            work = Path(root) / ".work"
            for directory in ("plans", "briefs", "decisions", "temp-notes", ""):
                destination = work / directory
                destination.mkdir(parents=True, exist_ok=True)
                (destination / "record.md").touch()
            subprocess.run(["git", "-C", root, "add", ".work"], check=True)
            command = f"MIRKET_CLEANUP_DONE=1 git -C {shlex.quote(root)} commit -m records"
            self.assertEqual(before_shell(command), {})

    def test_device_routine_is_ignored_and_blocked_if_force_added(self):
        with tempfile.TemporaryDirectory() as root:
            project = Path(root)
            subprocess.run(["git", "init", "-q", root], check=True)
            (project / ".gitignore").write_bytes((HOOK.parents[1] / ".gitignore").read_bytes())
            routine = project / ".work/routines/deploy.md"
            routine.parent.mkdir(parents=True)
            routine.touch()
            path = routine.relative_to(project).as_posix()
            subprocess.run(["git", "-C", root, "check-ignore", "-q", "--", path], check=True)
            subprocess.run(["git", "-C", root, "add", "-f", "--", path], check=True)
            command = f"MIRKET_CLEANUP_DONE=1 git -C {shlex.quote(root)} commit -m routine"
            result = before_shell(command)
            self.assertTrue(denied(result))
            self.assertIn(path, result["hookSpecificOutput"]["permissionDecisionReason"])

    def test_staged_work_is_blocked_even_after_cleanup_acknowledgment(self):
        with tempfile.TemporaryDirectory() as root:
            subprocess.run(["git", "init", "-q", root], check=True)
            work = Path(root) / ".work" / "temp"
            work.mkdir(parents=True)
            (work / "private.txt").write_text("private")
            subprocess.run(["git", "-C", root, "add", ".work/temp/private.txt"], check=True)
            def request(command):
                return before_shell(command.replace("git commit", f"git -C {shlex.quote(root)} commit"), cwd=root)
            result = request("MIRKET_CLEANUP_DONE=1 git commit -m x")
            self.assertTrue(denied(result))
            self.assertIn(".work/temp/private.txt", result["hookSpecificOutput"]["permissionDecisionReason"])
            self.assertEqual(request("MIRKET_CLEANUP_DONE=1 MIRKET_WORK_EXCEPTION=.work/temp/private.txt git commit -m x"), {})
            self.assertTrue(denied(request("MIRKET_CLEANUP_DONE=1 MIRKET_WORK_EXCEPTION=.work/temp/other.txt git commit -m x")))
            (work / "other.txt").write_text("other")
            subprocess.run(["git", "-C", root, "add", ".work/temp/other.txt"], check=True)
            self.assertTrue(denied(request("MIRKET_CLEANUP_DONE=1 MIRKET_WORK_EXCEPTION=.work/temp/private.txt git commit -m x")))

    def test_staged_work_targets_git_c_directory(self):
        with tempfile.TemporaryDirectory() as root:
            session = Path(root) / "session"
            target = Path(root) / "target project"
            subprocess.run(["git", "init", "-q", str(session)], check=True)
            subprocess.run(["git", "init", "-q", str(target)], check=True)
            subprocess.run(["git", "-C", str(target), "config", "diff.relative", "true"], check=True)
            (target / "nested").mkdir()
            work = target / ".work" / "stashes"
            work.mkdir(parents=True)
            (work / "secret").write_text("x")
            subprocess.run(["git", "-C", str(target), "add", ".work/stashes/secret"], check=True)
            for prefix in ("git", "git -C ."):
                result = before_shell(f"MIRKET_CLEANUP_DONE=1 {prefix} commit -m x", cwd=session)
                self.assertTrue(denied(result))
                self.assertIn("absolute", result["hookSpecificOutput"]["permissionDecisionReason"])
            payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "cwd": str(session),
                       "tool_input": {"command": f"MIRKET_CLEANUP_DONE=1 git -C {shlex.quote(str(target))} -C nested commit -m x"}}
            result = invoke(payload)
            self.assertTrue(denied(result))
            self.assertIn(".work/stashes/secret", result["hookSpecificOutput"]["permissionDecisionReason"])
            result = invoke(payload, env={**os.environ, "GIT_INDEX_FILE": str(target / "alternate-index")})
            self.assertTrue(denied(result))
            self.assertIn("inherited GIT_*", result["hookSpecificOutput"]["permissionDecisionReason"])

    def test_index_inspection_failure_blocks_an_acknowledged_commit(self):
        with tempfile.TemporaryDirectory() as root:
            result = before_shell(f"MIRKET_CLEANUP_DONE=1 git -C {shlex.quote(root)} commit -m x", cwd=HOOK.parents[1])
            self.assertTrue(denied(result))
            self.assertIn("target Git index", result["hookSpecificOutput"]["permissionDecisionReason"])

    def test_compound_commands_cannot_change_index_before_inspection(self):
        for command in ("git add -f .work/a && MIRKET_CLEANUP_DONE=1 git commit -m x",
                        "cd other && MIRKET_CLEANUP_DONE=1 git commit -m x",
                        "MIRKET_CLEANUP_DONE=1 git commit -m x && MIRKET_CLEANUP_DONE=1 git commit -m y",
                        f"git commit --dry-run && MIRKET_CLEANUP_DONE=1 git -C {REPOSITORY} commit -m x"):
            with self.subTest(command=command):
                self.assertTrue(denied(before_shell(command)))


if __name__ == "__main__":
    unittest.main()
