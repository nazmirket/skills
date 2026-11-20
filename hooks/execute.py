#!/usr/bin/env python3
"""Inject Execute guidance at session and turn start."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
EXECUTE = ROOT / "skills" / "execute" / "SKILL.md"
CLEAN = ROOT / "skills" / "clean" / "SKILL.md"
ROUTING = ROOT / "skills" / "execute" / "references" / "Routing.md"

SELECTION = (
    "Choose one Mirket owner per outcome. Read selected skills missing from context. "
    "Announce them with lowercase backticked names, as in ‘I’ll use `execute` and `design` skills.’"
)


def handle(payload):
    event = payload.get("hook_event_name") if isinstance(payload, dict) else None
    if event == "SessionStart":
        context = (
            f"Apply {EXECUTE} throughout the session. {SELECTION} "
            "Take the simplest complete path within existing authority. Run the narrowest meaningful check "
            "plus required checks. Skip routine narration. Report the result, verification and material limits. "
            "Add supporting skills only for distinct unresolved questions; they return evidence to that owner. "
            f"If ownership is unclear, consult {ROUTING}."
        )
    elif event == "UserPromptSubmit":
        context = (
            f"Apply Execute. {SELECTION} Work directly within scope, run focused and required checks, "
            f"and skip routine narration. Apply {CLEAN} before delivering edits or artifacts."
        )
    else:
        return {}
    return {"hookSpecificOutput": {"hookEventName": event, "additionalContext": context}}


if __name__ == "__main__":
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        payload = None
    print(json.dumps(handle(payload)))
