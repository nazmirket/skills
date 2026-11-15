# Contributing to Mirket

The repository root is the shared plugin package. Both marketplaces point to it. The [Codex descriptor](.codex-plugin/plugin.json) declares `./skills/`, and the [Claude Code descriptor](.claude-plugin/plugin.json) uses the host’s default root `skills/` discovery. Add future targets by wiring them to the same catalog. Keep shared `references/`, `hooks/`, and `assets/` alongside `skills/` so installed links and hooks resolve. See the [root catalog decision](docs/decisions/0004-RootSkillsCatalog.md) for packaging and local install guidance.

## Skills

Add a skill at `skills/<name>/SKILL.md` with a lowercase name and a clear trigger. Add `agents/openai.yaml` for its Codex display metadata. If ownership changes, update the [routing guide](references/Routing.md) and related skill references.

The catalog has 20 skills. Search owns external research; Adapt owns internal orientation. Ship supports product decisions and readiness; Market owns marketing strategy and communications; Code supplies stack guidance to the current task. Audit owns security and privacy findings, Architect owns design-time threat modeling, and the implementer owns authorized hardening. The task owner prepares and publishes versioned artifacts when authorized. Migrate owns persistent-state transitions; Deploy owns environment rollout, service health, incidents, and recovery.

Write original skill guidance based on Mirket's requirements and observed behavior. When the maintainer specifies external influences, cite what informed the work and adapt the useful ideas to Mirket's ownership and authority rules. Do not import external skills, prompts, or workflow guides wholesale. Use maintained upstream sources for stack-specific facts. The root license is included in the plugin package.

## Markdown filenames

Use PascalCase for ordinary Markdown files, such as `ReviewLoop.md`. Keep the numeric prefix on numbered records, such as `0001-ExplicitGitTarget.md`. Preserve conventional names such as `README.md`, `CONTRIBUTING.md`, `SKILL.md`, `AGENTS.md`, and `CLAUDE.md`. Skill directory names and site routes stay lowercase.

## Checks

```sh
python3 -B -m unittest discover -s tests
```

These tests cover hook logic and package wiring. Use the [host smoke checks](tests/HostSmoke.md) for installed skill discovery, hook activation, and representative routing. Report host checks separately from the local test results.

Package checks include exact-case paths and heading anchors, catalog/display metadata, host manifest identity, the packaged license and identical optional global instructions. Use the behavioral fixtures to record actual owners, permitted writes, stopping behavior and reused evidence. A fixture prepared with unverified results is not a passing evaluation.

For documentation or catalog changes, also run `npm run docs:diagrams`, `npm run build`, and `npm run seo:check` in `website/`, then inspect changed pages at desktop and narrow mobile widths. Update source Markdown rather than copying skill prose into the website.

## Release and installation checks

Use the Codex compatibility manifest without a root `plugin.json`. In Codex CLI 0.167.0, a controlled comparison found that the portable root manifest exposed all 25 skills but suppressed hook discovery, even with a compatibility manifest alongside it. The same package using the compatibility layout exposed all four hooks. See the [packaging decision](docs/decisions/0003-CodexHookCompatibility.md); discovery alone does not establish activation or enforcement.

Keep both plugin versions and marketplace descriptions aligned. Verify the exact candidate package, all referenced files and supported installation/upgrade behavior. Installed caches and manually merged global instructions have separate lifecycles: compare the active package with the candidate and merge matching instructions without replacing unrelated user guidance. Use the host's supported reload/install command; never patch a version cache in place or bypass hook trust. Open a fresh session and record the host version, source revision, installed version and results using the smoke guide.

Use the [versioned distribution guide](references/VersionedDistribution.md) to prepare release notes, artifact identity, compatibility and recovery instructions. Public distribution and website activation require their authorized scope; [Deploy](skills/deploy/SKILL.md) verifies the served version separately. Keep candidate checks distinct from publication and installation results.

## Lifecycle hooks

Mirket handles three lifecycle events and requires Python 3.8 or later in the host environment:

- **At session start:** supply [Execute](skills/execute/SKILL.md) guidance for taking the simplest complete path and reporting what matters. Point to the [routing guide](references/Routing.md) to keep one owner per outcome.
- **On a user prompt:** repeat the core Execute guidance and remind the agent to apply Clean before delivery when relevant. Mirket does not request an extra review at turn end.
- **Before an agent-issued commit:** for supported direct `git commit` calls through the agent's Bash tool, ask for [Clean](skills/clean/SKILL.md) before inspecting staged files. Use a standalone literal command such as `MIRKET_CLEANUP_DONE=1 git -C "/absolute/worktree" commit -m "message"`. The first `-C` must be absolute; later literal `-C` values can be relative to it. Codex's hook session directory may differ from the tool's execution directory, so the same explicit target rule applies in both hosts. A standalone supported `git commit --dry-run` preview needs neither an acknowledgment nor an absolute target; keep the flag when retrying a preview.

The staged check requires system Git from `/usr/bin` or `/bin` with `--no-lazy-fetch` support and an absolute-only `PATH` that selects it. External helpers are disabled. The hook supports basic `env` and `command` wrappers and known staged commit flags. It blocks recognized commits with custom executables, overrides such as `git -c` or `GIT_INDEX_FILE`, or modes such as `-a`, `--include`, `--only`, or a pathspec. Stage intended paths explicitly for a real commit. If the human authorizes one exact `.work/` path, add `MIRKET_WORK_EXCEPTION=.work/path` to the commit command. Both markers record assertions and neither overrides host permissions. See the [Git target decision](docs/decisions/0001-ExplicitGitTarget.md) for the tradeoff.

The commit guard instructs the agent to use [Clean](skills/clean/SKILL.md); it does not delete or stage files. Hooks cannot guarantee agent compliance. Codex requires review and trust of plugin hooks before they run; changing a hook requires renewed review. Verify activation and behavior separately in each host; a successful startup hook does not prove commit enforcement.

Coverage is limited: disabled or untrusted hooks, interruptions, API failures, unsupported tool paths, PowerShell, Git aliases, scripts, nested shells, heredocs or here-strings, wrapper options, interactive shell input and commits outside the agent can bypass these checks. The shell recognizer handles direct commands and basic `env`/`command` wrappers, not a complete shell grammar; it warns about some recognizable unsupported forms but cannot detect every indirect commit. An index check examines staged changes at invocation time; it does not cover unrecognized commands or all alternative commit modes. Hooks are guardrails, not a security boundary. See the [Codex hook documentation](https://learn.chatgpt.com/docs/hooks) and [Claude Code hook reference](https://code.claude.com/docs/en/hooks).
