#!/usr/bin/env python3
"""Request cleanup before delivery or a supported agent-shell commit."""

import json
import os
from pathlib import Path
import re
import shlex
import sys

SKILL = str(Path(__file__).resolve().parent.parent / "skills" / "clean" / "SKILL.md")
MARKER = "MIRKET_CLEANUP_DONE=1"
ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=.*$", re.DOTALL)
SEPARATOR = re.compile(r"^[;&|()\n]+$")
GIT_OPTIONS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--config-env", "--exec-path"}


def heredoc_start(command):
    """Detect an unquoted heredoc or here-string operator without parsing its body."""
    quote = None
    index = 0
    while index < len(command):
        char = command[index]
        if char == "\\" and quote != "'":
            index += 2
            continue
        if quote:
            if char == quote:
                quote = None
        elif char in "\"'":
            quote = char
        elif command[index:index + 2] == "<<":
            return index
        index += 1
    return None


def strip_shell_comments(command):
    """Remove shell comments while retaining newlines and hashes inside words."""
    result = []
    quote = None
    word_start = True
    index = 0
    while index < len(command):
        char = command[index]
        if char == "\\" and quote != "'" and index + 1 < len(command):
            result.append(command[index:index + 2])
            if command[index + 1] != "\n":
                word_start = False
            index += 2
            continue
        if quote:
            if char == quote:
                quote = None
        elif char in "\"'":
            quote = char
            word_start = False
        elif char == "#" and word_start:
            end = command.find("\n", index)
            if end == -1:
                break
            index = end
            continue
        else:
            word_start = char in " \t\r\n;&|()<>"
        result.append(char)
        index += 1
    return "".join(result)


def segments(command):
    lexer = shlex.shlex(strip_shell_comments(command), posix=True, punctuation_chars=";&|()\n")
    lexer.whitespace = " \t\r"
    lexer.whitespace_split = True
    lexer.commenters = ""
    current = []
    for token in lexer:
        if SEPARATOR.fullmatch(token):
            if current:
                yield current
                current = []
        else:
            current.append(token)
    if current:
        yield current


def unacknowledged_commit(tokens):
    i = 0
    acknowledged = False
    while i < len(tokens):
        token = tokens[i]
        if ASSIGNMENT.match(token):
            if token.startswith("MIRKET_CLEANUP_DONE="):
                acknowledged = token == MARKER
            i += 1
        elif token in {"env", "command"}:
            i += 1
            if i < len(tokens) and tokens[i] == "--":
                i += 1
            # Options that modify env or execute another shell are not parsed.
            if i < len(tokens) and tokens[i].startswith("-"):
                return False
        else:
            break
    if i >= len(tokens) or os.path.basename(tokens[i]) != "git":
        return False
    i += 1
    while i < len(tokens):
        token = tokens[i]
        if token in GIT_OPTIONS_WITH_VALUE:
            i += 2
        elif token.startswith("-"):
            i += 1
        else:
            return token == "commit" and not acknowledged
    return False


def handle(payload):
    event = payload.get("hook_event_name")
    if event == "Stop" and "stop_hook_active" not in payload:
        return {"systemMessage": "Mirket cleanup was not requested: the Stop continuation flag is missing."}
    if event == "Stop" and not isinstance(payload.get("stop_hook_active"), bool):
        return {"systemMessage": "Mirket cleanup was not requested: the Stop continuation flag is invalid."}
    if event == "Stop" and payload.get("stop_hook_active") is False:
        return {
            "decision": "block",
            "reason": (
                f"Before delivering, read {SKILL} and perform its task-scoped cleanup review "
                "where relevant. Respect the user's scope, read-only restrictions and existing work; "
                "make no changes when cleanup is not applicable. Report any material gap."
            ),
        }
    if event != "PreToolUse" or payload.get("tool_name") != "Bash":
        return {}
    tool_input = payload.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str):
        return {"systemMessage": "Mirket could not inspect the shell command for pre-commit cleanup."}
    command = strip_shell_comments(command)
    heredoc = heredoc_start(command)
    try:
        needs_cleanup = any(unacknowledged_commit(part) for part in segments(command if heredoc is None else command[:heredoc]))
    except ValueError:
        return {"systemMessage": "Mirket could not parse the shell command; pre-commit cleanup coverage is unknown."}
    if not needs_cleanup:
        if heredoc is not None:
            return {"systemMessage": "Mirket did not fully inspect a shell command containing a heredoc or here-string for pre-commit cleanup."}
        return {}
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"Before committing, read {SKILL} and perform its repository-wide cleanup review. "
                "Preserve unrelated changes and historical evidence; do not auto-stage. "
                "Then retry each commit with MIRKET_CLEANUP_DONE=1 in that command, "
                "for example: MIRKET_CLEANUP_DONE=1 git commit -m 'message'. "
                "The marker acknowledges the review and does not prove cleanup occurred."
            ),
        }
    }


def main():
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        print(json.dumps({"systemMessage": "Mirket could not read the hook event; cleanup was not requested."}))
        return
    if not isinstance(payload, dict):
        print(json.dumps({"systemMessage": "Mirket received an invalid hook event; cleanup was not requested."}))
        return
    print(json.dumps(handle(payload)))


if __name__ == "__main__":
    main()
