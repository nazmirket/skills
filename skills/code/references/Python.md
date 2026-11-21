# Python

Read the project metadata, supported interpreter versions, lock or constraints files, and existing types, formatter and test runner. Distinguish application runtime from the tool environment.

- Keep interfaces readable and side effects visible. Use context managers for owned resources. Use a mutable default only when shared state is deliberate; otherwise initialize per call. Use dataclasses or structured types when they clarify data ownership, not to replace every small mapping.
- Catch the narrow errors the caller can recover from, and keep the operation inside the try block small enough to identify its source. Add useful context and preserve exception chains. Do not broadly suppress errors or mistake a sentinel for a valid value.
- Type hints clarify an interface and support checks; parse and validate external data at its boundary. Avoid a project-wide type rewrite because a local change touches old code.
- Match concurrency to the work and deployed runtime. Keep blocking calls out of event-loop paths, make cancellation and resource cleanup visible, and prefer simple synchronous code if no overlapping work is required.

## Keep I/O and cost visible

- Put filesystem, network, time, and database access at the boundary of the feature. Pass real values into deterministic rules; keep import-time work small so tests and tools can import a module safely. Use a fixture or real adapter when the contract depends on its behavior.
- Prefer iteration or bounded batches when input can grow. Generators are single-pass and can delay exceptions or hold open resources, so document the lifetimes a caller depends on. Check algorithmic cost, repeated parsing, and database or network round trips before tuning syntax.
- Use the installed runtime's supported task and cancellation constructs; test a failed task and cleanup under a timeout. For speed or memory work, profile representative data and record whether the bottleneck is Python CPU, allocation, or blocking I/O before choosing concurrency.

Run the configured tests and type checks in the project environment. Exercise one malformed input or prerequisite failure and ensure packaging or module imports work through the intended entry point if those changed.
