# Browser inspection

Use a direct browser to inspect a real render or exercise a short path. Use [Playwright](Playwright.md) when the path needs to be replayed. For every critique or visual check, use the [full-resolution capture standard](Screenshot.md).

1. Open the actual route or component fixture in an authorized environment. Identify build, data and state. Set the layout viewport and zoom separately from native capture density. Match theme, locale, motion and input to the use case. Use a fresh session or safe fixture for actions that change state.
2. Inspect the initial render and accessible controls. Wait for the state the user depends on. Reacquire controls after navigation, rerender or an opened dialog. Exercise the affected path through completion or recovery, including keyboard-only use where relevant. Observe focus, feedback and data persistence after each meaningful action.
3. For a visual finding, inspect the element and its context. For overflow, compare scroll width to client width and locate the first offending child. For unreadable text, inspect its rendered font and foreground against the actual background. For a blocked action, check hit targets, overlays, computed states or failed resources. Test near the content's breaking width, not just preset phone and desktop labels.
4. Capture the complete settled surface in high resolution. Use native full-page capture at the actual device scale and inspect the saved original. If these controls cannot produce verifiable full coverage, use an equivalent permitted renderer or mark visual acceptance incomplete. A viewport grab remains useful for sticky, focus and overlay states alongside the full original.
5. Return the actual steps, expected and observed result, evidence paths and environments covered. Identify what device emulation simulated. For a physical keyboard, touch, safe-area, assistive technology or performance claim that depends on the device, use that environment or state the gap.

## Capture without a test runner

In Chromium DevTools, open the device toolbar, choose the responsive dimensions and select the device type appropriate for the task. Under its options, enable the device pixel ratio control and set it to 2 or higher. Check the actual value with `window.devicePixelRatio`. Once the page is ready, use the toolbar’s full-size screenshot command. Save the downloaded PNG, check both dimensions against the measured document and inspect the footer and any deferred sections. Use the equivalent full-page export in another browser when it meets the same requirements.
