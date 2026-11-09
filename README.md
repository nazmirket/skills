# Mirket

Mirket is a collection of agent skills for understanding a project, planning work, coordinating execution, debugging and reviewing quality. The `mirket` plugin shares one set of skills across Codex and Claude Code; `mirket-native-marketplace` provides a local marketplace for each host.

The skills are under active development. Catalog-wide behavioral testing, plugin installation and host-specific discovery remain outstanding. An earlier limited exercise of the plan skill is preserved in [history](docs/history/plan-evaluation.md).

## Skills

| Skill | Purpose |
| --- | --- |
| [mirket:adapt](plugins/mirket/skills/adapt/SKILL.md) | Understand the target, its conventions and the human's working preferences without making fixes. |
| [mirket:discover](plugins/mirket/skills/discover/SKILL.md) | Assess environment readiness against project requirements and propose fixes for blockers. |
| [mirket:plan](plugins/mirket/skills/plan/SKILL.md) | Create an evidence-based plan and record the desired outcome and human decisions. |
| [mirket:orchestrate](plugins/mirket/skills/orchestrate/SKILL.md) | Coordinate subagents working on distinct scopes of an agreed plan. |
| [mirket:debug](plugins/mirket/skills/debug/SKILL.md) | Investigate and fix a concrete finding identified during orientation. |
| [mirket:critique](plugins/mirket/skills/critique/SKILL.md) | Review relevant visual, integration, performance, simplicity and efficiency concerns. |

Skill names in `SKILL.md` remain unprefixed, such as `plan`; the plugin supplies the `mirket:` namespace. Claude Code documents plugin commands such as `/mirket:plan`. Codex-facing labels are configured separately in each skill's `agents/openai.yaml`. Exact host display and invocation remain unverified.

## Project layout

```text
.agents/plugins/marketplace.json       Codex marketplace
.claude-plugin/marketplace.json        Claude Code marketplace
plugins/mirket/plugin.json             Portable plugin metadata
plugins/mirket/.claude-plugin/plugin.json Claude Code plugin metadata
plugins/mirket/skills/                 Shared skill instructions and display metadata
templates/                             Materials for authoring another skill
docs/history/                          Earlier research, outline and plan evaluation
.planning/                             Historical and current task planning records
```

The marketplace source paths are relative to this project root. Both descriptors point to `plugins/mirket`, and both plugin manifests identify the plugin as `mirket`. The Claude marketplace owner `mirket` is a project label; it does not assert a legal author or license.

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

## Authoring and verification

Add each skill at `plugins/mirket/skills/<skill-name>/SKILL.md` with a matching lowercase, hyphenated `name` and a description of when to use it. Add `agents/openai.yaml` for its Codex-facing display name and short description. The [skill brief](templates/skill-brief.md) and [skill template](templates/skill-template.md) are optional authoring aids; they are not installed skills.

Once the catalog is ready for testing, evaluate each skill in fresh Codex and Claude Code sessions, covering discovery, explicit invocation, representative tasks, counterexamples and unavailable capabilities. Structural metadata checks do not demonstrate behavior. Preserve source attribution and applicable licenses if adapting external material; a license for this collection has not yet been chosen.

The [initial outline](docs/history/OUTLINE.md) and [parent-skill review](docs/history/PARENT-REVIEW.md) record earlier design decisions and are historical, not current instructions. A license for this collection has not yet been chosen.
