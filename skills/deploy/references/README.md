# Deployment stack guides

Identify the installed version, execution environment, and tool responsible for the unresolved question. Consult that guide before acting on its tool-specific advice. Add another only when a separate unresolved question depends on it, such as Helm rendering after Kubernetes status has been understood.

| Work | Start here |
| --- | --- |
| Build or run a container | [Docker](Docker.md), [Podman](Podman.md) |
| Schedule workloads, package manifests, or reconcile desired state | [Kubernetes](Kubernetes.md), [Helm](Helm.md), [Argo CD](ArgoCD.md) |
| Serve HTTP, terminate TLS, or proxy to an application | [Nginx](Nginx.md), [Caddy](Caddy.md), [Apache HTTP Server](Apache.md) |
| Reach a host, configure fleets, or provision infrastructure | [SSH](SSH.md), [Ansible](Ansible.md), [Terraform](Terraform.md) |
| Build delivery pipelines or trace a release revision | [GitHub Actions](GitHubActions.md), [Jenkins](Jenkins.md), [Git](Git.md) |
| Interpret a PromQL query, counter reset, recording rule, or alert expression | [Prometheus](Prometheus.md) |
| Diagnose a panel, dashboard query, or notification routing owned by Grafana | [Grafana](Grafana.md) |
| Promote or verify a platform-managed workload | [Vercel](Vercel.md), [AWS](AWS.md), [Azure](Azure.md) |
| Verify a public route through an edge worker, cache or bound service | [Edge delivery](EdgeDelivery.md) |
| Publish or retrieve objects, or serve a static site from a bucket | [Google Cloud Storage (GCS)](GCS.md) |

Use [Delivery Pipeline Practices](DeliveryPipelines.md) for CI/CD design, throughput, or promotion problems that cut across tools.

- For a container build, start with its builder guide. Open Kubernetes for unresolved questions about cluster workload behavior or rollout. For Argo CD, a sync can succeed before the workload or user path is ready.
- For an HTTP issue, start with the server or proxy the request actually reaches. Add the managed platform guide when it owns traffic, certificates, or promotion.
- When a Prometheus expression is the open question, read Prometheus alone. A recorded Kubernetes readiness result or a Grafana panel that mirrors the same series does not require a guide.
- Treat provider guides as routers to the actual service and its documented limits. GCS covers object storage; do not assume Cloud Run, GKE, or an unrelated cloud service follows the same model.

Deploy owns the rollout and served behavior. Preparation and publication still require the [distribution workflow](../../execute/references/VersionedDistribution.md); [Migrate](../../migrate/SKILL.md) owns persistent state changes, and [Audit](../../audit/SKILL.md) owns independent review findings. Match commands, features and defaults to the installed versions and the project's authority.
