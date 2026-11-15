# C#

Confirm the SDK, target frameworks, C# version, nullable settings and host. Follow the existing project conventions; language features can be newer than the deployed runtime or downstream build.

- Keep nullability intent visible. Validate results at external boundaries and annotate interfaces accurately; the null suppression operator does not check a value. Use records and value types when their equality, copying or default behavior suits the domain.
- Await I/O rather than synchronously blocking on tasks. Propagate cancellation tokens across the work that can honor them. Avoid async void outside the appropriate event handlers. Treat cancellation separately from failure when the caller needs to distinguish them.
- Dispose owned resources using the project's supported synchronous or async pattern. Respect dependency injection lifetimes; a singleton should not casually retain request-scoped services. Keep expensive work out of lazy enumeration if ownership or replay would be surprising.
- Consider execution provider behavior when using LINQ. A query executed remotely and a sequence in memory differ in translation, timing and failure; measure against the real provider instead of assuming equivalence.

Build against configured targets. Test cancellation, disposal and relevant null or invalid input; when data access changes, verify translation or behavior on the intended provider.

Official: [C# coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions), [Asynchronous programming](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/).
