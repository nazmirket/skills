---
name: deploy
description: "Use to roll a known artifact or configuration into a target environment, verify service behavior, or execute an authorized deployment rollback."
---

# Deploy

Put an identified change into the intended environment and verify the resulting service. [Release](../release/SKILL.md) owns the versioned artifact, [Migrate](../migrate/SKILL.md) owns persistent-state changes, and [Operate](../operate/SKILL.md) owns continuing service health and incident response. Use the [routing guide](../../references/Routing.md) for combined requests.

## Establish readiness

1. Identify the exact artifact or configuration, target environment/account/region, current version, requested scope and deployment authority. Read the existing deployment process and current state. Preparation and a successful build do not authorize production activation. Honor authority already given; resolve an ambiguous target before changing it.
2. Verify artifact identity, prerequisites, compatible dependencies and configuration, required access, capacity and observability. Use [Preflight](../preflight/SKILL.md) for missing environment evidence and [Secure](../secure/SKILL.md) for material security or privacy questions. Do not print secrets. Check environment-specific differences instead of assuming staging proves production behavior.
3. Define the rollout method, order, health and user-path checks, observation period, stop conditions and rollback or forward-recovery action. Reuse established thresholds; ask for consequential unknown limits. Confirm that the previous artifact and configuration are recoverable and compatible with any state migration. Hand state changes to Migrate before crossing their irreversible boundary.

## Roll out and observe

4. Use the established deployment mechanism with the smallest appropriate exposure. Avoid rebuilding a different artifact during promotion. Record the operation identifier and actual state so interruption or an uncertain response can be resolved before retrying. Do not mark a queued or accepted operation complete.
5. Verify from the served environment: artifact/version, routing, critical dependencies and a representative user action. Include authentication, assets, background work or data access when affected. Observe the defined period and compare to the health baseline. A process running, successful upload or HTTP 200 alone is insufficient for an end-to-end claim.
6. If a stop condition occurs, halt further exposure and execute the already authorized recovery path when safe. Check actual state before repeating commands. If recovery would require new authority, an irreversible data change or a tradeoff outside the agreed bounds, preserve evidence, explain the decision and continue safe investigation. Recheck service behavior after recovery; distinguish a rolled-back deployment from a successful rollout.
7. Hand [Operate](../operate/SKILL.md) the deployed identity, health evidence, remaining observation, runbook and known risks. A requested bounded watch stays with the task until its completion condition or a material blocker; do not claim indefinite monitoring without an operating mechanism.

**Done:** Report what is active, where, its verified behavior, rollout or recovery result, and any unfinished operation or check. Keep deployment evidence in the established project record; use the [workspace rules](../../references/Workspace.md) for scratch files. Publishing a release and deploying it are separately observable outcomes.
