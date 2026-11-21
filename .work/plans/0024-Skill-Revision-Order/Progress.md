# Progress

Previously completed catalog revisions: Execute (committed as `af10e43`), Adapt, Focus removal, and the Design and Brief merges. The latter changes are present in the working tree; their earlier verification is recorded in the corresponding scope and agreement records.

## Plan revision

- [x] Confirm the approved survey scope and affected catalog references.
- [x] Convert this active plan in place and preserve its original agreement.
- [x] Implement the [Plan skill](../../../skills/plan/SKILL.md), workspace guidance, and relevant fixtures.
- [x] Verify package wiring and fixtures: 41 repository tests passed. The stale status fixture's focused check exposed the intended regression and left all fixture files unchanged.
- [x] Generate diagrams, build and check the website. Chrome confirmed that all five filenames render intact and the tracking link works at desktop and mobile widths. SEO checks passed.

Live agent behavior in Codex and Claude was not evaluated for Plan.

## Clean revision

- [x] Confirm the approved survey scope and locate active Stop references and commit guard coverage.
- [x] Update the Clean skill, remove the Stop review, and align docs and fixtures.
- [x] Verify with 40 repository tests. The two Stop regressions failed against the old code and passed after removal. Existing commit guard tests passed. In the stale-guide fixture, `make verify` passed, `make check` failed, and all files stayed unchanged.
- [x] Build the website and run SEO checks. Check both Clean sections and page width in Chrome at desktop and mobile sizes; no overflow observed.

Live agent behavior in Codex and Claude was not evaluated for Clean. Installed plugins were not changed.

## Curate removal

- [x] Remove Curate and its active references, align both plugin descriptions and site counts, and retain tool-fit decisions in Equip. Record Search as a future deep research skill.
- [x] Verify 40 repository tests, the website build and SEO, and the rendered desktop and mobile catalog. Equip loads and the Curate route is absent. Installed plugins were not changed.

## Equip revision

- [x] Confirm approved boundaries, existing examples, and the handoff to Preflight.
- [x] Revise Equip, align the examples and routing, and clarify Preflight’s handoff.
- [x] Verify 40 repository tests, the site build and SEO checks, and the Equip-to-Preflight link on desktop and mobile. Prepare the fit, pilot approval, and readiness fixtures. Live Codex and Claude behavior was not evaluated.

## Preflight revision

- [x] Confirm the approved scope, existing readiness checks, and Equip handoff.
- [x] Revise Preflight and align routing, the handoff, and fixtures.
- [x] Verify 40 repository tests, the website build and SEO, and desktop and mobile rendering for Preflight and Equip. Both fallback fixtures prepared successfully; the example keyboard order was exercised in Chrome. Live Codex and Claude agent behavior was not evaluated.

## Architect revision

- [x] Confirm the approved scope, existing ADR conventions, and handoff to Plan.
- [x] Revise Architect and align the handoff, routing, and fixtures.
- [x] Verify 40 repository tests, the site build and SEO checks, and the Architect-to-Plan handoff on desktop and mobile. Both Architect fixtures prepared successfully. Live Codex and Claude behavior was not evaluated.

## Debug revision

- [x] Confirm the approved scope, existing Debug guidance, and fixture boundaries.
- [x] Revise Debug and align routing and fixtures.
- [x] Verify 40 repository tests, the site build and SEO, and the Debug page on desktop and mobile. The direct-fix fixture failed before the correction and passed afterward; both fixtures prepared successfully. Live Codex and Claude behavior was not evaluated.

## Refactor revision

- [x] Confirm the approved scope, existing behavior guidance, and fixture coverage.
- [x] Revise Refactor and align routing and fixtures.
- [x] Verify 40 repository tests, the website build and SEO, and the Refactor page on desktop and mobile. Both fixtures exercised locally: the focused checks passed before and after the direct simplification, blank-input rejection survived the parser simplification, and the quoted-comma case passed only after the separate fix. Live Codex and Claude behavior was not evaluated.

## Test revision

- [x] Confirm the approved scope, current rules, and existing fixtures.
- [x] Revise Test and align routing and representative fixtures.
- [x] Verify 40 repository tests, the website build and SEO checks, and the rendered Test page at desktop and mobile widths. The verification-only fixture reproduced the expected failure without a source edit. The same quoted-comma check failed against the original parser and passed against the fix; the fixture export entry point produced the expected fields. Live Codex and Claude behavior was not evaluated.

## Audit revision

- [x] Confirm the approved scope and existing review and Plan boundaries.
- [x] Simplify Audit and align routing, Plan, and the independent review fixture.
- [x] Verify 40 repository tests, the website build and SEO checks, and the Plan link to Audit’s independence guidance on desktop and mobile. The read-only fixture reproduced the expected failure without changes; the high-risk fixture prepared as unverified. Live agent behavior and independent agent review were not evaluated.

## Design revision

- [x] Confirm the approved choices against the post-Imagine-merge guidance and fixtures.
- [x] Revise Design and align relevant references and fixtures.
- [x] Verify 40 repository tests; website diagrams, build, and SEO; and the rendered Design page at desktop and mobile widths. All three Design fixtures prepared and the reference SVG parsed. Live agent behavior was not evaluated.

