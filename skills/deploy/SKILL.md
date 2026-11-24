---
name: deploy
description: "Design CI/CD, assess rollout readiness, deploy or roll back, assess health, freshness or alerts, or handle incidents and backup recovery."
---

# Deploy

Use [delivery pipeline practices](references/DeliveryPipelines.md) for CI/CD design or performance. Open the matching [stack guide](references/README.md) only for unresolved tool behavior. Go directly to [operations](#operate-and-recover) for health, monitoring or incidents. Bring material security or privacy questions to [Audit](../audit/SKILL.md#security-and-privacy-review).

## Establish readiness

1. Pin the [candidate](../execute/references/VersionedDistribution.md) or configuration, environment, account or region and current state. Resolve target ambiguity before changes. Verify final authority for the exact production candidate and target independently of publication.
2. Reuse checks for the same candidate under equivalent conditions. Check differences in dependencies, access, capacity and observability that matter in the target. Use [Preflight](../preflight/SKILL.md) for unresolved setup. Keep secrets out of evidence.
3. Choose the simplest rollout within agreed limits. Stage exposure when impact or recovery cost warrants it. Use agreed thresholds or resolve material gaps. Set the observation window and stop conditions. Confirm recovery is usable before activation. For state changes, use [Migrate](../migrate/SKILL.md)'s evidence to verify rollout and recovery compatibility. A readiness-only request ends with the candidate, target, judgment and gaps.

## Roll out and observe

4. Promote the tested artifact where supported. If the target rebuilds it, verify its inputs and resulting behavior before directing traffic. Record the operation ID. For uncertain outcomes, inspect the operation and what is served. Retry only if unapplied and safe.
5. Verify the served identity, consumer paths and dependencies. Compare health with the baseline over the agreed window. Record activation and verified behavior separately. Keep unmet criteria open. Continue a requested watch until its condition is met or blocked.
6. At a stop condition, halt further exposure. Check preconditions for authorized rollback or forward repair and verify recovery. Preserve evidence and escalate if recovery exceeds authority or could damage state.
7. Record the active identity, target, outcome, health evidence and open checks or risks. Keep device-specific runbooks in `.work/routines/` per the [workspace rules](../execute/references/Workspace.md).

## Operate and recover

- **Assess health.** Pin the service, environment, affected users and relevant dependencies or changes. Check the consumer path and component status against runbook objectives. Check signal freshness and coverage, and compare expected events or revisions with actual status. Distinguish accepted, pending, failed and completed work. Report missing thresholds. For a watch, define mechanism, scope, duration and escalation owner.
- **Mitigate.** Establish impact and timeline, preserve sanitized evidence and prioritize authorized, reversible action. Distinguish transient lag from persistent failure. Reconcile state before bounded retries and use verified checkpoints. Use the rollout steps for software recovery and Migrate for state. [Debug](../debug/SKILL.md) investigates causes. External messages require authority.
- **Verify recovery.** Recheck the consumer path and original health condition over a meaningful window. Verify backup recovery by restoring in an authorized isolated environment and reconciling data and permissions. Record backlog, lost work and manual reconciliation. Address runbook gaps and recurring failures within scope.
- Report the observed window and scope, continuing monitoring, unresolved issues and the next owner and action.
