# Jest

Identify Jest version, project, test environment, transforms, setup files, and ESM or CommonJS mode. Reuse the repository’s scripts and config. For a mismatch, check what Jest actually loads rather than assuming it behaves like the production bundler.

- Assert what a caller can observe: values, errors, visible state, or a consequential effect. Avoid snapshots or mock call counts that only encode implementation details. Mock a specific boundary, and exercise the real dependency separately when it defines the behavior being verified.
- Match setup and teardown to the resource lifetime. Avoid mutating shared state during test declaration. Distinguish clearing mock call history, resetting implementations, and restoring spies or replaced properties. Check the installed mocking behavior for the module format; a static ESM import may evaluate before the mock is registered.
- Await returned work or use the runner’s callback contract, not both. When testing timers, advance the time the contract actually uses, await resulting asynchronous work, and restore real timers afterward. A test that completes before its assertion is not evidence.
- When a run hangs, look for servers, intervals and other resources left open. Use focused diagnostics when needed; do not force exit to silence a leaked handle. Measure transforms, startup and suite duration before changing workers or caches. Do not compare diagnostic mode directly with a normal run.

Run the smallest matching test or file, then the affected suite when config, setup or shared behavior changed. Record environment, exact command, initial failure, and post-fix outcome.

Upstream: [Setup and teardown](https://jestjs.io/docs/setup-teardown), [Mock functions](https://jestjs.io/docs/mock-function-api), [Timer mocks](https://jestjs.io/docs/timer-mocks), [CLI options](https://jestjs.io/docs/cli).
