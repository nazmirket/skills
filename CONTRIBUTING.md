# Contributing to Mirket

The repository root is the shared plugin package. Both marketplaces point to it. The [Codex descriptor](.codex-plugin/plugin.json) declares `./skills/`, and the [Claude Code descriptor](.claude-plugin/plugin.json) uses the host’s default root `skills/` discovery. Add future targets by wiring them to the same catalog. Keep plugin references, `hooks/`, and `assets/` alongside `skills/` so native installs retain their existing paths. See the [root catalog decision](docs/decisions/0004-RootSkillsCatalog.md) for packaging and local install guidance.

## Skills

Extend the skill that owns the result. Each has a lowercase name, a clear trigger in `skills/<name>/SKILL.md`, and Codex display metadata in `agents/openai.yaml`. If ownership changes, update the [routing guide](skills/execute/references/Routing.md) and related skill references. Start each routing row’s owner column with a link to the skill responsible for that result.

The [other-agent guide](docs/OtherAgents.md) uses `npx skills add`, which copies individual skill directories. Keep skill links within the catalog and shared skill references in [Execute](skills/execute/references/Routing.md). The old root reference paths still point to the maintained guides. Keep the [catalog's copy of the license](skills/execute/LICENSE) in sync with the [root license](LICENSE).

The catalog has 20 skills. Search owns external research, including papers and technical documentation. Adapt owns internal orientation. Execute owns authorized implementation of settled requirements when no specialist owns the result. Ship supports product decisions and readiness; Market owns marketing strategy and communications; Code supplies stack guidance to the current task. Audit owns security and privacy findings, Architect owns design-time threat modeling, and the implementer owns authorized hardening. The task owner prepares and publishes versioned artifacts when authorized. Migrate owns persistent-state transitions; Deploy owns environment rollout, service health, incidents, and recovery.

Write original guidance from project requirements, research and observed behavior. Package usable procedures, decision criteria and examples in the skill catalog. All links in skill guidance must resolve inside the catalog. Design can also install on its own, so keep its references and capture helper inside its folder. Check version-sensitive advice against the installed stack or primary sources during authoring. Preserve applicable license notices. The root license is included in the plugin package.

## Markdown filenames

Use PascalCase for ordinary Markdown files, such as `ReviewLoop.md`. Keep the numeric prefix on numbered records, such as `0001-ExplicitGitTarget.md`. Preserve conventional names such as `README.md`, `CONTRIBUTING.md`, `SKILL.md`, `AGENTS.md`, and `CLAUDE.md`. Skill directory names and site routes stay lowercase.

## Checks

```sh
python3 -B -m unittest discover -s tests
```

These tests cover hook logic and package wiring. Use the [host smoke checks](tests/HostSmoke.md) for installed skill discovery, hook activation, and representative routing. Report host checks separately from the local test results.

For changes to Design’s capture helper, run `node --test tests/design_capture.cjs` with an available Playwright and its Chromium browser. It checks full document coverage, horizontal overflow, quirks-mode viewport sizing and rejection of cropped or low-density evidence.

Package checks include exact-case paths and heading anchors, catalog/display metadata, host manifest identity, the packaged license and identical optional global instructions. Use the behavioral fixtures to record actual owners, permitted writes, stopping behavior and reused evidence. A fixture prepared with unverified results is not a passing evaluation. For blind routing, use unpublished evaluator-owned cases, keep results in an evaluator-only directory and report explicit invocation separately.

For documentation or catalog changes, also run `npm run docs:diagrams`, `npm run build`, and `npm run seo:check` in `website/`, then inspect changed pages at desktop and narrow mobile widths using the [full-surface capture standard](skills/design/references/tools/Screenshot.md). Update source Markdown rather than copying skill prose into the website.

## Release and installation checks

Use the Codex compatibility manifest without a root `plugin.json`. A controlled comparison in Codex CLI 0.167.0 found that the portable root manifest suppressed hook discovery, even with a compatibility manifest alongside it. See the [packaging decision](docs/decisions/0003-CodexHookCompatibility.md). Verify discovery and execution for the current package separately.

Keep both plugin versions and marketplace descriptions aligned. Verify the exact candidate package, all referenced files and supported installation/upgrade behavior. Installed caches and manually merged global instructions have separate lifecycles: compare the active package with the candidate and merge matching instructions without replacing unrelated user guidance. Use the host's supported reload/install command; never patch a version cache in place or bypass hook trust. Open a fresh session and record the host version, source revision, installed version and results using the smoke guide.

Use the [versioned distribution guide](skills/execute/references/VersionedDistribution.md) to prepare release notes, artifact identity, compatibility and recovery instructions. Public distribution and website activation require their authorized scope; [Deploy](skills/deploy/SKILL.md) verifies the served version separately. Keep candidate checks distinct from publication and installation results.

## Lifecycle hooks

Mirket handles three lifecycle events and requires Python 3.8 or later in the host environment:

- **At session start:** supply [Execute](skills/execute/SKILL.md) guidance for taking the simplest complete path and reporting what matters. Point to the [routing guide](skills/execute/references/Routing.md) to keep one owner per outcome.
- **On each user prompt** the hook reminds the agent to select the owner for the current outcome, apply Execute and use Clean for relevant delivery work.
- **Before an agent-issued commit:** for supported direct `git commit` calls through the agent's Bash tool, ask for [Clean](skills/clean/SKILL.md) before inspecting staged files. Use a standalone literal command such as `MIRKET_CLEANUP_DONE=1 git -C "/absolute/worktree" commit -m "message"`. The first `-C` must be absolute; later literal `-C` values can be relative to it. Codex's hook session directory may differ from the tool's execution directory, so the same explicit target rule applies in both hosts. Standalone commit help and supported previews, including `--dry-run`, `--short` and `--porcelain`, need neither an acknowledgment nor an absolute target. Preserve the original help or preview flags when splitting a command.

The staged check requires system Git from `/usr/bin` or `/bin` with `--no-lazy-fetch` support. Invoke that system path directly, or use bare `git` with an absolute-only `PATH` that selects it. External helpers are disabled. A host may supply URL-scoped HTTPS credential and HTTP transport settings through a complete `GIT_CONFIG_COUNT` block. Author and committer name, email and date settings are also supported. The offline index check receives neither identity nor transport settings. The hook supports basic `env` and `command` wrappers and known staged commit flags. It blocks recognized commits with custom executables, overrides such as `git -c` or `GIT_INDEX_FILE`, or modes such as `-a`, `--include`, `--only`, or a pathspec. Stage intended paths explicitly for a real commit. If the human authorizes one exact `.work/` path, add `MIRKET_WORK_EXCEPTION=.work/path` to the commit command. Both markers record assertions and neither overrides host permissions. See the [Git target decision](docs/decisions/0001-ExplicitGitTarget.md) for the tradeoff.

The commit guard instructs the agent to use [Clean](skills/clean/SKILL.md); it does not delete or stage files. Hooks cannot guarantee agent compliance. Codex can require renewed review after plugin contents change, even when the hook files match. Verify actual execution in each host: a trusted entry in the hook list or a successful startup hook does not prove commit enforcement. If an event reports that hook approval is required, review it through the host before relying on that guard.

An operating hook can deny a supported commit. Startup failures and timeouts follow the host’s native policy. Claude Code supports an explicit failure policy for eligible command hooks from 2.1.295. With the current Bash-wide matcher, blocking on hook failure could also stop ordinary reads. Evaluate a proposed policy in a disposable host before configuring it. For a protected branch that requires a merge-time rule, repository owners can configure a required check with the project’s exact exceptions. [Claude Code hook failures](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails) · [GitHub required status checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-status-checks-to-pass-before-merging)

Coverage is limited: disabled or untrusted hooks, interruptions, API failures, unsupported tool paths, PowerShell, Git aliases, scripts, nested shells, heredocs or here-strings, wrapper options, interactive shell input and commits outside the agent can bypass these checks. The shell recognizer handles direct commands and basic `env`/`command` wrappers, not a complete shell grammar; it warns about some recognizable unsupported forms but cannot detect every indirect commit. An index check examines staged changes at invocation time; it does not cover unrecognized commands or all alternative commit modes. Hooks are guardrails, not a security boundary. See the [Codex hook documentation](https://learn.chatgpt.com/docs/hooks) and [Claude Code hook reference](https://code.claude.com/docs/en/hooks).
