---
name: architect
description: "Use to compare technical designs, model threats and privacy tradeoffs between proposed designs, make architectural choices or record a settled system boundary."
---

# Architect

Architect owns consequential technical choices. Record a settled change to a lasting boundary, such as an interface, data ownership or host input, in an architecture decision record (ADR). Keep local choices in the diff or plan. [Refactor](../refactor/SKILL.md) owns structural changes within an agreed contract.

## Compare the options

- Define the decision and constraints. Read relevant ADRs and trace representative behavior, owners and data paths. Ask about requirements the evidence cannot settle, such as whether two writers must operate concurrently. Use an [authorized prototype](../execute/references/Prototype.md) when it would resolve the choice.
- Compare the current approach, or the leading proposal for new work, with its strongest viable alternative. Explain why serious contenders fall short. Consider failure, migration and recovery where relevant. Stop once the evidence supports a recommendation.
- Make technical choices within the approved outcome. Take material product, cost, security or operational tradeoffs requiring human judgment to the human. Draw on [Migrate](../migrate/SKILL.md) or [Deploy](../deploy/SKILL.md#operate-and-recover) when their evidence could change the choice.
- If an accepted assumption may have changed, flag the decision for review and name the deciding check. Keep the accepted decision in force. Reopen it only on evidence that challenges its rationale, preserving the record and linking any successor.

## Model threats during design

Identify protected assets, affected people and who crosses each trust or data boundary. Compare exposure, safeguards and sensitive data handling across designs. Record material assumptions and tradeoffs. The human resolves access, retention and sharing policy. [Audit](../audit/SKILL.md#security-and-privacy-review) owns a separate security or privacy assessment.

## Record the decision

- Return a recommendation in chat. Save an open draft in `.work/decisions/` when requested or required by the agreed deliverable. Link it from the active plan, if any.
- For a settled boundary change, follow the project's ADR format and numbering. If there is no ADR location, use `docs/decisions/` and the [numbering rules](../execute/references/Workspace.md#numbered-records). If saving fails, report the intended path.
- Include context, constraints, alternatives, choice, decision-maker, rationale, consequences and known reasons to revisit. Record the setup, commands or steps and observed results behind the decision so a maintainer can reproduce them from the ADR. Label unverified claims, link useful detail and include private material only when authorized.
- Give the ADR to [Plan](../plan/SKILL.md) for implementation steps and checks when needed. Implementation requires its own authority.
