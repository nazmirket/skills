---
name: focus
description: "Use to define or prioritize a product opportunity, model business rules, or evaluate shipped outcomes and user feedback before deciding what to do next."
---

# Focus

Turn a product opportunity into a brief the human can decide on. The human owns product priorities and business rules; label proposals and assumptions separately from confirmed decisions.

1. Identify who is affected, what they are trying to do, and the consequences of the current experience. Separate observed behavior, reported needs, and hypotheses. Research outside evidence when it would change the decision; use [Curate](../curate/SKILL.md) for sourced comparisons of options.
2. Define the desired outcome, constraints, goals and non-goals. Compare viable choices, including keeping the current behavior when plausible, using user impact, cost, and uncertainty. For each proposed success measure, say how it could be observed and mark an unknown baseline or unapproved target as such.
3. Recommend a priority with the evidence and tradeoffs behind it. For an uncertain product requirement or business rule that affects the outcome, present the evidence and options and ask the human to decide. State which decisions still need an answer. If an authorized experiment would resolve a concrete product uncertainty, use the [prototype method](../../references/Prototype.md) to test scenarios without treating simulated behavior as approved policy. For example, a refund model can expose what happens after a partial return; the refund rule remains the human's decision.

## Learn from shipped work

For an outcome review, start from the original hypothesis, intended audience and agreed success measures. Inspect what actually shipped and when; use [Release](../release/SKILL.md) or [Operate](../operate/SKILL.md) evidence rather than assuming a planned feature reached users.

Check the evidence before interpreting it: event definitions, missing or duplicate data, observation period, baseline, exposure and cohort differences. Combine relevant user feedback with measured behavior, distinguishing reported needs from observed use. A metric moving after deployment does not establish causation; state confounders and sample limits. Use [Test](../test/SKILL.md) for measurement validity and [Secure](../secure/SKILL.md) when new instrumentation would change data collection or sharing.

Compare outcomes to the agreed target and guardrails, including adverse effects. Recommend continuing, changing, investigating or retiring the feature with the evidence and uncertainty. The human owns consequential priorities and business rules. For a live experiment, define its decision, exposure, measures, stop conditions and recovery before routing authorized rollout to [Deploy](../deploy/SKILL.md); the disposable prototype method does not authorize experiments on real users.

**Done:** Deliver the product brief or outcome assessment: user problem, evidence, options, success measures, recommendation and decisions needed. If saving a standalone brief without a designated destination, use `.work/briefs/` under the [workspace rules](../../references/Workspace.md). Use [Plan](../plan/SKILL.md) to sequence agreed work when requested; use [Brief](../brief/SKILL.md) for instructions to transfer work to another worker.
