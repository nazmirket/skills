---
name: test
description: "Use when asked to select, write, or run software checks, verify a regression fix, or validate an observable behavior or performance claim."
---

# Test

## Purpose

Produce a record of which behaviors were checked, what the results establish, and where evidence is still missing. When another skill requested the check, return the evidence to that owner; see the [routing guide](../../references/Routing.md).

## Workflow

1. Identify the expected behavior, affected boundary, likely failure modes, and required project checks. Reuse relevant current evidence and existing tests. Choose the narrowest check that can catch the risk: a manual path for a simple observable outcome, a focused automated check for repeatable logic, or an integration or smoke check where wiring and contracts matter. Add adverse inputs where their impact warrants it. For a performance or resource claim, use the [measured improvement method](../../references/MeasuredImprovement.md).
2. Add an automated check when meaningful new behavior or regression risk warrants it and the work authorizes it; otherwise reuse sufficient focused checks or direct inspection. Derive the expected result from a spec, worked example, or known result independent of the implementation, and use the normal interface. For a test-first slice, run the check before the change and confirm it fails for the intended reason, then run it after the change and confirm it passes. Report if the old behavior cannot be exercised.
3. Run the focused checks and required project checks in a suitable environment. Record the target, command or steps, relevant inputs and environment, expected and actual results, and evidence. Save scratch outputs in `.work/temp/<task>/` under the [workspace rules](../../references/Workspace.md). If a required check cannot run, report it as unverified with its blocker and run other relevant checks that remain possible. Record unavailable, skipped, and inconclusive checks separately from passes. Return unexpected failures to the current investigator; use [Debug](../debug/SKILL.md) when a new causal investigation is needed. Rerun only when a change, suspected flake, or new risk warrants it.
4. When defect inspection or quality judgment is also needed, give the existing evidence to [Audit](../audit/SKILL.md) or [Critique](../critique/SKILL.md), respectively. Critique owns rendered quality checks.

## Completion

Match delivery evidence to its claim: [Release](../release/SKILL.md) needs checks of the packaged artifact and supported upgrade; [Deploy](../deploy/SKILL.md) needs served-environment behavior; [Migrate](../migrate/SKILL.md) needs reconciliation, retry and recovery evidence; [Secure](../secure/SKILL.md) needs legitimate and denied-boundary cases; [Operate](../operate/SKILL.md) needs current consumer health and freshness. Return those results to the owner. A synthetic payload, configuration inspection or build pass does not substitute for a live host or production-path check.

Stop when the requested behavior and required checks have sufficient evidence, or when an unresolved failure or prerequisite prevents that. Report the result and material gaps; selecting or running checks does not itself authorize product edits.
