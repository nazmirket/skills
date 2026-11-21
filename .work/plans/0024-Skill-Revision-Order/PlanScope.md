# Plan: scope for revision 4

**Status:** Approved and implemented in the [Plan skill](../../../skills/plan/SKILL.md). See [Progress](Progress.md) for verification.

Use Plan when material risk or coordination warrants planning, or when the human asks for a plan. A small change can warrant planning; file count alone does not. Keep a short plan in chat when it can be used there. Use a durable record when the plan needs to outlive the conversation. Save it under `.work/plans/` by default; use a shared project location only when the human asks or the project explicitly requires it.

| File | Responsibility |
| --- | --- |
| `Evidences.md` | Relevant project state before execution. Capture what the plan relies on and link the evidence. If the baseline will be hard to reconstruct, include enough detail to reproduce it, such as the revision, environment, commands, and results. |
| `Scope.md` | State what's authorized, what needs a separate decision, and which instruction establishes that boundary. Use plain language. |
| `Outcome.md` | Specify the desired result and how to tell it was reached. Separate confirmed specifications from pending decisions. Plan the work that can proceed either way; wait on dependent work. |
| `Plan.md` | Sequence the work and its checks. Use short steps for solo work. For shared interfaces or handoffs, name ownership, dependencies, deliverables, and checks. For migrations or rollouts, include integration, cutover, stop conditions, and recovery as applicable. |
| `Progress.md` | Maintain a live checklist through execution. Track implementation and required verification separately. Note meaningful changes, blockers, and evidence; for work spanning agents or sessions, also record active owners, dependencies, and handoff changes. One coordinating agent writes the checklist; workers report results, evidence, and blockers. |

## Execution and review

- A plan-only request ends with the plan. Inspect existing evidence and use read-only checks; do not implement or build or run a rehearsal.
- For substantial plans, seek fresh independent review when feasible and authorized. Disclose if unavailable; proceed within existing authority unless review is required. Approval to execute is distinct from approval of the written plan.
- Mark readiness by step. An already authorized step can start while another waits if it does not depend on the unresolved decision. Routine adjustments can proceed within the agreed outcome, scope, and checks. Pause affected work when a proposed change crosses that boundary; continue independent work.
- Keep the plan open while a required verification is blocked. It closes once the check passes or the human explicitly accepts the gap. Mark an accepted gap as such, not as a pass.

## Status and older records

- For a status request, verify stale claims that could change the next step. Rerun a safe, focused check if it would settle the question. Report which claims were verified; leave `Progress.md` unchanged unless the human asks to save the update. During authorized execution, keep the checklist current.
- When resuming an active older plan, convert it in the same folder to the five-file structure. Preserve the original agreement as history. Label reconstructed evidence and distinguish it from evidence captured before execution. Seed progress from verified work and leave completed plans alone.
