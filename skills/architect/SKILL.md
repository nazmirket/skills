---
name: architect
description: "Compare technical designs and their threats or privacy tradeoffs, choose a lasting system boundary, or record it in an ADR."
---

# Architect

Record settled changes to lasting boundaries, such as interfaces, data ownership or host inputs, in an architecture decision record (ADR). Keep local choices in the diff or plan. [Refactor](../refactor/SKILL.md) handles structure within a settled contract.

## Compare the options

- Check relevant ADRs and trace representative behavior, owners and data paths. Compare the current approach or leading proposal with its strongest viable alternative. Explain material constraints, why contenders fall short, and the effects on failure, migration and recovery. Use an [authorized prototype](../execute/references/Prototype.md) or evidence from [Migrate](../migrate/SKILL.md) or [Deploy](../deploy/SKILL.md#operate-and-recover) only if it could change the choice.
- Decide within the approved outcome. Bring unsettled requirements and consequential product, cost, security or operating tradeoffs to the human. Stop when evidence supports a recommendation or identifies the deciding question.
- Flag a potentially stale assumption and name the deciding check. Keep accepted decisions in force until evidence challenges their rationale. Preserve the record and link any successor.

For a system diagram, trace a representative operation to the actor that performs each read, write or transfer. Label consequential connections with the operation and source location at the inspected revision. Distinguish observed, proposed and unknown connections for [Design](../design/references/formats/DiagramDesign.md).

## Model threats during design

Identify protected assets, affected people and who crosses each trust or data boundary. Compare exposure, safeguards and sensitive data handling. Record assumptions and tradeoffs. The human decides access, retention and sharing policy. [Audit](../audit/SKILL.md#security-and-privacy-review) owns separate assessments.

## Record the decision

- Give open recommendations in chat. Save a proposed ADR when requested or required and an accepted ADR for a settled boundary change.
- Follow project instructions, index, format and numbering in the collection governing the affected component. Use `.work/decisions/` and the [numbering rules](../execute/references/Workspace.md#numbered-records) for a first collection. Link the ADR from the active plan if present. Report the intended path if a save fails.
- Include context, constraints, alternatives, choice, decision-maker, rationale, consequences and reasons to revisit. Record reproducible setup, steps and observed results, attributing supplied evidence and labeling unverified claims. Include private material only when authorized.
- Give [Plan](../plan/SKILL.md) the ADR when implementation needs sequencing. Implementation requires authority.
