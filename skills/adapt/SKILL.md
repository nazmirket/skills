---
name: adapt
description: "Use to discover or refresh missing or stale facts about a project, its implementation, and the decisions or rules that govern it."
---

# Adapt

Adapt owns read-only orientation to a project. [Search](../search/SKILL.md) owns external research. Identify the project and what the next task needs to know. Ask if the target is unclear.

## Build or refresh context

On a new codebase, trace representative paths across the main subsystems before editing. On familiar ground, reuse verified context. Refresh facts affected by the feature, worktree or new evidence. Check the working state and respect existing edits.

Consult relevant sources in order.

1. Read project instructions and guides for intended behavior and conventions.
2. Read applicable architecture decision records (ADRs), their rationale and any successors.
3. For substantial or resumed work, consult available, authorized project memory. Skip recall for routine tasks. Verify remembered facts that affect the next step.
4. Trace entry points, callers, dependencies and outputs. Use current code and checks to establish actual behavior.

When a project fact depends on PDFs, spreadsheets or a mixture of local records, use [finding evidence in project records](references/ProjectRecords.md) to locate and reconcile the relevant passages or cells.

Current human instructions and corrections take precedence over stale records. If documented intent and implementation disagree, use the contract established by the current request or applicable decision. Ask which contract governs only when the discrepancy leaves a material choice unresolved.

## Carry forward what matters

Reuse established decisions, design direction, patterns and enforced rules. Treat inferred preferences as leads. A correction becomes a project default only when the human repeats or confirms it. Before recording a durable rule, propose its wording and destination and wait for approval. Use only authorized history. Never build a persistent profile.

## Hand off the finding

Stop when the owner has enough evidence. Return facts, constraints and gaps. Give [Debug](../debug/SKILL.md) the expected and observed behavior for a failure or authorized repair. Give [Architect](../architect/SKILL.md) the affected boundaries and observed friction for a design decision. Either handoff can happen within the same agent.

Summarize orientation for the human when requested or when a decision is needed. If a finding changes the approach to authorized work, give a one-line update and continue under its owner.
