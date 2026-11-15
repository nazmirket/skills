# React

Confirm the React version and renderer, SSR or hydration setup, and existing state and data conventions. Use the framework guide when it owns fetching, caching or routing.

- Build components around clear data ownership. Keep the smallest state needed; calculate filtered or formatted values during render when possible. Move state to the nearest common owner when siblings must agree. Use a stable domain key for item identity; do not use a changing index for reorderable rows.
- Keep render pure. Put actions caused by a click or submission in handlers. Use effects to synchronize with an external system; pair subscriptions or imperative widgets with cleanup and handle stale responses. Do not use an effect to mirror props or create a loop between state variables.
- Handle pending, empty, and error states close to the surface that can explain or recover from them. Respect the host's hydration contract: the first client render should agree with server output. Move browser-only reads to a suitable client boundary.
- Measure a slow interaction before adding memoization. Prefer removing unnecessary work, narrowing state ownership, or reducing rerender scope where a profile supports it. Check compiler and framework settings before prescribing a blanket memo pattern.

Verify a real transition, reordered list or changed props as applicable; inspect console hydration warnings when supported. Exercise behavior through accessible controls using the existing test stack.

Official: [Thinking in React](https://react.dev/learn/thinking-in-react), [When an effect is useful](https://react.dev/learn/you-might-not-need-an-effect).
