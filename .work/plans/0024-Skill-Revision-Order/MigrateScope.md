# Migrate: scope for revision 19

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Migrate](../../../skills/migrate/SKILL.md) as the owner of planning, rehearsing, and carrying out authorized persistent-state transitions when preserving meaning, access, compatibility, or recoverability needs separate work. Handle routine reversible changes in the task that already owns them. [Plan](../../../skills/plan/SKILL.md) coordinates the wider work, [Deploy](../../../skills/deploy/SKILL.md) activates the application, and Operate held ongoing service health and observation at the time of this revision. The [later merge](DeployScope.md) moved that work into Deploy.

1. **Agree what must survive.** Before transforming affected state, agree on the source and target, what must stay true, what may change, and how exclusions or conflicts will be handled. Set the acceptance criteria for the transition.
2. **Choose the simplest authorized cutover.** Use one transition when affected consumers can switch together and interruption and recovery are within agreed bounds. Use a staged sequence when consumer coexistence, concurrent writes, or recovery constraints make a direct switch unsuitable.
3. **Reuse matching rehearsal evidence and prove recovery.** Accept recent evidence when it still covers the code, source contract, and relevant failure conditions. Rehearse only uncovered material risks. Before mutating the target, show that restoration or forward repair can recover the required state and invariants.
4. **Execute within existing authority.** Proceed with the agreed transition and cutover when prerequisites pass. A plan alone does not authorize execution. Ask only when a decision goes beyond the approved target or bounds. Resume from verified checkpoints when retries are known to be safe within agreed limits; stop the affected work when state or effects are uncertain.
5. **Close against the agreed criteria.** Reconcile the results with evidence proportionate to the criteria, using normal consumers where the criteria depend on them. Report deviations separately and leave unmet criteria open. Remove legacy state under existing authority once no consumers depend on it and the agreed recovery and retention conditions are met. Hand ongoing observation to Operate when needed.

## Implementation and checks

The revision updates the skill, routing, and migration fixtures. It keeps the local rehearsal case and covers a proved recovery path, safe checkpoint resumption, and unmet acceptance criteria. The approval covers skill guidance; it does not authorize an actual migration or cutover.
