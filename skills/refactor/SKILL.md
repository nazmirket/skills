---
name: refactor
description: "Use for distinct structural work that simplifies existing code while preserving its observable contract."
---

# Refactor

Make the smallest change that improves the structure. Handle incidental simplification within the current task. Raise a separate change when the work expands scope, such as merging untouched helpers with multiple callers.

## Establish what must stay true

- Inspect the callers and behavior the edit could affect, including outputs, ordering, errors, and side effects. Use [Adapt](../adapt/SKILL.md) if project facts are missing. If a consumer might rely on undocumented behavior, show the evidence and ask what to preserve. Continue work that cannot change it. Route lasting boundary choices to [Architect](../architect/SKILL.md).
- Reuse focused checks that cover the affected behavior. If an important outcome is untested and the edit could change it, add a focused characterization case and run it before and after. Reuse the existing test file when it fits.
- Record baseline failures. Continue if a failure is demonstrably unrelated; if it might overlap, investigate that overlap before editing.

## Simplify and verify

- Remove duplication when it enforces one shared rule. Keep similar logic local when its callers or requirements evolve independently. Review the affected diff for scope and unintended changes.
- Fix a bounded, in-scope violation of an established contract in the same task. Verify the correction separately and report the exact behavior that changed. Use [Debug](../debug/SKILL.md) if the cause is unclear. Flag unrelated defects and ask before changing a product rule.
- Compare against the baseline and rerun relevant and required project checks. Use [Test](../test/SKILL.md) when verification needs specialist work. Report pre-existing failures and what actually passed. If a behavior check cannot run, deliver the patch with the exact steps still needed and mark that behavior unverified. Honor explicit completion gates and use [Preflight](../preflight/SKILL.md) for setup blockers.
- Describe what became simpler or what work was removed. Claim a runtime gain only with [comparable measurements](../execute/references/MeasuredImprovement.md).
