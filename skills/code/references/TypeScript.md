# TypeScript

Read the effective tsconfig and build tooling. Confirm module resolution, target, strictness and runtime conventions; TypeScript's compile-time model does not validate runtime input.

- Use `unknown` at untrusted boundaries and narrow or parse once. Type what is established by that check. Avoid asserting a shape to silence a checker where data can be absent or malformed. Distinguish absent, undefined and null according to the contract.
- Represent meaningful states with tagged unions when they reduce invalid combinations. Let ordinary control flow narrow values and handle new variants deliberately. Prefer simple direct types; introduce generics where relationships between multiple inputs and outputs must survive.
- Keep external module types, exports and declaration generation compatible with the consumer. Use type-only imports where they keep runtime dependencies clear. Do not change tsconfig, rewrite all types, or indiscriminately drop into `any` to land a local change.
- Use the strictness that the repository supports, and improve the boundary locally when possible. If changing flags, verify affected projects and emitted declarations rather than assuming the editor's inferred configuration is the build's.

Run type checking separately from transpilation if necessary. Check representative malformed runtime input and a real importing consumer for shared interfaces.

Official: [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [Strict TSConfig options](https://www.typescriptlang.org/tsconfig/strict.html).
