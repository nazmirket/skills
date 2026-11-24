---
name: debug
description: "Use to find the cause of a concrete failure or unexpected behavior and make the smallest authorized fix."
---

# Debug

[Author](../author/references/IssueTriage.md) owns ticket drafts. During incidents, give [Deploy](../deploy/SKILL.md#operate-and-recover) causal evidence and any authorized fix.

## Find the cause

- Start with expected and observed behavior and reuse existing evidence. Use [Adapt](../adapt/SKILL.md) for a distinct project gap or [Design](../design/SKILL.md) for unresolved interaction intent. Open the matching [diagnostic guide](references/README.md), local help or version-matched docs only when tool behavior or trace interpretation matters.
- Stop diagnosing when the focused check and code establish the cause. Otherwise reproduce safely and trace the first divergence between a working and failing run. Use ruled-out hypotheses to choose a check that distinguishes remaining causes. If blocked, report the last confirmed event and the evidence or decision needed next.
- If the failure does not reproduce, report the conditions and uncertainty. Fix a separately proven defect within scope and leave the reported failure open until evidence connects them.

## Fix and verify

A diagnosis ends with cause and evidence. For authorized repair, apply [Engineering Practices](../code/references/EngineeringPractices.md) and preserve agreed behavior. Rerun the check that caught the failure and any required checks. Extend a suitable existing test for needed regression coverage. Report the cause, fix, results and any [outstanding check](../test/SKILL.md#run-and-report). Use [Audit](../audit/SKILL.md#security-and-privacy-review) for separate risk assessment and [Migrate](../migrate/SKILL.md) for state transitions.
