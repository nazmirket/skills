---
name: brief
description: "Use when writing a work handoff for another agent, session, or worker, or updating a recipient about a relevant change in parallel work."
---

# Brief

Write a concise, actionable handoff suited to its recipient. Preserve useful context without assuming it will still be current.

## Prepare the handoff

1. Identify the recipient and include a small core: the purpose and desired result, exact next action, authorized boundaries, essential evidence, and an instruction to check whether the context is still current. State what success looks like. Tailor other detail to the recipient and task.
2. Link authoritative plans, sources and results, particularly evidence expensive to gather again. If a source may be inaccessible, include the essential facts, identify the missing source and its evidence limits, and avoid implying those facts were independently verified. Redact secrets and unnecessary personal information.
3. Ask the recipient to check the current task and working state, relevant paths and evidence before relying on the handoff. Describe the actual authority already given; an authorized task need not have an approved written plan. A handoff supplies context, not new authority, and never overrides current instructions.

## Adapt to the target

4. For a future session, include task identity, current status, relevant workspace or plan paths, and enough context to continue without this conversation. Direct it to correct routine stale facts from current evidence and ask the human about material conflicts affecting the goal, product decisions or authorized scope. [Sleep](../sleep/SKILL.md) owns the pause and resume workflow; a brief alone does not pause work.
5. For a subagent, define its exact scope, ownership boundaries, expected deliverable, dependencies and verification. Explain relevant parallel work and shared boundaries. The worker reports routine corrections, such as a renamed internal symbol with unchanged behavior, and continues. If a discrepancy affects the target, authority, ownership, interface, or acceptance criteria, report the evidence and pause affected work until the root gives direction. The root updates affected workers; the subagent does not change another worker's scope.
6. When coordinating parallel work, [Orchestrate](../orchestrate/SKILL.md) decides when to update affected workers. Make each update actionable: state what changed, its impact on their scope, and what they should do. If it cannot be delivered, report the limitation; do not claim it was received.

Save a handoff intended for later reuse or when requested. Use its designated destination, or `.work/briefs/` at the project root for a standalone brief under the [workspace rules](../../references/workspace.md). An ordinary subagent assignment can remain in the coordination channel. Sending a message outside the authorized task requires authorization.

**Done:** The recipient has a clear purpose, next action, essential evidence, authorized boundaries and a relevance check appropriate to its role.
