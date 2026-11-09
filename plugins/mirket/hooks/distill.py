#!/usr/bin/env python3
"""Request Author and Distill guidance at the start of each user prompt."""

import json
from pathlib import Path

skills = Path(__file__).resolve().parent.parent / "skills"
author = skills / "author" / "SKILL.md"
distill = skills / "distill" / "SKILL.md"
clean = skills / "clean" / "SKILL.md"
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": f"Read {author} and {distill}; apply their lightweight combined pass to every user-facing message in this turn. Before delivery, apply {clean} when relevant. Respect the user's instructions and higher-priority rules.",
}}))
