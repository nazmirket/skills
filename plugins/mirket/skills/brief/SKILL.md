---
name: brief
description: "Use when writing a work handoff for another agent, session, or worker, or updating a recipient about a relevant change in parallel work."
---

# Brief

Write a concise, actionable prompt suited to its recipient and the work they need to continue. A handoff preserves useful context without assuming it will still be current.

## Prepare the handoff

1. Identify the recipient, the task's purpose and the desired outcome. State what the recipient should do and what success looks like. Tailor the detail to the recipient's role and access rather than using the same prompt for every handoff.
2. Put the exact next action first. Link the authoritative plan, source, or result rather than copying evidence the recipient can access. Include the approved scope, what is complete or pending, key risks, useful verification and its limits, and the skills that will help. Redact secrets and unnecessary personal information. Include enough context to act when a source is inaccessible.
3. Direct the recipient to check that the handoff is still relevant before relying on it. Have them inspect the current task and working state, confirm relevant paths and evidence, and account for changes since the handoff. If the task or material decisions no longer match, surface the discrepancy instead of following stale instructions blindly. A handoff supplies context; it does not create new authority or override the human's current instructions.

## Adapt to the target

4. For a future session, include the task identity, current status, applicable workspace or plan paths, and a concrete next step. Make the handoff usable without access to this conversation. If saving a standalone brief without a designated destination, use `.work/briefs/` under the project root and follow the [workspace rules](../../references/workspace.md). [Sleep](../sleep/SKILL.md) owns the pause and resume workflow; preparing a brief alone does not pause work.
5. For a subagent, define its exact work scope, ownership boundaries, expected deliverable, dependencies and verification. Describe relevant parallel agents or worktrees, including their scopes and shared boundaries, so the recipient understands what is happening around its work. Specify how to report findings, blockers and decisions to the root agent; do not assign it authority to change another agent's scope.
6. As the root agent, promptly update affected subagents when a meaningful change in another worktree, agent's work, shared interface, decision or dependency is relevant to them. State what changed, its impact on their scope and any action needed. Use the available coordination channel; if an update cannot be delivered, report that limitation and do not claim it was received.

**Done:** The recipient has a clear next action, authoritative evidence, explicit boundaries and a relevance check. Draft or save the brief within scope; external delivery requires authorization.
