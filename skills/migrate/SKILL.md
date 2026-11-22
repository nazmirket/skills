---
name: migrate
description: "Use to plan, rehearse, or carry out an authorized persistent-state transition when preserving meaning, access, compatibility, or recoverability needs separate work."
---

# Migrate

Migrate owns persistent data, schema, format or configuration transitions that need separate preservation, compatibility or recovery work. Routine reversible edits stay with their owner. [Architect](../architect/SKILL.md) owns lasting design choices, [Plan](../plan/SKILL.md) coordinates broader work and [Deploy](../deploy/SKILL.md) activates the application.

For overlapping versions or ongoing writes, open [Concurrent transitions](references/ConcurrentTransitions.md) only when compatibility, backfill or catch-up still needs design.

## Define the transition

1. Identify the stores, source and target versions and authorized environments. Inspect schemas or configuration and representative sanitized records. Agree on invariants, permitted changes, exclusions, conflict handling and acceptance evidence. Resolve ambiguous mappings and business rules before transforming affected state. Preserve identities, permissions, unknown fields and unrelated settings unless the target explicitly changes them.
2. Trace readers and writers, including jobs and older clients. Choose a single transition when consumers can switch together within interruption and recovery limits. Stage it when coexistence, concurrent writes or recovery requires it. Account for volume, locks and availability. Define checkpoints, stop conditions and any irreversible step. Coordinate with Deploy when cutover changes a shared running environment.

For a plan, return the preservation contract, cutover sequence, acceptance checks and recovery method. Rehearsal and execution need authority for those actions.

## Rehearse and execute

3. Reuse recent rehearsal results when transformation code, source contract and failure conditions match. Rehearse uncovered material risks on representative sanitized copies, using a dry run or preview where feasible. Before mutating the target, demonstrate that restoration or forward repair recovers the required state and invariants. Keep rehearsal files in ignored `.work/temp/` and recovery materials in authorized locations.
4. Once prerequisites pass, execute under existing authority. Ask only for decisions outside the agreed target or limits. Use a deterministic transformation. Validate inputs and conflicts before writes and record recoverable checkpoints without sensitive data. Resume from a verified checkpoint under existing authority when retry is safe. Stop affected work if an invariant fails or state or effects are uncertain, even when individual writes are atomic.
5. Reconcile actual results against independent expectations, through normal consumers where acceptance depends on them. Report deviations, exclusions and failed records separately. Record reconciled state, pending criteria, remaining consumers and recovery options. Retain recovery evidence for the agreed interval or acceptance condition. Retire legacy state only under existing authority after its last consumer leaves and recovery and retention criteria are met.

Follow the [workspace rules](../execute/references/Workspace.md) for evidence destinations. Give [Deploy](../deploy/SKILL.md#operate-and-recover) ongoing observation when needed.
