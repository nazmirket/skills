#!/usr/bin/env python3
"""Request cleanup before delivery or a supported agent-shell commit."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import NamedTuple, Optional

SKILL = str(Path(__file__).resolve().parent.parent / "skills" / "clean" / "SKILL.md")
MARKER = "MIRKET_CLEANUP_DONE=1"
ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=.*$", re.DOTALL)
SYSTEM_PATH = "/usr/bin:/bin"
GIT_OPTIONS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--config-env", "--exec-path"}
COMMIT_VALUES = {"-m", "-F", "-C", "-c", "--message", "--file", "--reuse-message", "--reedit-message", "--author", "--date"}
COMMIT_FLAGS = {"-q", "--quiet", "--amend", "--no-edit", "--allow-empty", "--allow-empty-message", "-s", "--signoff", "--no-signoff", "--no-gpg-sign"}


class Commit(NamedTuple):
    directories: list
    acknowledged: bool
    exception: Optional[str]
    problem: Optional[str]


def split_command(command):
    """Recognize literal words and operators without evaluating shell syntax."""
    parts, words, word = [], [], []
    quote = None
    started = dynamic = structural = heredoc = False
    i = 0

    def finish_word():
        nonlocal started
        if started:
            words.append("".join(word))
            word.clear()
            started = False

    def finish_part():
        finish_word()
        if words:
            parts.append(words.copy())
            words.clear()

    while i < len(command):
        char = command[i]
        i += 1
        if char == "\\" and quote != "'":
            if i == len(command):
                raise ValueError("incomplete escape")
            escaped = command[i]
            if quote is None or escaped in '\\"$`\n':
                i += 1
                if escaped == "\n":
                    continue
                char = escaped
            word.append(char)
        elif quote:
            if char == quote:
                quote = None
            else:
                word.append(char)
                dynamic |= quote == '"' and char in '$`!'
        elif char in "'\"":
            quote = char
        elif char == "#" and not started:
            end = command.find("\n", i)
            i = len(command) if end == -1 else end
            continue
        elif char in " \t":
            finish_word()
            continue
        elif char in ";&|()\n<>":
            finish_part()
            structural |= char not in ";\n"
            if char == "<" and command[i:i + 1] == "<":
                heredoc = True
                break
            continue
        else:
            word.append(char)
            dynamic |= char in "$`*?[]{}~!"
        started = True
    if quote:
        raise ValueError("unclosed quote")
    finish_part()
    return parts, structural, heredoc, dynamic


def uses_staged_index(args):
    """Accept only known commit arguments that do not change the staged inputs."""
    i = 0
    while i < len(args):
        token = args[i]
        i += 1
        if token in COMMIT_FLAGS or token == "-S" or token.startswith("--gpg-sign=") or token == "--gpg-sign":
            continue
        if token == "--":
            return i == len(args)
        if token in COMMIT_VALUES:
            if i == len(args):
                return False
            i += 1
            continue
        option = token.partition("=")[0]
        if (option.startswith("--") and option in COMMIT_VALUES and "=" in token) or (
            len(token) > 2 and token[:2] in COMMIT_VALUES and not token.startswith("--")
        ):
            continue
        return False
    return True


def commit_details(tokens):
    i = 0
    acknowledged = False
    exception = problem = None
    while i < len(tokens):
        token = tokens[i]
        if ASSIGNMENT.match(token):
            name, _, value = token.partition("=")
            if name == "MIRKET_CLEANUP_DONE":
                acknowledged = token == MARKER
            elif name == "MIRKET_WORK_EXCEPTION":
                exception = value
            else:
                problem = "command-local environment assignments"
            i += 1
        elif token in {"env", "command"}:
            i += 1
            if i < len(tokens) and tokens[i] == "--":
                i += 1
            if i < len(tokens) and tokens[i].startswith("-"):
                return None
        else:
            break
    if i == len(tokens) or os.path.basename(tokens[i]) != "git":
        return None
    if tokens[i] != "git":
        problem = "a path-qualified Git executable"
    i += 1
    directories = []
    while i < len(tokens) and tokens[i].startswith("-"):
        token = tokens[i]
        i += 1
        if token in GIT_OPTIONS_WITH_VALUE:
            if i == len(tokens):
                return None
            value = tokens[i]
            i += 1
        if token == "-C":
            directories.append(value)
        else:
            problem = "Git global options other than literal -C paths"
    if i == len(tokens) or tokens[i] != "commit":
        return None
    if not uses_staged_index(tokens[i + 1:]):
        problem = "commit options or paths outside the supported staged-index form"
    return Commit(directories, acknowledged, exception, problem)


def deny(reason):
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}


def check_staged_work(commit, cwd):
    git_overrides = any(name.startswith("GIT_") and name != "GIT_PAGER" for name in os.environ)
    if not isinstance(cwd, str) or not os.path.isabs(cwd) or git_overrides:
        return deny("Mirket cannot identify the index with an invalid working directory or inherited GIT_* overrides. Use a supported direct commit from its worktree.")
    # Resolve the probe from system directories, never from the submitted command
    # or a workspace PATH. Refuse to inspect when the inherited PATH selects a
    # different executable, since the actual command might use that executable.
    git = shutil.which("git", path=SYSTEM_PATH)
    path = os.pathsep.join(os.path.join(cwd, part) for part in os.get_exec_path())
    selected = shutil.which("git", path=path)
    if not git or not selected or os.path.realpath(selected) != os.path.realpath(git):
        return deny("Mirket requires the system Git executable for staged-index inspection. Use a supported direct commit with system Git on PATH.")
    env = {name: os.environ[name] for name in ("HOME", "XDG_CONFIG_HOME") if name in os.environ}
    env.update(PATH=SYSTEM_PATH, LC_ALL="C", GIT_ALLOW_PROTOCOL="")
    try:
        # Require Git to recognize the no-fetch option before entering the target.
        subprocess.run([git, "--no-lazy-fetch", "--version"], cwd="/", env=env,
                       capture_output=True, timeout=1, check=True)
    except (OSError, subprocess.SubprocessError):
        return deny("Mirket requires system Git with --no-lazy-fetch support to inspect the index without running Git helpers. Update system Git before retrying.")
    try:
        target = [arg for directory in commit.directories for arg in ("-C", directory)]
        result = subprocess.run(
            [git, "--no-lazy-fetch", "--no-optional-locks", "--no-pager",
             "-c", "core.fsmonitor=false", *target, "diff", "--cached",
             "--no-ext-diff", "--no-textconv", "--no-relative", "--no-renames",
             "--submodule=short", "--ignore-submodules=none",
             "--name-only", "-z", "--diff-filter=ACMRT", "--", ":(top).work"],
            cwd=cwd, env=env, capture_output=True, timeout=3, check=True,
        )
    except (OSError, ValueError, subprocess.SubprocessError):
        return deny("Mirket could not inspect the target Git index for staged .work files. Resolve the index or repository access issue before committing.")
    paths = [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]
    # A marker records the agent's assertion, not human authorization.
    blocked = [path for path in paths if path != commit.exception]
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
    try:
        parts, structural, heredoc, dynamic = split_command(command)
        commits = [commit for part in parts if (commit := commit_details(part))]
        uncertain = any("git" in part and "commit" in part and part[0] not in {"echo", "printf"} for part in parts)
    except ValueError:
        return {"systemMessage": "Mirket could not parse the shell command; pre-commit cleanup coverage is unknown."}
    if not commits:
        if heredoc:
            return {"systemMessage": "Mirket did not fully inspect a shell command containing a heredoc or here-string for pre-commit cleanup."}
        if uncertain:
            return {"systemMessage": "Mirket could not determine whether this shell command runs git commit; pre-commit cleanup and staged .work coverage are unknown."}
        return {}
    if any(not commit.acknowledged for commit in commits):
        return deny(
                f"Before committing, read {SKILL} and perform its repository-wide cleanup review. "
                "Preserve unrelated changes and historical evidence; do not auto-stage. "
                "Then retry each commit with MIRKET_CLEANUP_DONE=1 in that command, "
                "for example: MIRKET_CLEANUP_DONE=1 git commit -m 'message'. "
                "The marker acknowledges the review and does not prove cleanup occurred."
        )
    if len(parts) != 1 or structural:
        return deny("Mirket cannot reliably inspect the final target index inside a compound command, redirection or heredoc. Run each git commit as a separate direct shell command after the preceding commands finish.")
    commit = commits[0]
    if dynamic or commit.problem:
        reason = commit.problem or "shell expansion"
        return deny(f"Mirket cannot inspect a commit using {reason}. Stage the intended files explicitly and retry with a literal direct git commit command.")
    return check_staged_work(commit, payload.get("cwd", os.getcwd())) or {}



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
