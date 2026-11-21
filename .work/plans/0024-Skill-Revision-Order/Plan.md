# Draft: Mirket skill revision order

[Evidences](Evidences.md) · [Scope](Scope.md) · [Outcome](Outcome.md) · [Progress](Progress.md) · [Original agreement](Agreement.md)

The phases set the order for revising the catalog. They do not prescribe the order in which an agent must invoke skills. Within each phase, start with the first skill and use its neighboring entries to resolve boundaries before editing one at a time.

## 1. Set the working contract

These skills determine how the rest of the catalog behaves in ordinary work: what the agent communicates, what context it needs, who decides, and when a task is ready to deliver.

| Order | Skill | Principle and case to settle |
| --- | --- | --- |
| 1 | [Execute](ExecuteScope.md) | Implemented: take the simplest complete path, verify what matters, and speak only when it helps. |
| 2 | [Adapt](AdaptScope.md) | Implemented: discover and refresh project facts in the agreed source order, ask about material contract conflicts, and hand findings to the skill that will act on them. |
| 3 | Focus | Dropped at the user's direction. Product decisions stay with the human; Plan handles open rules when they affect implementation. |
| 4 | [Plan](PlanScope.md) | Implemented: plan for risk, coordination, or explicit request; save durable work in five files; track readiness and verification by step. |
| 5 | [Clean](CleanScope.md) | Implemented: keep delivery focused, review nearby guidance before commits, protect existing work, and remove the opt-in extra pass. |

## 2. Choose the tools and technical direction

Clarify the handoffs among researching options, deciding whether to switch tools, verifying readiness, and changing the system itself.

| Order | Skill | Principle and case to settle |
| --- | --- | --- |
| 6 | Curate | Dropped at the user's direction. Search will be considered separately for deep research. Equip still owns tool fit and adoption recommendations. |
| 7 | [Equip](EquipScope.md) | Implemented: focus on tools and formats, prefer the established stack, propose pilots before running them, and hand the chosen tool to Preflight. |
| 8 | [Preflight](PreflightScope.md) | Implemented: check readiness when needed, keep independent work moving, and verify setup without taking over acceptance checks. |
| 9 | [Architect](ArchitectScope.md) | Implemented: record lasting boundary changes in self-contained ADRs, reopen decisions with evidence, and hand the ADR to Plan. |

## 3. Make changes and prove the result

Separate causal investigation, structural changes, behavioral checks, and independent judgment. Start from an actual bug or refactor and reuse its evidence across the four skills.

| Order | Skill | Principle and case to settle |
| --- | --- | --- |
| 10 | [Debug](DebugScope.md) | Implemented: fix directly when the evidence is clear, trace unclear causes, and pause after two failed hypotheses. |
| 11 | [Refactor](RefactorScope.md) | Implemented: use for distinct structural work, clarify plausible reliance, and verify preserved behavior separately from bounded fixes. |
| 12 | [Test](TestScope.md) | Implemented: fill evidence gaps, prove regressions at the right layers, reuse matching CI, and report failures and blocked checks precisely. |
| 13 | [Audit](AuditScope.md) | Implemented: one read-only workflow, distinct categories for material findings, and mandatory independence for high-risk work or explicit gates. |

## 4. Design, generate, write, and assess

Set the brief and ownership first so a judgment about quality can refer back to the user's actual intent.

| Order | Skill | Principle and case to settle |
| --- | --- | --- |
| 14 | [Design](DesignScope.md) | Implemented: agree on art direction boundaries, preserve the live baseline, follow reference intent, and use a distinct visual review for substantial work. |
| 15 | Imagine | Merged into Design's concept generation branch; the Design revision covered its brief and implementation rules. |
| 16 | [Author](AuthorScope.md) | Implemented writing guidance. Issue intake and drafting remain in Author pending an agreed receiving owner. |
| 17 | [Critique](CritiqueScope.md) | Merged into Design, Author, and Audit. Substantial visual work still gets a distinct review. |

## 5. Ship and operate

Set what must survive before shaping the release and rollout. These are distinct outcomes; a task may need any subset.

| Order | Skill | Principle and case to settle |
| --- | --- | --- |
| 18 | [Secure](SecureScope.md) | Merged: Audit owns security and privacy review, Architect owns design-time threat modeling, and the implementer owns authorized hardening. |
| 19 | [Migrate](MigrateScope.md) | Implemented: agree what state must preserve, choose the simplest authorized cutover, prove recovery, and reconcile against agreed criteria. |
| 20 | [Release](ReleaseScope.md) | Merged: the task owner prepares and publishes with Test and Audit support; Deploy retains activation. |
| 21 | [Deploy](DeployScope.md) | Implemented: establish target readiness, authorize production separately, resolve uncertain operations before retrying, and verify against agreed criteria. |
| 22 | Operate | Merged into Deploy’s operations branch; no standalone skill. |

## 6. Transfer work and resume it

Revise these last because they pass on the ownership, authority, and evidence defined above. Define the transfer before defining coordination or pause.

| Order | Skill | Principle and case to settle |
| --- | --- | --- |
| 23 | [Brief](BriefScope.md) | Implemented: give the next action, traceable authority, and evidence pointers; preserve safe pause and resume. |
| 24 | [Orchestrate](OrchestrateScope.md) | Merged into Plan: flat delegation, exclusive write scopes, and lead-owned integration. |
| 25 | Sleep | Merged into Brief's pause and resume branch; reviewed with Brief. |

## Work through one skill at a time

1. **Start with a real case.** Reuse a project record or prior decision. Show what the current skill would tell the agent to do and where that differs from what you wanted. Ask only for the missing judgment. One question at a time is the default; skip a question when the evidence already answers it.
2. **Write the rule so it changes behavior.** Record the user's words or attributed paraphrase, what is a default or hard boundary, and any exception. Translate that into a trigger, first action, evidence requirement, handoff, and stopping point. Keep specialist examples in references when they would clutter the entry point.
3. **Compare before and after.** Show the smallest proposed change to the skill and walk the case through it. Try one nearby counterexample to check overreach or overlap. If the current skill already behaves correctly, keep it and record why.
4. **Check and carry forward.** When a revision is authorized, update only the affected guidance, metadata, routing or fixtures. Check links, catalog wiring and changed hook contracts as applicable. Keep walkthroughs distinct from live host evaluations; use the [existing smoke guide](../../../tests/HostSmoke.md) when the behavioral evaluation scope is agreed. Record the settled rule once and reuse it in later skills.

**Current status:** The root catalog and Execute are committed locally in `af10e43`; the remaining approved revisions, removals, and merges are committed in `cd5476b`. The catalog has 16 skills. This revision sequence is complete; Search and the Author issue triage handoff are deferred.
