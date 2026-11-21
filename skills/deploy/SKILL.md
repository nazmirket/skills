---
name: deploy
description: "Use for CI/CD, rollout readiness, activation and rollback, interpreting rollout monitoring and alerts, service health or freshness, incident response, or backup and recovery checks."
---

# Deploy

Deploy owns CI/CD and changes to shared running environments, from readiness through rollout and recovery. It also owns [service health and incidents](#operate-and-recover) between rollouts. The task owner supplies the [versioned artifact](../execute/references/VersionedDistribution.md). [Migrate](../migrate/SKILL.md) owns persistent-state transitions. [Audit](../audit/SKILL.md#security-and-privacy-review) assesses material security or privacy risks during readiness checks and incidents.

Before choosing a tool operation or interpreting tool behavior, consult the matching [stack guide](references/README.md). This includes saved queries, alerts and status output. Skip the guide for evidence you can reuse as-is. Use [delivery pipeline practices](references/DeliveryPipelines.md) for CI/CD design or performance across tools.

## Establish readiness

1. Pin the artifact or configuration, target environment, relevant account or region and current state. Follow the established process and existing authority for preparation and readiness. Resolve an ambiguous target before changing it. Production activation requires a distinct decision for the exact candidate and target, even after publication.
2. Reuse checks for the same candidate under equivalent conditions. Verify prerequisites and material differences in the target, including dependencies, access, capacity and observability where relevant. Use [Preflight](../preflight/SKILL.md) for missing environment evidence. Keep secrets out of output.
3. Use the simplest established rollout that meets agreed limits. Stage exposure when impact or recovery cost warrants it. Define the sequence, acceptance criteria, observation window, stop conditions and rollback or forward repair. Reuse thresholds and ask about consequential gaps. Confirm recovery is usable. For state changes, use Migrate's evidence to show rollout and recovery both work with the resulting state before activation.

## Roll out and observe

4. Promote the identified artifact without rebuilding it. Record the operation ID and actual state. For an uncertain outcome, check the operation record and what is served. Retry only when the attempt did not apply and retry is safe.
5. Verify the active identity, affected consumer paths and dependencies against target criteria. Compare health with the baseline over the agreed window. Record activation and verified behavior separately. Keep unmet criteria open, including when the only evidence is an accepted upload or HTTP 200.
6. At a stop condition, halt further exposure. Check recovery preconditions, carry out the authorized rollback or forward repair and verify service behavior. If recovery exceeds authority or could damage state, preserve evidence and escalate.
7. Record the active identity and target, rollout or recovery outcome, health evidence, runbook, risks and outstanding operations, checks or observation in the project record. Use the [workspace](../execute/references/Workspace.md) for scratch files. Keep device-specific deployment procedures in `.work/routines/` so later runs on this device can reuse them. Continue a requested bounded watch until its completion condition or a material blocker.

## Operate and recover

- **Assess health.** Identify the service or workflow, environment, affected users and authority. Read the runbook, dependencies and recent changes. Check the consumer path and component status against existing objectives. Report missing thresholds. For asynchronous work, distinguish accepted, pending, failed and completed operations. Compare expected events or revisions with actual results. Check signal freshness, coverage and who can act. For a watch, specify mechanism, scope, duration and escalation.
- **Mitigate.** Establish incident impact and timeline, preserve necessary sanitized evidence and prioritize authorized, reversible mitigation. [Debug](../debug/SKILL.md) investigates causes. Distinguish transient lag from persistent failure. Reconcile actual state before retrying, bound attempts and delays, and use supported checkpoints or safe retries. Use the rollout steps for software recovery and Migrate for state transitions. External incident messages require authorization.
- **Verify recovery.** Recheck the affected consumer path and original health condition over a meaningful window. For backups, restore in an authorized isolated environment and reconcile required data and permissions. Record backlog, lost or skipped work and manual reconciliation. Leave a runbook covering symptoms, evidence, safe checks, recovery, escalation and verification. Record supported causes and define bounded prevention work for recurring failures.
- Report observed health or recovery with evidence times and scope, open issues and the next owner and action. Identify monitoring still running or stopped. Limit a one-time observation to the window checked.
