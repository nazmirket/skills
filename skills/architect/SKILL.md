---
name: architect
description: "Use to assess architecture, make a consequential technical choice, or record a settled change to a lasting system boundary."
---

# Architect

Make consequential technical choices reviewable. Write an architecture decision record (ADR) for a settled choice that changes a lasting boundary, such as an interface, ownership of data, or where hosts get their inputs. Use [Refactor](../refactor/SKILL.md) for behavior-preserving work within an agreed boundary; keep local choices in the diff or plan.

## Compare the options

- Define the decision and constraints. Read relevant ADRs and trace representative behavior, ownership, and data. Ask the human about unresolved requirements that determine the design. For example, trace both write paths before asking whether concurrent writes must be supported. An [authorized prototype](../../references/Prototype.md) can test a design against that requirement.
- Compare the current approach with the strongest viable alternative. If there is no current approach, compare the leading proposal with its strongest alternative. Explain why serious contenders were ruled out. Use actual constraints, including failure, migration, and recovery where relevant. Stop when the evidence supports a recommendation.
- Make technical choices within the approved outcome. Bring material tradeoffs that need human judgment to the human, including effects on product, cost, security, or operations. Use [Migrate](../migrate/SKILL.md) or [Deploy’s operations branch](../deploy/SKILL.md#operate-and-recover) when their evidence could change the choice.
- If an accepted decision's assumption plausibly changed, note that it is under review and name the check that would settle it. Keep the accepted decision in force. Reopen it only when evidence challenges its rationale; keep the original record and link any successor.

## Model threats during design

When trust or data boundaries matter to the decision, identify what needs protection, who crosses the boundaries, and how each design changes exposure and sensitive data handling. Compare the safeguards, and record material assumptions and tradeoffs with the decision. Ask the human to resolve access, retention, or sharing policy that affects the choice. Use [Audit](../audit/SKILL.md#security-and-privacy-review) for a separate assessment when needed.

## Record the decision

- For an open decision that needs its own comparison, keep a private draft in `.work/decisions/` and link it from the active plan if there is one. Do not present a recommendation as an accepted decision.
- Once settled, follow the project's ADR format and numbering. If there is no established location, use `docs/decisions/` and the [workspace numbering rules](../../references/Workspace.md#numbered-records). If the record cannot be saved, report its intended location.
- Make the ADR usable on its own: include the context, constraints, alternatives, choice, decision-maker, rationale, and consequences. Include any known condition for revisiting. For checks that informed the decision, record the setup, commands or steps, and observed results so a maintainer can reproduce them without the private plan. Label unverified claims. Link useful supporting detail and keep private material out of the project record unless authorized.
- Hand the ADR to [Plan](../plan/SKILL.md) when execution planning is needed. Plan derives the implementation steps and checks. The ADR records the decision; it does not authorize implementation.
