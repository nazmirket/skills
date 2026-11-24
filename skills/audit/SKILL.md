---
name: audit
description: "Review a code change, draft plan, or scoped system for material technical, security, or privacy findings."
---

# Audit

Review a fixed target. Route rendered interface and interaction reviews to [design critique](../design/references/flows/Critique.md).

1. Pin the revision, snapshot or draft, scope and criteria. Trace affected callers, boundaries and data invariants. For code review, apply [Engineering Practices](../code/references/EngineeringPractices.md) to the changed paths.
2. Reuse [Test](../test/SKILL.md) evidence for the target and workload. Run focused, non-destructive checks for material gaps. Open the matching [review or scanner guide](references/README.md) when its procedure applies.
3. Prioritize findings by impact and likelihood. Give each a location, trigger, evidence, consequence and next action. Distinguish confirmed defects, unverified risks and improvements tied to a concrete cost. State coverage gaps or the absence of material findings.
4. Stop at findings for review-only work. The work's owner handles authorized corrections and [rechecks affected criteria](../execute/references/ReviewLoop.md).

For complex coverage or follow-up reviews, use the [coverage record](references/ReviewCoverage.md). For a focused recheck, give the prior conclusion, changed premise and current verdict in the finding.

## Security and privacy review

Identify protected assets and affected people. Trace trust boundaries and sensitive data from collection through sharing, copies and deletion as applicable. Compare intended safeguards with observed controls. Rank exposure and impact, use safe defensive checks and limit claims to the controls assessed.

Retain only sanitized evidence needed for the review in authorized locations. Exclude secrets from reports and fixtures. Leave access, retention and sharing policy decisions to the human. Give [Deploy](../deploy/SKILL.md#operate-and-recover) incident findings and evidence-preservation needs. The implementer owns authorized hardening.

## Independent review

Serious potential harm, hard-to-reverse consequences or an explicit gate require a reviewer who did not author the work. If unavailable or unauthorized, label the review inline and leave the gate open.
