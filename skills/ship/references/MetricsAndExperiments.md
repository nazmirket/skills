# Product metrics and experiments

Choose evidence that reflects the value users received. Define event semantics, unit of analysis, eligible population, time window, exclusion rules and baseline. Connect inputs the team can influence to outcomes that matter; use a guardrail for foreseeable harm such as slower tasks, support burden or more failed attempts.

- Pick a method for the uncertainty. A prototype can reveal comprehension or friction. A staged cohort can expose readiness issues. A randomized comparison can estimate a causal effect when assignment and measurement are valid. A before/after trend alone leaves seasonality, selection and concurrent changes unresolved.
- Set the hypothesis, primary measure, minimum meaningful effect, analysis window, assignment unit, sample or stopping rule and guardrails before exposure. Check instrumentation and assignment from end to end. If users influence each other, consider the right group boundary rather than treating sessions as independent.
- Check unexpected assignment ratios, crossover, delayed outcomes, missing events and inconsistent exposures before interpreting results. Report absolute rates, difference, uncertainty and guardrails; label exploratory subgroup findings. Do not quietly switch metrics or extend the window until a result looks favorable.
- Convert results to a decision: continue, widen, change, stop, or gather a specific missing signal. Distinguish a small effect from an inconclusive estimate. Mark what the evidence cannot generalize to.

Use Market for channel attribution and campaign performance while retaining the product outcome here.

Influence: [PM Skills analytics and experiment analysis](https://github.com/phuryn/pm-skills/tree/9af7bfd0bc47fdad43c2eaa7a43cd13918e7aaef/pm-data-analytics/skills).
