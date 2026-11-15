---
name: migrate
description: "Use to plan, rehearse, or carry out an authorized persistent-state transition when preserving meaning, access, compatibility, or recoverability needs separate work."
---

# Migrate

Own the transition of persistent data, schemas, formats, or configuration. Keep routine reversible changes with the task that already owns them. [Plan](../plan/SKILL.md) coordinates the broader work, [Architect](../architect/SKILL.md) owns consequential design choices, [Deploy](../deploy/SKILL.md) activates the application, and [Test](../test/SKILL.md) supplies verification.

## Define the transition

1. **Agree on a preservation contract.** Identify the actual stores, source and target versions, and authorized environments. Inspect the schemas or configuration and representative sanitized records. Agree what must stay true, what may change, how to handle exclusions and conflicts, and what evidence will satisfy acceptance. Resolve ambiguous mappings and business rules before transforming affected state. Preserve identities, permissions, unknown fields, and unrelated settings unless the agreed target changes them.
2. **Pick the simplest authorized cutover.** Trace affected readers and writers, including jobs and older clients. Use a single transition when consumers can switch together and interruption and recovery fit the agreed bounds. Stage the change when coexistence, concurrent writes, or recovery requires it. Account for volume, lock and availability impacts. Define checkpoints, stop conditions, and any irreversible boundary; coordinate the application switch with Deploy.

## Rehearse and execute

3. **Reuse rehearsal evidence and prove recovery.** Reuse recent results when the transformation code, source contract, and relevant failure conditions still match. Rehearse uncovered material risks against representative sanitized copies, using a dry run or preview where feasible. Before mutating the target, prove that restoration or forward repair can recover the required state and invariants. An application rollback alone does not establish data recovery. Keep rehearsal files under ignored `.work/temp/` and recovery materials in their authorized locations.
4. **Execute and resume within existing authority.** A migration plan alone does not authorize execution. Proceed with the agreed transition and cutover once prerequisites pass; ask only for decisions outside the agreed target or bounds. Use a deterministic transformation, validate inputs and conflicts before writing, and record recoverable checkpoints without exposing sensitive data. Resume from a verified checkpoint without asking again when the retry is known to be safe within agreed limits. Stop affected work if an invariant fails or the state or effects are uncertain. A series of atomic writes can still leave a partial transition.
5. **Reconcile and retire against agreed criteria.** Compare actual results with independently expected outcomes, using normal consumers when acceptance depends on them. Report deviations, exclusions, and failed records separately, and leave unmet criteria open. Retain recovery evidence for the agreed interval or until the agreed acceptance condition is met. Retire legacy state under existing authority once no consumers depend on it and the agreed recovery and retention conditions are met. Hand ongoing observation to [Deploy’s operations branch](../deploy/SKILL.md#operate-and-recover) when needed.

**Done:** For planning, deliver the preservation contract, cutover sequence, acceptance checks, and recovery method. For execution, report the reconciled state, unmet criteria, remaining consumers, and recovery position. Keep evidence in its designated destination under the [workspace rules](../execute/references/Workspace.md).
