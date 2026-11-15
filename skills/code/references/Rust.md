# Rust

Check the crate's edition, minimum supported Rust version, feature flags and target. Follow its existing error and async conventions.

- Make ownership visible. Borrow when the caller retains ownership and transfer it when the callee truly needs it. Use simple concrete types first. A clone can be right when it simplifies a real lifetime boundary; account for cost before using clones to bypass design questions.
- Use enums for state alternatives, `Option` for expected absence, and `Result` for recoverable failure. Preserve error context at useful boundaries. Panics are for broken invariants or deliberately terminal situations, not ordinary unsupported input or unavailable resources.
- Review async ownership and cancel safety separately from thread safety. Keep critical sections short and avoid holding a synchronous lock across an await. Bound concurrent work and align shutdown with the owning task or service.
- Keep unsafe or FFI scope small. Document the invariant each caller must uphold, ownership across the boundary, and target or ABI assumptions. Prefer an existing safe wrapper when it fits.

Run the repository's formatter, lints and tests on relevant targets and feature sets. Check errors, cancellation, and invariant boundaries that changed; distinguish compiler acceptance from runtime safety or latency evidence.

Official: [Ownership in the Rust Book](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/).
