# Helm

Identify the installed Helm major, chart version, dependencies, release name, namespace, cluster APIs, and layered values. Confirm whether Helm or a GitOps controller owns the target. Chart rendering under Argo CD is not the same as a Helm-managed release.

- Use a pinned chart and dependency lock where applicable. Make values and their precedence reviewable; use a schema for meaningful constraints. Keep templates readable and don't log rendered Secrets or sensitive values from a dry run.
- Render exactly the intended values and context. Use linting as a first check, then inspect effective manifests and compare them to the live target or previous release. A local rendering does not establish cluster admission or upgrade compatibility. Inspect resource names, immutable fields, hooks, and CRDs; Helm does not normally upgrade CRDs from a chart's `crds/` directory.
- Choose a timeout from the workload's real initialization time. Review how the installed upgrade command waits, reports a failed release, and handles failure rollback flags. Hooks or migrations can have side effects outside that rollback. Avoid complicating templates or adding job hooks without evidence they solve a repeatable problem.

For a Helm-owned release, verify release status, candidate workload identity, Ready endpoints, and a user request; check a hook or migration separately. Keep the prior release metadata and chart values. For a GitOps-owned release verify the rendered source and reconcile through [Argo CD](ArgoCD.md).
