# Kotlin

Check Kotlin and library versions, toolchain targets, framework conventions, and whether code is shared across platforms. Read Java interoperability or platform assumptions before treating nullable types as guarantees.

- Prefer clear data and state models. Use nullable types for real absence, safe access or boundary validation to narrow them, and sealed types when variants are finite and relevant. Avoid assertions that only defer failures. A data class copy is shallow.
- Use idiomatic operators and scope functions when ownership and the result remain obvious. Favor a named intermediate over nested scope calls that obscure what is changed. Use read-only collection types intentionally; they are not necessarily immutable snapshots.
- Give coroutines a scope with the correct lifetime. Choose dispatchers based on work and platform, make cancellation and failure propagation explicit, and do not swallow cancellation in broad exception handling. Choose Flow when the contract needs a stream, not for every asynchronous value.
- At platform or Java boundaries, validate platform types and document ownership, scheduling and thread expectations. Keep common code free of platform-only dependencies unless an explicit bridge is intended.

## Keep context and state predictable

- Keep scope ownership at the caller with the relevant lifecycle, and make a suspend function safe to call from its intended context. Avoid using an application-wide scope to fix a local lifetime problem. Decide whether a stream is cold or shared and what happens to emissions when collection stops.
- Prefer ordinary collection operations or explicit loops where they make intent clear. A sequence can avoid intermediate collections for large pipelines, but laziness can repeat work or add overhead over small collections. Measure allocation or UI frame time where the choice matters.
- Test coroutine behavior with the project's scheduler and test dispatcher where appropriate. Cover cancellation, repeated collection or stale emissions. Include a real platform-facing check when dispatch, lifecycle, or Java interoperability matters.

Run configured Gradle or platform checks and test nullable inputs, cancellation and the actual caller or UI lifecycle. Check generated Java or native-facing signatures if they form an API.

Official: [Kotlin conventions](https://kotlinlang.org/docs/coding-conventions.html), [Coroutine basics](https://kotlinlang.org/docs/coroutines-basics.html), [Coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html).
