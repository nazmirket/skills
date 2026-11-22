---
name: audit
description: "Use to review a code change, draft plan, or scoped system and report material findings, including security and privacy risks."
---

# Audit

Audit owns technical, security and privacy findings on a fixed target. [Design critique](../design/references/flows/Critique.md) owns reviews of a person's interaction with a rendered interface.

1. Identify the revision, snapshot or draft, scope and criteria. Trace affected behavior and integration boundaries. For code reviews, apply [Engineering Practices](../code/references/EngineeringPractices.md) to the changed paths. Identify which caller, dependency or data invariant a design finding affects.
2. Reuse [Test](../test/SKILL.md) evidence and run focused, non-destructive checks for gaps. Follow the matching [review or scanner guide](references/README.md) when its procedure governs the assessment. Bound performance claims to the tested target and workload.
3. Distinguish confirmed defects, supported but unverified risks, and improvements that address a concrete cost such as needless complexity. Prioritize by impact and likelihood. Give each finding a location, trigger, evidence, consequence and next action. Name missing evidence and coverage limits. Say when the reviewed scope has no material findings.
4. End a review-only request with the report. When corrections are authorized, the work's owner makes and verifies them using the [review loop](../execute/references/ReviewLoop.md).

When a review spans several boundaries or depends on earlier conclusions, use the [coverage record](references/ReviewCoverage.md) to show which evidence still applies and which areas remain open. A focused recheck can give the prior conclusion, changed premise and current verdict directly in the finding.

## Security and privacy review

Identify protected assets and affected people. Trace trust boundaries and sensitive data from collection to deletion, including secondary copies and external sharing where relevant. Compare intended safeguards with evidence of actual controls. Rank risks by exposure and impact. Use the smallest safe defensive check needed. Bound conclusions about security and compliance to the controls assessed, including when a scan is clean.

Retain only necessary, sanitized evidence in authorized locations. Exclude secrets from reports and fixtures. The human decides unresolved access, retention or sharing policy. Give [Deploy](../deploy/SKILL.md#operate-and-recover) incident findings and evidence-preservation needs. The implementer owns authorized hardening.

## Independent review

High risk (serious potential harm or hard-to-reverse consequences) or an explicit gate requires a reviewer who did not author the work. If that reviewer is unavailable or unauthorized, label your findings as inline and leave the gate open. For other reviews, independence is optional.
