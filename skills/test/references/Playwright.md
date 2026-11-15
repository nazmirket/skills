# Playwright Test

Identify the project, browser and server config, and whether the run uses a local dev server or the built app. Use the project’s real runner command. Choose a journey that exercises the boundary under test.

- Interact through roles, labels or agreed test IDs. Prefer locator assertions such as `toHaveText` that retry on current DOM state. Keep the action and its observable result distinct; use an exact request or state transition only when it matters to the contract. Avoid sleeps and selectors coupled to layout or implementation.
- Use isolated browser contexts and independent data. Reuse authenticated storage state only when role, expiry, and server-side state allow it; use separate test users for writes that could collide. Don’t commit or share auth state. Use a real service for the integration being verified, and route an external dependency only when its behavior is outside the claim or when deliberately exercising a particular failure.
- Start with the matching test and project, then run the required browsers or configurations. Don’t treat a test recovered by retry as a clean pass; keep the initial failure and compare trace, console and network evidence.
- Save a trace for the useful failure or retry, not by default for every successful CI run. Measure test time and setup separately. Adjust workers or shard only after fixture isolation and shared backend capacity are understood.

Report browser and project, build, test case and data, and whether services were real or stubbed. Sanitize traces and logs before sharing. For visual review or full-page screenshots, use the [Design Playwright guide](../../design/references/tools/Playwright.md).

Upstream: [Best practices](https://playwright.dev/docs/best-practices), [Authentication](https://playwright.dev/docs/auth), [Retries](https://playwright.dev/docs/test-retries), [Trace Viewer](https://playwright.dev/docs/trace-viewer).
