# esbuild

Pin the esbuild version, calling wrapper, entry points, target, platform, format, resolver settings and plugin list. Confirm whether the tool transforms one file or builds a dependency graph. The checks and outputs differ.

- On a resolution or runtime error, trace the import from the entry to the resolved file, its loader, external status and chosen exports. Mixing ESM and CommonJS, browser and Node targets, or bundling and external package resolution changes which failures appear at build versus runtime. Reproduce through the actual downstream entry point.
- Emit a metafile when bundle composition is in question. Use its input and output graph to explain why a dependency or asset appears, and compare entry-point bytes and shared chunks. Check delivered compression and runtime loading separately; build output size alone does not prove faster startup.
- Use rebuild contexts for repeated work when the wrapper supports them. Compare cold build, incremental rebuild, plugin overhead and I/O independently. Scope plugins to matching imports and files; do not change output formats or suppress warnings merely to improve build time.
- Source maps are evidence only when they match the emitted assets. If TypeScript is transpiled, run the project's separate type-check command when type correctness matters.

Rerun the original input with the installed configuration and check the artifact in the consuming environment. Record platform, target, format, and cache conditions when comparing behavior or performance.

Upstream: [API and build context](https://esbuild.github.io/api/#build), [Metafile](https://esbuild.github.io/api/#metafile), [Analyze](https://esbuild.github.io/api/#analyze), [TypeScript caveats](https://esbuild.github.io/content-types/#typescript).
