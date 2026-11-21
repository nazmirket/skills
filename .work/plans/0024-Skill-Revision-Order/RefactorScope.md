# Refactor: scope for revision 11

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Refactor](../../../skills/refactor/SKILL.md) for distinct structural work that makes existing code simpler while preserving its contract. Handle incidental simplification directly within the task. Raise a separate change when the cleanup expands scope, such as merging untouched helpers used by multiple callers.

- **Clarify plausible reliance.** If a consumer may depend on undocumented behavior, show the evidence and ask what to preserve. Continue portions that cannot alter the disputed behavior. For example, inspect whether an export consumer uses the first row before treating stable ordering as incidental.
- **Separate a proven defect from the refactor.** Fix a bounded, in-scope violation of an established contract in the same task. Verify it separately and report which behavior changed. Keep unrelated defects and unresolved product rules out of the refactor.
- **Capture behavior at risk.** Reuse a focused check when sufficient. When an edit could change an important untested outcome, such as rejection of an empty request, add a focused characterization case and run it before and after. Reuse the existing test file if it fits.
- **Record baseline failures.** Continue when a pre-existing failure is demonstrably unrelated. Record it and rerun relevant checks. If the failure could overlap, investigate that overlap before editing.
- **Keep independent logic local.** Remove duplication when the code enforces one shared rule. Leave similar code separate when its callers or requirements evolve independently.
- **Report what the evidence supports.** Describe the simplification and verify behavior. Mention eliminated work such as repeated allocations where useful, but claim no runtime gain without comparable measurements. If a behavior check cannot run, deliver the patch with the checks that passed and the exact steps still needed. Leave equivalence unverified for that behavior and honor any explicit completion gate.

Representative cases: retain the existing direct simplification fixture; exercise a structural change that risks an untested rejection; show how to keep a quoted-comma fix distinct when the parser contract explicitly supports it. A dialog patch with passing unit tests and no equivalent keyboard check can be handed back with the precise keyboard path still pending.
