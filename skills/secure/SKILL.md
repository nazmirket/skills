---
name: secure
description: "Use to assess security and privacy risks, model threats, or implement authorized hardening. Use Audit for a general review and Operate for an active incident."
---

# Secure

Reduce evidenced security and privacy risk within the authorized target. A security assessment ends with findings; hardening requires implementation authority. Return focused security evidence to the calling workflow rather than taking over its release or deployment. See the [routing guide](../../references/Routing.md).

## Establish the exposure

1. Identify the system, environment, assets and people to protect, allowed investigation, and the decisions the assessment must support. Read current architecture, access rules, data flows and relevant incidents. Distinguish verified controls from intended controls. Do not expand access, scan unrelated systems, extract sensitive records or test destructive paths without authorization for that scope.
2. Trace important trust boundaries: user to service, tenant to tenant, service to dependency, operator to infrastructure, and data to external processors. Identify who can supply inputs or change configuration and which checks enforce identity, authorization and isolation. Include background jobs, exports, administrative paths and failure behavior where they affect the threat.
3. Follow sensitive data through collection, use, storage, logs, backups, sharing, retention and deletion. Check whether permissions and capture scope survive defaults, upgrades and migrations. Use minimal sanitized evidence; never copy secrets into a report or test fixture. Bring unresolved access, retention or data-sharing policy to the human.

## Assess and reduce risk

4. Describe each material threat as a reachable condition, affected asset, existing defense and consequence. Prioritize using exposure and impact; distinguish a demonstrated failure from an untested hypothesis. Examine relevant input handling, authorization, credential lifecycle, dependency provenance and configuration. A tool score or absence of scanner findings does not establish security or regulatory compliance.
5. Choose the smallest safe check that can establish or falsify the issue. Prefer isolated fixtures and ordinary interfaces. Check denied and cross-boundary cases as well as legitimate use. Use [Test](../test/SKILL.md) for repeatable evidence and current authoritative guidance when a platform or standard determines the requirement. Record inaccessible boundaries explicitly.
6. For authorized hardening, fix the evidenced cause, preserve intended access and behavior, and verify both protection and legitimate use. Plan compatibility and credential/configuration transitions through [Migrate](../migrate/SKILL.md) when state changes. Give rollout constraints to [Deploy](../deploy/SKILL.md); do not treat identifying a vulnerability as authority to change production or rotate shared credentials.
7. For an active compromise or service incident, give [Operate](../operate/SKILL.md) the evidence, containment options and preservation needs. Avoid destroying diagnostic evidence or claiming containment without observing it. Share sensitive findings only through an authorized destination.

**Done:** Report the assessed scope, prioritized findings or completed hardening, actual checks, residual risks and any human risk decision. A partial assessment is not a whole-system assurance. Keep reusable evidence with the relevant plan or designated report under the [workspace rules](../../references/Workspace.md).
