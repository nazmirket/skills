---
name: operate
description: "Use to assess or maintain service health, observability and freshness, respond to incidents, or verify backup and recovery. Use Debug for causal investigation."
---

# Operate

Keep an existing service or automated workflow useful and recoverable. Own the operational outcome: health, containment, restoration or a bounded observation. [Debug](../debug/SKILL.md) investigates causes, [Deploy](../deploy/SKILL.md) rolls out changes, and [Migrate](../migrate/SKILL.md) changes persistent state. Return evidence to the calling workflow without restarting it.

## Establish useful health

1. Identify the service, environment, users, authorized actions and the operational question. Read current runbooks, dependencies, recent changes and known incidents. Establish what good means using existing objectives: availability, latency, error rate, data correctness, backlog, freshness or resource limits as relevant. Report missing thresholds rather than inventing a service guarantee.
2. Inspect the actual user or consumer path as well as component status. Distinguish configured, running, reachable and working. For asynchronous work, track accepted, pending, failed and completed operations separately; compare expected source revisions or events with processed results. A healthy process or a successful seed does not prove current data, complete capture or successful retrieval.
3. Verify observability: useful signals, their timestamps and scope, detection of stale or missing signals, and who can act. Collect only necessary sanitized evidence. If monitoring is requested, define its mechanism, scope, duration and escalation path; running a one-time check is not continuous monitoring.

## Respond and recover

4. For an incident, establish impact and timeline, preserve relevant evidence, and prioritize an authorized reversible mitigation. Compare recent changes and known failure modes; use Debug for the smallest discriminating investigation. Use [Secure](../secure/SKILL.md) for suspected compromise, sensitive-data exposure or changed access boundaries. External incident messages require authorization.
5. Check operation state before retries. Bound attempts and delays, use supported idempotency/checkpoints, and separate transient lag from a persistent failure. Do not hide an unresolved incident by clearing errors or marking records current. If recovery changes state or software, give Migrate or Deploy the exact target, authority and constraints.
6. Verify recovery through the affected consumer path and the original health condition, including a meaningful observation window. For backup/recovery work, exercise restoration in an isolated authorized environment and reconcile necessary data and permissions; backup creation alone does not establish recoverability. Record residual backlog, lost or skipped work and any manual reconciliation.
7. Leave an actionable runbook or update the existing one: symptom, evidence, safe checks, recovery command, stop/escalation condition and verification. Record the cause only to the extent supported. Turn recurring failures into bounded prevention work and give [Focus](../focus/SKILL.md) product-outcome evidence where relevant.

**Done:** Report observed health or recovery, evidence times and scope, unresolved failures and the next owner/action. State exactly what remains monitored and what has stopped. Keep records in their designated location under the [workspace rules](../../references/Workspace.md); never promise permanent freshness or uptime from a one-time check.
