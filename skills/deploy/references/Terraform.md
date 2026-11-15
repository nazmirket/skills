# Terraform

Confirm the CLI and provider versions, lock file, backend, state identity, workspace, actual cloud account, and execution role. A directory or workspace name alone does not identify the target. Use the team's state lock and approved runner.

- Validate the config and review a plan with the intended provider and backend. Treat a saved plan as sensitive and bind approval to that plan, revision and target. Apply only the approved candidate while still current; generate and review a new plan when state, inputs or approval assumptions change.
- Look beyond add/change/delete counts: inspect replacements, matching identities, dependencies, network or IAM exposure and provider defaults. Use supported address moves for a rename when they preserve identity; handle imports, state repairs and destructive replacements as distinct decisions. Keep state access restricted and backups recoverable.
- Separate validation, provider refresh and apply time. Prefer coherent state and module boundaries to broad targeting by default. Increase parallelism only after measuring rate limits and eventual consistency; do not disable locking or routine refresh merely to make a run faster.
- A Git revert or old state snapshot does not reverse provider mutations. Define a real recovery or forward repair path before changing a shared environment. Reconcile partial application against real resources instead of retrying a stale plan.

After apply, inspect relevant state and provider status and verify the consumer path. If a follow-up plan still changes the target, distinguish expected drift, unmodeled dependencies and a defective rollout.

Upstream: [Plan](https://developer.hashicorp.com/terraform/cli/commands/plan), [State locking](https://developer.hashicorp.com/terraform/language/state/locking), [Module refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring).
