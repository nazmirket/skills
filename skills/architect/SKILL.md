---
name: architect
description: "Use for consequential technical choices in a new or existing system, or when asked to assess architecture or record an architectural decision."
---

# Architect

Make consequential technical decisions reviewable and record each decision when made. For a behavior-preserving change within an agreed boundary, use [Refactor](../refactor/SKILL.md).

1. Pin the decision, desired outcome, affected system and constraints. For an existing system, read relevant architecture decision records (ADRs), use project terminology and trace representative behavior, ownership, data and tests. Ground friction in concrete examples. For a new system, use the stated outcomes, constraints and available evidence; identify unknowns and assumptions rather than inventing existing behavior.
2. Compare viable alternatives before settling on an interface. Consider the current approach when applicable. For each option, explain boundaries, responsibilities, what callers must know and how behavior can be tested. For a questionable existing boundary, ask whether removing the module would simplify the system or scatter complexity among callers. Research external technologies or patterns when they could materially change the decision; use [Curate](../curate/SKILL.md) to compare outside options. Use a diagram when it clarifies boundaries, flows or tradeoffs.
3. Compare tradeoffs against actual constraints, including failure modes, migration and rollback where relevant. Cite conflicts with prior ADRs and explain evidence for reopening a decision. For a narrow uncertainty, use the [prototype method](../../references/Prototype.md) when an experiment is authorized. Present options, evidence, consequences and a recommendation; keep unresolved questions explicit.
4. Bring decisions with material effects on product, cost, security or operations to the human. Make routine technical choices within the authorized scope, preserving prior decisions. An architectural assessment or recommendation alone does not authorize implementation.

Use [Secure](../secure/SKILL.md) for threat and privacy evidence, [Migrate](../migrate/SKILL.md) for persistent-state compatibility and recovery, and [Operate](../operate/SKILL.md) for operational requirements when those could change the choice. Give the chosen constraints to [Release](../release/SKILL.md) and [Deploy](../deploy/SKILL.md) when delivery is in scope; an ADR is not proof that a rollout or restore works.

## Record the decision

After an architectural decision is made, record it in the project's established ADR location and follow its format and numbering. If no location is established, create `docs/decisions/` at the project root and save the first [numbered ADR](../../references/Workspace.md#numbered-records) there, such as `0001-ProjectCleanup.md`. Record the context, options considered, chosen decision, decision-maker, evidence, rationale and consequences; link any useful diagram and related plan. Attribute the decision truthfully: a recommendation is not a decision or human approval. Preserve previous records and link superseded decisions rather than rewriting history.

Use `.work/decisions/` only for private notes or drafts. Do not copy older private material into shared records without authorization. If the ADR destination cannot be written, report the missing record and its intended location.

**Done:** The decision has an ADR, or the missing record is reported. For an unresolved choice, present the options and open decisions without creating an ADR. Route a chosen change to [Plan](../plan/SKILL.md) when execution planning is requested.
