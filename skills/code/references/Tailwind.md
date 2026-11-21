# Tailwind CSS

Confirm the installed major, the build adapter, the source files it scans, and the existing tokens and component conventions. Advice about v4 CSS configuration does not automatically apply to v3 projects. Use [CSS](CSS.md) for cascade, layout, or rendering behavior.

- Use named design tokens for repeated color, type, spacing, and breakpoints. Keep one-off values local if there is no design relationship. Extract a component when markup and behavior are reused; short repeated class lists can be cheaper to read than a new abstraction.
- Map supported variants to complete class strings the compiler can find. Building a class from arbitrary string fragments can look correct in source and disappear in the built CSS. For an actual runtime value, pass a validated value through a CSS variable or style property and keep the utility class static.
- Keep variants near the condition they express. Prefer selectors for responsive layout, focus, or disabled state rather than recreating browser state in JavaScript. Include reduced motion or color-scheme behavior where relevant. Use existing project tools for class ordering and class merging.
- When styles conflict, inspect the computed declaration and cascade layers. Class order in markup does not generally establish the winning utility. Check Preflight or other resets when a native control or third-party widget changes.

Build the production CSS and verify affected states in the browser, especially classes originating in a workspace package or variant map. Check missing utilities, disabled and focus states, and the relevant breakpoints. Inspect compiled CSS size if adding sources or broad variants.
