# webpack

Pin webpack version, effective config, mode, target, entry point and the framework wrapper. Start with the failing build or rebuild, not a fresh configuration that omits project loaders or plugins.

- Follow the first module or compilation error to its importer, resolved resource, matching loader rules, plugin hooks and output. Check environment, export conditions and publishing format. If development and production differ, compare optimization, source map and chunk decisions under the actual config.
- Use stats or a scoped profiling run to inspect module inclusion and build cost. Choose the smallest stats output that answers the question. For a large asset, trace which import brought it in, then distinguish duplicate dependencies, source maps, side effects, chunking and compression. Confirm changes at the browser or consuming package, not just in the stats file.
- Separate cold build, warm build, and incremental rebuild. Narrow costly loader scope, avoid opening unnecessary watchers, and test persistent caching with a key that accounts for config and version changes. Extra workers can cost more in startup and data transfer than they save on small inputs.
- Preserve dynamic import and public path behavior when reducing bundle size. Ensure emitted chunks, hashes and assets can be found under the actual served path.

Rerun the failing case with representative inputs and the intended target mode. Compare build time and delivered bytes separately. Inspect runtime behavior before claiming tree shaking, code splitting or cache changes improved the user experience.
