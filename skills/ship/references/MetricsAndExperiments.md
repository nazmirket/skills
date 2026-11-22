# Product metrics and experiments

Choose evidence that reflects the value users received. Define event semantics, unit of analysis, eligible population, time window, exclusion rules and baseline. Connect inputs the team can influence to outcomes that matter; use a guardrail for foreseeable harm such as slower tasks, support burden or more failed attempts.

- Pick a method for the uncertainty. A prototype can reveal comprehension or friction. A staged cohort can expose readiness issues. A randomized comparison can estimate a causal effect when assignment and measurement are valid. A before/after trend alone leaves seasonality, selection and concurrent changes unresolved.
- Set the hypothesis, primary measure, minimum meaningful effect, analysis window, assignment unit, sample or stopping rule and guardrails before exposure. Check instrumentation and assignment from end to end. If users influence each other, consider the right group boundary rather than treating sessions as independent.
- Check unexpected assignment ratios, crossover, delayed outcomes, missing events and inconsistent exposures before interpreting results. Report absolute rates, difference, uncertainty and guardrails; label exploratory subgroup findings. Do not quietly switch metrics or extend the window until a result looks favorable.
- Recommend whether to continue, widen, change, stop, or gather a specific missing signal. Distinguish a small effect from an inconclusive estimate. Mark what the evidence cannot generalize to.

In a randomized trial, preserve the assigned groups for the primary comparison. If only people who finished setup appear in the event stream, check whether the variant changed who reached setup before interpreting completion rates. Define how to handle delayed events, repeated attempts and clustering at the assignment unit.

For example, 40 of 200 assigned teams complete setup in control and 50 of 200 in the variant. That is 20% versus 25%, a five percentage point difference and 25% relative lift. Estimate uncertainty at the team level and compare its range with the pre-agreed minimum useful lift and harm limits. If the data remain compatible with both harm and useful benefit, report an inconclusive decision and the next evidence worth its cost.

Give the recommendation to the product decision-maker. For channel attribution and campaign performance, use [Marketing measurement](../../market/references/Measurement.md).
