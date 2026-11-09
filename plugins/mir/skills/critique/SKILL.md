---
name: critique
description: "Use when reviewing or verifying work for visual quality, system integration, performance requirements, simplicity, duplication, or efficiency."
---

# Critique

Review the result against the intended outcome and project context. Select every relevant check below; a task may need more than one. Apply the human's instructions and project requirements, and keep the scope proportionate to the work.

## Establish the scope

1. Identify the change, intended behavior or appearance, relevant project conventions and agreed acceptance criteria. Inspect the connected context and distinguish evidence from assumptions. Surface material uncertainty instead of inventing requirements or a new design direction.
2. Choose focused checks that provide sufficient evidence for the affected behavior and risks, including required project checks. Inspect the actual result and report concrete findings with their location, evidence and effect.

## Choose relevant checks

### Visual

For a design, interface or visual change, compare the actual rendered elements with the human's direction, supplied references, approved designs and existing conventions. Inspect relevant sizes, themes and interaction states, including layout, hierarchy, alignment, typography, color, imagery and interaction clarity. View the image or live interface itself; merely capturing a screenshot or reading code is not visual verification. If the intended appearance, rendering or a relevant state is unavailable, report the gap.

### Integration

For a change that connects with an existing system, trace relevant callers, inputs, outputs, dependencies and end-to-end flows. Examine contracts, state changes, errors and compatibility against actual project assumptions and conventions. Exercise the affected boundaries and connected flow; isolated tests alone do not establish integration. Report unavailable checks or unverified boundaries.

### Performance

When the task has a performance criterion or performance problem, identify the agreed metric, target or acceptable regression, workload, environment and conditions. Do not invent a target; ask the human to decide when a required criterion is unclear. Use existing benchmarks or profiling conventions when suitable, choose the smallest representative measurement, and establish a baseline where meaningful. Record the method and conditions, and compare results under similar conditions after changes. Avoid disruptive load or production changes without authorization. Do not claim a target is met or performance improved without evidence.

### Simplicity and quality

Review for unnecessary complexity, repeated knowledge, confusing flow, avoidable work and abstractions that do not earn their cost. Identify concrete opportunities to improve quality or efficiency while preserving behavior, errors, validation, accessibility, security and relevant performance. Apply KISS and DRY with judgment: repeated lines are not automatically defects, and premature abstraction can be less clear than duplication. Prefer the smallest useful improvement; do not sacrifice correctness or readability to minimize lines. Surface behavioral or product tradeoffs to the human.

## Correct and recheck

3. If corrections are authorized, make focused changes within the requested scope and project conventions. Otherwise report actionable findings. Do not use this skill as permission to redesign, refactor or alter unrelated work.
4. Re-run the checks affected by each meaningful batch of corrections, including relevant visual inspection and comparable performance measurement. Repeat while material issues remain and useful progress can be made; stop when the agreed criteria are met or report unresolved issues and verification limits. Avoid repeating unchanged checks without a reason.
5. Report the relevant checks, actual evidence and results, material findings and any unavailable or unverified areas. Do not claim a check passed when it did not run or its evidence is insufficient.

**Done:** Each applicable quality dimension has been examined against the agreed outcome, necessary corrections have been verified, and material issues or limitations are explicitly reported.
