---
name: audit
description: "Use to review a code change, draft plan, or scoped system and report material findings, including security and privacy risks."
---

# Audit

Audit owns technical, security and privacy findings on a fixed target. [Design critique](../design/references/flows/Critique.md) owns reviews of a person's interaction with a rendered interface.

1. Identify the revision, snapshot or draft, scope and criteria. Trace affected behavior, dependencies and integration boundaries. Reuse [Test](../test/SKILL.md) evidence and run focused, non-destructive checks for gaps. Open only the matching [tool guide](references/README.md) when a scanner or tool affects the assessment. Bound performance claims to the tested target and workload.
2. Distinguish confirmed defects, supported but unverified risks, and improvements that address a concrete cost such as needless complexity. Prioritize by impact and likelihood. Give each finding a location, trigger, evidence, consequence and next action. Name missing evidence and coverage limits. Say when the reviewed scope has no material findings.
3. End a review-only request with the report. When corrections are authorized, the work's owner makes and verifies them using the [review loop](../execute/references/ReviewLoop.md).

For a broad assessment or a follow-up review, use the [coverage record](references/ReviewCoverage.md) to show which conclusions still hold at the current revision and which areas remain open.

## Security and privacy review

Identify protected assets and affected people. Trace trust boundaries and sensitive data from collection to deletion, including secondary copies and external sharing where relevant. Compare intended safeguards with evidence of actual controls. Rank risks by exposure and impact. Use the smallest safe defensive check needed. Bound conclusions about security and compliance to the controls assessed, including when a scan is clean.

Retain only necessary, sanitized evidence in authorized locations. Exclude secrets from reports and fixtures. The human decides unresolved access, retention or sharing policy. Give [Deploy](../deploy/SKILL.md#operate-and-recover) incident findings and evidence-preservation needs. The implementer owns authorized hardening.

## Independent review

High risk (serious potential harm or hard-to-reverse consequences) or an explicit gate requires a reviewer who did not author the work. If that reviewer is unavailable or unauthorized, label your findings as inline and leave the gate open. For other reviews, independence is optional.
