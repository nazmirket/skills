---
name: deploy
description: "Use for CI/CD, rollout readiness, activation and rollback, interpreting rollout monitoring and alerts, service health or freshness, incident response, or backup and recovery checks."
---

# Deploy

Own readiness, activation, verification, and rollout recovery for artifact or configuration changes to shared running environments. Scale the work to risk. Use [the operations branch](#operate-and-recover) for health, observation, incidents, or backup recovery even when there is no rollout. The task owner supplies the [versioned artifact](../execute/references/VersionedDistribution.md), [Migrate](../migrate/SKILL.md) owns persistent-state transitions, and [Debug](../debug/SKILL.md) investigates causes.

Before deciding how to use a tool or interpreting its behavior, open its [stack guide](references/README.md) first and on its own. This includes interpreting saved queries, alerts, and status output. Skip guides for evidence you can reuse as-is. For CI/CD design or performance across tools, use [delivery pipeline practices](references/DeliveryPipelines.md).

## Establish readiness

1. **Pin the target and authority.** Identify the exact artifact or configuration, target environment, account or region as relevant, and current state. Read the established process and honor existing authority for preparation and readiness checks. Production activation requires a distinct decision authorizing the exact candidate and production target. Preparation and publication alone do not authorize it. Resolve an ambiguous target before changing it.
2. **Reuse matching evidence.** Carry forward checks only for the same artifact or configuration under equivalent conditions. Verify required prerequisites and meaningful differences directly in the target, including dependencies, access, capacity, or observability as relevant. Use [Preflight](../preflight/SKILL.md) for missing environment evidence and [Audit](../audit/SKILL.md#security-and-privacy-review) for material security or privacy questions. Do not print secrets.
3. **Choose the simplest rollout within agreed limits.** Use the established mechanism and stage exposure when impact or recovery cost warrants it. Define the sequence, target acceptance criteria, observation period, stop conditions, and rollback or forward repair. Reuse established thresholds and ask about consequential gaps. Confirm the recovery path is usable. If state changes, use [Migrate](../migrate/SKILL.md) evidence for the required transition and show before activation that rollout and recovery are compatible with the resulting state.

## Roll out and observe

4. **Reconcile uncertain operations before retrying.** Roll out the identified artifact without rebuilding it during promotion. Record the operation identifier and actual state. If the outcome is uncertain, check the operation record and what is actually served. Retry only when evidence shows the attempt did not apply and another attempt is safe. Queued or accepted is not complete.
5. **Verify against the agreed target criteria.** Reuse equivalent evidence and fill material gaps in the served environment. Verify the active identity and any affected paths or dependencies the criteria depend on. Observe the agreed period and compare relevant health signals to the baseline. Report activation separately from verified behavior, and leave unmet criteria open. A successful upload or HTTP 200 alone does not prove an end-to-end outcome.
6. **Halt further exposure at a stop condition.** Use the agreed and authorized rollback or forward repair after checking its preconditions. If recovery exceeds authority or could damage state, preserve evidence and escalate the decision. Verify service behavior after recovery and report whether rollout succeeded or was reversed.
7. Record the deployed identity, health evidence, remaining observation, runbook and known risks. Continue a requested bounded watch using the operations branch until its completion condition or a material blocker.

**Done:** Report what is active, where, its verified behavior, rollout or recovery result, and any unfinished operation or check. Keep deployment evidence in the established project record; use the [workspace rules](../execute/references/Workspace.md) for scratch files. Publishing a release and deploying it are separately observable outcomes.

## Operate and recover

1. **Assess health.** Identify the service or workflow, environment, affected users, and authorized actions. Read the runbook, dependencies, and recent changes. Use existing health objectives and report missing thresholds. Check the actual consumer path as well as component status. For asynchronous work, distinguish accepted, pending, failed, and completed operations, and compare expected events or revisions with actual results. Check whether signals are current, what they cover, and who can act. For a requested watch, define the mechanism, scope, duration, and escalation path.
2. **Respond to incidents.** Establish impact and timeline, preserve necessary sanitized evidence, and prioritize authorized, reversible mitigation. Use [Debug](../debug/SKILL.md) for causal investigation and [Audit](../audit/SKILL.md#security-and-privacy-review) for security or privacy findings. Check actual operation state before retrying, bound attempts and delays, and use supported checkpoints or safe retries. Distinguish transient lag from persistent failure. Use the rollout branch for software recovery and [Migrate](../migrate/SKILL.md) when recovery changes persistent state. External incident messages require authorization.
3. **Verify recovery.** Recheck the affected consumer path and the original health condition over a meaningful window. When assessing backup recovery, exercise restoration in an authorized isolated environment and reconcile needed data and permissions. Record residual backlog, lost or skipped work, and any manual reconciliation. Leave an actionable runbook with symptoms, evidence, safe checks, recovery and escalation steps, and how to verify. Record causes only as supported, and turn recurring failures into bounded prevention work.

**Done:** Report observed health or recovery, evidence times and scope, remaining issues, and the next owner and action. Say what remains monitored and what has stopped; a one-time check cannot establish continuing health or freshness.
