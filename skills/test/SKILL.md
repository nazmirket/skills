---
name: test
description: "Use for explicit verification requests or when the task owner needs evidence about a behavior, regression, or performance claim."
---

# Test

Fill a verification gap and return the evidence to the task owner. The owner can run known focused checks directly. Reuse relevant results and choose the smallest checks that can catch the meaningful failure.

## Choose the check

- Get the expected result from a specification, accepted example, or prior decision independent of the implementation. If sources conflict or are silent on a material rule, ask and continue with undisputed checks.
- Use the existing harness for deterministic behavior when adding coverage is warranted and authorized. Use a manual check when automation cannot exercise the interaction reliably. Keep a fast regression test near the cause. If the regression reached a user-facing workflow, run one smoke check through that path as well. For a quoted comma, the parser test checks the field; a real export checks that the job uses the corrected parser.
- For a new regression test, run the same check against the original code in isolation and against the fix. Confirm the old code fails for the intended reason and the fix passes. Preserve the working tree. If you cannot exercise the original code, state the gap.

## Run and report

- Reuse CI results for the exact revision and relevant matrix when they cover the behavior in question. Run more checks only for a material evidence gap or an outstanding required check.
- If a new failure passes on retry, run one targeted diagnostic when available, such as repeating just the failed browser test with tracing. Report each attempt and hand any further investigation to [Debug](../debug/SKILL.md) or the task owner.
- Report passes, failures, and unverified checks separately. For a blocked check, give the missing target or capability, the exact command or steps still needed, and the expected outcome. Continue checks that can run. Match evidence to the claim: a build or package inspection cannot verify a live install. Honor environment and release gates.
- Claim a speedup only after repeated comparable runs on the same inputs and relevant conditions, with output correctness verified. Use the [measurement method](../../references/MeasuredImprovement.md).
- Hand back the smallest useful evidence: target checked, command or steps, relevant input, and expected and actual results. Verification alone does not authorize product edits. Give evidence to [Audit](../audit/SKILL.md) for technical review, [Design](../design/SKILL.md#visual-critique) for visual review, or [Author](../author/SKILL.md) for writing review when relevant.
