---
name: migrate
description: "Use to plan or execute changes to persistent data, schemas, formats or configuration while preserving required meaning and compatibility."
---

# Migrate

Move persistent state from a known starting contract to a defined target without silently losing its meaning, access rules or recoverability. [Architect](../architect/SKILL.md) owns consequential design choices, [Deploy](../deploy/SKILL.md) owns application rollout, and [Test](../test/SKILL.md) supplies verification. A migration plan alone does not authorize execution.

## Define the transition

1. Identify source and target versions, the actual stores and consumers, authorized environments, scope and invariants. Inspect real schemas, configuration layers and representative sanitized records. Inventory identities, precision, encoding, null/default behavior, ordering, ownership, permissions and capture/retention policy where relevant. Resolve ambiguous mappings and business rules with the human before transforming affected state.
2. Trace every reader and writer, including scheduled jobs, old clients and versions that may coexist during rollout. Specify compatibility and ordering: additive expansion, backfill, validation, consumer switch and later removal when appropriate. State how concurrent writes are handled. Do not equate filesystem path normalization with canonical application identity.
3. Estimate volume, lock or availability impact and the resources required. Define checkpoints, reconciliation, abort conditions and the irreversible boundary. Choose rollback, forward repair or restore based on what can actually recover the invariants; application rollback cannot undo every data transformation. Keep backup location/access and retention within authorized policy.

## Rehearse and execute

4. Build a deterministic, inspectable transformation with dry-run or preview where feasible. Make retries idempotent or detect completed work explicitly. Validate inputs and conflicts before mutation; preserve unknown fields and unrelated settings unless their removal is intended. For multi-file or multi-store updates, define partial-failure recovery rather than assuming each atomic write makes the whole operation atomic.
5. Rehearse against representative sanitized copies, including conflicting identities, missing/defaulted values, reruns, interruption and old/new consumers. Put disposable rehearsal/staging files under ignored `.work/temp/`; keep actual outputs and important recovery copies in their designated locations. Compare independent expected counts, keys, totals, relationships and policy—not only whether the script exits successfully. Verify that the recovery material can restore the needed state before relying on it.
6. Execute only within the authorized scope and readiness conditions. Capture a recoverable checkpoint, record source/target and progress without leaking sensitive data, and observe the agreed limits. Stop affected work when an invariant fails; do not blindly rerun an uncertain partial transition. Coordinate a consumer switch with Deploy and bring new data-loss or access-policy decisions to the human.
7. Reconcile actual results through the normal consumers, verify preserved permissions and semantics, and record any excluded or failed records. Retain recovery evidence until the agreed observation period or acceptance condition is met. Delete old state only when its consumers and retention obligations are resolved and removal is authorized.

**Done:** For planning, deliver the transition, invariants, compatibility sequence, verification and recovery method. For execution, report the verified state, reconciliation, remaining consumers and recovery position. Keep evidence in its designated destination under the [workspace rules](../../references/Workspace.md); use [Operate](../operate/SKILL.md) for continued observation.
