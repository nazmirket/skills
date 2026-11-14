---
name: adapt
description: "Use to discover or refresh missing or stale facts about a project, its implementation, and the decisions or rules that govern it."
---

# Adapt

Adapt finds and explains project facts. It is read-only. The skill responsible for the requested outcome acts on the findings.

## Build or refresh context

Establish the target and what the next task needs to know. Ask a focused question if the target cannot be determined. On a new codebase, survey the main subsystems and how they fit together through representative paths before any edit. On a familiar project, reuse verified context. A different feature, worktree, or change in evidence may make earlier findings stale; refresh only what matters to the current task. Check the relevant working state and respect existing changes.

Consult relevant sources in this order:

1. **Project documentation:** Read the applicable instructions and guides for the intended behavior and conventions.
2. **Architecture decision records (ADRs):** Find relevant decisions, their rationale, and any superseding records.
3. **Project memory:** For substantial or resumed work, consult relevant, authorized project memory when available. Skip recall for routine tasks. Treat remembered facts as leads and check anything that affects the next step against current evidence.
4. **Codebase:** Trace the relevant entry points, callers, dependencies, and outputs. Use current code and checks to establish what is implemented.

The order is for gathering context. Current user instructions and corrections take precedence over stale records. When documented intent and implementation disagree and the work depends on which contract applies, show the discrepancy and ask the human which should govern before proceeding on that part.

## Carry forward what matters

Reuse relevant architecture decisions, solution patterns, system design direction, and enforced rules. A one-off correction stays local; apply it as a project default only when the human repeats or confirms it. Use inferred patterns as leads, without treating them as stated preferences. If a durable rule would help, propose its exact wording and destination and wait for approval before recording it. Do not search unauthorized private history or create a persistent profile.

## Hand off the finding

Stop once the next task has enough context. Pass the relevant facts, evidence, constraints, and remaining gaps to the skill that will act on them. For an observed problem that explains the requested issue, give [Debug](../debug/SKILL.md) the expected and observed behavior and the supporting evidence; an authorized fix continues there. For a consequential system boundary or tradeoff, give [Architect](../architect/SKILL.md) the affected boundaries and observed friction. Routing evidence to a skill does not require a separate agent.

Share an orientation summary only when requested or when a finding needs the human's decision. If a finding changes the approach to already authorized work, give a one-line update and continue under the responsible skill. Adapt does not make repairs or broaden the authorized scope.

**Done:** The responsible skill has the evidence it needs, or the human has the specific gap or decision needed to proceed.
