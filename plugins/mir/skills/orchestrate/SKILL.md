---
name: orchestrate
description: "Use when coordinating subagents to execute an agreed plan across distinct domains or isolated work scopes."
---

# Orchestrate

Act as the manager of the plan's execution. The root agent is the sole orchestrator: it organizes the work, directs all subagents, communicates with the human, and owns the integrated outcome. Subagents perform assigned work and report to the root; they do not delegate or create their own subagents.

## Organize the work

1. Read the current plan, outcome, decisions and human instructions. Confirm that the plan applies to this task, that its material decisions are settled and that the human approved it. If an agreed plan is missing or a material decision remains unresolved, use [plan](../plan/SKILL.md) and resolve that gap before executing dependent work. Preserve existing approval and any explicit execution authorization.
2. Divide the plan into domains and bounded scopes with clear outcomes, responsibilities and dependencies. Identify what can run independently and what must happen in order. Assign exclusive ownership of writable files or areas, or use isolated workspaces when appropriate; coordinate shared boundaries through the root to avoid conflicting edits. Keep the split proportional to the work instead of creating subagents without useful scopes.
3. Check which subagent tools, concurrency limits, model choices and effort controls the host actually permits. Follow the human's explicit preferences and higher-priority host rules. For each scope, choose an available model and effort appropriate to its complexity, uncertainty and consequences when the host allows it. Use only supported settings; if the host controls model or effort, use its permitted default and state that you could not select it. Never claim a choice you could not make.

## Direct and coordinate

4. Give each subagent a self-contained work plan: objective, relevant context and plan path, owned scope and boundaries, prerequisites, expected deliverables, verification, and reporting instructions. State that the root handles delegation, cross-agent coordination and communication with the human. Require workers to surface questions, blockers and product decisions rather than deciding them on the human's behalf.
5. Dispatch independent scopes when their prerequisites are met. Manage dependencies, monitor meaningful progress and adapt assignments as evidence or priorities change. Negotiate conflicts between scopes, resolve routine technical decisions within the agreed plan, and bring unresolved product choices or material changes to the human. Preserve the human's agreed decisions; do not treat a subagent's recommendation as approval.
6. Inform the human briefly as meaningful subagent outcomes, blockers or decisions arrive. Summarize what changed and its effect on the plan; avoid reporting unchanged status. The root is the messenger: subagents report to the root, and external messages require the human's authorization.

## Integrate and deliver

7. Inspect the actual work and evidence from every subagent instead of relying on completion claims. Coordinate integration, resolve ownership conflicts and use [critique](../critique/SKILL.md) for the applicable quality checks and focused checks for the combined outcome. Keep the plan's records current and preserve user changes. If a result fails verification, return a bounded correction to its owner or handle the integration within the root's authorized scope.
8. Report the outcome against the agreed plan, meaningful verification, unresolved issues and any required human action. The root remains accountable for the result, including unfinished or unverified work; do not invent a subagent result, model choice or passing check.

If subagents, required isolation or model selection are unavailable or prohibited, explain the specific limitation and its impact. Do not bypass host rules, invent delegation, or silently substitute an inferior method. Continue independent authorized work where possible and involve the human in any decision needed to proceed.

**Done:** The agreed work has been organized into clear scopes, the root has coordinated and integrated the permitted work, and the human has a truthful account of outcomes and remaining gaps.
