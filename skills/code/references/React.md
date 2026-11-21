# React

Confirm the React version and renderer, SSR or hydration setup, and existing state and data conventions. Use the framework guide when it owns fetching, caching or routing.

- Build components around clear data ownership. Keep the smallest state needed; calculate filtered or formatted values during render when possible. Move state to the nearest common owner when siblings must agree. Use a stable domain key for item identity; do not use a changing index for reorderable rows.
- Keep render pure. Put actions caused by a click or submission in handlers. Use effects to synchronize with an external system; pair subscriptions or imperative widgets with cleanup and handle stale responses. Do not use an effect to mirror props or create a loop between state variables.
- Handle pending, empty, and error states close to the surface that can explain or recover from them. Respect the host's hydration contract: the first client render should agree with server output. Move browser-only reads to a suitable client boundary.
- Measure a slow interaction before adding memoization. Prefer removing unnecessary work, narrowing state ownership, or reducing rerender scope where a profile supports it. Check compiler and framework settings before prescribing a blanket memo pattern.

## Make components easier to change and measure

- Preserve ownership of controlled and uncontrolled state. Extract a custom hook for a cohesive lifecycle or repeated behavior, and return just what the consumer needs. Test visible transitions rather than calls to internal hooks.
- Use a reducer when multiple events mutate a coordinated state and the transitions need a readable place to live. Keep it deterministic. Keep broad context or shared stores for state with real cross-tree consumers; check updates against the existing selectors and memoization model.
- Use the React Profiler and a browser performance trace when rendering appears slow. Separate rerenders from DOM, network and asset work, and compare the same interaction before and after. Prefer a narrow state owner or simpler render path before introducing cache and identity concerns.

Verify a real transition, reordered list or changed props as applicable; inspect console hydration warnings when supported. Exercise behavior through accessible controls using the existing test stack.
