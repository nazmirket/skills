# Vite

Confirm Vite and framework versions, plugin order, package manager, active config and mode, and whether the issue occurs in dev, production build, preview, or SSR. Check the installed optimizer and bundler; different Vite versions do not necessarily use the same engines.

- Reproduce with the project's actual script. Compare the failing module's resolved file, importer, conditions, aliases and exports with a working import. Inspect the transform pipeline when generated output first diverges. Separate dependency optimization in dev from production bundling and SSR externalization.
- For HMR, check the changed file, accepted update boundary, full reloads, and duplicate module or watcher paths. A cold restart can help separate cache state from a repeatable graph error; don't make cache clearing the permanent fix.
- Break startup and rebuild latency into config loading, dependency optimization, plugin transforms and filesystem watching. Use installed debug timing or a supported profiler to find expensive transforms; narrow plugin input and avoid repeated work before increasing resources. Compare cold startup, warm update, and production output separately.
- For production-only behavior, check base paths, environment mode, generated chunks, dynamic imports and source maps. Do not infer deployed routing, headers or cache behavior from a local preview server.

Verify the changed path in the failing mode and a representative adjacent mode, such as start plus update or build plus serving the output. Record lockfile, mode, cache state and measured change.
