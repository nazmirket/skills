# Browser inspection

Use to see the actual rendered web target or exercise a short path with available browser controls. Use the project's preview or an authorized environment. If starting it needs setup, use [Preflight](../../../preflight/SKILL.md); an inaccessible runtime does not turn a capture into a live baseline.

1. Confirm the route or target and its build, and select the representative input, content, viewport, zoom, theme or preference the check needs. Use a safe fixture or session. Avoid real submissions or other state changes the task did not authorize.
2. Wait for the relevant content to be ready, inspect what appears, then exercise the scoped action and observe its result. Recheck the page state after navigation or a major transition. When an issue calls for it, inspect computed layout, focus, console or network evidence to narrow the cause.
3. Record the environment, route, conditions, steps and actual outcome. Capture a visual state only when it helps someone assess the claim. If using [device emulation](https://developer.chrome.com/docs/devtools/device-mode/), name what was simulated; that does not prove behavior on the physical device.

Use another authorized browser if it can answer the same question. Use [Playwright](Playwright.md) if the interaction needs repeatable evidence. If only source or a supplied capture is available, report the limited observation and leave live behavior unverified.
