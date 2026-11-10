# Contributing to Mirket

The plugin lives in [plugins/mirket](plugins/mirket). Codex and Claude Code use their own marketplace manifests and share the packaged skills.

## Skills

Add a skill at `plugins/mirket/skills/<name>/SKILL.md` with a lowercase name and a clear trigger. Add `agents/openai.yaml` for its Codex display metadata. If ownership changes, update the [routing guide](plugins/mirket/references/routing.md) and related skill references. Record substantial third-party adaptations in [sources.json](plugins/mirket/sources.json) and preserve their applicable notices in the [packaged license](plugins/mirket/LICENSE). Keep the root and packaged license files in sync.

## Checks

```sh
python3 -B -m unittest discover -s tests
python3 -B -m unittest discover -s memory
```

These tests cover hook logic and memory tooling. Check skill discovery, explicit invocation, and representative prompts in fresh host sessions to verify live behavior.

## Lifecycle hooks

Mirket includes three plugin hooks, requiring Python 3.8 or later in the host environment:

- **On a user prompt:** request that the agent read and apply [Distill](plugins/mirket/skills/distill/SKILL.md) to its user-facing messages for the turn, and apply Clean before delivery when relevant. This provides an earlier reminder if another Stop hook affects the final review.
- **Before delivery:** on a supported `Stop` event, request one task-scoped cleanup review before the response finishes. It uses the host's continuation flag to avoid repeated loops.
- **Before an agent-issued commit:** for supported direct `git commit` calls through the agent's Bash tool, block an unacknowledged attempt and request a repository-wide cleanup review. After reviewing, retry with a command-local marker, for example `MIRKET_CLEANUP_DONE=1 git commit -m "message"`. The hook uses system Git from `/usr/bin` or `/bin` with `--no-lazy-fetch` support and checks the staged index with external helpers disabled. It supports literal `-C` paths, basic `env` and `command` wrappers, and known commit flags that leave the staged inputs unchanged. It blocks recognized commits when it cannot inspect the target, including custom Git executables, overrides such as `git -c` or `GIT_INDEX_FILE`, and modes such as `-a`, `--include`, `--only`, or a pathspec. Stage the intended paths explicitly and retry with a standalone direct commit. If the human authorizes an exact `.work/` path, add `MIRKET_WORK_EXCEPTION=.work/path` to that command; other staged `.work/` changes remain blocked. Both markers record assertions and neither overrides host permissions.

The cleanup hooks instruct the agent to use [Clean](plugins/mirket/skills/clean/SKILL.md); they do not themselves delete or stage files. Hooks cannot guarantee agent compliance. Codex requires review and trust of plugin hooks before they run; changing a hook requires renewed review. Hook activation and behavior in each host have not been verified.

Coverage is limited: disabled or untrusted hooks, interruptions, API failures, shared Stop-loop state, unsupported tool paths, PowerShell, Git aliases, scripts, nested shells, heredocs or here-strings, wrapper options, interactive shell input and commits outside the agent can bypass these checks. The shell recognizer handles direct commands and basic `env`/`command` wrappers, not a complete shell grammar; it warns about some recognizable unsupported forms but cannot detect every indirect commit. An index check examines staged changes at invocation time; it does not cover unrecognized commands or all alternative commit modes. Hooks are guardrails, not a security boundary. See the [Codex hook documentation](https://learn.chatgpt.com/docs/hooks) and [Claude Code hook reference](https://code.claude.com/docs/en/hooks).
