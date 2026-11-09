#!/usr/bin/env python3
"""Request cleanup before delivery or a supported agent-shell commit."""

import json
import os
from pathlib import Path
import re
import shlex
import subprocess
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


def commit_details(tokens):
    i = 0
    acknowledged = False
    exception = None
    git_environment = False
    while i < len(tokens):
        token = tokens[i]
        if ASSIGNMENT.match(token):
            if token.startswith("MIRKET_CLEANUP_DONE="):
                acknowledged = token == MARKER
            if token.startswith("MIRKET_WORK_EXCEPTION="):
                exception = token.partition("=")[2]
            if token.startswith("GIT_"):
                git_environment = True
            i += 1
        elif token in {"env", "command"}:
            i += 1
            if i < len(tokens) and tokens[i] == "--":
                i += 1
            # Options that modify env or execute another shell are not parsed.
            if i < len(tokens) and tokens[i].startswith("-"):
                return None
        else:
            break
    if i >= len(tokens) or os.path.basename(tokens[i]) != "git":
        return None
    git = tokens[i]
    i += 1
    options = []
    while i < len(tokens):
        token = tokens[i]
        if token in GIT_OPTIONS_WITH_VALUE:
            if i + 1 >= len(tokens):
                return None
            options.extend(tokens[i:i + 2])
            i += 2
        elif token.startswith("-"):
            options.append(token)
            i += 1
        else:
            if token == "commit":
                return git, options, acknowledged, exception, git_environment
            return None
    return None


def deny(reason):
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}


def check_staged_work(details, cwd):
    git, options, _, exception, git_environment = details
    if git_environment:
        return deny("Mirket cannot safely determine the index when command-local GIT_* variables are set. Inspect the target index and use a supported direct commit command.")
    try:
        result = subprocess.run([git, *options, "diff", "--cached", "--no-ext-diff", "--no-renames", "--name-only", "-z", "--diff-filter=ACMRT", "--", ":(top).work"], cwd=cwd, capture_output=True, timeout=3, check=True)
    except (OSError, subprocess.SubprocessError):
        return deny("Mirket could not inspect the target Git index for staged .work files. Resolve the index or repository access issue before committing.")
    paths = [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]
    # A marker records the agent's assertion, not human authorization.
    blocked = [path for path in paths if path != exception]
    if blocked:
        return deny("Staged .work files require an explicitly named human exception: " + ", ".join(repr(path) for path in blocked) + ". Unstage them, or only when the human explicitly authorizes one exact path, retry with MIRKET_WORK_EXCEPTION=<that-path>. The marker does not prove authorization.")
    return None


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
        parts = list(segments(command if heredoc is None else command[:heredoc]))
        commits = [details for part in parts if (details := commit_details(part))]
        uncertain = any("git" in part and "commit" in part and part[0] not in {"echo", "printf"} and not commit_details(part) for part in parts)
    except ValueError:
        return {"systemMessage": "Mirket could not parse the shell command; pre-commit cleanup coverage is unknown."}
    if not commits:
        if heredoc is not None:
            return {"systemMessage": "Mirket did not fully inspect a shell command containing a heredoc or here-string for pre-commit cleanup."}
        if uncertain:
            return {"systemMessage": "Mirket could not determine whether this shell command runs git commit; pre-commit cleanup and staged .work coverage are unknown."}
        return {}
    if any(not details[2] for details in commits):
        return deny(
                f"Before committing, read {SKILL} and perform its repository-wide cleanup review. "
                "Preserve unrelated changes and historical evidence; do not auto-stage. "
                "Then retry each commit with MIRKET_CLEANUP_DONE=1 in that command, "
                "for example: MIRKET_CLEANUP_DONE=1 git commit -m 'message'. "
                "The marker acknowledges the review and does not prove cleanup occurred."
        )
    if len(parts) != 1 or heredoc is not None:
        return deny("Mirket cannot reliably inspect the final target index inside a compound command or heredoc. Run each git commit as a separate direct shell command after the preceding commands finish.")
    for details in commits:
        result = check_staged_work(details, payload.get("cwd") or os.getcwd())
        if result:
            return result
    if uncertain:
        return {"systemMessage": "Mirket could not determine whether part of this shell command runs git commit; pre-commit cleanup and staged .work coverage are unknown for that part."}
    if heredoc is not None:
        return {"systemMessage": "Mirket did not fully inspect a shell command containing a heredoc or here-string for pre-commit cleanup."}
    return {}


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
