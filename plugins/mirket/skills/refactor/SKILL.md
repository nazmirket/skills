---
name: refactor
description: "Use when simplifying or restructuring existing code while preserving observable behavior and staying within an agreed scope."
---

# Refactor

Improve the target code with the smallest complete, evidence-backed change. Preserve its intended behavior and the project's conventions; clarity and correctness matter more than minimizing lines.

## Understand and bound the work

1. Use [adapt](../adapt/SKILL.md) to understand the target, its purpose, connected behavior, project patterns and the human's constraints. Reuse a current orientation when it covers the same scope. Inspect callers, inputs, outputs, side effects, errors, ordering, validation and existing checks relevant to the change. Preserve the human's existing work.
2. Define the requested scope, structural improvement and observable behavior to preserve. Route consequential system boundary decisions to [Architect](../architect/SKILL.md) and performance targets to the [measured improvement method](../../references/measured-improvement.md). Obtain the human's direction if the change requires a product rule or public behavior to change.
3. When the required development or verification environment is unknown or blocked, use [Preflight](../preflight/SKILL.md) to assess it. Reuse existing readiness evidence when current. Follow its confirmation requirements for installations, environment changes and inferior fallbacks.

## Establish evidence and improve

4. Choose the most efficient reliable way to establish the relevant behavior before changing it. Use an existing focused check or reproduction when sufficient; add a targeted characterization check when important behavior is untested and at risk. Include relevant edge cases and project-required checks. Record any baseline failure or unavailable verification rather than treating it as a pass.
5. Choose a simple approach that addresses the actual problem. Reuse existing facilities, remove unnecessary complexity and duplication where doing so improves clarity, and make coherent, reviewable changes. Avoid unrelated cleanup, speculative abstractions or new dependencies. Preserve necessary validation, error handling, security, accessibility and externally observable behavior.
6. If orientation or verification reveals a defect or unexpected failure, use [debug](../debug/SKILL.md) to investigate the evidence and cause. Repair it only when the human's request or existing authorization covers the fix; report unrelated defects and keep the refactor within scope. Do not stack guesses onto a failing change.

## Verify the result

7. Use [Test](../test/SKILL.md) for focused behavior and required project checks. Compare with the baseline, including public inputs, outputs, errors and side effects. Use [Critique](../critique/SKILL.md) when an artifact's qualitative result needs assessment; a cleaner structure alone does not establish a speedup.
8. Inspect the full affected diff and relevant surrounding code. Confirm the change stays within the requested scope and has not shifted complexity or changed behavior unintentionally. Recheck after material corrections; report actual checks and results, baseline failures, remaining risks and anything that could not be verified.

**Done:** The requested code is improved within scope, the intended behavior is supported by appropriate evidence, and any verification gaps are explicit.
