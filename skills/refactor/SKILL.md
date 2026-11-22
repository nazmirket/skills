---
name: refactor
description: "Use for distinct structural work that simplifies existing code while preserving its observable contract."
---

# Refactor

Refactor owns structural changes that preserve observable behavior. Keep incidental simplification with the current task. Make the smallest useful change and scope broader work separately. [Architect](../architect/SKILL.md) owns changes to lasting boundaries.

## Establish what must stay true

- Trace affected callers, outputs, ordering, errors and side effects. Use [Adapt](../adapt/SKILL.md) for a distinct orientation gap. Preserve observed behavior that a consumer relies on. Ask when conflicting contracts or an unavoidable behavior change require a decision. Continue unaffected work.
- Run existing focused checks and record baseline failures. Proceed past demonstrably unrelated failures. Investigate possible overlap before editing.
- Add a characterization case for important untested behavior the edit could change. Use the existing test file if it fits. Run the same case before and after.

## Simplify and verify

Apply [Engineering Practices](../code/references/EngineeringPractices.md) to the changed boundary. Consolidate a duplicated rule when its callers must change together. Inspect the diff for a simpler path and unintended contract changes.

If a behavior-preserving refactor uncovers a defect, report it. When the request also authorizes a bounded correction, fix the established contract violation and verify that behavior change separately. [Debug](../debug/SKILL.md) investigates an unclear cause. Ask before changing a product rule.

Compare with the baseline and run relevant and required checks. Report what became simpler, what passed and any pre-existing failures. If verification is blocked, hand over the patch with the [outstanding check](../test/SKILL.md#run-and-report). Claim runtime gains only with [comparable measurements](../execute/references/MeasuredImprovement.md).
