# Debug tool guides

Start with the failure and the next observation that could change the diagnosis. Use the smallest available probe. Open a guide when the tool's behavior or interpretation is material; add another only when the investigation crosses a boundary. Read the actual project version and reproduce the actual execution mode.

| Question | Start here |
| --- | --- |
| What happened in the browser request, event loop, layout, or rendering? | [Chrome DevTools](ChromeDevTools.md) |
| Is an expected TCP service reachable from the affected source? | [Nmap](Nmap.md) for narrowly scoped, authorized diagnostics |
| Where did an expected network conversation stall? | [Wireshark](Wireshark.md) for an approved capture |
| What was the native program doing when it failed? | [LLDB](LLDB.md), [GDB](GDB.md) |
| Which release, error event, or trace explains a production symptom? | [Sentry](Sentry.md) |
| Which framework state, update, or render caused an issue? | [Vue Devtools](VueDevTools.md), [React Developer Tools](ReactDevTools.md), [Angular DevTools](AngularDevTools.md) |
| Did Vite accept a hot update, perform a full reload, or miss a change? Did its resolver or dependency optimizer affect the result? | [Vite](Vite.md) |
| Did another bundler's resolver, transform, or build change behavior or become slow? | [webpack](Webpack.md), [esbuild](Esbuild.md) |

- Start with the browser request or trace when a user interaction is slow. Use a framework profiler when evidence points to component updates, and a build tool when the problem is startup, rebuild, or emitted output.
- For network symptoms, compare an affected client with a known working path. Prefer existing logs, connection checks and approved captures. A port state, successful handshake or single capture point does not prove application health.
- For production incidents, investigate the cause and return evidence to [Deploy](../../deploy/SKILL.md), which owns mitigation and recovery. Use [Test](../../test/SKILL.md) when a performance claim needs a separate comparison. Use [Preflight](../../preflight/SKILL.md) for setup blockers; a missing tool does not authorize installing it or widening access.

Record the conditions that could change the result: exact build or release, input, versions, execution mode, timestamps, and probe settings. Preserve just the evidence needed to distinguish causes; sanitize it before sharing. Separate timing evidence from a debugger or profiler that changed the workload. Retest the original case and a useful comparison after an authorized fix. Use the [measurement method](../../execute/references/MeasuredImprovement.md) for a formal performance claim.
