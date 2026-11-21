# Vue Devtools

Confirm the Vue version, application instance, Devtools mode, and whether the symptom occurs during initial SSR hydration, navigation, or a normal client update. Use a compatible extension or project integration already approved for the environment. Prefer the browser trace for network, layout, and paint questions.

- Inspect the component that owns the affected element, then trace its props, local state, computed values and emitted events. Follow writes through the actual parent or store. Compare each observed value to the expected flow; a value that never changes and a fresh value displayed incorrectly need different probes.
- For state in Pinia, compare the store and relevant action or event timing with the rendered component. With several app instances or multiple roots, check that the inspected instance owns the failing DOM. A manual Devtools state edit can isolate the view, but it does not prove how production reached that state.
- Use the timeline or installed profiler when an interaction points to mount or update work. Record the same route, data size and interaction before and after. Identify unnecessary update sources or expensive render work before changing reactive depth, state placement, or list rendering.
- If a component or timeline event is missing, check the installed Vue/Devtools versions and supported debug build. For hydration, compare server HTML and initial client state before relying on the later component tree.

Repeat the actual event or route transition on normal settings. Verify the component and user-visible output; use [Chrome DevTools](ChromeDevTools.md) to check a runtime performance claim on a representative build.
