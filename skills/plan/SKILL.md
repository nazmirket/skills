---
name: plan
description: "Plan substantial or risky work, coordinate workers, or check progress on authorized work."
---

# Plan

Use a plan on request or when dependencies, risk or coordination warrant one. Keep routine authorized work direct. Go straight to [coordination](#coordinate-workers) for assignments or [tracking](#track-authorized-work) for status.

## Build the plan

- Establish the outcome, baseline, authority and acceptance criteria. Reuse settled decisions and evidence. Use [Adapt](../adapt/SKILL.md) for missing facts that affect the plan and [Architect](../architect/SKILL.md) for consequential system choices. Surface assumptions and bring material product or scope decisions to the human.
- Sequence work by dependency and pair each step with a check. Specify owners, interfaces and integration checks for shared work. Include migration, cutover, stop and recovery steps when the risk warrants them. Use [Audit](../audit/SKILL.md#independent-review) when independent review is required or a distinct review would change readiness.

## Save only what needs to last

Keep a plan in chat when the session can carry it. For durable tracking or handoff, use `Plan.md` in a [numbered folder](../execute/references/Workspace.md#numbered-records) under `.work/plans/` per the [workspace rules](../execute/references/Workspace.md). Use a shared location only on request or project requirement.

Record the outcome, source of authority and material decisions, pending criteria, evidence links, steps and current status. Capture revision, environment, commands and results for baselines that are hard to reconstruct. Track implementation and verification separately. Split evidence, scope, outcome or progress into dedicated files only when scale or project convention calls for it. Resume existing plans in their current layout, preserve the agreement and update status from verified evidence.

## Hand off or execute

For a plan-only request, use read-only checks and stop at the plan. Implement, build candidates or rehearse under existing execution authority. Mark a written plan approved only on its explicit approval. Adjust routine details within the agreed boundaries. Keep blocked decisions and review gates open while independent authorized work proceeds. Close when work and required checks are complete or the human explicitly accepts remaining gaps.

## Coordinate workers

- When authorized and supported, the root delegates directly on request or where parallel work saves time or adds independent evidence. Only the root spawns workers. Keep coupled edits together. If requested delegation is unavailable, report the limit and continue within authority. Keep required independence and isolation gates open.
- Set the assignment's authority, outcome, interface and integration order before dispatch. Bounded read-only investigation can start earlier. Use [Brief](../brief/SKILL.md) to communicate scope, guidance, deliverable and checks. Give concurrent writers exclusive paths or isolated workspaces and sequence shared writes. Match available model capability to the work, with a strong model for creative work and sufficient reasoning for consequential decisions.
- Workers report results, checks and blockers to the root and flag boundary changes before acting. The root resolves conflicts, updates shared progress and verifies the integrated result.

## Track authorized work

Read the matching record. Report completed, next and blocked work with evidence, distinguishing reported, verified and unknown status. Recheck stale evidence only where it affects readiness, or name the gap. Stop after a status-only snapshot. During authorized execution, give the update and continue unless asked to pause. Save a standalone status update only on request in the existing status location.
