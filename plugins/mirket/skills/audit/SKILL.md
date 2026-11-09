---
name: audit
description: "Use when asked to audit or review a code change, draft plan, or explicitly scoped module, system, or repository."
---

# Audit

## Purpose

Return prioritized, evidence-backed findings about the requested target. Audit is read-only unless fixes are authorized. [Test](../test/SKILL.md) owns behavioral checks; [Critique](../critique/SKILL.md) judges work against its brief, including visual quality. Reuse their evidence where relevant.

## Set scope and independence

Identify the target, purpose, governing requirements, project conventions and intended coverage. Read enough connected context to understand the behavior and its boundaries. Seek a reviewer independent of the work's author when risk, the task or an applicable gate warrants it, subject to host permissions. If unavailable, state the gap; never call a self-review independent.

## Code change

1. Pin the target. Record the base and head or the exact diff and snapshot; include staged, unstaged, and new files when in scope. Resolve refs and confirm the intended changes are present.
2. Find the governing intent in the request, issue, plan, or documented behavior, and find the relevant project standards. Review spec fit and standards as separate passes so neither obscures the other. When no written spec is available, state the limit and continue with evidenced behavior and standards; label open questions about intent.
3. Trace connected callers, contracts, failure paths, and checks to assess correctness and risk. Confirm each finding's triggering condition and practical consequence. Distinguish observed defects and supported risks from preferences or questions. Use existing evidence and focused non-destructive checks when useful. If delegation is unavailable or unnecessary, perform the passes inline; do not describe self-review as independent.
4. When corrections are authorized, follow the [review loop](../../references/review-loop.md), keep changes within scope and recheck material repairs.

## Existing module, system or repository

For an explicitly scoped audit, identify entry points, important flows, data and trust boundaries, dependencies and existing checks. Trace connected behavior and failure paths; inspect correctness, security, reliability, integration and other risks relevant to the target. Choose coverage based on the repository's size and structure: read the relevant repository in full when manageable; for a larger one, select a defensible scope using risk and connected behavior. State the areas examined and excluded, why they were selected, and any limits. Reading every file does not prove every execution path is safe.

## Draft plan

Review the fixed draft and criteria provided by the requester or [Plan](../plan/SKILL.md). Check outcome fit, evidence, assumptions, authorization and product decisions, dependencies, failure modes and verification. Identify missing decisions and unsupported claims. Return findings and open questions without editing the draft. Plan owns review coordination, repairs and the record of authorization.

## Completion

Report confirmed defects, supported but unverified risks, and concrete material improvements as distinct categories. Prioritize by impact and likelihood; give the location, triggering condition, evidence, consequence and useful next step. For an unverified risk, identify the missing evidence. Keep preferences and style suggestions out unless their impact is material. State the target or revision, coverage and exclusions, independence, and actual checks. If no material findings exist, say so without claiming complete safety. Stop after the report unless fixes were already authorized.
