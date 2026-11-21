# JavaScript

Confirm the actual runtime, module format, language support and transpilation target. Use the project's conventions instead of assuming the same globals or import behavior across browser, Node and other hosts.

- Keep values and ownership explicit. Prefer simple immutable data flow when it makes shared state easier to reason about; avoid mutating a caller's value by surprise. Treat falsy values and missing values separately when zero, empty text or false has a meaning.
- Keep promise chains returned or awaited so readers can follow failure propagation. Use concurrency only for independent work that can run safely together; `Promise.all` rejects without cancelling other work. Supply cancellation and a concurrency bound when necessary.
- Use module boundaries to express API and dependencies. Account for top-level side effects and initialization cycles; test actual package consumers after changing exports. Keep serialization details explicit for dates, numbers and missing fields.
- Check the observed edge cases instead of adding defensive abstractions everywhere. Avoid shared mutable async state without a clear owner. Clean up event listeners and timers using the same ownership lifetime.

## Choose data structures and async boundaries

- Use a `Map` for a dynamic collection keyed by arbitrary values and a `Set` for repeated membership queries when their semantics fit. Keep arrays for straightforward ordered data. Build an index once when repeatedly scanning the same large collection is the measured cost.
- Prefer an explicit loop when cancellation, bounded concurrency, or early exit makes it easier to read. An async `forEach` callback is not awaited by the iteration. Choose sequential work when order or rate limits matter and bound independent work when overlap helps.
- Use a real runtime profile or browser recording to locate long tasks and allocations before optimizing expression syntax. Treat numeric precision and serialization as contract issues: check large integers, dates, and missing values at the actual wire boundary.

Exercise rejection, a relevant empty or cancelled path, and concurrent completion if order matters. Run against the supported environment rather than assuming transpilation supplies missing platform APIs.
