"""Exercise installer safeguards without invoking or installing Hindsight."""

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
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
    @patch.object(installer.subprocess, "run")
    def test_installer_selects_local_daemon_and_codex(self, run, _mcp, _which, _connect):
        with patch.object(installer.Path, "home", return_value=self.home), patch.dict(
            os.environ, {"HINDSIGHT_API_LLM_PROVIDER": "openai-codex"}
        ), patch.object(installer.sys, "argv", ["install.py"]):
            self.assertEqual(installer.main(), 0)
        run.assert_called_once_with(
            ["npx", "-y", installer.PACKAGE, "install", "codex", "--server", "daemon"], check=True
        )


if __name__ == "__main__":
    unittest.main()
