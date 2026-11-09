# Mirket

Mirket is a collection of agent skills for engineering, QA, design, document authoring, product decisions, and project coordination. The `mirket` plugin shares one catalog across Codex and Claude Code; `mirket-native-marketplace` provides a local marketplace for each host.

The skills are under active development. Package checks and synthetic hook tests are separate from installation and behavioral testing in Codex and Claude Code.

## Skills

| Skill | Purpose |
| --- | --- |
| [mirket:adapt](plugins/mirket/skills/adapt/SKILL.md) | Understand the target, its conventions and the human's working preferences without making fixes. |
| [mirket:architect](plugins/mirket/skills/architect/SKILL.md) | Compare consequential technical designs and prepare a decision or ADR draft. |
| [mirket:audit](plugins/mirket/skills/audit/SKILL.md) | Report evidence-backed defects in a code change or explicitly requested draft plan. |
| [mirket:author](plugins/mirket/skills/author/SKILL.md) | Produce and verify documents, or triage bug reports and draft issue tickets. |
| [mirket:brief](plugins/mirket/skills/brief/SKILL.md) | Prepare a recipient-specific handoff with the next action, authority and evidence. |
| [mirket:clean](plugins/mirket/skills/clean/SKILL.md) | Remove verified leftovers and keep project guidance current. |
| [mirket:critique](plugins/mirket/skills/critique/SKILL.md) | Judge the delivered result against its brief using rendered and qualitative evidence. |
| [mirket:curate](plugins/mirket/skills/curate/SKILL.md) | Research a question or compare options with sourced evidence of fit, adoption and stability. |
| [mirket:debug](plugins/mirket/skills/debug/SKILL.md) | Trace an observed failure to its cause and verify any authorized fix. |
| [mirket:design](plugins/mirket/skills/design/SKILL.md) | Set or implement visual direction, including redesigns and supplied references. |
| [mirket:distill](plugins/mirket/skills/distill/SKILL.md) | Communicate concisely, directly and factually in every user-facing response. |
| [mirket:equip](plugins/mirket/skills/equip/SKILL.md) | Identify why a tool or workflow cannot deliver the result or wastes effort, and recommend a better fit. |
| [mirket:focus](plugins/mirket/skills/focus/SKILL.md) | Frame a product opportunity, success measures and the decisions for the human. |
| [mirket:imagine](plugins/mirket/skills/imagine/SKILL.md) | Agree on an image-generation brief and translate the generated design into code. |
| [mirket:orchestrate](plugins/mirket/skills/orchestrate/SKILL.md) | Coordinate bounded investigations, independent draft reviews, or approved execution. |
| [mirket:plan](plugins/mirket/skills/plan/SKILL.md) | Prepare an evidence-based plan, record decisions, and track approved work. |
| [mirket:preflight](plugins/mirket/skills/preflight/SKILL.md) | Check environment readiness against project requirements and propose fixes for blockers. |
| [mirket:refactor](plugins/mirket/skills/refactor/SKILL.md) | Simplify existing code within scope while preserving observable behavior. |
| [mirket:sleep](plugins/mirket/skills/sleep/SKILL.md) | Pause work and create a handoff with a prompt for resuming later. |
| [mirket:test](plugins/mirket/skills/test/SKILL.md) | Select and run checks for behavior, regressions and performance claims. |

Use the [routing guide](plugins/mirket/references/routing.md) to choose a workflow. [Prototyping](plugins/mirket/references/prototype.md) and [measured improvement](plugins/mirket/references/measured-improvement.md) are shared methods.

Earlier IDs have no aliases: use `clean` for `cleanup`, `brief` for `handoff`, `preflight` for `discover`, `audit` for `review`, and `focus` for `scope`. Issue triage now lives in Author and progress tracking in Plan. General implementation no longer has a separate skill.

`distill` is intended for every user-facing response. A prompt hook asks the agent to read and apply it each turn. Hook activation and the agent's compliance are not guaranteed; host behavior remains unverified.

Skill names in `SKILL.md` remain unprefixed, such as `plan`; the plugin supplies the `mirket:` namespace. Claude Code documents plugin commands such as `/mirket:plan`. Codex-facing labels are configured separately in each skill's `agents/openai.yaml`. Exact host display and invocation remain unverified.

## Project layout

```text
.agents/plugins/marketplace.json       Codex marketplace
.claude-plugin/marketplace.json        Claude Code marketplace
plugins/mirket/plugin.json             Portable plugin metadata
plugins/mirket/.claude-plugin/plugin.json Claude Code plugin metadata
plugins/mirket/skills/                 Shared skill instructions and display metadata
plugins/mirket/references/            Native methods, routing and workspace guidance
plugins/mirket/sources.json           Attribution and license locations
plugins/mirket/hooks/                  Distill and cleanup lifecycle hooks
instructions/                          Global instructions for Codex and Claude Code
memory/                                Hindsight installation guidance and installer
tests/                                 Synthetic plugin hook tests
```

