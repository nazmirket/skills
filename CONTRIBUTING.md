# Contributing to Mirket

The plugin lives in [plugins/mirket](plugins/mirket). Codex and Claude Code use their own marketplace manifests and share the packaged skills. Their package descriptors are [`.codex-plugin/plugin.json`](plugins/mirket/.codex-plugin/plugin.json) and [`.claude-plugin/plugin.json`](plugins/mirket/.claude-plugin/plugin.json). Keep the shared `skills/`, `hooks/` and `assets/` at the package root.

## Skills

Add a skill at `plugins/mirket/skills/<name>/SKILL.md` with a lowercase name and a clear trigger. Add `agents/openai.yaml` for its Codex display metadata. If ownership changes, update the [routing guide](plugins/mirket/references/Routing.md) and related skill references.

The catalog has 25 skills. Keep outcomes distinct: Secure owns security/privacy evidence and authorized hardening; Migrate owns persistent-state transitions; Release owns versioned artifacts and distribution; Deploy owns environment rollout; Operate owns health and recovery. Focus evaluates shipped product outcomes. A lifecycle skill supplies only the work needed by the request; it does not create a mandatory pipeline.

Write original skill guidance based on Mirket's requirements and observed behavior. Do not use external skills, prompts, or workflow guides as sources for authoring. Keep the root and packaged license files in sync.

## Markdown filenames

Use PascalCase for ordinary Markdown files, such as `ReviewLoop.md`. Keep the numeric prefix on numbered records, such as `0001-ExplicitGitTarget.md`. Preserve conventional names such as `README.md`, `CONTRIBUTING.md`, `SKILL.md`, `AGENTS.md`, and `CLAUDE.md`. Skill directory names and site routes stay lowercase.

## Checks

```sh
python3 -B -m unittest discover -s tests
python3 -B -m unittest discover -s memory
```

These tests cover hook logic, package wiring, and memory tooling. Use the [host smoke checks](tests/HostSmoke.md) for installed skill discovery, hook activation, and representative routing. Report host checks separately from the local test results.

Package checks include exact-case paths and heading anchors, catalog/display metadata, host manifest identity, license parity and identical optional global instructions. Use the behavioral fixtures to record actual owners, permitted writes, stopping behavior and reused evidence. A fixture prepared with unverified results is not a passing evaluation.

For documentation or catalog changes, also run `npm run docs:diagrams`, `npm run build`, and `npm run seo:check` in `website/`, then inspect changed pages at desktop and narrow mobile widths. Update source Markdown rather than copying skill prose into the website.

## Release and installation checks

Use the Codex compatibility manifest without a root `plugin.json`. In Codex CLI 0.167.0, a controlled comparison found that the portable root manifest exposed all 25 skills but suppressed hook discovery, even with a compatibility manifest alongside it. The same package using the compatibility layout exposed all four hooks. See the [packaging decision](docs/decisions/0003-CodexHookCompatibility.md); discovery alone does not establish activation or enforcement.

Keep both plugin versions and marketplace descriptions aligned. Verify the exact candidate package, all referenced files and supported installation/upgrade behavior. Installed caches and manually merged global instructions have separate lifecycles: compare the active package with the candidate and merge matching instructions without replacing unrelated user guidance. Use the host's supported reload/install command; never patch a version cache in place or bypass hook trust. Open a fresh session and record the host version, source revision, installed version and results using the smoke guide.

Prepare release notes, artifact identity, compatibility and recovery instructions through [Release](plugins/mirket/skills/release/SKILL.md). Public distribution and website activation require their authorized scope; [Deploy](plugins/mirket/skills/deploy/SKILL.md) verifies the served version separately. Keep candidate checks distinct from a claim that a release is published or installed.

## Memory reliability

The optional memory subsystem must preserve existing banks, effective capture restrictions and unrelated configuration during rewiring. Test canonical identity and legacy mapping together, and compare diagnostics to the pinned runtime's actual configuration semantics. See [the memory guide](memory/README.md) for freshness settings, bounded recovery and the real capture/recall check. Do not mark a survey complete by updating a receipt, equate page refresh with source ingestion, or use manual document ingestion as proof that automatic chat capture works.

## Lifecycle hooks

Mirket handles four lifecycle events and requires Python 3.8 or later in the host environment:

- **At session start:** supply compact [Distill](plugins/mirket/skills/distill/SKILL.md) guidance and point to the [routing guide](plugins/mirket/references/Routing.md). Use one owner per outcome; supporting skills return evidence to it.
- **On a user prompt:** remind the agent to apply Distill before it sends a reply and Clean before delivery when relevant. The reminder stands alone if session context or the final hook is unavailable.
- **At turn end:** the `Stop` hook is neutral by default. To opt in, start the host with `MIRKET_FINAL_REVIEW=1` in its environment (for example, prefix the CLI launch with that assignment). This requests one Distill and Clean pass together if no Stop hook has already continued the turn. It can request another model pass after initial output; it cannot rewrite text already shown or impose a token cap. Desktop apps must inherit the variable at launch for it to take effect.
- **Before an agent-issued commit:** for supported direct `git commit` calls through the agent's Bash tool, ask for [Clean](plugins/mirket/skills/clean/SKILL.md) before inspecting staged files. Use a standalone literal command such as `MIRKET_CLEANUP_DONE=1 git -C "/absolute/worktree" commit -m "message"`. The first `-C` must be absolute; later literal `-C` values can be relative to it. Codex's hook session directory may differ from the tool's execution directory, so the same explicit target rule applies in both hosts. A standalone supported `git commit --dry-run` preview needs neither an acknowledgment nor an absolute target; keep the flag when retrying a preview.

The staged check requires system Git from `/usr/bin` or `/bin` with `--no-lazy-fetch` support and an absolute-only `PATH` that selects it. External helpers are disabled. The hook supports basic `env` and `command` wrappers and known staged commit flags. It blocks recognized commits with custom executables, overrides such as `git -c` or `GIT_INDEX_FILE`, or modes such as `-a`, `--include`, `--only`, or a pathspec. Stage intended paths explicitly for a real commit. If the human authorizes one exact `.work/` path, add `MIRKET_WORK_EXCEPTION=.work/path` to the commit command. Both markers record assertions and neither overrides host permissions. See the [Git target decision](docs/decisions/0001-ExplicitGitTarget.md) for the tradeoff.

The cleanup hooks instruct the agent to use [Clean](plugins/mirket/skills/clean/SKILL.md); they do not themselves delete or stage files. Hooks cannot guarantee agent compliance. Codex requires review and trust of plugin hooks before they run; changing a hook requires renewed review. Verify activation and behavior separately in each host; a successful startup hook does not prove commit or Stop enforcement.

Coverage is limited: disabled or untrusted hooks, interruptions, API failures, shared Stop-loop state, unsupported tool paths, PowerShell, Git aliases, scripts, nested shells, heredocs or here-strings, wrapper options, interactive shell input and commits outside the agent can bypass these checks. The shell recognizer handles direct commands and basic `env`/`command` wrappers, not a complete shell grammar; it warns about some recognizable unsupported forms but cannot detect every indirect commit. An index check examines staged changes at invocation time; it does not cover unrecognized commands or all alternative commit modes. Hooks are guardrails, not a security boundary. See the [Codex hook documentation](https://learn.chatgpt.com/docs/hooks) and [Claude Code hook reference](https://code.claude.com/docs/en/hooks).
