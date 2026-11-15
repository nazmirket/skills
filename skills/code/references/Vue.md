# Vue

Confirm the Vue major, loader and state conventions; Vue 2, Vue 3 and Nuxt do not share every feature. Prefer the project's established Options or Composition API style.

- Keep props as inputs and use events or the agreed binding for writes. Keep local state local. Use computed values for derivation; reserve watchers for effects and clean up subscriptions or asynchronous work when inputs or ownership change.
- Use refs or reactive objects deliberately. Replacing a reactive object or destructuring a reactive primitive without an appropriate binding can break tracking; compiler handling of destructured props is version-sensitive. Preserve stable keys in lists that can reorder or retain input state.
- Extract a composable when behavior needs reuse or ownership is clearer. Document reactive inputs and cleanup. Avoid module-level request state under SSR. Use a store for genuinely shared state, not every form field.
- Keep template behavior legible and use native semantics for controls. Verify pending and rejected state and unmount or route changes when asynchronous work is involved.

## Keep reactivity understandable

- Pass reactive inputs to a composable in a form the composable can track. Keep input changes and side effects traceable; handle stale responses after a route or prop change. Choose flush timing only when work depends on updated DOM.
- Keep props stable for large lists; computing a per-item boolean at the parent can narrow updates when that boolean is the only value a child needs. For expensive trees or large immutable data, profile before using virtualization or shallow reactivity. Check memory as well as update speed.
- Test through emitted events, rendered state, and user input. Test composable logic directly when it contains independent rules; use a mounted component when the behavior depends on reactivity or disposal.

Check the installed template/type checker and reproduce an actual prop change or user interaction; if server rendering is used, check hydration and isolation between requests.

Official: [Reactivity fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html), [Composables](https://vuejs.org/guide/reusability/composables.html), [Performance](https://vuejs.org/guide/best-practices/performance.html).
