---
name: plan
description: "Use when asked to plan work or develop an implementation plan, including changes to existing software, features, projects, or workflows."
---

# Plan

Produce an evidence-based plan for the outcome the human wants. Product decisions and business rules belong to the human; the plan is a proposal until the human explicitly agrees to it.

## 1. Establish the outcome and evidence

- Identify the desired outcome, scope, constraints, stakeholders and observable measures of success. Separate what the human has decided from questions and proposals. Do not fill gaps in requirements or business logic with assumptions. When an existing business rule might carry over, identify it as observed behavior and propose its preservation; do not present it as an agreed requirement until the human confirms it. For example, if a request changes the free-shipping threshold but says nothing about the fee for other orders, record the existing fee as evidence, ask whether to retain it, and mark the proposed fee and related acceptance checks pending in all three files.
- Inspect the relevant current implementation, connected behavior, tests, documentation and project conventions before proposing changes. Reuse established behavior and mechanisms where they fit. Cite the relevant paths or other evidence in the planning files; identify missing or inaccessible evidence.
- Compare the human's factual statements with the evidence. When they conflict, explain the discrepancy respectfully and ask how to proceed where it changes the decision. A deliberate hypothetical, simulation or explicit product decision may be planned as such, but must not be recorded as a verified fact about the current implementation.
- Ask focused questions for unresolved product choices, business rules, acceptance criteria or material scope. Offer evidence-based alternatives and a recommendation where useful. Continue independent investigation while an answer is pending; do not decide a business rule for the human or treat silence as agreement. Routine technical choices may be proposed with their reasoning, subject to project conventions and human direction.

## 2. Keep one plan folder per task

At the repository root, create or resume `.plans/<task-name>/` for this task, using a descriptive, unique name. Check existing folders and task identity before reusing one; never overwrite an unrelated plan. Keep these three files current throughout planning:

- **`Outcome.md`** — desired outcome, scope and constraints; observable acceptance criteria and how the eventual work will be checked; unresolved criteria marked pending. Describe expected behavior without asserting that unfinished work is complete.
- **`Agreement.md`** — decisions and the alternatives considered, including the human's choice, reason and relevant evidence when known. Attribute decisions accurately; distinguish proposed, pending, agreed and superseded choices. Record unanswered questions and retain prior decisions and alternatives when they change. Do not invent alternatives or agreement; say when no alternative has yet been identified.
- **`Plan.md`** — an explicitly marked draft or approved detailed outline, grounded in the inspected implementation and conventions. For each meaningful step record the intended action, affected area, dependencies and verification against `Outcome.md`. Identify unresolved decisions and limits instead of presenting guesses as settled requirements.

Create the files while investigating, update them as evidence and decisions emerge, and preserve them for the human's historical reference. If the repository root or write access is unavailable, explain the blocker and ask for a suitable repository or access; do not silently store the plan elsewhere or claim the required files exist.

## 3. Reach agreement and propose the plan

Before presenting the plan, check `Outcome.md`, `Agreement.md` and `Plan.md` for any proposed business rule or acceptance check presented as settled without human confirmation; mark each pending and ask the human to decide.

Present a concise brief of the intended execution actions, the outcome and checks, relevant evidence or constraints, and any unresolved product decisions. Link the three files. Ask the human to resolve material choices and approve the plan after they can review the concrete proposal. Iterate the files and brief as needed; record each decision and its alternatives in `Agreement.md`.

Mark `Plan.md` approved only after the human has explicitly approved the current plan and its material decisions are resolved. Record that approval in `Agreement.md`; do not infer it from silence, elapsed time, a draft, or the agent's own recommendation. Do not begin executing the proposed plan until it has been approved. If a material decision or scope changes after approval, update the affected files and seek renewed agreement before proceeding with that change. Approval of a plan does not itself authorize an external action beyond the user's instructions and host permissions.

**Done:** The human has a concise, reviewable proposal backed by current evidence, with the three required files and a truthful approval status. If information or approval is pending, identify it and leave the plan in draft.
