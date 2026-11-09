# Triage issue reports

Turn reports into a deduplicated, prioritized set of issue drafts with the evidence and next action for each.

## Workflow

1. Collect expected and actual behavior, affected users or workflow, environment, reproduction steps or intermittent conditions, frequency, and impact. Keep the project's user-facing terms. Inspect relevant context and existing issues when available. Ask only for missing details that would change reproduction, priority, or routing.
2. Try a small, safe reproduction where feasible. Mark what was **reported**, what you **reproduced**, and what remains **unknown**. Preserve the evidence needed to repeat the observation; for a UI issue, include the input or state, viewport when relevant, and observed effect. If you cannot reproduce it, retain the report and conditions without inventing steps or declaring a cause.
3. Group duplicate reports by evidenced symptom and conditions; keep distinct, independently verifiable failures separate. Prioritize using the observed impact, reach, frequency, workaround, and dependencies. Mark tentative priorities, suspected duplicates, and unknown owners as such. Route cause investigation to [Debug](../../debug/SKILL.md).
4. Draft each issue with a behavior-based title, expected and actual results, steps or intermittent conditions, evidence, priority rationale, and suggested next action and owner. If a scratch file is needed, use `.work/temp/<task>/` under the [project workspace rules](../../../references/workspace.md). File or update issues only when explicitly authorized; return links for any tracker writes performed.

## Completion

Stop when the reports in scope are accounted for as issue drafts, linked duplicates, or entries awaiting specific evidence, with priority and the next action recorded. A triage request does not authorize diagnosis or fixes.
