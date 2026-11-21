# Product delivery and readiness

Use to decide whether a product change is ready for a defined audience. State the offer or capability, launch cohort, what is promised, critical paths, and policy for partial availability. Read the agreed requirements and current evidence; separate completion of code from readiness for customers.

1. List only launch conditions that could change the decision: tested core paths, access and entitlements, migration or compatibility, support and communication readiness, trusted measurement, and a way to pause or recover. Assign an owner and evidence to each condition rather than accepting a green status without proof.
2. Imagine the launch failed. Ask what failed first, who would notice, who can act, and whether the issue is reversible. Distinguish blockers, risks acceptable to monitor, and work safe to defer. Stage exposure when it resolves a material uncertainty or limits impact; don't invent a rollout procedure for a trivial change.
3. Compare the approved intent with what is actually available in the candidate version. Check previews and Test, Audit or Deploy evidence where they apply. Record version, environment, eligibility and date so a later review can distinguish the candidate from a production outcome.
4. Recommend go, hold, or a narrower launch with conditions. Name the decision owner, open gates, and reset or stop triggers. Coordinate Market communications only when scope and availability are agreed.

An agreed recommendation is not a release or deployment. The task owner follows [versioned distribution](../../execute/references/VersionedDistribution.md); [Deploy](../../deploy/SKILL.md) owns rollout and operational recovery.

## Decide whether to retire a capability

Identify active consumers, commitments and what each would lose. Include infrequent callers, paying customers on older terms, stored records and dependencies outside the visible interface. Compare continuing support, narrowing availability and retirement against usage, service cost, obligations and the viability of a replacement.

Separate closing new enrollment, stopping use by existing customers and ending support. For each step, record the responsible owner, notice or migration conditions, evidence that affected users have a workable path, exceptions and when to pause. A planned replacement needs evidence from the workflows that depend on it. Return a recommendation and any unresolved customer commitments. [Market](../../market/SKILL.md) prepares approved communications, [Migrate](../../migrate/SKILL.md) owns persistent-state transitions and [Deploy](../../deploy/SKILL.md) owns activation.
