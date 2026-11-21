---
name: refactor
description: "Use for distinct structural work that simplifies existing code while preserving its observable contract."
---

# Refactor

Refactor owns structural changes that preserve observable behavior. Keep incidental simplification with the current task. Make the smallest useful change and scope broader work separately. [Architect](../architect/SKILL.md) owns changes to lasting boundaries.

## Establish what must stay true

- Trace affected callers, outputs, ordering, errors and side effects. Use [Adapt](../adapt/SKILL.md) for missing project facts. If a consumer may rely on undocumented behavior, show the evidence and ask what to preserve. Continue unaffected work.
- Run existing focused checks and record baseline failures. Proceed past demonstrably unrelated failures. Investigate possible overlap before editing.
- Add a characterization case for important untested behavior the edit could change. Use the existing test file if it fits. Run the same case before and after.

## Simplify and verify

Consolidate copies of a shared rule. Keep logic local where callers or requirements evolve independently. Inspect the diff for scope and unintended changes.

Fix a bounded, in-scope violation of an established contract. Verify and report that behavior change separately. [Debug](../debug/SKILL.md) investigates an unclear cause. Flag unrelated defects and ask before changing a product rule.

Compare with the baseline and run relevant and required checks. Report what became simpler, what passed and any pre-existing failures. If verification is blocked, hand over the patch with the [outstanding check](../test/SKILL.md#run-and-report). Claim runtime gains only with [comparable measurements](../execute/references/MeasuredImprovement.md).
