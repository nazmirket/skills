#!/usr/bin/env python3
"""Point the session to the installed Execute skill."""

import json
from pathlib import Path
import sys

EXECUTE = Path(__file__).resolve().parents[1] / "skills" / "execute" / "SKILL.md"


def handle(payload):
    if not isinstance(payload, dict) or payload.get("hook_event_name") != "SessionStart":
        return {}
    return {"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": f"Apply `execute` throughout this session ({EXECUTE}). Reuse guidance in context and choose one owner per outcome.",
    }}


if __name__ == "__main__":
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        payload = None
    print(json.dumps(handle(payload)))
