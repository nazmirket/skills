---
name: plan
description: "Use when asked to plan work, develop an implementation plan, or report or record progress against an approved plan."
---

# Plan

Produce an evidence-based plan for the outcome the human wants. Product decisions and business rules belong to the human; the plan is a proposal until the human explicitly agrees to it.

For a status request on approved work, go directly to [Track approved work](#track-approved-work).

## 1. Establish the outcome and evidence

- Identify the desired outcome, scope, constraints, stakeholders and observable measures of success. Separate what the human has decided from questions and proposals. Do not fill gaps in requirements or business logic with assumptions. When an existing business rule might carry over, identify it as observed behavior and propose its preservation; do not present it as an agreed requirement until the human confirms it. For example, if a request changes the free-shipping threshold but says nothing about the fee for other orders, record the existing fee as evidence, ask whether to retain it, and mark the proposed fee and related acceptance checks pending in all three files.
- Inspect the relevant current implementation, connected behavior, tests, documentation and project conventions before proposing changes. Reuse established behavior and mechanisms where they fit. Cite the relevant paths or other evidence in the planning files; identify missing or inaccessible evidence.
- Compare the human's factual statements with the evidence. When they conflict, explain the discrepancy respectfully and ask how to proceed where it changes the decision. A deliberate hypothetical, simulation or explicit product decision may be planned as such, but must not be recorded as a verified fact about the current implementation.
- Ask focused questions for unresolved product choices, business rules, acceptance criteria or material scope. Offer evidence-based alternatives and a recommendation where useful. Continue independent investigation while an answer is pending; do not decide a business rule for the human or treat silence as agreement. Routine technical choices may be proposed with their reasoning, subject to project conventions and human direction.
- Use [Focus](../focus/SKILL.md) for an unresolved product choice or [Architect](../architect/SKILL.md) for a consequential technical design. Keep their evidence with the decision; sequence the chosen work here.

## 2. Keep one plan folder per task

At the project root, create or resume `.work/plans/<task-name>/` using the [workspace rules](../../references/workspace.md). Check existing folders and task identity before reusing one; preserve unrelated plans. Keep task-specific evidence alongside the plan and keep these three files current:

- **`Outcome.md`** — desired outcome, scope and constraints; observable acceptance criteria and how the eventual work will be checked; unresolved criteria marked pending. Describe expected behavior without asserting that unfinished work is complete.
- **`Agreement.md`** — decisions and the alternatives considered, including the human's choice, reason and relevant evidence when known. Attribute decisions accurately; distinguish proposed, pending, agreed and superseded choices. Record unanswered questions and retain prior decisions and alternatives when they change. Do not invent alternatives or agreement; say when no alternative has yet been identified.
- **`Plan.md`** — an explicitly marked draft or approved detailed outline, grounded in the inspected implementation and conventions. For each meaningful step record the intended action, affected area, dependencies and verification against `Outcome.md`. Identify unresolved decisions and limits instead of presenting guesses as settled requirements.

Create the files while investigating, update them as evidence and decisions emerge, and preserve them for the human's historical reference. If the repository root or write access is unavailable, explain the blocker and ask for a suitable repository or access; do not silently store the plan elsewhere or claim the required files exist.

## 3. Reach agreement and propose the plan

Before presenting the plan, check `Outcome.md`, `Agreement.md` and `Plan.md` for any proposed business rule or acceptance check presented as settled without human confirmation; mark each pending and ask the human to decide.

For a substantial plan, commission a fresh read-only [Audit](../audit/SKILL.md) of the identified draft before asking for approval. Dispatch only when delegation is authorized and the host allows it; use [Orchestrate](../orchestrate/SKILL.md) when coordination is needed. Give the reviewer the goal, files, constraints and evidence. Use the [shared review loop](../../references/review-loop.md) to handle material findings and record the reviewer, findings, repairs and focused recheck in `Agreement.md`. If independent review is unavailable, share an explicitly unreviewed draft for discussion, record the unmet gate and stop before readiness or execution. An inline check or ordinary approval cannot substitute for the missing review.

Present a concise brief of the intended execution actions, the outcome and checks, relevant evidence or constraints, and any unresolved product decisions. Link the three files. Ask the human to resolve material choices; request approval once required review and material repairs are complete. Iterate the files and brief as needed; record each decision and its alternatives in `Agreement.md`.

Mark `Plan.md` approved and begin execution only after the human explicitly approves the current plan, material decisions are resolved and required review is satisfied. Record approval in `Agreement.md`; silence, elapsed time and the agent's recommendation are not approval. If a material decision or scope changes, update the files and seek renewed agreement before acting on that change. Plan approval does not grant authority beyond the human's instructions and host permissions.

**Done:** The human has a concise, reviewable proposal backed by current evidence, with the three required files and a truthful approval status. If information or approval is pending, identify it and leave the plan in draft.

## Track approved work

1. Identify the matching approved plan. Read `Plan.md`, `Outcome.md` and `Agreement.md` to recover commitments and acceptance criteria. Check actual artifacts, checks or owner reports; distinguish direct, reported, stale and unavailable evidence. If no approved record matches, report what you can verify and leave plan files untouched.
2. Give an as-of snapshot of completed and remaining work, milestone variance, blockers or dependencies, known owners and dates, and decisions needed. Link material evidence and mark unknowns. Surface proposed changes without treating them as approved commitments.
3. Return status questions read-only. When asked to save status, update only the `## Current status` section in the approved `Plan.md`, adding it if absent. Keep a single plan record and preserve the approval state. Assignments, external updates, and ongoing monitoring require their own authorization.

**Done:** Return the evidence-backed snapshot and link its location if saved.
