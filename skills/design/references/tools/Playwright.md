# Playwright

Use when the check benefits from repeating a browser action or capturing a reproducible failure. Start with the project's existing tests, settings and fixtures, or an available Playwright interface. A direct [browser check](Browser.md) may be enough for a one-off inspection. If Playwright is absent, use that equivalent when it answers the question or report the coverage gap; setup belongs to [Preflight](../../../preflight/SKILL.md).

1. Pin the target, build, browser and viewport. Use an isolated context and known data; reuse authenticated state only when authorized and keep it out of shareable evidence.
2. Navigate to the real entry point. Locate controls by their user-facing role, name or label, or use a deliberate test identifier when necessary. If the interface returns snapshot identifiers, reacquire them after navigation or a relevant DOM change. Avoid ambiguous position-based selectors and fixed sleeps; wait for the condition that matters.
3. Check the observable result, such as a visible error, navigation, or focus return. Reuse a suitable existing test. Capture the smallest screenshot or trace that explains the result or reproduces a failure. Check the capture before sharing it; traces may contain session or request data.
4. Return the case or steps, expected and actual behavior, settings and relevant evidence. A Chromium pass covers that run and configuration. Name engines, device conditions or assistive technology that the result did not cover when they matter.

For host-specific commands, use the project's installed runner and the official [locator](https://playwright.dev/docs/locators) and [trace](https://playwright.dev/docs/trace-viewer) guides.
