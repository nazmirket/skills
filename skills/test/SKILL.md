---
name: test
description: "Use to verify behavior, regressions or performance, interpret test results, or fill a verification gap for the task owner."
---

# Test

Task owners run known checks directly. The implementer owns product changes.

## Choose the check

- Derive expectations from a specification, accepted example or decision. Resolve material conflicts and continue undisputed checks.
- Reuse applicable evidence, including CI for the exact revision and relevant matrix. Run the smallest remaining meaningful check plus unmet required checks. Open the matching [runner guide](references/README.md) only when runner behavior matters.
- For warranted, authorized coverage, use the existing harness for deterministic behavior and manual checks for interactions automation cannot verify reliably. Keep the regression case near the cause. If the regression reached a user workflow, exercise that entry point once.
- Run new regression cases against the original in isolation and against the fix. Confirm failure for the intended reason and a pass on the fix. Preserve the worktree and report any blocked baseline.

## Run and report

If a failure passes on retry, run one targeted diagnostic when available. Report each attempt and give further investigation to [Debug](../debug/SKILL.md) or the owner.

Follow the [measurement method](../execute/references/MeasuredImprovement.md) for benchmarks. A measurement-only request ends with results and limits. A speedup claim needs repeated comparable measurements.

Report target, steps, input, expected and actual results. Distinguish passes, failures and unverified checks. Name a blocker's missing capability and exact remaining check. Continue available checks and honor environment and release gates.

Use the [full-resolution capture standard](../design/references/tools/Screenshot.md) for visual checks. Give evidence to the owner of the result or review, such as [Audit](../audit/SKILL.md), [Design critique](../design/references/flows/Critique.md) or [Author](../author/SKILL.md).
