# Test: scope for revision 12

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Test](../../../skills/test/SKILL.md) as the owner of verification evidence. Invoke it for an explicit verification request or when the task owner needs a distinct check. The task owner can run known focused checks directly; Test fills the missing evidence without repeating covered work.

- **Check the regression and the path that uses it.** Keep a fast regression check near the cause. When a failure reached a user-facing workflow, run one smoke check through that workflow before handing back the fix. For a quoted-comma bug, the parser test proves the field stays intact; a real export proves the job uses the corrected parser.
- **Extend the existing harness for deterministic behavior.** When the work authorizes writing tests, add a reliable case to the existing harness, such as verifying that closing a dialog returns keyboard focus to its opener. Use a manual check when automation cannot represent the interaction reliably. Record what was actually exercised.
- **Use an independent source for the expected result.** Look for an accepted example, specification, or decision before asking. If sources conflict or are silent on a material rule, ask and continue with undisputed checks. For half-cent rounding, use an approved invoice that settles the tie; do not take the expected value from the proposed implementation.
- **Prove a new regression check can fail.** Run the same check against the original code in isolation, confirm it fails for the intended reason, and confirm it passes against the fix. Preserve the working tree. If the original code cannot be exercised, name that gap.
- **Reuse matching CI evidence.** Identify the exact revision and matrix, verify that it covers the relevant behavior, and stop when evidence is sufficient. Run more only if there is a material gap or a required check is outstanding.
- **Investigate mixed results once before handoff.** If a new failure passes on retry, run one targeted diagnostic when available, such as repeating only the failed browser test with tracing. Report every attempt. Hand further causal investigation to Debug or the task owner rather than treating a retry as a clean pass.
- **Name the blocked check.** Report verified results and the exact missing target, command or steps, and expected outcome. For example, a successful Mac install does not verify Windows; give the Windows runner the install command and expected behavior. Keep the unrun check unverified.
- **Measure performance on comparable runs.** Repeat the old and new workloads using the same inputs and relevant conditions, such as cache state. Check output correctness before claiming a speedup. Different cache states plus one run per version are insufficient.
- **Hand back the smallest useful evidence.** For a failure, give the task owner or Debug the target, command, input, expected result, and actual result. Verification alone does not authorize product edits.

Representative cases: reuse the verification-only fixture to confirm that a failure is reported without a product edit; use the quoted-comma example to distinguish a check that fails on the old parser from a smoke check through the real export path. Preserve environment and release gates: an unavailable check remains unverified.
