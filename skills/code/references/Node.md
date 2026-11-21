# Node.js

Confirm the Node major, package manager and module boundary (ESM or CommonJS), production process model, and configured test runner. Keep package and runtime expectations aligned.

- Keep request work bounded. Avoid synchronous filesystem or heavy CPU work in hot paths, and constrain user-driven parsing, large allocations and concurrent work. Separate CPU-heavy processing only when measures or risk justify it.
- Use stream pipeline or the project's supported streaming abstraction to manage backpressure, failures and cleanup. Handle aborted clients and propagate deadlines across I/O. Bound retries and decide whether the operation can safely repeat.
- Choose a single path for propagating failures and cancellation. Distinguish operational errors from programmer errors; do not swallow a rejection or report success after partial work. Close servers, pools and timers on a controlled shutdown with a bounded wait.
- Review module and package boundaries before changing imports or exports. Test the same startup and build entry points that production uses. Keep credentials in runtime configuration and exclude sensitive details from logs and error responses.

Verify a success, timeout or cancellation, and one prerequisite failure. For performance, measure representative concurrency and event-loop responsiveness rather than relying on a microbenchmark alone.
