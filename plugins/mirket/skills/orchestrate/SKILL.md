---
name: orchestrate
description: "Use when coordinating subagents across bounded scopes for an approved plan, read-only investigation, or independent draft review."
---

# Orchestrate

Act as the manager of the plan's execution. The root agent is the sole orchestrator: it organizes the work, directs all subagents, communicates with the human, and owns the integrated outcome. Subagents perform assigned work and report to the root; they do not delegate or create their own subagents.

## Organize the work

1. For execution, confirm the current plan applies, material decisions are settled and the human approved it. Use [Plan](../plan/SKILL.md) to resolve any gap before dependent work. A bounded read-only investigation or independent draft review may run before approval when delegation is authorized; give the reviewer a fixed target and read-only scope. That exception grants no execution authority.
2. Divide work into bounded scopes with outcomes, dependencies and one owner for each shared interface. Assign exclusive writable areas or isolate workspaces where needed. If workers save scratch files, give them distinct destinations under the [workspace rules](../../references/workspace.md). Run dependent or shared-state work sequentially. Handle small scopes inline when delegation adds no value; an inline check cannot stand in for required independence.
3. Check which subagent tools, concurrency limits, model choices and effort controls the host actually permits. Follow the human's explicit preferences and higher-priority host rules. For each scope, choose an available model and effort appropriate to its complexity, uncertainty and consequences when the host allows it. Use only supported settings; if the host controls model or effort, use its permitted default and state that you could not select it. Never claim a choice you could not make.

## Direct and coordinate

4. Use [Brief](../brief/SKILL.md) to prepare each subagent's self-contained assignment: objective, relevant context and plan path, owned scope and boundaries, prerequisites, expected deliverables, verification, and reporting instructions. The root handles delegation, coordination and communication with the human. Workers surface blockers and product decisions.
5. Dispatch independent scopes when their prerequisites are met. Manage dependencies, monitor meaningful progress and adapt assignments as evidence or priorities change. Promptly update affected subagents about relevant changes in other agents' work, worktrees, shared interfaces or dependencies, including their impact and any required action. Negotiate conflicts between scopes, resolve routine technical decisions within the agreed plan, and bring unresolved product choices or material changes to the human. Preserve the human's agreed decisions; do not treat a subagent's recommendation as approval.
6. Inform the human briefly as meaningful subagent outcomes, blockers or decisions arrive. Summarize what changed and its effect on the plan; avoid reporting unchanged status. The root is the messenger: subagents report to the root, and external messages require the human's authorization.

## Integrate and deliver

7. Inspect actual work and evidence from each subagent. Integrate once, resolve ownership conflicts and select [Test](../test/SKILL.md), [Audit](../audit/SKILL.md) or [Critique](../critique/SKILL.md) for the needed evidence. Use [Plan’s tracking branch](../plan/SKILL.md#track-approved-work) for a saved plan status, and preserve user changes. Return a bounded correction to its owner or handle it within the root's authorized scope.
8. Report the outcome against the agreed plan, meaningful verification, unresolved issues and any required human action. The root remains accountable for the result, including unfinished or unverified work; do not invent a subagent result, model choice or passing check.

If subagents, required isolation or model selection are unavailable or prohibited, explain the specific limitation and its impact. Do not bypass host rules, invent delegation, or silently substitute an inferior method. Continue independent authorized work where possible and involve the human in any decision needed to proceed.

**Done:** The agreed work has been organized into clear scopes, the root has coordinated and integrated the permitted work, and the human has a truthful account of outcomes and remaining gaps.
