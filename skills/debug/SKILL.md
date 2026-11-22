---
name: debug
description: "Use to find the cause of a concrete failure or unexpected behavior and make the smallest authorized fix."
---

# Debug

Debug owns diagnosis and authorized repair of a concrete failure. [Author](../author/references/IssueTriage.md) owns turning a report into a ticket. During an incident, give [Deploy](../deploy/SKILL.md#operate-and-recover) causal evidence and any authorized fix for its mitigation and recovery work.

## Find the cause

Start with expected behavior, observed behavior and existing evidence. Use [Adapt](../adapt/SKILL.md) for a distinct project-orientation gap or [Design](../design/SKILL.md) for unresolved interaction intent. When a tool-specific diagnostic or interpretation matters, including for a saved trace, use the matching [Debug guide](references/README.md) if available. For an unlisted tool, use its local help or version-matched documentation. Skip tool selection when the evidence already establishes the cause.

- When a focused check and the code establish the cause, skip further investigation.
- Otherwise use the smallest safe reproduction. Trace a working and a failing run to their first divergence. After two hypotheses fail, use what they ruled out to choose a different check. Run it when it can distinguish the remaining causes within scope. When no such check is available, report the last confirmed event and the evidence or decision needed to proceed.
- If the report will not reproduce, record the conditions and uncertainty. Fix an independently proven defect when it falls within the authorized repair. Leave the original failure unverified until evidence connects the two.

## Fix and verify

A diagnosis ends with the cause and evidence. For a repair, make the smallest fix and rerun the check that caught the failure. Ask before changing agreed behavior. Extend an existing test for a regression when it fits. Use a separate test if setup differs or the existing test would become unclear. Run required project checks.

Report the cause, fix and results. If the original check is blocked, deliver the in-scope fix with its evidence and the [outstanding check](../test/SKILL.md#run-and-report). [Audit](../audit/SKILL.md#security-and-privacy-review) owns a separate security or privacy assessment and [Migrate](../migrate/SKILL.md) owns persistent-state transitions.
