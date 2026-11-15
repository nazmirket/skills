# Rust

Check the crate's edition, minimum supported Rust version, feature flags and target. Follow its existing error and async conventions.

- Make ownership visible. Borrow when the caller retains ownership and transfer it when the callee truly needs it. Use simple concrete types first. A clone can be right when it simplifies a real lifetime boundary; account for cost before using clones to bypass design questions.
- Use enums for state alternatives, `Option` for expected absence, and `Result` for recoverable failure. Preserve error context at useful boundaries. Panics are for broken invariants or deliberately terminal situations, not ordinary unsupported input or unavailable resources.
- Review async ownership and cancel safety separately from thread safety. Keep critical sections short and avoid holding a synchronous lock across an await. Bound concurrent work and align shutdown with the owning task or service.
- Keep unsafe or FFI scope small. Document the invariant each caller must uphold, ownership across the boundary, and target or ABI assumptions. Prefer an existing safe wrapper when it fits.

## Keep abstractions close to their contracts

- Choose a trait when callers need substitutable behavior or a real generic relationship; begin with a concrete type for one implementation. Expose only the error variants or ownership behavior clients should build on. Check feature combinations and downstream callers for a public API change.
- For streaming and shared resources, reason about the value kept across each await and what dropping a pending operation leaves incomplete. Keep locks local and avoid unbounded channels or collecting an entire stream unless size and lifetime are known.
- Profile a release build with representative payloads before replacing comfortable ownership with complex lifetimes or introducing unsafe code. Look for copies of large buffers, repeated reallocation, and synchronization cost. If an unsafe boundary changes, exercise its invariants with the project's available checkers.

Run the repository's formatter, lints and tests on relevant targets and feature sets. Check errors, cancellation, and invariant boundaries that changed; distinguish compiler acceptance from runtime safety or latency evidence.

Official: [Ownership in the Rust Book](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/), [Clippy](https://doc.rust-lang.org/clippy/).
