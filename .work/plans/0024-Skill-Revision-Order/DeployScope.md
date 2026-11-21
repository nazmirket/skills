# Deploy: scope for revision 21

**Status:** The Operate merge and additional Deploy policies are approved and implemented. See [Progress](Progress.md) for verification.

[Deploy](../../../skills/deploy/SKILL.md) stays the owner of readiness, authorized activation, rollout recovery, and verification in the target environment. By later direction it also owns [service health, incidents, observation and recovery](../../../skills/deploy/SKILL.md#operate-and-recover), including when no rollout is requested. There is no standalone Operate skill or handoff to it. The timing of any operational handoff outside Deploy was unanswered and remains open.

1. **Use Deploy for changes to shared running environments.** Include artifact and configuration activation. Scale the process to risk.
2. **Make production activation a distinct decision.** Prepare and check readiness under existing authority. Confirm authorization for the exact candidate and production target before activation. Preparation and publication do not confer that authority.
3. **Reuse matching readiness evidence.** Carry checks forward only for the same artifact and equivalent conditions. Verify meaningful differences and required prerequisites directly in the target.
4. **Use the simplest rollout within agreed limits.** Follow the established mechanism. Stage exposure when potential impact or recovery cost warrants it.
5. **Prove compatibility and recovery before activation when state changes.** Use [Migrate](../../../skills/migrate/SKILL.md) evidence for the required state transition and show that rollout and recovery are compatible with the resulting state.
6. **Resolve uncertain operations before retrying.** Check the operation record and what is actually served. Retry only when the prior attempt did not apply and retrying is safe.
7. **Verify against agreed target criteria.** Reuse equivalent target evidence and fill material gaps. Keep unmet criteria open and distinguish activation from verified behavior.
8. **Stop exposure and use agreed recovery.** When a stop condition is met, halt further exposure. Use authorized rollback or forward repair after checking its preconditions. Escalate if recovery exceeds authority or could damage state.

Approval covered edits to the skill, routing, and verification fixtures. It did not authorize a real rollout or recovery action.
