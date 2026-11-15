# Python

Read the project metadata, supported interpreter versions, lock or constraints files, and existing types, formatter and test runner. Distinguish application runtime from the tool environment.

- Keep interfaces readable and side effects visible. Use context managers for owned resources. Use a mutable default only when shared state is deliberate; otherwise initialize per call. Use dataclasses or structured types when they clarify data ownership, not to replace every small mapping.
- Catch the narrow errors the caller can recover from, and keep the operation inside the try block small enough to identify its source. Add useful context and preserve exception chains. Do not broadly suppress errors or mistake a sentinel for a valid value.
- Type hints clarify an interface and support checks; parse and validate external data at its boundary. Avoid a project-wide type rewrite because a local change touches old code.
- Match concurrency to the work and deployed runtime. Keep blocking calls out of event-loop paths, make cancellation and resource cleanup visible, and prefer simple synchronous code if no overlapping work is required.

Run the configured tests and type checks in the project environment. Exercise one malformed input or prerequisite failure and ensure packaging or module imports work through the intended entry point if those changed.

Official: [PEP 8](https://peps.python.org/pep-0008/) (follow project conventions when they differ), [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html).
