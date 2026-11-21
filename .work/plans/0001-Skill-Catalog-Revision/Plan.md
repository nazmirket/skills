# Plan: revise the Mirket skill catalog

**Approved for catalog authoring.** [Outcome](Outcome.md) · [Agreement](Agreement.md)

**Current target:** The user superseded the original expansion with an exact 19-skill catalog. Rename Discover → Preflight, Review → Audit, and Scope → Focus; move Triage into Author and Track into Plan; remove Build as a standalone skill. Verify the entrypoint set, display labels, routes, and provenance; preserve existing hook behavior and defer host evaluation. The original plan and initial implementation record below are retained as history.

Keep the current catalog recognizable. Add workflows where the task ends in a different kind of result, and move specialized guidance into references where it shares a trigger and output. The proposed ceiling is 24 canonical skills: 14 existing capabilities (two renames), eight recommended additions, and two conditional additions. Start with Test, Review, Triage and Build; settle their boundaries before expanding into the role workflows.

## Skills to author

| Skill | Trigger and output | Boundary and strongest influence |
| --- | --- | --- |
| **Build** | Implement a known, authorized outcome. Deliver the smallest working slice, then the complete change and evidence. | Reuse an approved Plan, bring material ambiguity back to Scope or Plan, call Test when useful. Use TDD’s vertical slices for behavior that merits them. Keep bug investigation with Debug. |
| **Test** | Select, write or run checks. Produce a risk-based test record with the evidence and gaps. | Cover manual, automated and integration checks as appropriate; use a small red/green slice when needed. Prefer public interfaces and independent expected results. Test checks behavior; Review evaluates a change; Critique judges quality against the brief. |
| **Review** | Review a code change by default, or an implementation plan when explicitly requested or delegated. Deliver prioritized, evidenced findings. | Adapt spec and standards as distinct lenses plus correctness and risk. Pin the target; include staged/unstaged work when in scope. Plan still owns plan readiness and human approval. A correction loop requires authorized edits and a stop condition. |
| **Triage** | Intake bug reports or a backlog. Deliver deduplicated, reproducible, prioritized issue drafts and next owners. | Adapt conversational QA and Break UI findings. Distinguish reported, reproduced and unknown. File or update externally only if explicitly authorized; route diagnosis to Debug. |
| **Author** | Create or revise a durable document for a named audience and purpose. Deliver the artifact, supporting sources and verification. | Choose the format by use; use relevant host tools for spreadsheets, decks or PDFs. For rendered formats inspect the result, not merely the source. Brief owns transfer notes; Distill governs communication style. |
| **Architect** | Evaluate a system boundary or propose a consequential technical design. Deliver options, tradeoffs, and a recommendation or ADR draft. | Adapt the architecture reference: hotspots, domain vocabulary, testable boundaries, deletion test, and before/after diagrams where useful. Cover failure modes, migration and rollback as appropriate; preserve ADRs and route chosen execution to Plan. |
| **Scope** | Define or prioritize a product opportunity. Deliver a product brief: user problem, goals/non-goals, options, success measures, and decisions needed. | Human owns priorities and business rules. Curate brings external evidence; use the prototype method to reduce uncertainty; Plan sequences agreed work. Keep product briefs distinct from the transfer skill Brief. |
| **Track** | Record a current snapshot of approved work across sessions or milestones. Deliver status, dependencies, risks, owners, next decisions and evidence. | Reuse Plan’s files and approved scope. Surface variance without changing commitments or inventing dates. No automatic external updates or ongoing monitoring. Orchestrate manages the agents doing the work; Track maintains the project record. |
| **Prototype** (conditional) | Resolve a concrete uncertainty cheaply. Deliver a disposable UI or logic experiment and what it showed. | Start with shared guidance under Design, Scope and Architect. Promote it if examples show repeated direct requests for an experiment outside those workflows. Label synthetic data, record stop/discard criteria, and isolate the full experiment from production. |
| **Optimize** (conditional) | Improve an agreed performance or resource metric. Deliver a measured before/after comparison with correctness guardrails. | Start with shared Build/Test guidance; promote it if direct requests need a standalone measured-improvement workflow. Profile a representative baseline, isolate material changes, compare variance and regressions, and revert if the agreed gain does not hold. |

## Revise all 14 authored skills

