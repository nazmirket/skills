---
name: migrate
description: "Plan, rehearse or execute persistent-state changes that require separate preservation, compatibility or recovery work."
---

# Migrate

Routine reversible edits stay with their owner. Use [Concurrent transitions](references/ConcurrentTransitions.md) when versions overlap or writes continue. [Architect](../architect/SKILL.md) owns lasting design choices, [Plan](../plan/SKILL.md) coordinates broader work and [Deploy](../deploy/SKILL.md) owns environment activation and monitoring.

## Define the transition

1. Pin stores, versions and authorized environments. Inspect schemas, configuration and representative sanitized records. Resolve ambiguous mappings and rules. Define invariants, permitted changes, exclusions, conflict handling and acceptance evidence. Preserve identities, permissions, unknown fields and unrelated settings unless explicitly changing them.
2. Trace readers and writers, including jobs and older clients. Use a single transition where interruption and recovery limits allow it. Stage it for coexistence, ongoing writes or recovery. Account for volume, locks and availability. Define checkpoints, stop conditions and irreversible steps. Coordinate shared environment cutover with Deploy.

A plan ends with the preservation contract, sequence, checks and recovery method. Rehearsal and execution each require applicable authority.

## Rehearse and execute

3. Reuse rehearsal evidence that matches transformation code, source contract and failure conditions. Test uncovered risks on representative sanitized copies, using a dry run or preview where feasible. Before changing the target, demonstrate restoration or forward repair against the preservation contract. Follow the [workspace rules](../execute/references/Workspace.md) for scratch and recovery evidence.
4. Execute within approved limits once prerequisites pass. Validate inputs and conflicts before writes. Transform deterministically, record checkpoints without sensitive data and verify the checkpoint against current state before a safe retry. Halt affected work if an invariant fails or state or effects become uncertain.
5. Reconcile actual results against independent expectations and exercise normal consumers where acceptance depends on them. Report deviations, exclusions, failures, remaining consumers, recovery options and open criteria. Keep recovery evidence for the agreed interval or acceptance condition. Retire legacy state under authority after its last consumer leaves and recovery and retention criteria pass.
