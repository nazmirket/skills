---
name: architect
description: "Use for consequential technical choices in a new or existing system, or when asked to assess architecture or record an architectural decision."
---

# Architect

Make consequential technical decisions reviewable and record each decision when made. For a behavior-preserving change within an agreed boundary, use [Refactor](../refactor/SKILL.md).

1. Pin the decision, desired outcome, affected system and constraints. For an existing system, read relevant architecture decision records (ADRs), use project terminology and trace representative behavior, ownership, data and tests. Ground friction in concrete examples. For a new system, use the stated outcomes, constraints and available evidence; identify unknowns and assumptions rather than inventing existing behavior.
2. Compare viable alternatives before settling on an interface. Consider the current approach when applicable. For each option, explain boundaries, responsibilities, what callers must know and how behavior can be tested. For a questionable existing boundary, ask whether removing the module would simplify the system or scatter complexity among callers. Research external technologies or patterns when they could materially change the decision; use [Curate](../curate/SKILL.md) to compare outside options. Use a diagram when it clarifies boundaries, flows or tradeoffs.
3. Compare tradeoffs against actual constraints, including failure modes, migration and rollback where relevant. Cite conflicts with prior ADRs and explain evidence for reopening a decision. For a narrow uncertainty, use the [prototype method](../../references/prototype.md) when an experiment is authorized. Present options, evidence, consequences and a recommendation; keep unresolved questions explicit.
4. Bring decisions with material effects on product, cost, security or operations to the human. Make routine technical choices within the authorized scope, preserving prior decisions. An architectural assessment or recommendation alone does not authorize implementation.

## Record the decision

After an architectural decision is made, create an ADR for it in `.work/decisions/` at the project root using the [workspace rules](../../references/workspace.md). Use a unique, descriptive filename. Record the context, options considered, chosen decision, decision-maker, evidence, rationale and consequences; link any useful diagram and related plan. Attribute the decision truthfully: a recommendation is not a decision or human approval. Preserve previous records and link superseded decisions rather than rewriting history.

Use only `.work/decisions/` for Architect's ADRs, including shared decisions. This directory is ignored by Git; make that limitation clear when a teammate needs the record. If it cannot be written, report the missing ADR and do not claim the decision was recorded.

**Done:** The decision has an ADR, or the missing record is reported. For an unresolved choice, present the options and open decisions without creating an ADR. Route a chosen change to [Plan](../plan/SKILL.md) when execution planning is requested.