| Current skill | Recommendation |
| --- | --- |
| Adapt | Keep read-only orientation; produce a compact map of the relevant flow, conventions, and evidence gaps. Let Debug consume an observed problem and Architect consume the map when structural friction is the target. |
| Discover | Keep environment readiness. Clarify handoff of missing tools or blockers to Build, Test or Orchestrate, preserving the confirmation rule for unapproved changes and inferior fallbacks. |
| Plan | Preserve `.plans/<task>/`, its three files, and human approval. Use Scope or Architect when an unresolved decision needs its own deliverable. For substantial plans, the planner commissions a fresh read-only Review before asking for approval, records repairs, and reports the gate unmet if independence is unavailable. Give Track a place in the existing plan files. |
| Orchestrate | Keep the approved-plan gate for execution. Permit bounded read-only investigations and independent draft review before approval when delegation is authorized and available. Define dependencies, shared interface owner, transfer and integration evidence. Use sequential or inline work where splitting adds risk; an inline check cannot substitute for required independence. |
| Debug | Heavily adapt Systematic Debugging: trace the data to its first bad boundary, use falsifiable hypotheses and re-evaluate a failing strategy. Preserve Adapt’s evidence gate; use Test for regression and Critique or Review only where relevant. |
| Refactor | Restrict to behavior-preserving clarity and structure. Compare existing or characterization evidence, preserve public seams and errors, and route performance work to the measured-improvement method and architectural choices to Architect. |
| Cleanup → Clean | Keep evidence and ownership safeguards and the lifecycle intent. Update hook target, test expectations, docs and authoring metadata in the same migration. Preserve historical records and licenses. |
| Critique | Keep one qualitative artifact review with findings by condition, evidence, impact and next step. Add an opt-in UI stress reference (Break UI). Reuse relevant Test evidence instead of rerunning it: Test executes measurable checks, Review inspects changes for defects, and Critique judges the delivered result against its brief. Separate findings from authorized correction. |
| Distill | Keep as a communication overlay. Preserve uncertainty, citations and necessary decision detail. Keep hook language honest about activation and compliance; avoid attaching it to other skills as a repeated step. |
| Curate | Keep options and recommendations; add a question-led research branch for a sourced evidence note when there is nothing to rank. Borrow the primary-source habit without mandatory background delegation or a file for a trivial question. |
| Sleep | Keep explicit pause, saved handoff and exact resume prompt. Call Brief for content, keep `.plan/.handoff/` unless the human changes it, and check source/work state when resuming. |
| Imagine | Preserve approved brief before generation. Add a practical reference extraction and render-compare recipe; record visual evidence, inferred details and accessibility overrides. Use only the number of images needed. |
| Handoff → Brief | Make it a recipient-specific transfer: exact next action, authoritative artifact links, authorized scope, stale-context checks and suggested skills. Preserve explicit pause and resume behavior in Sleep; no automatic external sends. |
| Design | Keep one direction and implementation skill with optional routes. Capture a live baseline and protect content and working behavior on redesigns. Add supplied-reference fidelity, an optional identity-board reference and style examples. Use Imagine when generating the reference, the prototype method to resolve uncertainty, and Critique as the single owner of rendered QA. |

Do not merge whole skills or split Critique into specialist skills. Fold primary-source research into Curate, the correction loop into a shared review reference, and branding and visual stress into their owning skills. Split a workflow into a skill only if a direct request has its own outcome and stop condition.

## Coverage and boundaries

| Requested scope | Primary skills |
| --- | --- |
| Software Engineering | Build, Debug, Refactor, Review, Adapt, Discover, Clean |
| QA Engineering | Test, Triage, Critique, Review |
| Document Authoring | Author, Distill, Brief |
| Design | Design, Imagine, Critique; Design owns visual prototypes before any promotion |
| Product Management | Scope, Curate, Triage; Scope owns product-logic prototypes |
| Software Architecture | Architect, Adapt, Review, Refactor |
| Optimization | Build and Test use a shared measured-improvement method; Optimize may become a direct entry point |
| Project Management | Plan, Track, Sleep, Brief |
| Team Management | Orchestrate, Brief, Track |

Team Management here covers work allocation, coordination, review and escalation. It does not grant people-management or personnel decision authority.

| Representative request | First release route | Boundary |
| --- | --- | --- |
| “Implement the agreed export flow.” | Build owns the change; Test runs or adds the checks it needs. | “Why does export stall?” goes to Debug. “Review this export diff” goes to Review and does not authorize edits. |
| “Several users say export stalls.” | Triage records conditions, impact and unknowns and prepares issue drafts. | Triage neither diagnoses the cause nor posts to a tracker without authorization. |
| “Mock up three onboarding flows”; “model our refund decisions”; “prototype two cache invalidation strategies before choosing.” | Design owns the visual experiment, Scope the product-logic experiment, and Architect the technical experiment. Use the shared prototype method. | Production implementation is a separate decision. Approved business rules and technical decisions stay with their human owners. |
| “Make this report load within 300 ms.” | Build owns the change; Test measures before and after and checks correctness, using the same workload. | An unexplained slowdown starts in Debug; cleaner code with the same behavior belongs to Refactor. |
| “Is this screen usable with long localized names?” | Critique owns the quality review; Test can substantiate behavioral claims. | A request to compare visual alternatives starts in Design. A generated design reference starts in Imagine. |
| “Write a migration guide for support.” | Author delivers a usable document grounded in verified steps and the audience’s needs. | A prompt for the next worker goes to Brief; a shorter chat answer uses Distill. |
| “Which user problem should this product address first?” | Scope recommends a priority, outcome measure and decisions for the human. | “What do competing products offer?” uses Curate. An agreed product choice can move to Plan. |
| “Should we split this shared persistence layer?” | Architect traces actual change friction, compares options and drafts an ADR if useful. | No implementation on a recommendation request. Behavior-preserving local simplification belongs to Refactor. |
| “Where are we against the agreed milestones?” | Track records completed work, variance, blockers and decisions in the current plan record. | It does not rescope commitments, issue assignments or start ongoing monitoring. |

