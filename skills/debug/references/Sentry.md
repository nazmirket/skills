# Sentry

Confirm organization, project, environment, SDK, deployed release, time window, and the affected operation. Read existing telemetry within the approved scope. Instrumentation changes and additional data capture require their own authority.

- Pin one representative event. Read the exception chain, breadcrumbs, stack and release together. Verify that debug symbols or JavaScript source maps correspond to the deployed artifact. For a grouped issue, inspect more than one example when inputs, code paths or releases differ. First seen and suspect commits help narrow a search; neither proves causality.
- Follow a trace through the actual slow transaction. Look for repeated spans, queue time, downstream calls, or time outside the instrumented spans. Use trace and event IDs to correlate other logs. A missing child may indicate missing propagation or sampling, not a fast operation.
- Compare equivalent releases, traffic cohorts, and time windows. Keep sampling and filtering in mind before interpreting counts or spans. Avoid increasing sample rates or recording sensitive request data just to improve visibility. Reuse existing scrubbers and confirm the event payload is suitable before adding diagnostic fields.
- After a fix, reproduce in an approved test path, confirm the new release is identifiable, and check the expected error or span behavior. Leave production mitigation to [Deploy](../../deploy/SKILL.md); low volume or sampling may delay evidence of recovery. A resolved issue status alone is not verification.

Upstream: [Tracing concepts](https://docs.sentry.io/concepts/key-terms/tracing/), [Release API and correlation](https://docs.sentry.io/api/releases/create-a-new-release-for-an-organization/), [Source map diagnostics](https://docs.sentry.io/api/events/get-debug-information-related-to-source-maps-for-a-given-event/).
