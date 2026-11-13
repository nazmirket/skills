---
name: adapt
description: "Use when relevant understanding of a project, workspace, feature, workflow, or the human's working preferences is missing or stale."
---

# Adapt

Understand the target and the human's working context as a thoughtful coworker. Orient when the task needs understanding that is missing or stale; reuse current evidence that covers the same scope. Adapt is read-only.

## Understand the target

1. Establish the target and the purpose of this orientation from the human's request and available context. Identify the relevant scope and current task; ask a focused question if the target cannot be determined.
2. Inspect the relevant instructions, current work, documentation and version-control state where available. Follow the affected entry points through connected behavior, outputs and dependencies. For a broader request, examine representative areas and how they fit together. Respect existing user changes.
3. Establish the purpose, behavior, conventions, assumptions and constraints needed for the requested scope and its risks. Include architecture, principles and prior decisions when they matter. Distinguish documented reasons from inferences. Stop once the next task has enough grounded context; report material gaps rather than expanding into an unrelated audit.

## Get to know the human

4. Use the human's stated goals, working principles, preferences, prior decisions and feedback from the conversation and relevant project records. Carry useful context forward instead of repeatedly starting from zero.
5. Separate explicit preferences from tentative patterns. Check remembered context against current instructions and project evidence when it could affect a decision; ask only if a material uncertainty remains. Current instructions and corrections take precedence over stale records. Do not infer a diagnosis or fixed personality, search unauthorized private history, or create a persistent profile without authorization.


## Share the understanding

6. Carry a compact map of the relevant purpose, entry points, flow, conventions, evidence and gaps into the next task. Show the human the findings when requested or when they affect a decision; otherwise keep the handoff focused. Distinguish observed facts, the human's statements, inferences and unanswered questions. Give [Debug](../debug/SKILL.md) the expected and observed finding and supporting evidence, or give [Architect](../architect/SKILL.md) the affected boundaries and observed friction.
7. Surface a discrepancy, questionable assumption or potential problem when it matters; do not repair it during orientation. After orientation, continue to a fix or other work already authorized by the human without asking again. Resolve any new product decision or scope change with the human.

**Done:** The next task has enough evidence about its target, relevant conventions, human context and remaining gaps. No fix is performed during orientation.
