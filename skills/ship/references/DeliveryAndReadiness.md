# Product delivery and readiness

Use to decide whether a product change is ready for a defined audience. State the offer or capability, launch cohort, what is promised, critical paths, and policy for partial availability. Read the agreed requirements and current evidence; separate completion of code from readiness for customers.

1. List only launch conditions that could change the decision: tested core paths, access and entitlements, migration or compatibility, support and communication readiness, trusted measurement, and a way to pause or recover. Assign an owner and evidence to each condition rather than accepting a green status without proof.
2. Imagine the launch failed. Ask what failed first, who would notice, who can act, and whether the issue is reversible. Distinguish blockers, risks acceptable to monitor, and work safe to defer. Stage exposure when it resolves a material uncertainty or limits impact; don't invent a rollout procedure for a trivial change.
3. Compare the approved intent with what is actually available in the candidate version. Check previews and Test, Audit or Deploy evidence where they apply. Record version, environment, eligibility and date so a later review can distinguish the candidate from a production outcome.
4. Recommend go, hold, or a narrower launch with conditions. Name the decision owner, open gates, and reset or stop triggers. Coordinate Market communications only when scope and availability are agreed.

An agreed recommendation is not a release or deployment. The task owner follows [versioned distribution](../../execute/references/VersionedDistribution.md); [Deploy](../../deploy/SKILL.md) owns rollout and operational recovery.

Influence: [PM Skills pre-mortem](https://github.com/phuryn/pm-skills/tree/9af7bfd0bc47fdad43c2eaa7a43cd13918e7aaef/pm-execution/skills/pre-mortem).
