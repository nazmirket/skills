---
name: test
description: "Use to verify behavior, regressions or performance, interpret test results, or fill a verification gap for the task owner."
---

# Test

Test owns verification of behavior, regressions and performance. Task owners run known focused checks directly. The implementer owns product changes.

## Choose the check

- Establish the expected result independently from a specification, accepted example or prior decision. Ask about conflicting or missing material rules and continue undisputed checks.
- Reuse relevant results, including CI for the exact revision and relevant matrix. Run the smallest check that can catch the meaningful failure, plus outstanding required checks. Open only the matching [runner guide](references/README.md) when runner behavior matters.
- For warranted, authorized coverage, use the existing harness for deterministic behavior. Use a manual check when automation cannot reliably exercise the interaction. Keep a fast regression test near the cause. If the regression reached a user-facing workflow, also run one smoke check through that entry point.
- Run a new regression case against the original code in isolation and against the fix, preserving the worktree. Confirm the original fails for the intended reason and the fix passes. State the gap if the original cannot be exercised.

## Run and report

If a new failure passes on retry, run one targeted diagnostic when available, such as a trace of the failed browser test. Report each attempt. Give further investigation to [Debug](../debug/SKILL.md) or the task owner.

For a benchmark, use the [measurement method](../execute/references/MeasuredImprovement.md) to define the workload and verify its outputs. A measurement-only request ends with the observed result and its limits. A speedup claim also needs a comparable baseline and repeated measurements under matching conditions.

Report the target, command or steps, input, expected and actual results. Distinguish passes, failures and unverified checks. For a blocker, name the missing capability or target, exact remaining check and expected outcome. Continue available checks and honor environment and release gates. Limit claims to the path exercised, including for a live installation.

For every visual check, follow [Design's full-resolution screenshot requirements](../design/references/tools/Screenshot.md). Return evidence to the responsible reviewer when relevant. [Audit](../audit/SKILL.md) owns technical findings, [Design critique](../design/references/flows/Critique.md) visual and interaction findings, and [Author](../author/SKILL.md) writing findings.
