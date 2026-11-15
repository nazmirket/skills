# Test runner guides

Identify the runner, installed version, and project command from the lockfile, config and CI. Open only the guide for the check you’re running. Use the repository’s existing harness and choose the smallest check that can disprove the expected behavior. An existing check that already answers the question does not require another guide.

| Existing harness | Guide |
| --- | --- |
| Playwright Test: browser journeys, isolation, and failure traces | [Playwright](Playwright.md) |
| Cypress: end-to-end or component tests, retryable assertions, and controlled network cases | [Cypress](Cypress.md) |
| Vitest: JavaScript or TypeScript tests with the project’s module graph and environment | [Vitest](Vitest.md) |
| Jest: JavaScript or TypeScript tests with Jest’s transforms, mocks, and environments | [Jest](Jest.md) |
| pytest: Python tests, fixtures, and integration boundaries | [pytest](Pytest.md) |

When several runners coexist, choose by the behavior and boundary, not by language or file name alone. Use a browser runner for real browser behavior, a local test for deterministic logic, and a real integration check when the contract depends on a database, filesystem or framework. Do not introduce a second runner to cover a routine case. Use [Design’s Playwright guide](../../design/references/tools/Playwright.md) for visual evidence rather than test authoring or runner behavior.
