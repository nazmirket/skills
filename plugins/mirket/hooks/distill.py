#!/usr/bin/env python3
"""Request Distill guidance at the start of each user prompt."""

import json
from pathlib import Path

skills = Path(__file__).resolve().parent.parent / "skills"
distill = skills / "distill" / "SKILL.md"
clean = skills / "clean" / "SKILL.md"
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": f"Read {distill} and apply it to every user-facing message in this turn. Before delivery, apply {clean} when relevant. Respect the user's instructions and higher-priority rules.",
}}))
