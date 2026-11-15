# Nuxt

Confirm the Nuxt major, Nitro target, rendering mode, route rules and generated directory conventions. Separate shared app code, browser-only work, and server routes.

- Use SSR-aware fetching for page data that needs to survive hydration. Choose the existing convention around `useFetch` or `useAsyncData`; give intentional shared data a stable key and keep the handler free of unrelated side effects. Use `$fetch` for imperative actions where a framework payload transfer is unnecessary.
- Keep private runtime configuration and privileged work on the server. Serialize only values safe for the browser. Treat server endpoints as independent boundaries for validation, authentication and authorization.
- Pick rendering and cache behavior by route: static generation, request time or client rendering should follow content freshness, private state and deployment support. Check build-time versus runtime config and avoid global state leaking across requests.
- Reuse middleware and error conventions; avoid duplicating the same check at several navigation layers. Exercise direct navigation, client navigation, one hydration case, and the relevant failure state.

Inspect the actual build target and output for the affected route. Verify the installed version's fetching and rendering defaults before applying current examples.

Official: [Data fetching](https://nuxt.com/docs/4.x/getting-started/data-fetching), [Rendering modes](https://nuxt.com/docs/4.x/guide/concepts/rendering).
