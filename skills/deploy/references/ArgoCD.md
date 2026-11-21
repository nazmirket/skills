# Argo CD

Identify the Application, project, destination cluster and namespace, source revision and renderer. Check reconcile policy, automated sync, pruning and self-healing before changing desired state.

- Make the release identity traceable from reviewed Git to image digests, pinned chart and values. Use the repo that owns the environment. Restrict sources and destinations to the intended scope; avoid an imperative cluster change that the controller will immediately overwrite.
- Separate sync from health. Check the exact observed revision, effective diff, resource conditions and controller operation details. Use waves or hooks only for real ordering constraints; verify what readiness the controller waits for. Review pruning and empty-application behavior explicitly before enabling automation that can remove live resources.
- If promotion is slow, break down rendering, reconciliation queue, Kubernetes readiness, and external verification. Reduce unnecessary diffs and oversized application work only when measured. Ignore a diff only if a known controller owns the specific field and important drift remains visible.

Recover through the reviewed source of truth when automatic reconciliation is active. Confirm compatibility with any migrations and check the new desired revision before sync. A previous application history entry, Synced status, or Healthy status alone does not prove rollback or the public path. Verify the served revision and one real request.
