# TypeScript

Read the effective tsconfig and build tooling. Confirm module resolution, target, strictness and runtime conventions; TypeScript's compile-time model does not validate runtime input.

- Use `unknown` at untrusted boundaries and narrow or parse once. Type what is established by that check. Avoid asserting a shape to silence a checker where data can be absent or malformed. Distinguish absent, undefined and null according to the contract.
- Represent meaningful states with tagged unions when they reduce invalid combinations. Let ordinary control flow narrow values and handle new variants deliberately. Prefer simple direct types; introduce generics where relationships between multiple inputs and outputs must survive.
- Keep external module types, exports and declaration generation compatible with the consumer. Use type-only imports where they keep runtime dependencies clear. Do not change tsconfig, rewrite all types, or indiscriminately drop into `any` to land a local change.
- Use the strictness that the repository supports, and improve the boundary locally when possible. If changing flags, verify affected projects and emitted declarations rather than assuming the editor's inferred configuration is the build's.

## Keep type boundaries useful

- Export the smallest contract a caller needs. Use overloads or generics only when input/output relationships have to survive at the call site; test them through a consumer. When a lookup can miss, model that result even if the current compiler options infer a broader contract.
- Check the actual module host before changing resolution, extensions, or exports. A path alias that passes TypeScript checks can still fail after emit. Check type and value imports, the emitted package, and one consumer built with the supported resolution mode.
- When type checking is slow, collect compiler timing or a trace before simplifying types or altering project references. Narrow recursive or distributive types around the expensive call sites; preserve the public types that prevent real mistakes.

Run type checking separately from transpilation if necessary. Check representative malformed runtime input and a real importing consumer for shared interfaces.

Official: [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [Strict TSConfig options](https://www.typescriptlang.org/tsconfig/strict.html), [Module resolution and hosts](https://www.typescriptlang.org/docs/handbook/modules/theory.html).
