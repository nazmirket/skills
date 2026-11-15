---
name: audit
description: "Use to review a code change, draft plan, or scoped system and report material findings, including security and privacy risks."
---

# Audit

Review the work and return findings to its owner.

1. **Pin the target.** Identify the revision, snapshot, or draft; state the scope and governing criteria. Trace affected behavior, integration boundaries, and dependencies far enough to support your conclusions. Reuse [Test](../test/SKILL.md) evidence for behavior and performance, and use focused non-destructive checks when needed. Judge performance claims against the target and workload the evidence covers.
2. **Report material findings.** Separate confirmed defects, supported but unverified risks, and concrete improvements that address a meaningful cost, including unnecessary complexity. Prioritize by impact and likelihood. Give the location, triggering condition, evidence, consequence, and next step. Name missing evidence for risks and any material coverage limits. If there are no findings, say so for the reviewed scope.
3. **Stop at the report.** Return findings to the task owner without editing the target. If corrections are already authorized, follow the [review loop](../execute/references/ReviewLoop.md).

Require an [independent reviewer](#independent-review) for high-risk changes or an explicit gate.

## Security and privacy review

- Identify the protected assets, affected people, and scope. Trace relevant trust boundaries and sensitive data from collection to deletion, including secondary copies and external sharing when they matter. Distinguish intended safeguards from those supported by evidence.
- Assess the affected controls and prioritize findings by exposure and impact. Reuse [Test](../test/SKILL.md) evidence or use the smallest safe defensive check within scope. State what remains unverified; a partial assessment or a clean scanner result cannot establish overall security or compliance.
- Keep only necessary, sanitized evidence in an authorized destination. Keep secrets out of reports and fixtures. Bring unresolved access, retention, or sharing policy to the human. Give [Deploy’s operations branch](../deploy/SKILL.md#operate-and-recover) relevant findings and evidence preservation needs during an active incident. Return hardening recommendations to the implementer; the review does not authorize changes.

## Independent review

Treat serious potential harm or hard-to-reverse consequences as high risk. The reviewer must not have authored the work. If an independent reviewer is unavailable or not authorized, report inline findings, identify them as such, and leave the gate open. Independence is optional otherwise.
