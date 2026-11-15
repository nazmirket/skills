# Java

Read the JDK, target or release level, dependency platform and runtime limits. Fit existing package and build conventions. Do not assume that records, pattern matching or virtual threads are available everywhere.

- Model stable values with clear constructors, invariants and equality semantics. Use immutable or defensively copied collections when the caller should not retain mutation rights. Keep `equals` and `hashCode` consistent if adding them.
- Use generics to preserve type relationships. Avoid unchecked casts or raw types at library boundaries. Keep collection ordering explicit where consumers rely on it. Understand stream laziness and keep operations free of surprising side effects.
- Handle exceptions where context or recovery is available, and keep the cause for diagnostics. Use try-with-resources for owned resources. Restore the interrupted status when catching an interruption you cannot propagate and the contract calls for preserving it.
- Choose concurrency primitives from the target JDK and workload. Respect executor and connection pool ownership, deadlines and shutdown. Lightweight threads do not make downstream capacity unlimited.

Check the supported build and a representative runtime, including a failure and any important ordering or concurrency condition. Confirm serialization and public API compatibility if across process or library boundaries.

Sources: [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/index.html) (select the target edition), [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) as an example style, not a replacement for local conventions.
