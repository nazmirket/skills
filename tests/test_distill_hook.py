"""Exercise the packaged Distill lifecycle event contracts."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1] / "plugins/mirket"
HOOKS = ROOT / "hooks"
DISTILL = HOOKS / "distill.py"
CLEAN = ROOT / "skills/clean/SKILL.md"


def invoke(payload):
    result = subprocess.run(
        [sys.executable, "-I", str(DISTILL)],
        input=payload if isinstance(payload, str) else json.dumps(payload),
        text=True, capture_output=True, check=True,
    )
    return json.loads(result.stdout)


class DistillHookTest(unittest.TestCase):
    def test_session_and_prompt_share_distill_hook(self):
        hooks = json.loads((HOOKS / "hooks.json").read_text())["hooks"]
        for event in ("SessionStart", "UserPromptSubmit"):
            with self.subTest(event=event):
                commands = [hook["command"] for group in hooks[event] for hook in group["hooks"]]
                self.assertEqual(commands, ['python3 -I "${CLAUDE_PLUGIN_ROOT}/hooks/distill.py"'])

    def test_session_context_sets_action_and_final_reporting(self):
        for source in ("startup", "resume", "compact"):
            with self.subTest(source=source):
                output = invoke({"hook_event_name": "SessionStart", "source": source})["hookSpecificOutput"]
                self.assertEqual(output["hookEventName"], "SessionStart")
                self.assertIn("authorized work", output["additionalContext"])
                self.assertIn("verified checks", output["additionalContext"])

    def test_prompt_context_can_stand_alone_without_echoing_prompt(self):
        output = invoke({"hook_event_name": "UserPromptSubmit", "prompt": "private sample prompt"})["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "UserPromptSubmit")
        context = output["additionalContext"]
        self.assertIn("Distill", context)
        self.assertIn("Before sending", context)
        self.assertIn(str(CLEAN), context)
        self.assertNotIn(str(ROOT / "skills/distill/SKILL.md"), context)
        self.assertNotIn("private sample prompt", context)

    def test_unknown_or_invalid_events_have_no_effect(self):
        for payload in ("", "{", [], {"hook_event_name": "Stop"}):
            with self.subTest(payload=payload):
                self.assertEqual(invoke(payload), {})


if __name__ == "__main__":
    unittest.main()
