# Measure an improvement

Use for a measurement request or an authorized improvement to latency, throughput, memory, resource use, or another measurable outcome. [Test](../skills/test/SKILL.md) owns measurements and correctness checks; the implementer owns any authorized product changes. If the problem is an unexplained slowdown, begin with [Debug](../skills/debug/SKILL.md).

1. Define the metric, target or acceptable tradeoff, representative workload, and correctness guardrails. If a consequential target is missing, ask for it. Keep load, profiling and data use within the authorized environment.
2. Establish a reproducible baseline or use a documented comparable one. Record the code revision or worktree state, workload and data size, environment, run method and relevant conditions (such as warmup, caching or concurrent load). Sample enough to distinguish a useful change from run-to-run noise.

**Measurement only:** Measure the specified target without changing the product. Compare against the requested threshold or an available comparable baseline, verify relevant correctness guardrails, and report the observed result, uncertainty and gaps. If a baseline is missing, report the observed value without claiming an improvement. Stop before the change workflow.

**Authorized improvement:** The implementer uses the baseline and continues below; Test supplies evidence for each comparison.
3. Locate the expensive work using existing instrumentation, profiling or targeted measurements. Form a hypothesis and change one material variable at a time where practical. Preserve public behavior, security and accessibility.
4. Re-run the same workload and correctness checks against the changed target. Compare distributions or repeated values where noise matters; report relevant regressions, costs and changes in conditions. If measurements are not comparable, record the gap.
5. Keep the change if it meets the agreed goal and guardrails. If it does not, report the result and undo only the experiment's own changes when safe, or bring the tradeoff to the human. Report the baseline, observed result, method, uncertainty and any incomplete check. A faster-looking run is not proof of a durable gain.
