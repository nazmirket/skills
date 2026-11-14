---
name: brief
description: "Use to hand off work to another agent or session, send a relevant coordination update, or pause and resume work on request."
---

# Brief

Write a concise, actionable handoff suited to its recipient. Preserve useful context without assuming it will still be current.

## Prepare the handoff

1. Identify the recipient. Give them the desired outcome, exact next action, authorized scope and its source, essential evidence, and what to recheck. Add detail only when it changes what the recipient should do.
2. Link authoritative plans, sources, and results or give their exact locations when the recipient can access them. Copy only what they cannot retrieve or what would materially delay the next action. Label evidence limits, and omit secrets and unnecessary personal information.
3. Recheck the current working state and the facts needed for the next action. Reuse authority recorded in the handoff only while it still applies and agrees with current instructions. Correct routine drift and continue within scope. Pause affected work if a conflict changes the goal, authority, product decision, ownership, interface, or acceptance criteria. Give the evidence to the human or coordinating owner for a decision.

## Adapt to the target

4. For a future session, include task identity, current status, and the workspace or plan location so the recipient can proceed without the old conversation.
5. For a subagent, specify owned scope, deliverable, dependencies, and verification. Include parallel work only where it affects the assignment. The worker reports routine corrections and continues. Raise material conflicts with the coordinator before changing assignments or shared boundaries.
6. [Plan’s coordination branch](../plan/SKILL.md#coordinate-workers) decides which workers need a material update. State what changed, its impact on their work, and what they should do next. Report when delivery cannot be confirmed.

Save handoffs intended for reuse or when requested. Use the designated destination or a [numbered Markdown brief](../../references/Workspace.md#numbered-records) in `.work/briefs/` at the project root. Keep immediate worker assignments and updates in the coordination channel. Sending a message outside the authorized task requires authorization.

## Pause or resume

- **Pause on request:** Stop starting new work. Check only enough to leave a reliable resume point. Stop task-owned workers only when safe and supported; leave operations running if interruption would be unsafe. Record what is still running or uncertain. For unfinished work, save a numbered handoff in `.work/briefs/` with the current state and next action. Give the human the path and a resume prompt, or give the handoff in the reply if saving fails. If no unfinished work is identifiable, say so and save context only if asked. Stop until the human asks to resume.
- **Resume on request:** Read the named handoff or the one for the clearly identified task. Recheck current state and evidence, correct routine drift, and continue work already authorized. Escalate material conflicts before proceeding with the affected work.

**Done:** The recipient can take the next authorized action, or the task is paused with a usable resume point.
