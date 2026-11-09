---
name: debug
description: "Use when investigating and fixing a concrete problem, defect, failure, or unexpected behavior identified through an orientation of the target."
---

# Debug

Debug from understanding and evidence. Start with an orientation finding, investigate its cause, and use guidance suited to the kind of work being fixed.

## 1. Start with an orientation finding

1. Use [adapt](../adapt/SKILL.md) to understand the target, its purpose, relevant flow, conventions and the human's context. Reuse a current orientation outcome for the same target when it already contains the needed evidence; otherwise complete or update the orientation first.
2. Identify the specific finding that starts debugging: expected and observed behavior, where it occurs, and supporting evidence. Distinguish a verified issue from an open question. If the orientation has not identified a concrete finding, continue understanding the target or ask for the missing information; do not invent a defect or begin a speculative fix.

## 2. Choose the right specialist guidance

3. Identify the type and affected surface of the issue. Discover and load the available specialist skill guidance appropriate for spotting and fixing that kind of issue, and the relevant quality-check skill for verifying the result. Apply their guidance throughout the investigation, fix and verification. More than one specialist may be needed when the issue spans different kinds of work.
4. Use [critique](../critique/SKILL.md) for the quality checks relevant to the issue and fix: visual appearance, system integration, performance criteria, and simplicity or quality. Use other specialist guidance when the task calls for it. For a visual issue, inspect the rendered element and its affected states; code inspection or a screenshot that has not been inspected is not visual verification.
5. If the needed specialist or quality-check skill is unavailable, say which guidance is missing and what cannot be verified. Continue independent evidence gathering where useful, but do not claim the required specialist guidance was followed or the fix fully verified. Ask the human for the missing guidance or an explicit decision about the unmet gate; do not invent a skill or silently substitute an inferior method. Honor the human's instructions and host capabilities.

## 3. Investigate before changing the target

6. Establish the smallest safe way to observe the finding, including the conditions, expected result and actual result. Trace the relevant behavior and evidence toward its cause; compare established working patterns and check relevant changes or boundaries. State hypotheses as hypotheses, and use focused checks to distinguish them. If the issue cannot be reproduced or the cause remains uncertain, report the evidence and uncertainty instead of guessing.
7. Once the evidence supports a cause, identify the smallest complete, convention-compatible fix and any affected behavior. Respect the human's product decisions and existing work. Resolve material changes in behavior with the human. Only implement changes within the authorized task; orientation alone does not authorize a repair.

## 4. Fix and verify efficiently

8. Select the fastest, most focused checks that provide sufficient evidence for the original issue and the risks of the fix. Prefer an existing reproduction or targeted test; add a regression check when needed to prevent a meaningful recurrence. Include required project checks and the applicable specialist quality checks. A quick check is insufficient if it cannot establish the expected outcome.
9. Apply the authorized fix at the evidenced cause, then run the chosen checks. Confirm the original finding is resolved and the affected behavior still meets its expected outcome. If a check fails or reveals a new risk, investigate the evidence and adjust; do not repeat unchanged checks or stack speculative fixes. If a check cannot run, record the gap instead of calling it passed.
10. Report the finding, evidenced cause, fix, actual checks and results, and any unresolved limitations. State whether required specialist guidance or quality verification remains unavailable.

**Done:** A concrete orientation finding has an evidence-backed cause and authorized fix, the original behavior and relevant risks have sufficient verification, and the applicable specialist quality guidance has been followed. If evidence, authorization, specialist guidance or verification is missing, report the precise remaining gap rather than declaring the issue fully fixed.
