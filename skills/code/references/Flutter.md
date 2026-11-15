# Flutter

Confirm the SDK, deployment platforms, app navigation and state conventions, and any platform plugin or rendering constraints. Use [Dart](Dart.md) for language or library questions.

## State and lifecycle

- Keep transient UI state near its widget. Move state to the nearest shared owner when screens or widgets need the same transition. Introduce a separate view model, controller, or repository when it owns a real policy or boundary and fits the app. Keep domain decisions and storage or platform access outside widget build methods.
- Make loading, content, empty and failure states observable. Preserve stable identity for reorderable or stateful items, and give owned controllers and subscriptions a disposal path. Check `mounted` or arrange ownership before using a context after asynchronous work. Ignore superseded results when a newer request owns the displayed state.
- Build should describe current UI. Keep expensive computations and irreversible actions out of rebuilds. Check whether a state change can rebuild a narrower subtree, and use lazy list builders for large lists. Reuse existing layout and accessibility conventions including text scaling, focus, and safe areas.

## Inspect real frame cost

Profile on representative devices in profile mode where supported. Use DevTools to separate widget build, layout, painting and raster work. Inspect decoded image size, repeated layouts and scroll behavior before adding caching or paint boundaries. Verify that an improvement holds with realistic content and does not retain excessive memory.

Use unit tests for deterministic decisions, widget tests for rendering and interaction, and a device integration check for navigation, plugin or platform behavior. Exercise one meaningful lifecycle case, such as leaving a page while its request is pending.

Upstream: [Architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations), [Performance best practices](https://docs.flutter.dev/perf/best-practices), [Flutter testing](https://docs.flutter.dev/testing/overview).
