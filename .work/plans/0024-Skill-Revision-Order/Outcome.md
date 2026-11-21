# Outcome: make the Mirket skills reflect how Nazmi works

Create a revision order for the 25 current skills in the root catalog. The revision should make each skill recognizable through the decisions it makes, the work it does, and where it stops. Start from real work and the user's own words; a change in tone alone is insufficient.

The requested deliverable now is the order and method. The eventual result is a catalog in which each retained skill has a distinct outcome, a clear boundary, and guidance that changes behavior in a representative situation. Preserve current skill IDs and host wiring by default; a proposed merge, split or rename needs a distinct reason and a user decision.

For each eventual revision, capture the source example, the principle in the user's words or a clearly attributed paraphrase, and whether it is a default, a hard rule, or an exception. Define what the agent does, when it asks, what evidence it needs, and when it stops. Check one real positive case and one nearby case that should route elsewhere or stop. Reuse existing cases when they fit. Document an unchanged skill as reviewed if its existing guidance already matches.

Success for the original planning turn: all 25 entries occur exactly once, the order follows dependencies, each entry has a specific question or case, and documented preferences are clearly distinguished from open decisions. No skill edits, packaging changes, host changes, or release were in scope for that turn.

## Approved Plan revision

The packaged Plan skill follows the [surveyed specifications](PlanScope.md): keep short plans in chat, use the five-file record for durable work, track readiness and verification by step, and keep status requests read-only unless asked to save. The workspace reference and status fixture reflect the new format. Convert this active record in place and preserve the original agreement. Check repository wiring and the exported Plan page.

## Approved Clean revision

The [surveyed specifications](CleanScope.md) distinguish task-scoped delivery from the wider commit check, protect existing work and limit deletions, and keep verification evidence proportionate. The shared package no longer registers a Stop review. Commit guard behavior is preserved. Check the repository suite, the representative commit scenario, and the exported Clean page.

## Approved Equip revision

The packaged [Equip revision](EquipScope.md) focuses on tool and format fit, prefers the established stack, proposes pilots before running them without prior authority, and hands chosen tools to Preflight for authorized setup and readiness. Verify the routing and example boundaries, package checks, and rendered Equip and Preflight pages.

## Approved Preflight revision

The packaged [Preflight revision](PreflightScope.md) checks readiness on request or evidence of a blocker. It preserves independent work, distinguishes equivalent from weaker fallbacks, and verifies setup without taking over acceptance checks. Verify package wiring, the readiness fixtures, and the rendered Preflight page.

## Approved Architect revision

The packaged [Architect revision](ArchitectScope.md) distinguishes lasting boundary changes from local edits, preserves accepted decisions pending contrary evidence, and hands self-contained ADRs to Plan. Verify the settled and unresolved decision fixtures, package checks, and rendered Architect guidance.

## Approved Debug revision

The packaged [Debug revision](DebugScope.md) allows direct fixes when the cause is clear, pauses unclear investigations after two failed hypotheses, and reports exactly what verification remains. Verify the direct-fix and stop-boundary fixtures, package checks, and rendered Debug guidance.

## Approved Refactor revision

The packaged [Refactor revision](RefactorScope.md) distinguishes structural work from incidental cleanup, preserves behavior with focused before-and-after checks, and handles an established in-scope defect as a separately verified correction. Check the repository suite, representative fixtures, and the rendered Refactor page.

## Approved Test revision

The packaged [Test revision](TestScope.md) fills verification gaps, proves regressions with focused and workflow evidence, and reports mixed, blocked, and performance results at the strength the evidence supports. Verify package checks, the verification-only and export fixtures, and the rendered Test page.

## Approved Audit revision

The packaged [Audit revision](AuditScope.md) uses one workflow, separates the three categories of findings, and requires an independent reviewer for high-risk changes or an explicit gate. Verify package wiring, review fixture preparation, and the rendered Audit and Plan guidance.

## Approved Design revision

The packaged [Design revision](DesignScope.md) defines who decides the direction, requires a live redesign baseline, defaults to reference intent, preserves explicit concept brief agreement, and routes substantial work to Critique after first inspection. Verify package and website checks, representative fixtures, and desktop and mobile Design documentation.

## Approved Author revision

The packaged [Author revision](AuthorScope.md) defines the boundary for substantive writing, defaults to project voice, allows structural revision within scope, and asks writers to verify or qualify material claims. Keep risk-based checks and the existing issue triage branch. Verify the repository and website checks, the Author fixture's documented command, and the rendered Author page.

## Approved Critique merge

The [Critique merge](CritiqueScope.md) leaves one 20-skill catalog for both hosts. Design keeps a separate visual review for substantial work, Author absorbs writing review, and Audit absorbs technical quality findings while reusing Test evidence. Review-only work ends with findings; existing approval and independence rules stand. Verify package wiring, rendered documentation, the removed route, and representative findings-only fixtures.

## Approved Secure merge

The [Secure merge](SecureScope.md) leaves one 19-skill catalog for both hosts. Audit owns security and privacy findings, Architect models threats during design, and the implementer owns authorized hardening. Operate retains incident response. Verify package wiring, rendered guidance, the removed route, and the reassigned review and design fixtures.

## Approved Migrate revision

The [Migrate revision](MigrateScope.md) keeps substantive persistent-state transitions with Migrate. It requires an explicit preservation contract and proved recovery before mutation, favors the simplest authorized cutover, reuses matching rehearsal evidence, and closes against agreed acceptance and retirement criteria. Verify routing, the recovery and checkpoint fixtures, and the rendered Migrate guidance.

## Approved Release merge

The [Release merge](ReleaseScope.md) leaves 18 shared skills. The task owner prepares and publishes the exact artifact with Test and Audit support. Deploy owns activation and preparation alone does not authorize publication. Verify package wiring, the prepare-only fixture, the shipping example, and the removed standalone route.

## Authorized Operate merge

Deploy contains a distinct [operations branch](../../../skills/deploy/SKILL.md#operate-and-recover) for service health, incidents, observation, and verified recovery, including without a rollout. Both hosts share 17 skills.

## Approved Deploy revision

The [Deploy revision](DeployScope.md) separates production activation authority from readiness, reuses matching evidence, requires compatible rollout and recovery when state changes, and verifies the target against agreed criteria. The operations branch remains available for work without a rollout.

## Approved Brief revision

The [Brief revision](BriefScope.md) keeps continuity with Brief and progress and assignments with their existing owners. Handoffs give the exact next action, source of authority, accessible evidence pointers, and what to recheck. Preserve safe pause and resume and stop only the work affected by a material conflict.

## Approved Orchestrate merge

The [Orchestrate merge](OrchestrateScope.md) leaves 16 shared skills. Plan coordinates authorized workers directly, isolates writes, and owns integration; Brief owns handoffs and Audit owns review independence. Read-only coordination does not create an execution plan or authorize changes.
