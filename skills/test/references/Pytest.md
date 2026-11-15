# pytest

Confirm the project interpreter, virtual environment, config, test collection roots, plugins and how the target package is imported. Check a packaging fix against the installed package when that is what users run.

- Prefer small fixtures with explicit dependencies, scoped to the resource lifetime. Separate state-changing setup so teardown runs for completed steps even if later setup fails. Use temporary paths, local data, and scoped monkeypatching so a failure or parallel run does not corrupt other cases.
- Parametrize meaningful inputs with readable IDs. Set expected values from the contract, not by recalculating them with the code under test. Use specific expected exceptions and assert relevant outcomes. A skip or expected failure is not a pass for the behavior.
- Use the narrow node ID or a focused selector through the project runner. Confirm which tests actually collected, then run the wider related set if the change affects shared fixtures, import layout or a plugin. Prefer a real database, filesystem or HTTP boundary when a fake would miss the contract.
- Inspect slow tests with duration reports before changing scope or parallelism. Separate setup, call and teardown; widen fixture scope only when isolation allows it. Use parallel execution only when already supported or authorized and test data, fixtures, and external resources can safely be independent.

Record interpreter, command, selected case, data and outcome. For a regression, show the same check failed for the intended reason against the baseline and passed after the fix, or name the evidence that is unavailable.

Upstream: [Good integration practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html), [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [Invocation and duration reports](https://docs.pytest.org/en/stable/how-to/usage.html).
