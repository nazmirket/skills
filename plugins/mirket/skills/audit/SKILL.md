---
name: audit
description: "Use when asked to audit or review a code diff, branch, pull request, or work in progress for defects, or when explicitly asked to review a draft implementation plan."
---

# Audit

## Purpose

Return prioritized, evidence-backed findings about an identified change or draft. Audit is read-only by default.

## Code change

1. Pin the target. Record the base and head or the exact diff and snapshot; include staged, unstaged, and new files when in scope. Resolve refs and confirm the intended changes are present.
2. Find the governing intent in the request, issue, plan, or documented behavior, and find the relevant project standards. Review spec fit and standards as separate passes so neither obscures the other. When no written spec is available, state the limit and continue with evidenced behavior and standards; label open questions about intent.
3. Trace connected callers, contracts, failure paths, and checks to assess correctness and risk. Confirm each finding's triggering condition and practical consequence. Distinguish observed defects and supported risks from preferences or questions. Use existing evidence and focused non-destructive checks when useful. If delegation is unavailable or unnecessary, perform the passes inline; do not describe self-review as independent.
4. Follow the [review loop](../../references/review-loop.md) only when corrections are authorized. Keep fixes within scope and recheck material changes.

## Draft plan

Review the fixed draft and criteria provided by the requester or [Plan](../plan/SKILL.md). Check whether the steps achieve the intended outcome, respect constraints and dependencies, and address likely failures and verification. Return findings and open questions without editing the draft. Plan owns independent reviewer selection, repairs, readiness, and human approval.

## Completion

Report findings in priority order with location, condition, impact, and suggested remedy; keep intent and standards findings distinguishable. State the reviewed revision, coverage limits, and any checks run. If there are no material findings, say so. Stop after the findings for a read-only review, or at the authorized correction loop's stop condition.