Before promoting Prototype or Optimize, collect representative direct prompts that fit the new contract and counterexamples that should stay with an existing owner. Record the observed gap and approval in Agreement. Static routing examples are enough to make that decision; live skill evaluations remain deferred.

## Execution after approval

1. **Define shared contracts.** Agree on naming and old-ID compatibility. Turn the routing examples into short guidance for the shared `plugins/mirket` catalog. Verify each example has one owner, a handoff where needed, and a stop condition. Preserve the `mirket` identity and the two marketplace manifests.
2. **Build the engineering and QA core.** Author Build, Test, Review and Triage together; revise Adapt, Discover, Debug, Refactor and Critique against those contracts. Include a read-only route, a scoped authorized correction route, and a no-delegation fallback. Check references and source notices.
3. **Add missing role workflows.** Author Scope, Architect, Author and Track; revise Curate and Plan. Reuse the plan files and existing conventions for evidence and status. Check that approved business rules remain human decisions and that proposed architecture changes cannot silently enter implementation.
4. **Add specialist methods and migrate names.** Revise Design and Imagine and add the prototype and optimization methods; promote them only if they meet the conditions above. Migrate Clean and Brief with their callers (including Orchestrate and Sleep), display metadata, README links, and invocation examples. Update the installed skill path in [the cleanup hook](../../../plugins/mirket/hooks/cleanup.py) and its synthetic assertions; retain `MIRKET_CLEANUP_DONE` as the hook’s acknowledgment protocol. Preserve historical handoffs and docs as records. Throughout authoring, map each adapted destination to its pinned source, license notice and changes. Ship required notices and self-contained guidance inside the plugin; the copied snapshots stay outside it.
5. **Validate and review.** During authoring check frontmatter, naming, uniqueness, source notices, and relative links confined to the shipped plugin; run the existing synthetic hook suite where affected. The Desktop checkout’s current hook test command is `python3 -B -m unittest discover -s tests`; inspect the actual checkout for any other required commands. After the full draft is ready and the user confirms behavioral evaluation may begin, use fresh Codex and Claude sessions to check discovery, invocation, routing, package-local references, unavailable capabilities, stale cached installations, and the chosen old-ID migration. Check hook behavior with and without trust where supported; plan for renewed Codex trust after hook changes. Report only checks actually run.

Representative acceptance cases: implement an approved small feature with one useful test; accept an intermittent bug report without filing or fixing it; review a change with no written spec; refine an existing UI without changing its working behavior; compare a prototype with production scope; test a performance claim under a comparable workload; resume a paused task with stale facts; and coordinate shared-file work without overlapping ownership.

## Initial implementation record

- Authoring and migration are complete in the Desktop checkout: 22 canonical skills, two renamed IDs, and shared Prototype and measured-improvement methods. Both marketplaces still target the shared plugin.
- A static check against an isolated package copy verified 22 skill and display records, 126 local links, 16 adaptation records, both marketplace targets, and all three hook events. The pinned source index and five shipped license notices were checked against the snapshots.
- The two cleanup-path assertions failed against the old path as expected. After migration, all 14 synthetic hook tests passed with `python3 -B -m unittest discover -s tests`. The tests do not exercise host activation.
- The independent implementation review found two material routing gaps, rechecked the repairs, and reported no remaining material findings. See [Agreement](Agreement.md).
- Fresh Codex and Claude installation, invocation, routing, cache and trust checks remain deferred until the human authorizes behavioral evaluation.

## Current status

- Consolidated the Desktop catalog to the requested 19 skills. Author owns issue triage and Plan owns approved-work tracking. The new IDs are Preflight, Audit and Focus. Build has no standalone entry.
- Verified the exact skill IDs and display labels in an isolated package copy, 116 local links, 16 attribution records, both marketplace targets, and both embedded workflows. All 14 existing synthetic hook tests passed. Host installation and behavioral evaluations remain deferred.
