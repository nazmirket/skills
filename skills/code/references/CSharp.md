# C#

Confirm the SDK, target frameworks, C# version, nullable settings and host. Follow the existing project conventions; language features can be newer than the deployed runtime or downstream build.

- Keep nullability intent visible. Validate results at external boundaries and annotate interfaces accurately; the null suppression operator does not check a value. Use records and value types when their equality, copying or default behavior suits the domain.
- Await I/O rather than synchronously blocking on tasks. Propagate cancellation tokens across the work that can honor them. Avoid async void outside the appropriate event handlers. Treat cancellation separately from failure when the caller needs to distinguish them.
- Dispose owned resources using the project's supported synchronous or async pattern. Respect dependency injection lifetimes; a singleton should not casually retain request-scoped services. Keep expensive work out of lazy enumeration if ownership or replay would be surprising.
- Consider execution provider behavior when using LINQ. A query executed remotely and a sequence in memory differ in translation, timing and failure; measure against the real provider instead of assuming equivalence.

## Choose boundaries that hold under load

- Put a pure business rule in a directly testable method or type. Use dependency injection for real runtime boundaries and align the scope with who disposes resources. Access data through its intended provider when the contract includes translated LINQ, cancellation, or transactions.
- Check accidental repeated enumeration, unnecessary buffering, long-lived references, and synchronous waits when measuring a slow path. Avoid changing to span-based or pooled buffers before profiling allocation and defining the lifetime clearly.
- Exercise a realistic async path for latency and cancellation; verify a retry or parallel operation does not duplicate effects. Compare allocation, GC and throughput under representative load where a resource optimization motivated the change.

Build against configured targets. Test cancellation, disposal and relevant null or invalid input; when data access changes, verify translation or behavior on the intended provider.
