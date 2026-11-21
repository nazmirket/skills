# Evidences

## Before the Plan revision

- The working tree is based on local commit `af10e43`. It contains the pending Adapt revision, Focus removal, and Design and Brief merges. The catalog has 22 skills.
- The [approved Plan scope](PlanScope.md) is based on the 16 survey answers. Before this revision, the packaged Plan used three files for substantial work or one file for a small saved plan; status was saved in Plan.md. The Workspace guide and the status fixture still reflected that contract.

## Reconstructed baseline for the catalog revision

This folder predates the five-file format. The original [Agreement](Agreement.md) and [Outcome](Outcome.md) preserve the earlier planning record. The original sequence covered 25 skills; the current count reflects authorized removals and merges. Earlier evidence is preserved in the [Execute](ExecuteScope.md) and [Adapt](AdaptScope.md) scope records and commit `af10e43`. This is a reconstruction from the records and current Git state, not a fresh baseline captured before the earlier work.

## Before the Clean revision

- The working tree still contains the earlier uncommitted catalog revisions and has no staged changes. Clean and the hook files match `af10e43`.
- The shared hook config registers SessionStart, UserPromptSubmit, Stop, and PreToolUse. Stop requests one continuation when opted in; UserPromptSubmit already reminds the agent to apply Clean. The commit guard separately handles Bash PreToolUse events and checks the target index.

## Before the Equip revision

- The catalog has 21 skills and an empty Git index. Equip already has a pending edit from Curate's removal. Its trigger includes representations, abstractions, and workflows; its last step owns tool acquisition and setup. Preflight already inspects readiness and requires authority for setup.
- The existing Equip fixture covers a format that cannot meet fidelity requirements. It does not cover whether a pilot can start without authorization.

## Before the Preflight revision

- Preflight already requires installation authority and accepts an Equip handoff. Its instructions do not explicitly default to reactive checks, define equivalent environments, or separate basic readiness from acceptance evidence.
- The existing fixture covers a weaker fallback: source or screenshot review cannot prove keyboard behavior. There is no corresponding fixture for an equivalent fallback.

## Before the Architect revision

- Architect records every settled architectural decision, without defining the threshold as a lasting boundary. It mentions evidence for reopening but does not distinguish review from reopening or require enough setup and results to reproduce the checks from the ADR.
- The existing smoke case covers an unresolved storage choice. The shared catalog and compatibility ADRs illustrate lasting boundaries; neither decision is reopened by this revision.

## Before the Debug revision

- The packaged Debug skill requires an orientation finding and specialist selection up front. It says to revisit assumptions after repeated attempts but has no explicit stop after two failed hypotheses.
- The existing `debug-authorized-fix` fixture has a focused test for a dropped item. Its criteria expect Adapt and Test even though the test and code establish the cause directly.

## Before the Refactor revision

- The packaged skill already calls for preserving observable behavior and reusing focused checks. It does not explain when incidental simplification should stay with the current task, how to handle plausible reliance, or how to separate evidence for a bounded defect fix.
- The `refactor-preserve-behavior` fixture covers ordinary simplification with sufficient existing checks. It does not cover an untested rejection or a proven contract violation.

## Before the Test revision

- Test already chooses checks by risk and separates verification from repair, but does not explicitly pair a focused check with a user-facing smoke check or give a rule for matching CI evidence and mixed retry results.
- The verification-only fixture has a passing baseline. No Test fixture pairs a new regression test against old and fixed code with an actual export workflow check.

## Before the Audit revision

- Audit already separates defects, risks, and material improvements. It has separate workflows by target, requires two passes for code, and advises seeking independence when warranted without defining a high-risk gate. Plan already distinguishes self-checks from independent review.

## Before the Design revision

- The working tree already included the Imagine merge. Design required a live redesign baseline and an explicitly agreed concept brief. Reference guidance defaulted to matching the supplied view, and delivery and several specialist references sent work to Critique without a substantial-work threshold.
- The supplied-reference fixture assumed literal fidelity. The concept fixture already covered missing generation authority, and no fixture covered the missing live redesign baseline.

## Before the Author revision

- Author already inferred routine writing details, used risk-based verification, and owned issue triage through a separate reference. It did not explicitly set a project voice default or define how broadly it could revise structure and tone.
- The existing Author document fixture asks for a local Quickstart supported by a runnable command documented in its README.

## Before the Critique merge

- Critique was the owner of visual review, writing quality judgments, and selected technical quality checks. Design already required the Critique pass for substantial visual work after a first inspection. Test already owned measurements, and Audit already owned material technical findings and independent review gates.
- The read-only `critique-report` fixture assessed a written draft; realistic interface stress guidance lived under Critique.

## Before the Secure merge

- Secure owned assessment, threat modeling, and authorized hardening. Audit already owned findings and independent review gates, Architect owned lasting design decisions, and Operate owned containment and recovery.
- The original security fixture exercised findings-only review. No fixture distinguished design-time threat modeling from a separate security review.

## Before the Migrate revision

- Migrate already defined invariants, rehearsed transitions, and accounted for partial failure. It did not distinguish routine reversible changes at routing, expressly allow matching rehearsal evidence, or set verified checkpoint resumption as the default when safe and authorized.
- The existing migration fixture rehearsed locally with an intact rollback source. There was no case for resuming an authorized partial transition while leaving consumer acceptance open.

## Before the Release merge

- Release owned the exact candidate, readiness, and authorized publication. Deploy already owned environment activation, and Test and Audit supplied verification and review.
- The prepare-only fixture already excluded publication and deployment. The active instructions, catalog, and shipping example still named Release as a standalone owner.

## Before the Operate merge

- Deploy owned target readiness, rollout, and rollout recovery. Operate owned service and workflow health, ongoing observation, incident containment, and backup recovery. Both used consumer-path checks and called for reconciling ambiguous operation state before retrying.
- The Deploy survey kept the activation owner and left its operational handoff timing unanswered. The later instruction placed both branches under Deploy.

## Before the Deploy policy revision

- Deploy already checked the served environment and had stop and recovery guidance. The survey made exact production authority, evidence reuse, compatibility before activation, and retry and acceptance conditions explicit.
- The existing readiness fixture was staging-only; the incident fixture deliberately lacked mitigation authority.

## Before the Brief revision

- Brief already owned handoffs and the merged Sleep branch. The revision clarifies that authority has a source and accessible evidence should travel as links or exact locations.
- Existing fixtures distinguished routine staleness, a material authority conflict, and an explicit pause. The routine fixture had no separate authority or evidence record for the recipient to reference.

## Before the Orchestrate merge

- Plan sequenced work and tracked progress. Orchestrate assigned workers and owned integration; Brief defined what each assignment carried. The existing read-only coordination fixture excluded implementation and nested delegation.
