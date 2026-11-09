---
name: critique
description: "Use when judging a delivered design or artifact against its brief, including rendered quality, integration fit, simplicity, or what existing performance evidence establishes."
---

# Critique

Judge the delivered result against the brief and the project context. Own the quality assessment; [Test](../test/SKILL.md) owns measurable checks, and [Audit](../audit/SKILL.md) owns defect findings on a diff or draft plan.

## Establish the scope

1. Identify the change, intended behavior or appearance, relevant project conventions and agreed acceptance criteria. Inspect the connected context and distinguish evidence from assumptions. Surface material uncertainty instead of inventing requirements or a new design direction.
2. Select relevant lenses and inspect the actual result. Reuse current Test evidence; request only missing checks that could change the verdict. Put saved screenshots and other temporary evidence in `.work/temp/<task>/` under the [workspace rules](../../references/workspace.md). A finding records the condition or location, evidence, impact and next step. Identify inferred, observed and unavailable evidence explicitly.

## Choose relevant checks

### Visual

For a design, interface or visual change, compare the actual rendering with the brief, supplied reference and project conventions. Inspect relevant sizes, themes and interaction states, including hierarchy, layout, type, imagery and interaction clarity. View the rendering yourself; a screenshot capture or source alone is insufficient. Use [stress the interface](references/ui-stress.md) for realistic adverse data and states. Report a missing render or state as unverified; a screenshot cannot establish interaction behavior or accessibility by itself.

### Integration

Judge whether the result fits its connected workflow, conventions and user expectations. Trace the affected boundaries, failure states and dependencies. Use Test evidence when claiming those behaviors work; route change inspection to Audit when the requested deliverable is a review of the change.

### Performance

Judge whether supplied measurements support the agreed target, expected workload and acceptable tradeoffs. Test owns a missing measurement or baseline using the [measured improvement method](../../references/measured-improvement.md). Report what the measurements support and what remains unknown.

### Simplicity and quality

Review for unnecessary complexity, repeated knowledge, confusing flow, avoidable work and abstractions that do not earn their cost. Identify concrete opportunities to improve quality or efficiency while preserving behavior, errors, validation, accessibility, security and relevant performance. Apply KISS and DRY with judgment: repeated lines are not automatically defects, and premature abstraction can be less clear than duplication. Prefer the smallest useful improvement; do not sacrifice correctness or readability to minimize lines. Surface behavioral or product tradeoffs to the human.

## Correct and recheck

3. A review-only request ends with findings. If corrections are authorized, use the [shared review loop](../../references/review-loop.md) to repair and recheck affected criteria. For visual repairs, inspect the changed render; after a stress-related fix recheck normal and adverse views.

**Done:** Applicable quality criteria have findings or supporting evidence, any authorized correction has been checked, and material gaps are explicit.