The marketplace source paths are relative to this project root. Both descriptors point to `plugins/mirket`, and both plugin manifests identify the plugin as `mirket`. The Claude marketplace owner `mirket` is a project label; it does not assert a legal author or license.

For optional persistent memory in Codex, see [Hindsight setup](memory/README.md). Hindsight's runtime and data remain in its own user-level locations.

## Local installation

The following instructions describe local setup after the skills are ready for host testing. They change your local plugin configuration; no registration or installation has been performed for this project.

From the project root, for Codex:

```sh
codex plugin marketplace add .
codex plugin add mirket@mirket-native-marketplace
```

For Claude Code:

```sh
claude plugin marketplace add .
claude plugin install mirket@mirket-native-marketplace
```

Start a new session after installation. Installed copies may be cached: refresh the marketplace and plugin after source changes, and restart the host as needed. Refer to [OpenAI's local marketplace guide](https://developers.openai.com/plugins/build/plugins) and [Claude Code's marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces) for current host behavior and update commands. The two hosts have separate marketplace files and installations.

### Global instructions

Merge the matching file into your existing user instructions, or copy it if the destination does not exist:

| Host | Source | Default destination |
| --- | --- | --- |
| Codex | [AGENTS.md](instructions/AGENTS.md) | `~/.codex/AGENTS.md` |
| Claude Code | [CLAUDE.md](instructions/CLAUDE.md) | `~/.claude/CLAUDE.md` |

If Codex uses a custom `CODEX_HOME`, use that directory; an existing `AGENTS.override.md` takes precedence. These files guide the agent to use the active Mirket plugin. Copying them does not install the plugin or activate hooks. See the [Codex AGENTS.md guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [Claude Code instructions guide](https://code.claude.com/docs/en/memory).

### Project work files

Use the project-root [`.work/` directory](plugins/mirket/references/workspace.md) for plans, temporary stashes, important recovery copies, standalone briefs, and scratch artifacts. Verify the ignore rule in the project where you are working. Keep `.work/` out of commits unless the human explicitly names an exception.

## Lifecycle hooks

Mirket includes three plugin hooks, requiring Python 3 in the host environment:

- **On a user prompt:** request that the agent read and apply [distill](plugins/mirket/skills/distill/SKILL.md) to its user-facing messages for the turn.
- **Before delivery:** on a supported `Stop` event, request one task-scoped cleanup review before the response finishes. It uses the host's continuation flag to avoid repeated loops.
- **Before an agent-issued commit:** for supported direct `git commit` calls through the agent's Bash tool, block an unacknowledged attempt and request a repository-wide cleanup review. After reviewing, retry with a command-local marker, for example `MIRKET_CLEANUP_DONE=1 git commit -m "message"`. Each commit in a compound command needs its own marker. The marker acknowledges the review; it does not prove cleanup occurred or override host permissions.

The cleanup hooks instruct the agent to use [Clean](plugins/mirket/skills/clean/SKILL.md); they do not themselves delete or stage files. Hooks cannot guarantee agent compliance. Codex requires review and trust of plugin hooks before they run; changing a hook requires renewed review. Hook activation and behavior in each host have not been verified.

Coverage is limited: disabled or untrusted hooks, interruptions, API failures, shared Stop-loop state, unsupported tool paths, PowerShell, Git aliases, scripts, nested shells, heredocs or here-strings, wrapper options, interactive shell input and commits outside the agent can bypass these checks. The shell recognizer handles direct commands and basic `env`/`command` wrappers, not a complete shell grammar. For a heredoc or here-string, it inspects only the prefix before the operator and warns when it cannot fully inspect the command. Hooks are guardrails, not a security boundary. OpenAI's public plugin directory does not accept lifecycle hooks; local marketplace distribution has different rules. See the [Codex hook documentation](https://learn.chatgpt.com/docs/hooks) and [Claude Code hook reference](https://code.claude.com/docs/en/hooks).

## Authoring and verification

Add each skill at `plugins/mirket/skills/<skill-name>/SKILL.md` with a matching lowercase command verb and a clear trigger. Add `agents/openai.yaml` for its Codex-facing display name and short description. Keep skill guidance self-contained. Record substantial adaptations and applicable notices in [sources.json](plugins/mirket/sources.json).

Run `python3 -B -m unittest discover -s tests` for synthetic hook checks and `python3 -B -m unittest discover -s memory` for the memory installer and registry checks.

Once the catalog is ready for behavioral testing, evaluate discovery, explicit invocation and representative tasks in fresh Codex and Claude Code sessions. Package checks do not establish live host behavior. A license for this collection has not yet been chosen.
