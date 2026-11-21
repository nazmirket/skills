# Jenkins

Identify the controller, agent labels and executors, plugin versions, shared libraries and credential scopes. Prefer a reviewed Jenkinsfile and project conventions; do not assume an example plugin or step is available.

- Keep pipeline logic in the Jenkinsfile or a reviewed library. Run heavy build, file and data processing on agents using the project tools. Keep controller Groovy and large serialized state small. Use narrow agent labels and clean workspaces for jobs that otherwise inherit unverifiable outputs.
- Keep untrusted contributions separate from agents and credentials that can promote. Bind credentials only for the relevant steps. Masking is not permission to print a secret; avoid exposing it through shell tracing, argument handling, and artifacts. Review shared library trust because it changes what code can run.
- Compare executor queue, provisioning, build and artifact transfer time. Avoid large transfers through controller storage when the configured artifact manager or registry fits. Parallelize independent stages only when agent capacity supports it; allocate idle executors and matrices deliberately.
- Bound stage time, use retry only for transient or idempotent steps, and guard mutations to shared targets with the project's serialization mechanism. Avoid automatic abort or replay of an operation whose state can't be reconciled.

Use a test branch or safe pipeline run to verify stage selection, credentials scope, and the failure path. Confirm what artifact was retained and promoted; check service behavior and restore the previous artifact through the documented path when needed.
