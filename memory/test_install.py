"""Exercise installer safeguards without invoking or installing Hindsight."""

import importlib.util
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from subprocess import CalledProcessError
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("memory_install", Path(__file__).with_name("install.py"))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)

    def test_rejects_unparseable_or_non_object_hooks(self):
        hooks = self.home / ".codex/hooks.json"
        hooks.parent.mkdir()
        for content in ("{invalid", "[]", "null", '{"hooks":[]}', '{"hooks":{"Stop":"bad"}}'):
            with self.subTest(content=content):
                hooks.write_text(content)
                with self.assertRaisesRegex(ValueError, "hooks.json"):
                    installer.check_existing(self.home)

    def test_preserves_existing_hindsight_config(self):
        config = self.home / ".hindsight/coding-agent.json"
        config.parent.mkdir()
        config.write_text('{"serverMode":"cloud"}')
        with self.assertRaisesRegex(ValueError, "already exists"):
            installer.check_existing(self.home)
        self.assertIn('"cloud"', config.read_text())

    @patch.object(installer.socket, "create_connection", side_effect=OSError("no listener"))
    def test_valid_existing_hooks_are_accepted(self, _connect):
        hooks = self.home / ".codex/hooks.json"
        hooks.parent.mkdir()
        hooks.write_text('{"hooks":{"Stop":[]}}')
        installer.check_existing(self.home)

    def test_alternate_hindsight_configuration_is_not_overwritten(self):
        with patch.dict(os.environ, {"HINDSIGHT_CONFIG": "/another/config.json"}):
            with self.assertRaisesRegex(ValueError, "HINDSIGHT_CONFIG"):
                installer.check_existing(self.home)

    @patch.object(installer.subprocess, "run")
    def test_existing_hindsight_mcp_is_not_replaced(self, run):
        run.return_value.stdout = '[{"name":"hindsight"}]'
        with self.assertRaisesRegex(ValueError, "MCP"):
            installer.check_codex_mcp()

    @patch.object(installer.socket, "create_connection")
    def test_running_service_prevents_silent_adoption(self, _connect):
        with self.assertRaisesRegex(ValueError, "9077"):
            installer.check_existing(self.home)

    @patch.object(installer.shutil, "which", return_value=None)
    def test_missing_tools_are_reported(self, _which):
        with self.assertRaisesRegex(ValueError, "npx"):
            installer.check_requirements()

    @patch.object(installer.socket, "create_connection", side_effect=OSError("no listener"))
    @patch.object(installer.shutil, "which", return_value="/stub")
    @patch.object(installer, "check_codex_mcp")
    @patch.object(installer, "wire")
    @patch.object(installer.subprocess, "run")
    def test_installer_selects_local_daemon_and_codex(self, run, wire, _mcp, _which, _connect):
        with patch.object(installer.Path, "home", return_value=self.home), patch.dict(
            os.environ, {"HINDSIGHT_API_LLM_PROVIDER": "openai-codex"}
        ), patch.object(installer.sys, "argv", ["install.py"]):
            self.assertEqual(installer.main(), 0)
        run.assert_called_once_with(
            ["npx", "-y", installer.PACKAGE, "install", "codex", "--server", "daemon"], check=True
        )
        wire.assert_called_once_with(self.home, "openai-codex")

    def stock_wiring(self):
        root = self.home / ".hindsight"
        dist = root / "coding-agents/dist"
        dist.mkdir(parents=True)
        (dist.parent / "package.json").write_text('{"version":"0.8.6"}')
        (root / "coding-agent.json").write_text('{"serverMode":"daemon"}')
        launcher = 'join5(dirname4(fileURLToPath(import.meta.url)), "deepen.js")'
        (dist / installer.registry.SCRIPTS["start"]).write_text("\n".join((
            installer.registry.SURVEY_COMMAND, installer.registry.SURVEY_ARGS,
            installer.registry.SURVEY_RECEIPT, launcher,
            "              for (const id of markers) {", installer.registry.SURVEY_CADENCE)))
        (dist / installer.registry.SCRIPTS["prompt"]).write_text(launcher)
        (dist / "deepen.js").write_text(installer.registry.SURVEY_RECEIPT + '\n' +
            '          const behind = commitsSince(REPO, sha);\n' +
            '        if (best) {\nmetadata: Object.keys(stamp.metadata).length ? stamp.metadata : void 0\n}\n' +
            '    await client.drain(client.opIds, "extraction");')
        (dist / "mcp-server.js").write_text(
            'function loadConfig() {}\nfunction applyBankConfig() {}\n'
            'if (process.argv[1] === fileURLToPath3(import.meta.url)) {}\n')
        path = self.home / ".codex/hooks.json"
        path.parent.mkdir()
        hooks = {event: [{"hooks": [{"command": f"node {dist / installer.registry.SCRIPTS[mode]}"}]}]
                 for event, mode in installer.HOOKS.items()}
        hooks["Stop"].append({"hooks": [{"command": "unrelated"}]})
        path.write_text(json.dumps({"hooks": hooks}))
        (path.parent / "config.toml").write_text('[mcp_servers.hindsight]\ncommand = "node"\nargs = [' + json.dumps(str(dist / "mcp-server.js")) + ']\n')
        return root, dist, path

    def test_wiring_keeps_other_hooks_and_routes_all_hindsight_events(self):
        self.stock_wiring()
        config, updated, adapter, env = installer.wiring(self.home)
        self.assertEqual(config["harnesses"]["codex"]["autoInject"], "pages")
        self.assertEqual(updated["hooks"]["Stop"][-1]["hooks"][0]["command"], "unrelated")
        self.assertIn("project_registry.py stop", updated["hooks"]["Stop"][0]["hooks"][0]["command"])
        self.assertIn("MIRKET_HINDSIGHT_EXPECTED_BANK", adapter[installer.registry.SURVEY_ENTRY])
        self.assertIn("SURVEY_DOC_IDS.every", adapter[installer.registry.DEEPEN_ENTRY])
        self.assertEqual(env["HINDSIGHT_MCP_HARNESS"], "codex")

    def test_wire_rolls_back_when_codex_rejects_mcp_registration(self):
        root, dist, hooks = self.stock_wiring()
        codex_config = self.home / ".codex/config.toml"
        codex_config.write_text("# existing settings\n" + codex_config.read_text())
        config = root / "coding-agent.json"
        original = {path: path.read_bytes() for path in (config, hooks, codex_config)}
        server = {"transport": {"command": "node", "args": [str(dist / "mcp-server.js")]}}

        def run(cmd, **kwargs):
            if cmd[0] == "codex":
                codex_config.write_text("# partial MCP edit\n")
                raise CalledProcessError(1, cmd)

        with patch.object(installer, "codex_mcp", return_value=server), patch.object(installer, "plain_upstream_mcp"), patch.object(installer.subprocess, "run", side_effect=run):
            with self.assertRaises(CalledProcessError):
                installer.wire(self.home)
        self.assertEqual({path: path.read_bytes() for path in original}, original)
        self.assertFalse((root / "mirket/project_registry.py").exists())
        self.assertFalse((dist / installer.registry.SURVEY_ENTRY).exists())

    def test_rewire_preserves_hook_capture_environment(self):
        _, _, path = self.stock_wiring()
        hooks = json.loads(path.read_text())
        entry = hooks["hooks"]["Stop"][0]["hooks"][0]
        entry["command"] = "env HINDSIGHT_OPT_IN_ONLY=true HINDSIGHT_RETAIN_SESSIONS=false " + entry["command"]
        path.write_text(json.dumps(hooks))
        _, updated, _, _ = installer.wiring(self.home)
        _, env = installer.launcher(updated["hooks"]["Stop"][0]["hooks"][0]["command"])
        self.assertEqual(env["HINDSIGHT_OPT_IN_ONLY"], "true")
        self.assertEqual(env["HINDSIGHT_RETAIN_SESSIONS"], "false")

    def test_ambiguous_hook_is_rejected_before_writes(self):
        _, _, path = self.stock_wiring()
        hooks = json.loads(path.read_text())
        hooks["hooks"]["Stop"][0]["hooks"][0]["command"] += " && echo completed"
        path.write_text(json.dumps(hooks))
        before = path.read_bytes()
        with self.assertRaises(ValueError):
            installer.wiring(self.home)
        self.assertEqual(path.read_bytes(), before)

    def test_rewire_preserves_mcp_environment_and_refuses_disabled_registration(self):
        _, dist, _ = self.stock_wiring()
        original_env = {"HINDSIGHT_API_PORT": "9999", "HINDSIGHT_OPT_IN_ONLY": "true", "CUSTOM_SETTING": "preserved"}
        config = self.home / ".codex/config.toml"
        config.write_text(config.read_text() + '\n[mcp_servers.hindsight.env]\n' + ''.join(f'{key} = {json.dumps(value)}\n' for key, value in original_env.items()))
        server = {"enabled": True, "transport": {"command": "node", "args": [str(dist / "mcp-server.js")], "env": original_env}}
        calls = []
        with patch.object(installer, "codex_mcp", return_value=server), patch.object(installer, "plain_upstream_mcp"), patch.object(installer.subprocess, "run", side_effect=lambda cmd, **kw: calls.append(cmd)):
            installer.wire(self.home)
        command = next(cmd for cmd in calls if cmd[0] == "codex")
        for key, value in original_env.items():
            self.assertIn(f"{key}={value}", command)
        server["enabled"] = False
        with patch.object(installer, "codex_mcp", return_value=server):
            with self.assertRaisesRegex(ValueError, "disabled"):
                installer.wire(self.home)

    def test_raw_mcp_custom_fields_are_rejected_before_mutation(self):
        _, dist, hooks = self.stock_wiring()
        config = self.home / ".codex/config.toml"
        original = config.read_text()
        # The list projection does not expose enabled_tools/disabled_tools or
        # unknown future options. The raw file must be inspected independently.
        server = {"enabled": True, "transport": {"command": "node", "args": [str(dist / "mcp-server.js")]}}
        for field in ('enabled_tools = ["read"]', 'disabled_tools = ["write"]',
                      'startup_timeout_sec = 12', 'tool_timeout_sec = 60', 'future_option = "keep"'):
            with self.subTest(field=field):
                config.write_text(original + field + "\n")
                before = {path: path.read_bytes() for path in (config, hooks)}
                parsed = {"mcp_servers": {"hindsight": {"command": "node", "args": server["transport"]["args"], field.split(" =")[0]: "custom"}}}
                with patch.object(installer, "codex_mcp", return_value=server), patch.object(installer, "runtime_toml", return_value=parsed), patch.object(installer.subprocess, "run") as run:
                    with self.assertRaisesRegex(ValueError, "Custom Hindsight MCP"):
                        installer.wire(self.home)
                # On Python 3.8 the sole allowed subprocess is the read-only TOML parser.
                self.assertFalse(any(call.args[0][0] == "codex" for call in run.call_args_list))
                self.assertEqual(before, {path: path.read_bytes() for path in before})
                self.assertFalse((self.home / ".hindsight/mirket/project_registry.py").exists())

    def test_wire_failure_does_not_print_preserved_credentials(self):
        secret = "sentinel-never-print-this"
        failure = CalledProcessError(1, ["codex", "mcp", "add", "hindsight", "--env", "HINDSIGHT_API_TOKEN=" + secret], output=secret, stderr=secret)
        output = io.StringIO()
        with patch.object(installer, "wire", side_effect=failure), patch.object(installer.sys, "argv", ["install.py", "--wire"]), contextlib.redirect_stderr(output):
            self.assertEqual(installer.main(), 1)
        self.assertNotIn(secret, output.getvalue())
        self.assertIn("exit 1", output.getvalue())

    @unittest.skipUnless(os.environ.get("MIRKET_TEST_RUNTIME"), "Set MIRKET_TEST_RUNTIME for bundled TOML parser parity")
    def test_python38_toml_fallback_reads_restrictions_without_running_installer(self):
        dist = Path(os.environ["MIRKET_TEST_RUNTIME"]) / "dist"
        parsed = installer.runtime_toml('[mcp_servers."hindsight"]\ncommand="node"\nargs=["test"]\nenabled_tools=["read"]\nfuture_option={nested=true}\n', dist)
        self.assertEqual(parsed["mcp_servers"]["hindsight"]["enabled_tools"], ["read"])
        self.assertEqual(parsed["mcp_servers"]["hindsight"]["future_option"], {"nested": True})

    @unittest.skipUnless(os.environ.get("MIRKET_TEST_RUNTIME"), "Set MIRKET_TEST_RUNTIME for real raw-TOML conversion guard")
    def test_real_raw_toml_guard_rejects_unreported_custom_options(self):
        _, dist, _ = self.stock_wiring()
        (dist / "installer.js").write_bytes((Path(os.environ["MIRKET_TEST_RUNTIME"]) / "dist/installer.js").read_bytes())
        config = self.home / ".codex/config.toml"
        transport = {"command": "node", "args": [str(dist / "mcp-server.js")]}
        installer.plain_upstream_mcp(self.home, dist, transport)
        original = config.read_text()
        for field in ('enabled_tools = ["read"]', 'disabled_tools = ["write"]', 'tool_timeout_sec = 60', 'future_option = {nested=true}'):
            config.write_text(original + field + "\n")
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "Custom Hindsight MCP"):
                installer.plain_upstream_mcp(self.home, dist, transport)

    def test_project_freshness_preserves_inherited_bank_policy(self):
        root, _, _ = self.stock_wiring()
        project = self.home / "project"
        project.mkdir()
        bank = "existing-bank"
        config_path = root / "coding-agent.json"
        config_path.write_text(json.dumps({"mapPathToBank": {str(project): bank},
            "banks": {bank: {"retainSessions": False, "autoSeed": False}},
            "harnesses": {"codex": {"mapPathToBank": {}, "autoUpdate": False}}}))
        server = {"enabled": True, "transport": {"args": [str(root / "mirket/project_registry.py"), "mcp"]}}
        with patch.object(installer, "codex_mcp", return_value=server), patch.object(installer.registry, "effective_config", return_value={"disabled": False}):
            result = installer.freshness_profile(self.home, project)
        updated = json.loads(config_path.read_text())["harnesses"]["codex"]["banks"][bank]
        self.assertFalse(updated["retainSessions"])
        self.assertFalse(updated["autoSeed"])
        self.assertEqual(updated["surveyRefreshCommits"], 1)
        self.assertFalse(result["capture_policy_changed"])
        self.assertTrue((Path(result["backup"]) / "coding-agent.json").is_file())


if __name__ == "__main__":
    unittest.main()
