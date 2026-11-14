# Mirket documentation

Mirket is a free, open-source plugin with 16 skills for Codex and Claude Code. Its workflows cover planning, design, engineering, security, migration, release, deployment and operations.

## Install Mirket

Add the Mirket marketplace in your host, install `mirket@mirket`, and start a fresh session. Install it in each host you want to use.

### Install in Codex

```sh codex-install
codex plugin marketplace add https://github.com/nazmirket/skills.git
codex plugin add mirket@mirket
```

### Install in Claude Code

```sh claude-code-install
claude plugin marketplace add nazmirket/skills
claude plugin install mirket@mirket
```

If your host asks you to trust hooks, [review what they do](../CONTRIBUTING.md#lifecycle-hooks). You can also use the [Codex setup prompt](#codex-setup-prompt) or the [Claude Code setup prompt](#claude-code-setup-prompt).

## Purpose

Use Mirket when you want the agent to follow a repeatable workflow: diagnose a bug before fixing it, plan a substantial change, design an interface, or review a result. You can ask for an outcome in plain language or name a skill directly: “Use Mirket Debug to reproduce this failure and find its cause.”

Use the plugin one request at a time. The [Codex](../instructions/AGENTS.md) and [Claude Code](../instructions/CLAUDE.md) instructions are optional if you want Mirket to guide work by default.

## Philosophy

- **Choose guidance for the job.** Pick one primary skill for the requested result. Add another when it supplies a distinct result or check. A small task can stay small.
- **Keep consequential choices with the human.** A request to do work and approval of a written plan are separate. Ask for decisions that affect the outcome; proceed with routine choices within the agreed scope.
- **Verify claims with evidence.** Inspect the actual change, run checks that match the risk, and say what could not be verified. A review or hook reminder does not prove that the work was checked.
- **Leave enough context to resume.** Keep substantial plans and handoffs in the project's [workspace records](../references/Workspace.md). Record settled architectural decisions in the repository's ADR location, using `docs/decisions/` when the project has none. Keep the response focused on what happened and what comes next.

## Skills

A skill is a Markdown workflow with a trigger, guidance, and sometimes more detailed references. The host can choose a skill from its description; you can also request one by name. See the [routing guide](../references/Routing.md) when several skills sound relevant.

| What you need | Skills |
| --- | --- |
| Solve the assigned problem directly and report what matters | [Execute](../skills/execute/SKILL.md), the default across Mirket workflows |
| Understand the project and its environment | [Adapt](../skills/adapt/SKILL.md), [Preflight](../skills/preflight/SKILL.md) |
| Compare options and plan the work | [Equip](../skills/equip/SKILL.md), [Architect](../skills/architect/SKILL.md), [Plan](../skills/plan/SKILL.md) |
| Make or improve something | [Design](../skills/design/SKILL.md), [Author](../skills/author/SKILL.md), [Debug](../skills/debug/SKILL.md), [Refactor](../skills/refactor/SKILL.md) |
| Check the result and tidy up | [Test](../skills/test/SKILL.md), [Audit](../skills/audit/SKILL.md), [Design](../skills/design/SKILL.md#visual-critique) for visual review, [Author](../skills/author/SKILL.md) for writing review, [Clean](../skills/clean/SKILL.md) |
| Review security and privacy or model design threats | [Audit](../skills/audit/SKILL.md#security-and-privacy-review) for findings, [Architect](../skills/architect/SKILL.md#model-threats-during-design) for design decisions |
| Change persistent state | [Migrate](../skills/migrate/SKILL.md) |
| Ship and operate | The task owner prepares and publishes; [Deploy](../skills/deploy/SKILL.md) activates and handles [service health and recovery](../skills/deploy/SKILL.md#operate-and-recover) |
| Coordinate, hand off, pause, or resume work | [Plan](../skills/plan/SKILL.md#coordinate-workers) coordinates workers; [Brief](../skills/brief/SKILL.md) owns handoffs and continuity |

## From a product decision to a running service

Choose the owner by the requested result. These responsibilities can overlap in a project without becoming mandatory steps for every task.

| Outcome | Owner | Evidence at the handoff |
| --- | --- | --- |
| Decide what is worth building or whether a shipped feature helped | The human | User problem, observed outcomes and options |
| Establish a technical approach and sequence substantial work | Architect and Plan | Boundaries, constraints, authority, acceptance and recovery criteria |
| Build the requested behavior or artifact | The implementer, with Design/Author/Debug/Refactor as relevant | Actual implementation, focused checks, and review findings from the relevant owner |
| Assess security and privacy or model design threats | Audit for review, Architect for design | Trust and data boundaries, evidence about safeguards, open risks and decisions |
| Harden an authorized target | The implementer | Verified safeguards and preserved legitimate access |
| Change schemas, data formats or persistent configuration | Migrate | Preserved meaning and access, compatible consumers, reconciled state and recovery |
| Prepare or publish a version | The task owner | Exact artifact, packaging and upgrade checks, notes, and distribution state |
| Roll that artifact into an environment | Deploy | Target, rollout and served-path verification, rollback or forward recovery |
| Maintain health and respond to failure | Deploy’s operations branch | Current signals, capture and freshness where relevant, recovery and runbook |

For example, a version adding a new persisted field may need Migrate to rehearse compatibility and reconciliation before Deploy switches consumers. A documentation edit can go directly through implementation and focused checks. Preparation is not publication, and publication is not proof of deployment. Existing execution authorization remains valid; new production targets or data-sharing decisions need their own authority.

## Architecture

The repository root is the shared plugin package. [Codex](../.agents/plugins/marketplace.json) and [Claude Code](../.claude-plugin/marketplace.json) marketplace entries both point to it. The canonical [skills catalog](../skills/) is independent of the marketplace descriptors, so future targets can package the same definitions.

- **Skills and references.** Each packaged skill has a `SKILL.md` with its trigger and workflow, plus `agents/openai.yaml` for its Codex display metadata. Skill-specific and shared references cover details such as routing, workspace records, and review loops.
- **Plugin descriptors and hooks.** [`.codex-plugin/plugin.json`](../.codex-plugin/plugin.json) and [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json) preserve the same identity and version. The [Codex compatibility layout](decisions/0003-CodexHookCompatibility.md) keeps hook discovery working in the verified host version. On supported host events, [lifecycle hooks](../CONTRIBUTING.md#lifecycle-hooks) supply routing, communication, and delivery guidance and guard certain commit paths. Hooks depend on host support and trust settings; they cannot guarantee compliance.
- **Documentation.** The website reads this guide and the packaged skill Markdown at build time. The documentation and the plugin workflows stay in the same repository.

### Codex setup prompt

Paste this into Codex to install Mirket.

```text codex-setup
Add https://github.com/nazmirket/skills.git as a Codex plugin marketplace, install mirket@mirket, and verify the installation. Tell me how to start a fresh Codex session and verify what was installed.
```

### Claude Code setup prompt

Paste this into Claude Code to install Mirket.

```text claude-code-setup
Add nazmirket/skills as a Claude Code plugin marketplace, install mirket@mirket, and verify the installation. Tell me how to start a fresh Claude Code session and verify what was installed.
```

## Common questions

### What does Mirket add to Codex or Claude Code?

Mirket adds reusable Markdown workflows to your existing coding agent. Each skill explains when to use it, what steps to follow, and what evidence to check. Mirket does not provide a model or run as a standalone coding agent.

### How do I use a Mirket skill?

Ask for the result you want, or name the skill directly. For example, “Use Mirket Debug to reproduce this failure and find its cause.” The agent can also choose a skill based on its description. Use the [skill catalog](#skills) to find the right starting point.

### Is Mirket free to use at work?

Yes. Mirket is free to use, modify, and redistribute, including commercially, under the [MIT License](../LICENSE). Your Codex or Claude Code access is separate.

### What is the difference between Test and Audit?

[Test](../skills/test/SKILL.md) checks whether behavior meets expectations and records the evidence. [Audit](../skills/audit/SKILL.md) reviews a change, plan, or system for defects and risks. A test result can be evidence in an audit.

### How do publication, deployment and operation differ?

The task owner follows the [versioned distribution guide](../references/VersionedDistribution.md) to identify, check, and distribute the artifact when authorized. [Deploy](../skills/deploy/SKILL.md) activates that artifact in a specific environment and verifies the served behavior. Its [operations branch](../skills/deploy/SKILL.md#operate-and-recover) covers ongoing health, incidents, and recovery. [Migrate](../skills/migrate/SKILL.md) handles persistent state. [Audit](../skills/audit/SKILL.md#security-and-privacy-review) supplies security and privacy findings when needed.

### How do I verify an update is actually in use?

Check the installed package version and skill files, merge the matching optional global instructions without replacing unrelated guidance, and open a fresh host session. Review changed hooks through the host's trust flow. Run the [host smoke cases](../tests/HostSmoke.md); source checks and cached package contents alone do not establish live invocation.
