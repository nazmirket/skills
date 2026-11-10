"""Exercise installer safeguards without invoking or installing Hindsight."""

import importlib.util
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
            installer.registry.SURVEY_RECEIPT, launcher)))
        (dist / installer.registry.SCRIPTS["prompt"]).write_text(launcher)
        (dist / "deepen.js").write_text(installer.registry.SURVEY_RECEIPT)
        path = self.home / ".codex/hooks.json"
        path.parent.mkdir()
        hooks = {event: [{"hooks": [{"command": f"node {dist / installer.registry.SCRIPTS[mode]}"}]}]
                 for event, mode in installer.HOOKS.items()}
        hooks["Stop"].append({"hooks": [{"command": "unrelated"}]})
        path.write_text(json.dumps({"hooks": hooks}))
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
        codex_config.write_text("# existing settings\n")
        config = root / "coding-agent.json"
        original = {path: path.read_bytes() for path in (config, hooks, codex_config)}
        server = {"transport": {"args": [str(dist / "mcp-server.js")]}}

        def run(cmd, **kwargs):
            if cmd[0] == "codex":
                codex_config.write_text("# partial MCP edit\n")
                raise CalledProcessError(1, cmd)

        with patch.object(installer, "codex_mcp", return_value=server), patch.object(installer.subprocess, "run", side_effect=run):
            with self.assertRaises(CalledProcessError):
                installer.wire(self.home)
        self.assertEqual({path: path.read_bytes() for path in original}, original)
        self.assertFalse((root / "mirket/project_registry.py").exists())
        self.assertFalse((dist / installer.registry.SURVEY_ENTRY).exists())


if __name__ == "__main__":
    unittest.main()
