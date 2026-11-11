#!/usr/bin/env python3
"""Inject compact Distill guidance at session and turn start."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
CLEAN = ROOT / "skills" / "clean" / "SKILL.md"
ROUTING = ROOT / "references" / "Routing.md"


def handle(payload):
    event = payload.get("hook_event_name") if isinstance(payload, dict) else None
    if event == "SessionStart":
        context = (
            "Distill throughout the session: do authorized work directly. Skip routine narration; "
            "report material progress or blockers. Lead final replies with the result, then verified "
            "checks and material limits. Keep the depth the user needs. "
            "Choose one Mirket skill to own each outcome; supporting skills return evidence to that owner. "
            f"If ownership is unclear, consult {ROUTING}."
        )
    elif event == "UserPromptSubmit":
        context = (
            "Distill: do authorized work directly; report meaningful progress only. Before sending, "
            f"lead with the result and verified facts, and cut repetition. Apply {CLEAN} when relevant."
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
