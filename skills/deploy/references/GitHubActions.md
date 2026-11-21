# GitHub Actions

Identify the runner type, event, trust boundary, workflow ref and environment. Check feature availability against the repository plan and GitHub Enterprise Server version if relevant.

- Separate pull request checks from privileged release jobs. Treat event payloads and contribution content as untrusted. Do not check out untrusted head code into a privileged `pull_request_target` job. Give `GITHUB_TOKEN` only the permissions each job needs and pin external actions to reviewed commit SHAs. Prefer short-lived OIDC credentials with trust scoped to the actual repo and environment where supported.
- Use named deployment environments to represent approval and credentials where supported. Validate trigger and branch rules; a skipped job or successful dry run is not a production approval. Cancel superseded checks when safe; group deployments by the shared target and verify queue and cancellation semantics instead of assuming FIFO.
- Optimize the critical path. Cache dependencies with keys tied to platform, toolchain and lockfiles; transfer the exact build artifact between stages rather than relying on cache. Cap matrix size and parallel jobs where they contend. Measure runner queue, checkout, cache restore, build, and upload time separately.
- Capture workflow run ID, source SHA and deployment or artifact digest. Verify job permissions, cold-cache correctness and a failed check path in a safe run. At promotion, verify environment gates, served revision and recovery path. Keep deployment credentials and outputs out of workflow logs.
