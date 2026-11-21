# Secure: scope for revision 18

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Retire Secure as a standalone skill. Move security and privacy review to [Audit](../../../skills/audit/SKILL.md#security-and-privacy-review), design-time threat modeling to [Architect](../../../skills/architect/SKILL.md#model-threats-during-design), and [authorized hardening](../../../references/Routing.md#authorized-hardening) to the implementer.

- **Audit owns security and privacy review.** Add a focused branch to its existing findings workflow. Trace the affected trust boundaries and sensitive data flows, assess safeguards, and distinguish confirmed findings from supported risks and missing evidence. Use the least sensitive evidence needed and return findings without changing the target. Preserve Audit’s existing independence rule for high-risk work and explicit gates.
- **Architect owns design-time threat modeling.** Identify what needs protection, which actors cross the affected boundaries, and how design options change exposure or data handling. Record material assumptions and tradeoffs with the architecture decision. Ask the human to resolve open access, retention, or sharing policy when it affects the choice. Use Audit when a separate assessment is needed.
- **The implementer owns authorized hardening.** Apply the smallest effective correction within scope. Reuse [Test](../../../skills/test/SKILL.md) evidence to check that the safeguard works and legitimate use still works. Route persistent-state transitions to [Migrate](../../../skills/migrate/SKILL.md) and rollout to [Deploy](../../../skills/deploy/SKILL.md) when relevant. Findings alone do not authorize production changes or shared credential rotation.
- **Keep incident ownership with the response workflow.** Give the incident owner relevant security and privacy findings, evidence that must be preserved, and unresolved exposure. Operate owned containment and recovery at the time of this revision; the [later merge](DeployScope.md) moved that work into Deploy. Keep sensitive evidence in the authorized destination.

## Open choices

Only ownership was answered. Questions 2–10 remain open: review triggers, threat modeling depth, privacy defaults, evidence requirements, prioritization, hardening boundaries, who accepts residual risk, incident handoff timing, and where to keep evidence. The draft carries forward existing safeguards and establishes no new approval or release gate.

## Implementation and checks

Move the guidance to its receiving owners, then remove the standalone skill and its agent metadata. Update shared instructions, routing, live references, the catalog, the website, and affected behavior fixtures. Verify that both hosts use the same 19 skills and that security review still stops at findings, independently authorized hardening has an owner, and incident response still routes to Operate. Retain the historical lifecycle decision as a record.
