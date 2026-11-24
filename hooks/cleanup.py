#!/usr/bin/env python3
"""Guard supported agent-shell commits."""

import json
import os
import re
import sys
from typing import NamedTuple, Optional

ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=.*$", re.DOTALL)
HEREDOC_COMMIT = re.compile(
    r"(?m)(?:^|[;&|(`])[ \t]*(?:[^\s;&|()`]+/)?git[ \t]+[^\n;&|()`]*\bcommit\b"
)
SYSTEM_PATH = "/usr/bin:/bin"
SYSTEM_GIT_PATHS = {directory + "/git" for directory in SYSTEM_PATH.split(":")}
IDENTITY_ENV = {"GIT_AUTHOR_NAME", "GIT_AUTHOR_EMAIL", "GIT_AUTHOR_DATE",
                "GIT_COMMITTER_NAME", "GIT_COMMITTER_EMAIL", "GIT_COMMITTER_DATE"}
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
    executable: str
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
    dry_run = status_format = changes_inputs = False
    args = iter(args)
    for token in args:
        if token in COMMIT_FLAGS or token.startswith("--gpg-sign="):
            continue
        if token in {"--dry-run", "--no-dry-run"}:
            dry_run = token == "--dry-run"
            continue
        if token in {"--short", "--porcelain", "--long", "-z", "--null"}:
            status_format = True
            continue
        if token in {"-a", "--all"}:
            changes_inputs = True
            continue
        if token == "--":
            if next(args, None) is not None:
                changes_inputs = True
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
    if dry_run or status_format:
        return True
    return None if changes_inputs else False


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
            elif name not in IDENTITY_ENV:
                problem = "command-local environment assignments"
            token = next(words, "")
    if os.path.basename(token) != "git":
        return None
    executable = token
    if executable != "git" and executable not in SYSTEM_GIT_PATHS:
        problem = "a non-system Git executable"
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
    args = list(words)
    preview = args in (["-h"], ["--help"]) or commit_is_preview(args)
    if preview is None:
        problem = "Git arguments outside the supported preview or staged commit forms"
    return Commit(executable, directories, acknowledged, exception, problem, preview is True)


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
    names = {name for name in environ if name.startswith("GIT_")} - IDENTITY_ENV - {"GIT_PAGER"}
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
        return deny("Mirket cannot identify the index with inherited GIT_* overrides. Retry only if the host environment changes and you can verify the same intended index. Otherwise report the blocked commit.")
    # An explicit system path selects the same binary for the commit and probe.
    # For bare git, check what the shell's inherited PATH would select.
    if commit.executable == "git":
        git = shutil.which("git", path=SYSTEM_PATH)
        if not git:
            return deny("Mirket needs system Git in /usr/bin or /bin to inspect the index.")
        if any(not os.path.isabs(part) for part in os.get_exec_path()):
            return deny(f"Mirket cannot verify Git on a relative PATH. Use {git} in the guarded commit command.")
        selected = shutil.which("git")
        if not selected or os.path.realpath(selected) != os.path.realpath(git):
            return deny(f"Mirket needs system Git to inspect the index. Use {git} in the guarded commit command.")
    else:
        git = commit.executable
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
             "--name-only", "-z", "--diff-filter=ACMRT", "--",
             ":(top).work/temp", ":(top).work/recover", ":(top).work/stashes", ":(top).work/routines"],
            cwd="/", env=env, capture_output=True, timeout=3, check=True,
        )
    except (OSError, ValueError, subprocess.SubprocessError):
        return deny("Mirket could not inspect the target Git index for staged .work files. Resolve the index or repository access issue before committing.")
    paths = [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]
    # A marker records the agent's assertion, not human authorization.
    blocked = [path for path in paths if path != commit.exception]
    if blocked:
        return deny("Staged files from ignored workspace directories require an explicitly named human exception: " + ", ".join(repr(path) for path in blocked) + ". Unstage them, or only when the human explicitly authorizes one exact path, retry with MIRKET_WORK_EXCEPTION=<that-path>. The marker does not prove authorization.")
    return None


def handle(payload):
    if payload.get("hook_event_name") != "PreToolUse" or payload.get("tool_name") != "Bash":
        return {}
    tool_input = payload.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str):
        return {"systemMessage": "Mirket could not inspect the shell command for pre-commit cleanup."}
    # Quotes and escapes can synthesize a commit token or cause a parse warning.
    if "commit" not in command and not any(marker in command for marker in ("'", '"', "\\")):
        return {}
    try:
        parts, structural, heredoc, dynamic = split_command(command)
    except ValueError:
        return {"systemMessage": "Mirket could not parse the shell command; pre-commit cleanup coverage is unknown."}
    for part in parts:
        commit = commit_details(part)
        if commit is not None:
            break
    else:
        # The lexer stops at the redirection. Warn on command-shaped text past
        # that boundary without treating prose in the body as a shell command.
        if heredoc and "commit" in command and HEREDOC_COMMIT.search(command):
            return {"systemMessage": "Mirket did not fully inspect a shell command containing a heredoc or here-string for pre-commit cleanup."}
        if any("git" in part and "commit" in part and part[0] not in {"echo", "printf", "rg", "grep"} for part in parts):
            return {"systemMessage": "Mirket could not determine whether this shell command runs git commit; pre-commit cleanup and staged .work coverage are unknown."}
        return {}
    if len(parts) != 1 or structural:
        return deny("Mirket cannot reliably inspect Git operations in a compound command, redirection or heredoc. Run the Git operation separately, preserving its help or preview flags (such as --dry-run).")
    if dynamic or commit.problem:
        reason = commit.problem or "shell expansion"
        return deny(f"Mirket cannot inspect a Git operation using {reason}. For a preview, keep --dry-run in a standalone literal command. For a commit, stage the intended files explicitly and use a standalone literal command.")
    if commit.preview:
        return {}
    if not commit.acknowledged:
        from pathlib import Path

        skill = Path(__file__).resolve().parents[1] / "skills" / "clean" / "SKILL.md"
        return deny(
            f"Before committing, read {skill} and perform its pre-commit review. "
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
