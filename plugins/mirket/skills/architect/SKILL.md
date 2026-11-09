---
name: architect
description: "Use when asked to assess a system boundary, compare consequential technical designs, or draft an architecture decision record."
---

# Architect

Make a technical decision reviewable. For a behavior-preserving change within an agreed boundary, use [Refactor](../refactor/SKILL.md).

1. Pin the decision, affected system, and constraints. Read relevant architecture decision records (ADRs) and use the project's domain language. Trace representative behavior, callers, ownership, data, and tests. For a broad assessment, start where recent changes or incidents show repeated friction; report concrete examples and links rather than treating file count or churn alone as evidence.
2. Compare the current design with viable alternatives before settling on an interface. For a boundary that looks shallow, ask what would happen if the module disappeared: would its complexity become simpler and more local, or be scattered among callers? For each option, explain what moves behind the boundary, what callers must know, and which behavior can be tested through the interface. A before-and-after dependency or flow diagram helps when it makes those changes easier to see.
3. Compare tradeoffs against the actual constraints. Include failure modes, migration and rollback where they affect the choice. If an option conflicts with an existing ADR, cite it and explain the evidence for reopening the decision. If a narrow uncertainty warrants an authorized experiment, use the [prototype method](../../references/prototype.md) to compare options without putting experiment code on the production path.

**Done:** Present the evidence, viable options, tradeoffs, recommendation, and unresolved decisions. If an ADR would help, draft it with context, options, the proposed decision, and consequences. Use the designated ADR location for a requested project record; keep an agent-only draft with its plan or in `.work/temp/<task>/` under the [workspace rules](../../references/workspace.md). Preserve existing records and route a chosen change to [Plan](../plan/SKILL.md) when execution planning is requested. An assessment or recommendation does not authorize implementation.
