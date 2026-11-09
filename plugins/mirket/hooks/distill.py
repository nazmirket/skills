#!/usr/bin/env python3
"""Request Distill guidance at the start of each user prompt."""

import json
from pathlib import Path

skill = Path(__file__).resolve().parent.parent / "skills" / "distill" / "SKILL.md"
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": f"Read {skill} and apply Distill to every user-facing message in this turn, respecting the user's instructions and higher-priority rules.",
}}))
