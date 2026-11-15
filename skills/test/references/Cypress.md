# Cypress

Confirm Cypress version, component or end-to-end mode, supported browser, runtime config, and whether the app starts from source or built files. Check how the suite manages accounts, test data and isolation.

- Use selectors based on user meaning or agreed `data-*` attributes. Use retryable queries and assertions for state that changes. Commands like click run once after actionability checks; the query chain and assertions retry under different rules. Re-query after a rerender when continuing from a captured element would leave a stale subject.
- Register `cy.intercept` before the app can send the request. Match the intended method and route, and wait on the alias when that request is part of the check. Assert the next visible state as well. A stub can prove a branch of the UI but does not establish the real API contract; use a deliberate real path for that.
- Seed server state explicitly. Keep tests individually runnable and avoid dependence on another test’s browser state. Reuse sessions only when scoped to the intended role and validated. Replace fixed waits with an observable condition. Keep a retry that changed the outcome visible in the report, and inspect the command log and request evidence.
- Before adding concurrency, measure setup, repeated login or seeding, and spec duration. Don’t disable isolation just to shorten the run. Reuse supported setup where it does not change the behavior being checked.

Run the failing spec in the relevant browser and mode, then the required spec set. Record app target, whether requests were real or stubbed, actual user-visible outcome, and any retry.

Upstream: [Best practices](https://docs.cypress.io/app/core-concepts/best-practices), [Retry-ability](https://docs.cypress.io/app/core-concepts/retry-ability), [Test isolation](https://docs.cypress.io/app/core-concepts/test-isolation), [Intercept](https://docs.cypress.io/api/commands/intercept).
