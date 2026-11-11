---
name: equip
description: "Use to choose or obtain tools, or to challenge a tool, library, format, data representation, abstraction, or workflow that cannot meet the job's requirements or works but fits poorly. Weigh the benefit of changing against the cost of switching."
---

# Equip

A choice can work today and still be a poor fit for the job. Call that out when it materially affects correctness, reliability, effort, performance, or control over the result. Critique the choice and its consequences. See [fit scenarios](references/FitScenarios.md) for examples of when to challenge, adjust, switch, or keep a choice, and the [routing guide](../../references/Routing.md) when a request also involves research, setup, or a system boundary.

## Establish fit

1. **Name the job and its requirements.** Identify the outcome, the inputs and consumers, and what would prove success. Distinguish hard requirements such as data fidelity, interoperability, permissions, or a mandated tool from preferences. Reuse [Adapt](../adapt/SKILL.md) findings. When no tool has been chosen, define the needed capability before naming products.
2. **Examine what actually happens.** Inspect the method, tools, inputs, outputs, handoffs, and representative cases. Look for costs a successful run can hide: silent rounding or data loss, unnecessary conversions, repeated manual work, resource use, dependence on internals, or difficult recovery. Point to where the cost or risk arises and what it means for the result. If you notice a material mismatch during another task, raise it when it can still change the outcome, even if nobody asked for a tool review. A minor preference does not warrant interrupting the work.
3. **Distinguish fit from readiness and failure.** A capable tool may need a different configuration or method. Use [Preflight](../preflight/SKILL.md) if a suitable choice is unavailable or misconfigured in the target environment, and [Debug](../debug/SKILL.md) if it unexpectedly fails. If the fit is uncertain, run the smallest authorized check that could change the recommendation, or state what you would check. A screenshot can establish appearance; verifying keyboard interaction requires exercising it.

## Compare staying and changing

4. **Start with the least disruptive viable change.** Compare keeping the current choice, adjusting it, and adopting a better fit where warranted. Check for capabilities already available in the project before introducing a dependency. Exclude options that cannot meet hard requirements; if the current approach misses one, state what cannot be relied on and propose a correction or staged transition. Use [Curate](../curate/SKILL.md) for sourced comparisons of outside options, and [Architect](../architect/SKILL.md) when the choice changes a system boundary.
5. **Weigh the gain against the full cost.** Compare the ongoing cost or risk of staying with the expected benefit of switching. Include setup, conversion, compatibility, retraining, rollout, rollback, and ongoing ownership where they matter. Compare options on the same workload and constraints over the period the choice is expected to serve. Use [Test](../test/SKILL.md) for comparable checks and performance measurements; label unmeasured benefits as expectations. Recommend keeping or adjusting a working choice when switching would deliver too little. If a small pilot could settle the decision, state what result would justify changing.

## Recommend and equip

6. **Make the recommendation concrete.** State the choice you assessed, the evidence, its practical consequence, and the next step: keep, adjust, pilot, or switch. Respect a tool the human explicitly requires; explain any material limitation and let them decide whether to relax the requirement. Ask before materially changing tooling or workflow, incurring material cost, expanding access or data sharing, or changing the intended outcome, unless that action is already specifically authorized. Continue independent work while a decision is pending.
7. **Guide acquisition and verify readiness when needed.** Identify the supported way to obtain or enable the capability, its version and prerequisites, where it will run, and what will change. Use Preflight to check the target environment. Get specific agreement before using a substitute that is inferior or whose suitability is uncertain. If setup is authorized, carry it through and verify it on a representative task. If the human is doing setup, give them the concrete steps and expected result. Distinguish installed from proven usable.

**Done:** The human knows whether the choice fits, the evidence and tradeoff behind your recommendation, and what to do next. If you set up a tool, report the check that showed it works for the job and any remaining limits.
