# Triage issue reports

Turn reports into a deduplicated, prioritized set of issue drafts with the evidence and next action for each.

## Workflow

1. Collect expected and actual behavior, affected users or workflow, environment, reproduction steps or intermittent conditions, frequency, and impact. Keep the project's user-facing terms. Inspect relevant context and existing issues when available. Ask only for missing details that would change reproduction, priority, or routing.
2. Try a small, safe reproduction where feasible. Mark what was **reported**, what you **reproduced**, and what remains **unknown**. Preserve the evidence needed to repeat the observation; for a UI issue, include the input or state, viewport when relevant, and observed effect. If you cannot reproduce it, retain the report and conditions without inventing steps or declaring a cause.
3. Group duplicates by symptom, conditions and affected version. Compare reproductions before linking a match. For a prior fix, check which release first contained it and which version the reporter ran. Split failures that can be fixed and verified independently, recording dependencies that block a fix or its verification. Prioritize by impact, reach, frequency, workaround and dependencies. Mark uncertain priorities, matches and owners. Route cause investigation to [Debug](../../debug/SKILL.md).
4. Give each draft a user-facing title, expected and actual results, reproducible steps or intermittent conditions, evidence, priority rationale and next owner. Describe an observable acceptance check in the project's domain language so it will still make sense after an implementation change. Use [project scratch space](../../execute/references/Workspace.md) for intermediate files. File or update issues only when explicitly authorized and return the resulting links.

## Completion

Stop when the reports in scope are accounted for as issue drafts, linked duplicates, or entries awaiting specific evidence, with priority and the next action recorded. A triage request does not authorize diagnosis or fixes.
