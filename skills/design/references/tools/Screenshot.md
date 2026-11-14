# Screenshot capture

Use to make an observed visual state reviewable. Prefer the target's own capture tool: a browser for a web viewport, the app or simulator for its own surface. Use a window, region, or desktop capture when the surrounding UI is essential or a target-native capture cannot show it. Respect host capture permissions and keep unrelated windows, private data and notifications out of the frame.

1. Reproduce the state first. Capture at the intended viewport, zoom and device scale. For comparisons, match content, state, dimensions, theme, and scroll position. If a necessary difference changes the comparison, name it.
2. Choose the smallest useful view: a region for the detail, a viewport for layout in context, or a full page for overall hierarchy. A full-page image can hide viewport-specific clipping or how fixed elements behave in use; capture the relevant viewport separately when needed.
3. Open the actual saved image and check content, crop, resolution and overlays. Record the target, revision or build, environment, viewport, state and reproduction steps. Put disposable captures in the [project scratch area](../../../../references/Workspace.md); use the requested destination for a delivered image.

If a capture is blocked, try a permitted target-native alternative or state the gap. An image establishes appearance at one state. Use runtime evidence for navigation, keyboard access, gestures, animation, or performance. For Playwright encoding and capture options, see its [screenshot guide](https://playwright.dev/docs/screenshots).
