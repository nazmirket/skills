---
name: orchestrate
description: "Use when deciding whether to delegate or coordinating subagents for implementation, investigation, or independent review."
---

# Orchestrate

The root agent is the sole orchestrator: it organizes and assigns work, manages subagents, communicates with the human, and owns the integrated outcome. Workers implement and correct their assigned work. Subagents report to the root and do not create or manage subagents.

## Organize the work

1. Delegate when it adds value: for example, independent work can progress concurrently, a specialist perspective matters, or a separate reviewer is needed. Consider coordination cost, dependencies and risk. Work inline when a split adds no value. Follow the human's explicit delegation instructions and host rules.
2. For substantial implementation, use [Plan](../plan/SKILL.md), resolve material decisions, and confirm execution is authorized before delegation. Honor clear existing authorization without calling an unapproved written plan approved. A small, clearly scoped task can be delegated directly when authorized. Bounded read-only investigation or independent draft review can precede plan approval; give the reviewer a fixed target and read-only scope.
3. Divide delegated work into bounded scopes with outcomes, dependencies and one owner for each shared interface. Separate confidently rule-driven work from creative or judgment-heavy work where that makes assignments clearer. Give workers exclusive writable areas or isolated workspaces and distinct scratch destinations under the [workspace rules](../../references/Workspace.md). Run dependent or shared-state work sequentially.
4. Check available subagent tools, concurrency, models and effort controls. For confidently simple, deterministic work, prefer a capable lower-cost, faster model; choose a strong model for creative work, including design. Be generous with reasoning effort and avoid an inadequately capable baseline. Consider ambiguity, complexity and consequences as well as determinism: a precise task can still be high-risk. Increase capability or review when evidence warrants it. Use only host-supported settings; if selection is unavailable, use the permitted default and say so.

## Direct and coordinate

5. Use [Brief](../brief/SKILL.md) for each self-contained assignment: objective, relevant context and plan path when applicable, owned scope, prerequisites, deliverable, checks and reporting. Workers surface blockers and product decisions.
6. Dispatch independent scopes when prerequisites are met. Manage dependencies and adapt assignments as evidence changes. Workers report routine handoff corrections and continue. For a discrepancy that changes the target, authority, ownership, interface, or acceptance criteria, pause the affected work, review the evidence and give direction before it resumes. Update affected workers promptly. Resolve ownership conflicts and routine technical decisions within the authorized scope; bring product choices or material changes to the human.
7. Inform the human briefly as meaningful outcomes, blockers or decisions arrive. Avoid reporting unchanged status. The root is the messenger; external messages require the human's authorization.

## Integrate and deliver

8. Inspect each worker's actual work and evidence proportionately to risk. Give corrections within a worker's scope back to that worker or reassign them. Assign an integration owner; the root may make a bounded integration correction directly once affected workers have handed back ownership. Recheck the affected result with [Test](../test/SKILL.md), [Audit](../audit/SKILL.md) or [Critique](../critique/SKILL.md) as needed. If independent review is required, send any root-authored correction to an independent reviewer. Preserve user changes and use [Plan’s tracking branch](../plan/SKILL.md#track-authorized-work) when a saved status is requested.
9. Report the outcome, verification, unresolved issues and any required human action. The root remains accountable for the result. A root review is not independent of work the root authored; record any required independent review that was unavailable.

If delegation is unavailable or prohibited, say so and continue authorized work inline where possible. Do not claim an inline review is independent. If required independence or isolation is unavailable, report the unmet gate; follow [Plan](../plan/SKILL.md) where its readiness requirements apply. Never invent an unavailable capability or model selection.

**Done:** The agreed work has been organized into clear scopes, the root has coordinated and integrated the permitted work, and the human has a truthful account of outcomes and remaining gaps.
