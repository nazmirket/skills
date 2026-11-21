#!/usr/bin/env python3
"""Guard supported agent-shell commits."""

import json
import os
from pathlib import Path
import re
import sys
from typing import NamedTuple, Optional

SKILL = str(Path(__file__).resolve().parent.parent / "skills" / "clean" / "SKILL.md")
ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=.*$", re.DOTALL)
SYSTEM_PATH = "/usr/bin:/bin"
HOST_LABEL = r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?"
HTTPS_SCOPE = re.compile(
    rf"https://{HOST_LABEL}(?:\.{HOST_LABEL})*(?::(?P<port>[0-9]{{1,5}}))?"
    r"(?:/(?:[a-z0-9._~/-]|%[0-9a-f]{2})*)?",
    re.ASCII | re.IGNORECASE,
)
TRANSPORT_OPTIONS = {"credential": {"helper", "usehttppath"}, "http": {"proactiveauth", "followredirects"}}
GIT_OPTIONS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--config-env", "--exec-path"}
COMMIT_VALUES = {"-m", "-F", "-C", "-c", "--message", "--file", "--reuse-message", "--reedit-message", "--author", "--date"}
COMMIT_FLAGS = {
    "-q", "--quiet", "--amend", "--no-edit", "--allow-empty", "--allow-empty-message",
    "-s", "--signoff", "--no-signoff", "-S", "--gpg-sign", "--no-gpg-sign",
}


class Commit(NamedTuple):
    directories: list
    acknowledged: bool
    exception: Optional[str]
    problem: Optional[str]
    preview: bool


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


def commit_is_preview(args):
    """Return True for a supported dry run, False for a staged commit, or None."""
    dry_run = changes_inputs = False
    args = iter(args)
    for token in args:
        if token in COMMIT_FLAGS or token.startswith("--gpg-sign="):
            continue
        if token in {"--dry-run", "--no-dry-run"}:
            dry_run = token == "--dry-run"
            continue
        if token in {"-a", "--all"}:
            changes_inputs = True
            continue
        if token == "--":
            if next(args, None) is not None:
                return None
            break
        if token in COMMIT_VALUES:
            if next(args, None) is None:
                return None
            continue
        option, equals, _ = token.partition("=")
        if option.startswith("--") and equals and option in COMMIT_VALUES:
            continue
        if len(token) > 2 and token[:2] in COMMIT_VALUES:
            continue
        return None
    return None if changes_inputs and not dry_run else dry_run


def commit_details(tokens):
    words = iter(tokens)
    token = next(words, "")
    acknowledged = False
    exception = problem = None
    while token in {"env", "command"} or ASSIGNMENT.match(token):
        if token in {"env", "command"}:
            token = next(words, "")
            if token == "--":
                token = next(words, "")
            if token.startswith("-"):
                return None
        else:
            name, _, value = token.partition("=")
            if name == "MIRKET_CLEANUP_DONE":
                acknowledged = value == "1"
            elif name == "MIRKET_WORK_EXCEPTION":
                exception = value
            else:
                problem = "command-local environment assignments"
            token = next(words, "")
    if os.path.basename(token) != "git":
        return None
    if token != "git":
        problem = "a path-qualified Git executable"
    directories = []
    for token in words:
        if token == "commit":
            break
        if not token.startswith("-"):
            return None
        if token in GIT_OPTIONS_WITH_VALUE:
            value = next(words, None)
            if value is None:
                return None
            if token == "-C":
                directories.append(value)
                continue
        problem = "Git global options other than literal -C paths"
    else:
        return None
    preview = commit_is_preview(words)
    if preview is None:
        problem = "Git arguments outside the supported preview or staged commit forms"
    return Commit(directories, acknowledged, exception, problem, preview is True)


def deny(reason):
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}


def is_scoped_transport_key(key):
    section, _, rest = key.partition(".")
    scope, _, option = rest.rpartition(".")
    if option.lower() not in TRANSPORT_OPTIONS.get(section.lower(), ()):
        return False
    match = HTTPS_SCOPE.fullmatch(scope)
    return match is not None and (match["port"] is None or 0 < int(match["port"]) <= 65535)


