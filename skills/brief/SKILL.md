---
name: brief
description: "Use to hand off work to another agent or session, send a relevant coordination update, or pause and resume work on request."
---

# Brief

Brief owns handoffs, coordination messages, and requested pauses and resumptions. [Plan](../plan/SKILL.md#coordinate-workers) assigns work and chooses who needs a material update.

## Prepare the handoff

Give the recipient the outcome, exact next action, authorized scope and its source, essential evidence and what to recheck. Link accessible plans and results. Copy only what the recipient cannot retrieve or what would materially delay the next action. State evidence limits and omit secrets and unnecessary personal information.

Check current state and authority against the instructions for the next action. Correct routine drift and continue within scope. If sources conflict on the goal, authority, product decision, ownership, interface or acceptance criteria, pause only the affected work and take the evidence to the coordinator or human.

## Adapt to the target

- **Future session.** Include the task identity, status and workspace or plan location so work can resume without the old conversation.
- **Worker.** Specify the owned scope, deliverable, dependencies and checks. Mention parallel work only where it affects the assignment. Report routine corrections.
- **Coordination update.** Tell affected recipients what changed, how it affects their work and what to do next. Report unconfirmed delivery.

Use the coordination channel for immediate assignments and updates. For a requested or reusable handoff, use the designated destination or save a [numbered brief](../execute/references/Workspace.md#numbered-records) in `.work/briefs/` at the project root. Get authorization before sending outside the task.

## Pause or resume

On a pause request, stop starting work. Check only what is needed for a reliable resume point. Stop task-owned workers when safe and supported. Leave unsafe-to-interrupt operations running and record what is running or uncertain. For unfinished work, save a numbered brief with current state and next action. Give the human its path and a resume prompt, or the handoff itself if saving fails. If no unfinished work is identifiable, say so and save context only on request. Wait for the human to resume.

On resume, read the named handoff or the one for the clearly identified task. Apply the state and authority checks above, then continue the authorized next action.
