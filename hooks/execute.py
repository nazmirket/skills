#!/usr/bin/env python3
"""Inject Execute guidance at session and turn start."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
EXECUTE = ROOT / "skills" / "execute" / "SKILL.md"
CLEAN = ROOT / "skills" / "clean" / "SKILL.md"
ROUTING = ROOT / "skills" / "execute" / "references" / "Routing.md"

GUIDANCE = (
    "Execute: choose one Mirket skill to own each outcome and read it if it is not already in context. "
    "Take the simplest complete path within existing authority. Preserve quality and run the "
    "narrowest meaningful check plus required checks. Skip routine narration; speak when the human needs "
    "to act, expectations change, or a material assumption or blocker matters. Lead the final reply with "
    "the result, useful verification, and material limits."
)


def handle(payload):
    event = payload.get("hook_event_name") if isinstance(payload, dict) else None
    if event == "SessionStart":
        context = (
            f"{GUIDANCE} Apply {EXECUTE} throughout the session. "
            "Add supporting skills only for distinct unresolved questions; they return evidence to that owner. "
            f"If ownership is unclear, consult {ROUTING}."
        )
    elif event == "UserPromptSubmit":
        context = (
            f"{GUIDANCE} If the task made changes or produced an artifact, apply {CLEAN} before delivery."
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
