# Engineering practices

Apply these principles where the change touches the relevant contract, boundary or state. When they pull in different directions, use the current requirement and a concrete caller or failure case to decide.

## Start at the contract

- **Principle of least surprise.** Trace a caller and an existing test where available. Preserve established defaults, output, errors, ordering and side effects unless the task changes them. Match neighboring APIs when adding a new entry point.
- Parse or validate external data where it enters. Use established types and invariants inside that boundary. Distinguish missing, invalid, and failed when callers act differently. Keep meaningful error details without exposing sensitive data.
- Where work can fail partway, make the owner of cleanup, cancellation, retry, and limits explicit. Retry only when the operation can safely replay or the contract provides deduplication.

## Keep the design proportional

- **KISS and YAGNI.** Implement the simplest design that satisfies today's contract. Require a present use for a new layer, dependency or extension point.
- **Clean Code.** Name functions for the behavior callers can expect. Keep control flow, ownership and side effects easy to trace. Use comments for constraints the code cannot express.
- **DRY.** Give a shared rule one owner when every caller must change together. Keep similar expressions local when they represent independent rules.
- **Separation of concerns.** Group code by what changes together. For separation of mechanism and policy, put the decision in one place and pass its result to the operation that carries it out. A retry rule can decide whether to retry while the transport sends the request.
- **SOLID.** Apply the single responsibility principle (SRP) by giving a module one reason to change. When behavior already varies, extend it at a stable boundary (open/closed), preserve the caller's contract across implementations (Liskov substitution) and expose only the operations each client needs (interface segregation). Apply the dependency inversion principle (DIP) where policy depends on infrastructure by defining the needed operation in policy terms and supplying its implementation at the boundary. A function parameter can suffice.
- **Design patterns.** Match a pattern to an observed problem. An adapter translates provider formats at entry. A strategy handles interchangeable behavior. Explicit states prevent illegal transitions. Keep a direct implementation when it expresses the rule more clearly.

## Protect transactional state

For a persistent change, identify the invariant and what the caller may rely on after success or failure. Apply **ACID** at the transaction boundary. Use atomicity for all-or-nothing writes, enforce consistency with constraints and application rules, choose isolation that preserves the invariant under competing operations and check the store's durability guarantee before acknowledging success. For example, a transfer must preserve the combined balance if the second write fails or another transfer overlaps. For effects outside the transaction, specify how retries or recovery avoid losing or duplicating the effect.

## Verify the change and its cost

- Trace the changed path in the diff. Resolve unjustified complexity, duplicated rules and contract surprises before handback. Verify behavior at the narrowest meaningful boundary. Use a deterministic check for a rule, a real integration for storage or framework semantics and a user journey when the contract spans boundaries. Exercise a relevant adverse case, such as an interrupted transaction or two competing writers.
- Bound work where it grows: input size, concurrency, round trips, copies, and retained memory. Fix the dominant cost first. Batching trades memory and latency for fewer calls; caching trades freshness and invalidation for repeated work; streaming trades simpler code for bounded memory. Keep the tradeoff visible at the owning boundary.
- Measure before claiming a performance gain. Compare representative inputs, release or production-like builds, and warm/cold conditions as relevant; keep result semantics constant. Report what changed in latency, throughput, resource use, or query count, and use [the measurement method](../../execute/references/MeasuredImprovement.md) when the request requires a formal comparison.
