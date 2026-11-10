# Mirket documentation

Mirket is a collection of reusable skills for Codex and Claude Code. Each skill gives an agent a way to approach a particular kind of work, from understanding a project to checking a change and handing it off.

## Purpose

Use Mirket when you want the agent to follow a repeatable workflow: diagnose a bug before fixing it, plan a substantial change, design an interface, or review a result. You can ask for an outcome in plain language or name a skill directly: “Use Mirket Debug to reproduce this failure and find its cause.”

[Installation and first prompts](../README.md#install) are in the project README. The plugin can be used one request at a time. The [Codex](../instructions/AGENTS.md) and [Claude Code](../instructions/CLAUDE.md) instructions are optional if you want Mirket to guide work by default.

## Philosophy

- **Choose guidance for the job.** Pick one primary skill for the requested result. Add another when it supplies a distinct result or check. A small task can stay small.
- **Keep consequential choices with the human.** A request to do work and approval of a written plan are separate. Ask for decisions that affect the outcome; proceed with routine choices within the agreed scope.
- **Verify claims with evidence.** Inspect the actual change, run checks that match the risk, and say what could not be verified. A review or hook reminder does not prove that the work was checked.
- **Leave enough context to resume.** Keep substantial plans, decisions, and handoffs in the project's [workspace records](../plugins/mirket/references/workspace.md). Keep the response focused on what happened and what comes next.

## Skills

A skill is a Markdown workflow with a trigger, guidance, and sometimes more detailed references. The host can choose a skill from its description; you can also request one by name. See the [routing guide](../plugins/mirket/references/routing.md) when several skills sound relevant.

| What you need | Skills |
| --- | --- |
| Understand the project and its environment | [Adapt](../plugins/mirket/skills/adapt/SKILL.md), [Preflight](../plugins/mirket/skills/preflight/SKILL.md), [Equip](../plugins/mirket/skills/equip/SKILL.md) |
| Decide what to do and how to approach it | [Focus](../plugins/mirket/skills/focus/SKILL.md), [Curate](../plugins/mirket/skills/curate/SKILL.md), [Architect](../plugins/mirket/skills/architect/SKILL.md), [Plan](../plugins/mirket/skills/plan/SKILL.md) |
| Make or improve something | [Design](../plugins/mirket/skills/design/SKILL.md), [Imagine](../plugins/mirket/skills/imagine/SKILL.md), [Author](../plugins/mirket/skills/author/SKILL.md), [Debug](../plugins/mirket/skills/debug/SKILL.md), [Refactor](../plugins/mirket/skills/refactor/SKILL.md) |
| Check the result and tidy up | [Test](../plugins/mirket/skills/test/SKILL.md), [Audit](../plugins/mirket/skills/audit/SKILL.md), [Critique](../plugins/mirket/skills/critique/SKILL.md), [Clean](../plugins/mirket/skills/clean/SKILL.md) |
| Coordinate and communicate | [Orchestrate](../plugins/mirket/skills/orchestrate/SKILL.md), [Distill](../plugins/mirket/skills/distill/SKILL.md), [Brief](../plugins/mirket/skills/brief/SKILL.md), [Sleep](../plugins/mirket/skills/sleep/SKILL.md) |

## Architecture

The [plugin package](../plugins/mirket/) is shared by both hosts. Separate [Codex](../.agents/plugins/marketplace.json) and [Claude Code](../.claude-plugin/marketplace.json) marketplace manifests point to it.

- **Skills and references.** Each packaged skill has a `SKILL.md` with its trigger and workflow, plus `agents/openai.yaml` for its Codex display metadata. Skill-specific and shared references cover details such as routing, workspace records, and review loops.
- **Plugin descriptor and hooks.** [`plugin.json`](../plugins/mirket/plugin.json) describes the package. On supported host events, [lifecycle hooks](../CONTRIBUTING.md#lifecycle-hooks) request communication and cleanup reviews and guard certain commit paths. Hooks depend on host support and trust settings; they cannot guarantee compliance.
- **Optional memory.** [Local Hindsight](#optional-local-hindsight) is separate from the plugin's skills. It can preserve project context across sessions and is not required to use Mirket.
- **Documentation.** The website reads this guide and the packaged skill Markdown at build time. The documentation and the plugin workflows stay in the same repository.

## Optional local Hindsight

Mirket works on its own. To carry project context across sessions, you can opt into Hindsight's local daemon in either host. Codex uses [Mirket's guarded installer and project registry](../memory/README.md#recommended-local-daemon). Claude Code uses the [upstream Coding Agents integration](../memory/README.md#claude-code-with-the-upstream-installer).

Before opting in, choose a model provider and decide which projects you want to capture. The daemon can store memory locally while a hosted model provider still processes captured context remotely. Review the guide's capture defaults before enabling the integration.

### Codex setup prompt

Paste this into Codex to install Mirket and decide separately whether to set up Hindsight.

```text codex-setup
Install Mirket for Codex, then ask me: “Set up optional local Hindsight for Codex, or keep Mirket only?” Wait for an explicit yes before changing Hindsight. If I decline or don't answer, leave it unchanged.

For Mirket, add https://github.com/nazmirket/skills.git as a Codex plugin marketplace, install mirket@mirket, and verify the install.

If I opt in, follow https://github.com/nazmirket/skills/blob/main/memory/README.md. Confirm my model provider and capture preferences. Check for an existing setup and use the read-only preflight before a fresh install. Preserve existing memory and configuration.

In either case, tell me how to start a fresh Codex session and verify what was installed.
```

### Claude Code setup prompt

Paste this into Claude Code. Hindsight is a separate, optional installation.

```text claude-code-setup
Install Mirket for Claude Code, then ask me: “Set up optional local Hindsight for Claude Code, or keep Mirket only?” Wait for an explicit yes before changing Hindsight. If I decline or don't answer, leave it unchanged.

For Mirket, add nazmirket/skills as a Claude Code plugin marketplace, install mirket@mirket, and verify the install.

If I opt in, follow the Claude Code setup at https://github.com/nazmirket/skills/blob/main/memory/README.md#claude-code-with-the-upstream-installer. Confirm my model provider and which projects to capture. Check for an existing daemon and shared runtime. If Mirket manages Hindsight for Codex, use the guide's existing-install path and verify the Codex adapters still work. Preserve existing banks and settings.

In either case, tell me how to start a fresh Claude Code session and verify what was installed.
```

### Manual Hindsight setup

- **Codex:** Follow the [local daemon guide](../memory/README.md#recommended-local-daemon) and run `python3 memory/install.py --check` from a checkout before a fresh install. If you opt in and the check passes, run `python3 memory/install.py`; for an existing install, follow the guide's wiring instructions.
- **Claude Code:** Follow the [upstream installer steps](../memory/README.md#claude-code-with-the-upstream-installer) to use a local daemon and check for a shared Hindsight runtime before installing.
- **Verify in the host you use:** Restart it, review the hooks, check the resolved bank, and test recall with a harmless fact in a fresh session.