## Author revision

- [x] Confirm the writing approval and keep issue triage in Author pending an agreed receiving owner.
- [x] Revise Author's writing guidance while preserving the current verification default and issue triage branch.
- [x] Pass 40 repository tests, the website diagrams, build and SEO checks, and the existing Author fixture's documented command. Inspect the Author page on desktop and mobile. Live agent behavior was not evaluated.

## Critique merge

- [x] Move visual review and the interface stress guide to Design, writing review to Author, and technical quality review to Audit. Preserve Design's separate review for substantial work and existing authorization and independence rules.
- [x] Remove the standalone skill and align both host manifests, catalog, active references, website, and behavior cases.
- [x] Pass 40 repository tests and the website diagrams, build, and SEO checks. Verify 20 skills and 22 indexable pages; check the catalog and owner pages at desktop and mobile widths and confirm the old Critique route is absent. Prepare both findings-only fixtures and verify their evidence. Live agent behavior was not evaluated.

## Secure merge

- [x] Move security and privacy review to Audit, design-time threat modeling to Architect, and authorized hardening to the implementer. Keep incident ownership with Operate and preserve existing approval and independence rules.
- [x] Remove the standalone skill and align shared instructions, both host manifests, the catalog, website, active references, and behavior cases.
- [x] Pass 40 repository tests and the website diagrams, build, and SEO checks. Verify 19 skills and 21 indexable pages; check the updated guidance on desktop and mobile, including the Architect link to Audit and the removed route. Prepare the Audit and Architect fixtures and check their evidence. Live agent behavior was not evaluated.

## Migrate revision

- [x] Keep consequential persistent-state transitions with Migrate and routine reversible changes with the task owner.
- [x] Require a preservation contract and proved recovery before target mutation. Reuse matching evidence; resume safely within existing authority and reconcile against agreed acceptance and retirement criteria.
- [x] Pass 40 repository tests and the website diagrams, build, and SEO checks. Inspect the Migrate page on desktop and mobile and confirm the Operate handoff. Prepare the local rehearsal and checkpoint fixtures, verify recovery source and checkpoint inputs, and confirm the unavailable consumer criterion stays open in the fixture. Live agent behavior was not evaluated.

## Release merge

- [x] Move candidate preparation, readiness, and authorized publication to the task owner. Keep Test and Audit as evidence providers and Deploy as the activation owner.
- [x] Remove the standalone entry and align the shared reference, instructions, routing, both host manifests, catalog, website, shipping example, and fixtures.
- [x] Pass 40 repository tests and the website diagrams, build, and SEO checks. Verify 18 shared skills and 20 indexable pages, inspect the updated site on desktop and mobile, and confirm the retired route is absent. Exercise the disposable prepare-only fixture by testing, assembling, and inspecting its local candidate. No publication or live host evaluation occurred.

## Operate merge into Deploy

- [x] Move health, observation, incidents, and recovery into a distinct Deploy branch. Preserve Debug and Migrate ownership and existing scope boundaries.
- [x] Remove the standalone skill and align the shared 17-skill catalog, routing, instructions, website, and incident fixture.
- [x] Pass 40 repository tests and the website diagrams, build, and SEO checks. Inspect Deploy on desktop and mobile and confirm the old Operate route is absent. Prepare both read-only Deploy fixtures; live host behavior was not evaluated.

## Deploy policy revision

- [x] Apply the approved policies to rollout and routing. Keep operations available without a rollout.
- [x] Add preparation-only production coverage for matching artifact evidence, missing target prerequisites and recovery compatibility, and distinct activation authority.
- [x] Pass 40 repository tests and website diagrams, build, and SEO checks. Inspect the Deploy page at desktop and mobile widths and confirm the operations entry point. Prepare the three Deploy fixtures; live host behavior and real rollout were not evaluated.

## Brief revision

- [x] Clarify the minimum handoff, traceable authority, evidence pointers, and material conflict rules. Keep progress tracking and worker coordination with their owners.
- [x] Preserve safe pause and resume, and align routing and the affected fixtures.
- [x] Pass 40 repository tests and website diagrams, build, and SEO checks. Inspect Brief at desktop and mobile widths. Prepare the three Brief fixtures and check their starting evidence and scope; live host behavior was not evaluated.

## Orchestrate merge into Plan

- [x] Move the approved worker coordination rules into Plan. Keep Brief responsible for handoffs and Audit responsible for independent review.
- [x] Remove standalone Orchestrate and align routing, host manifests, catalog, website, and the read-only coordination fixture.
- [x] Pass 40 repository tests and website diagrams, build, and SEO checks. Verify 16 shared skills and 18 indexable pages, inspect Plan and its catalog links on desktop and mobile, and confirm the old Orchestrate route is absent. Prepare the read-only fixture; no live delegation or host behavior was evaluated.

The coordinating agent maintains this checklist. Deferred work is outside the current authorization.
