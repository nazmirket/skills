---
name: plan
description: "Use when risk, coordination, or an explicit request calls for a plan, or to coordinate workers or track progress on authorized work."
---

# Plan

Turn the stated outcome into steps that can be executed and checked. Plan when material risk or coordination warrants it, or when the human asks. File count alone is no reason to plan; routine authorized work can proceed directly. For delegated work, use [Coordinate workers](#coordinate-workers). For status requests, go to [Track authorized work](#track-authorized-work).

## Build the plan

- Establish the outcome, relevant project state, and authority before outlining work. Use [Adapt](../adapt/SKILL.md) for missing or stale project facts. Derive steps and checks from any relevant settled ADRs. Separate confirmed requirements from assumptions. When a product rule, success criterion, or scope choice is unresolved, explain the evidence and ask the human. Continue planning the independent parts.
- Sequence steps by dependencies and give each a check against the desired outcome. Keep steps short for one agent. For handoffs and shared interfaces, specify ownership, inputs, deliverables, integration, and checks. Include migration, cutover, stop conditions, and recovery when the work calls for them. Use [Architect](../architect/SKILL.md) for consequential system design and [Test](../test/SKILL.md) when choosing checks needs specialist guidance.
- For substantial plans, seek a fresh read-only [Audit](../audit/SKILL.md) when feasible and authorized. Record material findings and how they were resolved. If review is unavailable, disclose the gap. Keep any [required independent review](../audit/SKILL.md#independent-review) open and continue only work that does not depend on it. A self-check is not independent review.

## Save only what needs to last

Keep a short plan in chat when it can be used there. When a plan needs to outlive the conversation, use one [numbered folder](../execute/references/Workspace.md#numbered-records) under `.work/plans/` at the project root. Use a shared project location only when the human asks or the project explicitly requires it. Follow the [workspace rules](../execute/references/Workspace.md) before writing.

- `Evidences.md`: The relevant project state before execution. Link the evidence the plan relies on. When the starting state will be hard to reconstruct, include enough to reproduce it: relevant revision, environment, commands, and baseline results. Label material gaps.
- `Scope.md`: In plain language, what is authorized, what needs a separate decision, and which instruction establishes that boundary. Keep material decisions traceable to the person who made them.
- `Outcome.md`: The desired result, clear specifications, and how to tell it was reached. Mark unresolved specifications as pending.
- `Plan.md`: The execution sequence, dependencies, checks, and any coordination, integration, migration, or recovery the work needs. Distinguish draft from explicitly approved plan.
- `Progress.md`: A live checklist with implementation and required verification tracked separately. Include meaningful changes, blockers, and links to evidence. For multiple agents or sessions, also record active owners, dependencies, and handoff changes.

When resuming an active older plan, convert it in the same folder. Preserve the original agreement as history, distinguish reconstructed evidence from evidence recorded before execution, and seed progress from verified work. Leave completed records alone. A status question by itself does not resume or convert a plan.

## Hand off or execute

- A plan-only request ends with the plan. Inspect existing evidence and use read-only checks; do not implement, build a candidate, or create or run a rehearsal.
- Honor existing execution authority without asking again. Approval to execute and approval of a written plan are separate. Mark the plan approved only when the human explicitly approves it. Mark readiness by step: start an authorized, independent step while another is blocked on a decision or required review.
- Make routine adjustments within the agreed outcome, scope, and checks. If a change crosses that boundary, pause the affected step, bring the decision to the human, and continue independent work.
- During execution, the coordinating agent is the single writer of `Progress.md`; workers report results, checks, and blockers. A completed implementation item can coexist with a blocked verification item. Close the plan only when the work is complete and required checks pass or the human explicitly accepts the remaining gaps. Record accepted gaps as gaps.

## Coordinate workers

- When delegation is authorized and the host permits it, prefer parallel work for substantial independent scopes. Keep tightly coupled work inline. The lead agent assigns workers directly, resolves conflicts, and owns integration. Workers report to the lead and do not delegate further.
- Before delegating implementation, settle the shared plan: pin the outcome, interfaces, integration order, and execution authority. Authorized bounded read-only investigation or review of a fixed target can happen earlier, without starting implementation or creating an execution plan.
- Split work along existing modules, artifacts, or roles. Keep work that crosses boundaries together unless the shared contract is clear. Use [Brief](../brief/SKILL.md) for assignments. Give concurrent workers exclusive write paths or isolated workspaces; sequence changes to shared state. Prefer stronger models or effort for consequential, creative, or ambiguous work, and cheaper capable options for bounded deterministic work. Use only host-supported settings.
- Workers report at completion unless a dependency, scope conflict, or material decision needs attention sooner. Correct routine drift within scope. Escalate changes to authority, ownership, interfaces, or acceptance criteria before acting and pause only the affected work. The lead updates affected workers and brings material product or scope decisions to the human.
- Inspect returned work and evidence before accepting it. Give substantial repairs to workers; the lead can make bounded integration corrections after handback once write ownership is clear. Verify the integrated result and use [Audit](../audit/SKILL.md#independent-review) to review the fixed target when independence is required or materially useful. If delegation is unavailable, say so and continue authorized work inline where possible. Leave required independence or isolation gates open when they cannot be met. Self-review is not independent.

## Track authorized work

Find the matching record and report what is done, next, or blocked, with relevant evidence and decisions needed. Distinguish reported, verified, and unknown status. Verify stale claims that could change the next step; rerun a safe focused check if it would settle the question. If the check cannot run safely, report the gap.

A status request does not start work or update the record. If asked to save the status, update `Progress.md` in the matching plan. For an older record that has not been resumed, use its existing status location without converting it. Preserve approval state.
