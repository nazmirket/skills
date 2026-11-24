---
name: refactor
description: "Use for distinct structural work that simplifies existing code while preserving its observable contract."
---

# Refactor

Keep incidental simplification with the current owner. [Architect](../architect/SKILL.md) owns lasting boundary changes.

## Establish what must stay true

- Trace caller-visible outputs, ordering, errors and effects. Use [Adapt](../adapt/SKILL.md) for a distinct orientation gap. Resolve material contract conflicts or necessary behavior changes before affected edits.
- Reuse matching baseline evidence or run focused existing checks. Investigate overlapping failures and record unrelated ones. Characterize important untested behavior the edit could change. Run the same cases before and after.

## Simplify and verify

Apply [Engineering Practices](../code/references/EngineeringPractices.md) and make the smallest useful structural change. Consolidate rules whose callers must change together. Inspect the diff for contract changes.

Report defects discovered during the refactor. Fix an established violation separately when authorized and verify that correction. Use [Debug](../debug/SKILL.md) for unclear causes. Ask before changing product rules.

Compare results to the baseline and run remaining required checks. Report the simplification, results, pre-existing failures and any [outstanding checks](../test/SKILL.md#run-and-report). Claim runtime gains only with [comparable measurements](../execute/references/MeasuredImprovement.md).
