---
name: critique
description: "Use when quality judgment is useful during implementation or before delivery, including visual quality, integration fit, simplicity, and performance evidence."
---

# Critique

Judge work in progress or a result against its brief and project context. Apply this skill during implementation when useful and before delivery when quality needs judgment. Own the quality assessment; [Test](../test/SKILL.md) owns measurable checks, and [Audit](../audit/SKILL.md) owns defect findings on changes, plans and scoped systems.

## Establish the scope

1. Identify the change, intended behavior or appearance, relevant project conventions and agreed acceptance criteria. Inspect the connected context and distinguish evidence from assumptions. Surface material uncertainty instead of inventing requirements or a new design direction.
2. Select lenses relevant to the task and its risks; not every lens applies. Inspect the actual result and reuse current Test evidence; request only missing checks that could change the verdict. Put saved screenshots and other temporary evidence in `.work/temp/<task>/` under the [workspace rules](../../references/Workspace.md). A finding records the condition or location, evidence, impact and next step. Distinguish observations, inferences and subjective judgments; identify unavailable evidence. Explain material matters of taste or possible product-direction changes and their options, and ask the human when the choice would materially change the outcome.

## Choose relevant checks

### Visual

For a design, interface or visual change, compare the actual rendering with the brief, supplied reference and project conventions. Inspect the hierarchy, layout, type, imagery or interaction states that matter. For motion, inspect normal playback and any meaningful interruption or reduced-motion case; for an export, inspect the delivered file at the intended scale. Use [Design's evidence guide](../design/references/ReviewAndDelivery.md) to choose cases and [stress the interface](references/UiStress.md) for realistic adverse data. Name the effect on use or communication before treating an aesthetic pattern as a defect. View the result yourself; a screenshot capture or source alone is insufficient. Report missing evidence as unverified; a static image cannot establish interaction behavior or accessibility by itself.

### Integration

Judge whether the result fits its connected workflow, conventions and user expectations. Trace the affected boundaries, failure states and dependencies. Use Test evidence when claiming those behaviors work; route change inspection to Audit when the requested deliverable is a review of the change.

### Performance

Judge whether supplied measurements support the agreed target, expected workload and acceptable tradeoffs. If performance matters but a useful target or comparable measurement is missing, state the gap and seek an appropriate target or measurement; do not claim the result is fast enough without evidence. Test owns measurement using the [measured improvement method](../../references/MeasuredImprovement.md). Report what the measurements support and what remains unknown.

### Simplicity and quality

Review for unnecessary complexity, repeated knowledge, confusing flow, avoidable work and abstractions that do not earn their cost. Identify concrete opportunities to improve quality or efficiency while preserving behavior, errors, validation, accessibility, security and relevant performance. Apply KISS and DRY with judgment: repeated lines are not automatically defects, and premature abstraction can be less clear than duplication. Prefer the smallest useful improvement; do not sacrifice correctness or readability to minimize lines. Surface behavioral or product tradeoffs to the human.

## Correct and recheck

3. A review-only request ends with findings. During authorized implementation, correct issues within the authorized scope and use the [shared review loop](../../references/ReviewLoop.md) to recheck affected criteria. Report material tradeoffs and seek the human's decision when product direction or the outcome would materially change. For visual repairs, inspect the changed render; after a stress-related fix recheck normal and adverse views.

**Done:** Applicable quality criteria have findings or supporting evidence, any authorized correction has been checked, and material gaps are explicit.
