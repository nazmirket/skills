"""Exercise the packaged Execute lifecycle event contracts."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
HOOKS = ROOT / "hooks"
EXECUTE = HOOKS / "execute.py"
SKILL = ROOT / "skills/execute/SKILL.md"


def invoke(payload):
    result = subprocess.run(
        [sys.executable, "-I", str(EXECUTE)],
        input=payload if isinstance(payload, str) else json.dumps(payload),
        text=True, capture_output=True, check=True,
    )
    return json.loads(result.stdout)


class ExecuteHookTest(unittest.TestCase):
    def test_guidance_runs_at_session_start_only(self):
        hooks = json.loads((HOOKS / "hooks.json").read_text())["hooks"]
        guidance_events = [event for event, groups in hooks.items() for group in groups
                           for hook in group["hooks"] if "/hooks/execute.py" in hook["command"]]
        self.assertEqual(guidance_events, ["SessionStart"])
        self.assertNotIn("UserPromptSubmit", hooks)

    def test_session_context_points_to_installed_guidance(self):
        self.assertTrue(SKILL.is_file())
        for source in ("startup", "resume", "compact"):
            with self.subTest(source=source):
                output = invoke({"hook_event_name": "SessionStart", "source": source})["hookSpecificOutput"]
                self.assertEqual(output["hookEventName"], "SessionStart")
                context = output["additionalContext"]
                self.assertIn(str(SKILL), context)
                self.assertLess(len(context) - len(str(SKILL)), 160)

    def test_unknown_or_invalid_events_have_no_effect(self):
        for payload in ("", "{", [], {"hook_event_name": "Stop"},
                        {"hook_event_name": "UserPromptSubmit", "prompt": "private sample prompt"}):
            with self.subTest(payload=payload):
                self.assertEqual(invoke(payload), {})


if __name__ == "__main__":
    unittest.main()
