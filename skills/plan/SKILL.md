---
name: plan
description: "Use when risk, coordination, or an explicit request calls for a plan, or to coordinate workers or track progress on authorized work."
---

# Plan

Plan owns execution plans, worker coordination and status checks. Plan on request or when risk or coordination warrants it. Routine authorized work can proceed directly regardless of file count. For assignments or status, go to [coordination](#coordinate-workers) or [tracking](#track-authorized-work).

## Build the plan

- Establish outcome, state and authority. Use [Adapt](../adapt/SKILL.md) for missing or stale facts and derive steps and checks from settled ADRs. Distinguish requirements from assumptions. Take unresolved product rules, success criteria or scope to the human with evidence. Continue independent planning.
- Order steps by dependency and pair each with an outcome check. Keep single-agent steps short. For handoffs or shared interfaces, name owners, inputs, deliverables and integration checks. Include migration, cutover, stop and recovery steps where needed. Use [Architect](../architect/SKILL.md) for consequential system design.
- Seek a fresh read-only [Audit](../audit/SKILL.md) for substantial plans when feasible and authorized. Record findings and resolutions or disclose unavailable review. Keep any [required independent review](../audit/SKILL.md#independent-review) open until met. Continue work that can proceed independently.

## Save only what needs to last

Keep a short plan in chat when it can be used there. For a durable plan, follow the [workspace rules](../execute/references/Workspace.md) and use one [numbered folder](../execute/references/Workspace.md#numbered-records) under `.work/plans/` at the project root. Use a shared project location only on request or explicit project requirement.

- `Evidences.md` records starting state, evidence links and gaps. For hard-to-reconstruct evidence, include revision, environment, commands and baseline results.
- `Scope.md` names the authorized work, separate decisions and the source of each boundary in plain language. Identify who made each material decision.
- `Outcome.md` gives the result, specifications and acceptance criteria. Mark unresolved specifications pending.
- `Plan.md` sequences dependencies and checks, including coordination, integration, migration or recovery where relevant. Mark the plan draft or explicitly approved.
- `Progress.md` tracks implementation and required verification separately in a live checklist. Record material changes, blockers and evidence links. For shared work, include active owners, dependencies and handoff changes.

On resuming an active older plan, convert it in place. Preserve the original agreement, distinguish reconstructed from contemporaneous evidence and seed progress from verified work. Leave completed records intact.

## Hand off or execute

A plan-only request ends with the plan. Use existing evidence and read-only checks. Implementation, candidate builds and rehearsals require execution authority.

Honor existing execution authority. Mark a written plan approved only on explicit approval of that plan. Assess readiness per step. Adjust routine details within the agreed outcome, scope and checks. When a decision or required review blocks a step, pause that step and proceed with authorized independent work. Bring changes beyond the agreed boundaries to the human.

The root agent [coordinates workers](#coordinate-workers) and owns the integrated result. If the plan has a `Progress.md`, only the root updates it. Keep completed work visible beside blocked checks. Close when required checks pass and the work is complete, or record the gaps the human explicitly accepts.

## Coordinate workers

- When delegation is authorized and supported, the root assigns most separable plan work to direct subagents. Its main job is to sequence assignments, resolve conflicts and integrate results. Only the root spawns workers. Keep tightly coupled changes together and handle routine single-agent work directly.
- Before dispatch, settle each outcome, interface, execution authority and integration order. Bounded read-only investigation or review of a fixed target can start earlier. Use [Brief](../brief/SKILL.md) to give each worker its scope, governing guidance, deliverable and checks. Run independent assignments in parallel with exclusive write paths or isolated workspaces. Sequence writes to shared state.
- Give each worker enough model capability and reasoning effort to exercise independent judgment. Choose a strong available model for creative work and high effort for ambiguous or consequential decisions. A lighter profile fits a bounded, deterministic check. Honor the human's limits and the host's model controls.
- Workers report results, checks and blockers directly to the root. They correct routine drift and flag changes to scope, authority, interfaces or acceptance before acting. The root redirects affected workers and takes material product or scope choices to the human.
- Inspect each handback and return substantial repairs to its worker. After handback the root can make bounded integration fixes and must verify the combined result. Use [independent Audit](../audit/SKILL.md#independent-review) on the fixed target when required or materially useful. If delegation is unavailable, disclose the limitation and continue authorized work inline. Required independence and isolation gates stay open.

## Track authorized work

For a status request, read the matching record. Report completed, next and blocked work with evidence and decisions needed. Distinguish reported, verified and unknown status. Verify stale claims that affect the next step. Rerun a safe focused check if it would settle the question, or name the gap.

For a status-only request, end with the snapshot. If the human asks for an update during authorized execution, give the snapshot and continue from the current step unless they ask to pause. Save a standalone status update only on request in the matching plan's `Progress.md` or an older plan's existing status location.
