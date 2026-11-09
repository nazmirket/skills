---
name: plan
description: "Use for substantial work, an explicit request for a plan, or reporting or recording progress against authorized work."
---

# Plan

Produce an evidence-based plan for the outcome the human wants. Product decisions and business rules belong to the human. Use this skill when requested or when work involves consequential risk, unresolved decisions, or multiple dependent stages. File count alone does not make work substantial. Keep routine work direct.

For a status request on authorized work, go directly to [Track authorized work](#track-authorized-work).

## 1. Establish the outcome and evidence

- Identify the desired outcome, scope, constraints, stakeholders and observable measures of success. Separate decisions from proposals and open questions; do not invent requirements or business logic. Preserve established behavior outside the requested change using current evidence. Ask the human when a business rule is affected, genuinely uncertain, or requires a product decision. For example, an unchanged, evidenced delivery fee needs no separate confirmation when only the free-shipping threshold changes; if the fee itself is affected or unclear, surface the decision.
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

For a substantial plan, request a fresh read-only [Audit](../audit/SKILL.md) of the identified draft when the host permits delegation and it is authorized. Give the reviewer the goal, files, constraints and evidence; use [Orchestrate](../orchestrate/SKILL.md) when coordination is needed. Handle material findings with the [review loop](../../references/review-loop.md), and record the reviewer, findings, repairs and focused recheck in `Agreement.md`. If independent review is unavailable, record and disclose the gap; label any self-check accurately. Follow any stronger review gate required by the human or host.

Present a concise brief of the intended actions, outcome and checks, relevant evidence or constraints, and unresolved product decisions. Link the three files. Ask the human to resolve material choices; continue independent authorized work while an answer is pending. If the request is for a plan or approval is otherwise required, obtain approval before dependent execution.

Honor clear existing authorization to execute without asking for it again. Record what was authorized and by whom in `Agreement.md`; distinguish that authorization from explicit approval of a particular written plan. Mark `Plan.md` approved only when the human actually approves it; silence, elapsed time and the agent's recommendation are not approval. Before dependent work, resolve decisions that require the human and satisfy any stronger host or user gate. During execution, record routine technical adjustments within scope; return to the human for changes to the outcome, product decisions or authorized scope. Neither a plan nor its approval grants authority beyond the human's instructions and host permissions.

**Done:** The three files describe the outcome, decisions, evidence and steps, with truthful authorization and review status. Report unresolved decisions or verification gaps; leave a written plan in draft until explicitly approved.

## Track authorized work

1. Identify the matching authorized work and plan record. Read `Plan.md`, `Outcome.md` and `Agreement.md` to recover commitments and acceptance criteria. Check actual artifacts, checks or owner reports; distinguish direct, reported, stale and unavailable evidence. If no matching record establishes authorized work, report what you can verify and leave plan files untouched.
2. Give an as-of snapshot of completed and remaining work, milestone variance, blockers or dependencies, known owners and dates, and decisions needed. Link material evidence and mark unknowns. Surface proposed changes without treating them as approved commitments.
3. Return status questions read-only. When asked to save status, update only the `## Current status` section in the matching `Plan.md`, adding it if absent. Keep a single plan record and preserve its approval state. Assignments, external updates, and ongoing monitoring require their own authorization.

**Done:** Return the evidence-backed snapshot and link its location if saved.
