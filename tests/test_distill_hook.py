"""Check the prompt hook's wiring and model-visible context, without testing the skill."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1] / "plugins/mirket"


class DistillHookTest(unittest.TestCase):
    def test_prompt_hook_requests_distill_with_an_installed_path(self):
        config = json.loads((ROOT / "hooks/hooks.json").read_text())
        command = config["hooks"]["UserPromptSubmit"][0]["hooks"][0]["command"]
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/hooks/distill.py", command)
        result = subprocess.run(
            [sys.executable, "-I", str(ROOT / "hooks/distill.py")],
            input=json.dumps({"hook_event_name": "UserPromptSubmit", "prompt": "hello"}),
            text=True, capture_output=True, check=True,
        )
        output = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "UserPromptSubmit")
        self.assertIn(str(ROOT / "skills/distill/SKILL.md"), output["additionalContext"])
        self.assertNotIn("hello", output["additionalContext"])


if __name__ == "__main__":
    unittest.main()
