# Angular DevTools

Confirm Angular version, the debug build, application root, and whether the signal comes from navigation, an event, change detection, or a remote wait. Check the installed DevTools version before relying on a panel. Angular DevTools inspection typically requires a supported development build.

- Inspect the affected component and directives. Trace inputs to their owners and compare rendered state with what the component reads. Where the installed tool supports it, trace injectors and provider scope to distinguish shared and per-route service state. Treat manual state edits as local probes, not proof of a user path.
- Use Profiler for a short reproduction. Identify the expensive change detection cycles and components; trace what scheduled the work. Distinguish repeated cycles from one slow template calculation or directive. Compare the same data, input and runtime conditions.
- Keep the fix local to the measured cause. Moving costly template work or narrowing unnecessary updates can help; switching change detection strategy or rewriting observables and signals changes behavior and needs evidence. Check input updates, teardown, and async results.
- If the issue depends on the served build, verify it outside the dev-only inspection session. Use browser traces for requests, layout, long tasks, and end-to-end timing.

Repeat the actual event, including navigation or teardown when relevant. Report which cycle or dependency explained the symptom and what the production-like check showed.
