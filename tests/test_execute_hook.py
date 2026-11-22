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
CLEAN = ROOT / "skills/clean/SKILL.md"
ROUTING = ROOT / "skills/execute/references/Routing.md"


def invoke(payload):
    result = subprocess.run(
        [sys.executable, "-I", str(EXECUTE)],
        input=payload if isinstance(payload, str) else json.dumps(payload),
        text=True, capture_output=True, check=True,
    )
    return json.loads(result.stdout)


class ExecuteHookTest(unittest.TestCase):
    def test_session_and_prompt_share_execute_hook(self):
        hooks = json.loads((HOOKS / "hooks.json").read_text())["hooks"]
        for event in ("SessionStart", "UserPromptSubmit"):
            with self.subTest(event=event):
                commands = [hook["command"] for group in hooks[event] for hook in group["hooks"]]
                self.assertEqual(commands, ['python3 -I "${CLAUDE_PLUGIN_ROOT}/hooks/execute.py"'])

    def test_session_context_sets_action_and_final_reporting(self):
        for source in ("startup", "resume", "compact"):
            with self.subTest(source=source):
                output = invoke({"hook_event_name": "SessionStart", "source": source})["hookSpecificOutput"]
                self.assertEqual(output["hookEventName"], "SessionStart")
                self.assertIn("within existing authority", output["additionalContext"])
                self.assertIn("simplest complete path", output["additionalContext"])
                self.assertIn("return evidence to that owner", output["additionalContext"])
                self.assertIn("reference needed for the task", output["additionalContext"])
                self.assertIn("lowercase backticks", output["additionalContext"])
                self.assertIn("supporting skills only for distinct unresolved questions", output["additionalContext"])
                self.assertIn(str(SKILL), output["additionalContext"])
                self.assertIn(str(ROUTING), output["additionalContext"])
                self.assertTrue(SKILL.is_file())
                self.assertTrue(ROUTING.is_file())

    def test_prompt_context_can_stand_alone_without_echoing_prompt(self):
        output = invoke({"hook_event_name": "UserPromptSubmit", "prompt": "private sample prompt"})["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "UserPromptSubmit")
        context = output["additionalContext"]
        self.assertIn("Execute", context)
        self.assertIn("Keep temporary artifacts in .work/temp/<task>/", context)
        self.assertIn("one owner per outcome", context)
        self.assertIn("reference needed for the task", context)
        self.assertIn("lowercase backticks", context)
        self.assertIn("within scope", context)
        self.assertIn("focused and required checks", context)
        self.assertIn("before delivering edits or artifacts", context)
        self.assertNotIn(str(ROUTING), context)
        self.assertLess(len(context) - len(str(CLEAN)), 350)
        self.assertIn(str(CLEAN), context)
        self.assertNotIn("private sample prompt", context)

    def test_unknown_or_invalid_events_have_no_effect(self):
        for payload in ("", "{", [], {"hook_event_name": "Stop"}):
            with self.subTest(payload=payload):
                self.assertEqual(invoke(payload), {})


if __name__ == "__main__":
    unittest.main()
