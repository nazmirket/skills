# JSX and TSX

Use for questions about markup, component props, emitted JSX, and authoring readable render code. Confirm which renderer owns JSX, the file extension rules, the transform, and the JSX typings. Check the bundler or TypeScript settings, including `jsx` and any `jsxImportSource`. Use [React](React.md) for React state and effects or [Vue](Vue.md) for Vue reactivity and templates.

## Markup and props

- Write a short render path that makes the visible states easy to scan. Derive values once, give complex conditions good names, and extract a component when it owns behavior or has a meaningful interface. Small fragments and a local conditional can be clearer than forwarding components.
- Map list items by stable domain identity when the renderer uses keys for reconciliation. Test a reorder when a row contains editable state. Avoid numeric `&&` guards if the renderer can display zero; use a Boolean condition or an explicit branch.
- Prefer semantic elements and preserve label, focus, keyboard, and form semantics when wrapping them. If props are forwarded, define precedence and pass through the attributes the wrapper promises. Keep raw HTML features at an explicit trust boundary.

## Types and build output

- In TSX, model only supported prop combinations. Use a discriminated union if the component has mutually exclusive modes, such as a link with `href` versus a button with an action. Derive native prop and event types from the actual renderer when wrapping a native element; avoid a loose index signature that accepts mistaken props.
- A TypeScript check proves the JSX type contract, while the transform and bundler prove the emitted runtime imports resolve. For transform or type errors, inspect which JSX namespace and runtime are actually selected. In TSX prefer `as` for assertions, since angle-bracket assertions collide with JSX syntax.
- When render cost matters, compare representative updates and bundle output under the framework's production build. Extract components for ownership and readability before considering memoization.

Verify through the existing type check, production transform when relevant, and a focused interaction (including keyboard or form submission if touched). If rendering on the server, compare the initial server and client output.

Upstream: [TypeScript JSX](https://www.typescriptlang.org/docs/handbook/jsx.html), [React markup](https://react.dev/learn/writing-markup-with-jsx).