def supports_index_probe(environ):
    names = {name for name in environ if name.startswith("GIT_") and name != "GIT_PAGER"}
    if not names:
        return True
    # Bound the check by the supplied keys. Git needs one complete pair per slot.
    count = sum(name.startswith("GIT_CONFIG_KEY_") for name in names)
    if environ.get("GIT_CONFIG_COUNT") != str(count):
        return False
    expected = {"GIT_CONFIG_COUNT"}
    for index in range(count):
        key = f"GIT_CONFIG_KEY_{index}"
        if not is_scoped_transport_key(environ.get(key, "")):
            return False
        expected.update((key, f"GIT_CONFIG_VALUE_{index}"))
    return names == expected


def check_staged_work(commit):
    import shutil
    import subprocess

    if not supports_index_probe(os.environ):
        return deny("Mirket cannot identify the index with inherited GIT_* overrides. Use a supported direct commit without those overrides.")
    # Resolve the probe from system directories, never from the submitted command
    # or a workspace PATH. Refuse to inspect when the inherited PATH selects a
    # different executable, since the actual command might use that executable.
    git = shutil.which("git", path=SYSTEM_PATH)
    search_path = os.get_exec_path()
    if any(not os.path.isabs(part) for part in search_path):
        return deny("Mirket cannot verify which Git a relative or empty PATH entry selects. Use a PATH containing only absolute directories for a guarded commit.")
    selected = shutil.which("git", path=os.pathsep.join(search_path))
    if not git or not selected or os.path.realpath(selected) != os.path.realpath(git):
        return deny("Mirket requires the system Git executable for staged-index inspection. Use a supported direct commit with system Git on PATH.")
    # Transport settings stay with the host. The local probe never receives helper values.
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
            cwd="/", env=env, capture_output=True, timeout=3, check=True,
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
    if payload.get("hook_event_name") != "PreToolUse" or payload.get("tool_name") != "Bash":
        return {}
    tool_input = payload.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str):
        return {"systemMessage": "Mirket could not inspect the shell command for pre-commit cleanup."}
    try:
        parts, structural, heredoc, dynamic = split_command(command)
    except ValueError:
        return {"systemMessage": "Mirket could not parse the shell command; pre-commit cleanup coverage is unknown."}
    for part in parts:
        commit = commit_details(part)
        if commit is not None:
            break
    else:
        if heredoc:
            return {"systemMessage": "Mirket did not fully inspect a shell command containing a heredoc or here-string for pre-commit cleanup."}
        if any("git" in part and "commit" in part and part[0] not in {"echo", "printf"} for part in parts):
            return {"systemMessage": "Mirket could not determine whether this shell command runs git commit; pre-commit cleanup and staged .work coverage are unknown."}
        return {}
    if len(parts) != 1 or structural:
        return deny("Mirket cannot reliably inspect Git operations in a compound command, redirection or heredoc. Run each Git operation separately. If you intended a preview, keep --dry-run.")
    if dynamic or commit.problem:
        reason = commit.problem or "shell expansion"
        return deny(f"Mirket cannot inspect a Git operation using {reason}. For a preview, keep --dry-run in a standalone literal command. For a commit, stage the intended files explicitly and use a standalone literal command.")
    if commit.preview:
        return {}
    if not commit.acknowledged:
        return deny(
            f"Before committing, read {SKILL} and perform its pre-commit review. "
            "Preserve unrelated changes and historical evidence; do not auto-stage. "
            "Then use the acknowledgment and an absolute Git target: "
            "MIRKET_CLEANUP_DONE=1 git -C '/absolute/worktree' commit -m 'message'. "
            "The marker acknowledges the review and does not prove cleanup occurred."
        )
    # Hook cwd can describe the session, not the shell tool's execution directory.
    if not commit.directories or not os.path.isabs(commit.directories[0]):
        return deny("Mirket cannot verify the Git target from the session directory. Use a first -C with an absolute worktree path in the guarded commit command.")
    return check_staged_work(commit) or {}


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
