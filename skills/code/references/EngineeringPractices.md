# Engineering practices

Use the smallest design that makes the required behavior clear, safe to change, and practical to verify. Prefer decisions visible in the code over rules the caller must memorize.

## Start at the contract

- Identify the caller, observable behavior, and constraints: input shape, errors, ordering, compatibility, and resource lifetime. Read one existing caller and test. Preserve behavior that the task did not authorize changing.
- Parse or validate external data where it enters. Use established types and invariants inside that boundary. Distinguish missing, invalid, and failed when callers act differently. Keep meaningful error details without exposing sensitive data.
- Where work can fail partway, make the owner of cleanup, cancellation, retry, and limits explicit. Retry only when the operation can safely replay or the contract provides deduplication.

## Choose a pattern for the problem

| Pressure | A useful starting point | Common mistake |
| --- | --- | --- |
| A rule spans several callers | Put the rule beside the data or operation whose invariant it protects | A general utilities module that hides ownership |
| Policy changes apart from storage, clock, or network | Keep policy in a deterministic function or module; pass in the effectful dependency at its boundary | Mocking every internal call or introducing an interface per class |
| Inputs come from two formats or vendors | Translate each input once at an adapter boundary | Propagating provider flags and raw fields through every layer |
| A workflow has real states and invalid transitions | Use a small explicit set of states and transitions | Several independent booleans, or a state-machine library for a binary choice |
| Behavior genuinely varies | Pass a function for one operation; use an interface when callers need several related operations | A hierarchy or registry for hypothetical variants |

Group things that change for the same reason. Keep private helpers private. Give modules names that describe capability and functions names that describe what callers can expect. Follow local idioms; extract duplicated code when it encodes the same rule and should change together. Prefer explicit data flow and a few meaningful layers to a chain of forwarding wrappers. Keep a new dependency, migration, or rewrite out of a local change if the existing stack can meet the contract.

## Verify the change and its cost

- Choose the narrowest check that could disprove the change. Use a small test for deterministic rules, a real integration check for behavior owned by a database, filesystem or framework, and a user journey when behavior spans those boundaries. Assert results and observable side effects. Test one meaningful adverse case when the change affects errors, cleanup, retries, or timing.
- Bound work where it grows: input size, concurrency, round trips, copies, and retained memory. Fix the dominant cost first. Batching trades memory and latency for fewer calls; caching trades freshness and invalidation for repeated work; streaming trades simpler code for bounded memory. Keep the tradeoff visible at the owning boundary.
- Measure before claiming a performance gain. Compare representative inputs, release or production-like builds, and warm/cold conditions as relevant; keep result semantics constant. Report what changed in latency, throughput, resource use, or query count, and use [the measurement method](../../execute/references/MeasuredImprovement.md) when the request requires a formal comparison.
