# Kubernetes

Identify context, namespace, API versions, workload owner, controller and traffic path. Confirm whether the cluster, Helm, or [Argo CD](ArgoCD.md) owns desired state before editing. A healthy control plane does not prove application readiness.

## Roll out the workload

- Pin the intended image digest and inspect the actual Pod template. Separate startup, readiness, and liveness: readiness decides when to receive traffic, liveness decides when to restart, and startup can protect a slow initialization. Avoid using transient remote dependency failure as the only signal to restart every replica.
- Set rolling-update surge and unavailability using real replica count and available cluster capacity. Observe scheduling, termination and traffic draining. Treat a disruption budget as protection for supported voluntary evictions; use the workload's own rollout settings for a rolling update.
- Choose CPU and memory requests against observed workload and scheduling needs. Check throttling, OOMs, pending Pods, replica scaling, and downstream saturation before raising limits or replicas. Establish baseline readiness time and error/latency under traffic; inspect tail behavior across old and new versions.

Check rollout conditions and events, running revision and Ready endpoints, then a request through the actual Service or Ingress path. A progress deadline identifies a stalled rollout; it does not automatically restore a Deployment. Reverting a Pod template will not restore separately changed data or configuration. Verify recovery compatibility before changing desired state back.

Upstream: [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [Container probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/), [Resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).
