# Audit: scope for revision 13

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Audit](../../../skills/audit/SKILL.md) as a short standalone skill for reviewing code changes, draft plans, and scoped systems. Replace separate target workflows and the mandatory two-pass review with one workflow.

1. **Pin the target.** Identify the revision or draft, the review scope, and the criteria that govern it. Follow affected behavior far enough to support the findings. Reuse evidence from Test or Critique when it answers a review question.
2. **Report material findings.** Keep confirmed defects, supported but unverified risks, and concrete improvements in distinct categories. Include an improvement only when the current approach has a meaningful cost. Prioritize by impact and likelihood; give the location, evidence, consequence, and next step. Name material coverage limits and the evidence still needed for unverified risks.
3. **Stop at the report.** Return findings to the task owner. Keep the review read-only unless corrections are already authorized.

**Independent review is required for high-risk changes or an explicit gate.** Treat serious potential harm or hard-to-reverse consequences as high risk. The reviewer must not have authored the work. If an independent reviewer is unavailable or not authorized, report inline findings, label them accurately, and leave the gate open. For other work, independence is optional.
