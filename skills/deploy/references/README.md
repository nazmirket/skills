# Deployment stack guides

Identify the installed version, execution environment, and the system that owns the change before opening a guide. Start with the guide for the decision or observation in front of you. Add another when the work crosses a distinct boundary, such as Helm rendering, Argo CD reconciliation, and Kubernetes service health. A guide is not required reading for every tool the project uses.

| Work | Start here |
| --- | --- |
| Build or run a container | [Docker](Docker.md), [Podman](Podman.md) |
| Schedule workloads, package manifests, or reconcile desired state | [Kubernetes](Kubernetes.md), [Helm](Helm.md), [Argo CD](ArgoCD.md) |
| Serve HTTP, terminate TLS, or proxy to an application | [Nginx](Nginx.md), [Caddy](Caddy.md), [Apache HTTP Server](Apache.md) |
| Reach a host, configure fleets, or provision infrastructure | [SSH](SSH.md), [Ansible](Ansible.md), [Terraform](Terraform.md) |
| Build delivery pipelines or trace a release revision | [GitHub Actions](GitHubActions.md), [Jenkins](Jenkins.md), [Git](Git.md) |
| Collect metrics, set alerts, or diagnose a rollout | [Prometheus](Prometheus.md), [Grafana](Grafana.md) |
| Promote or verify a platform-managed workload | [Vercel](Vercel.md), [AWS](AWS.md), [Azure](Azure.md) |
| Publish or retrieve objects, or serve a static site from a bucket | [Google Cloud Storage (GCS)](GCS.md) |

Use [Delivery Pipeline Practices](DeliveryPipelines.md) for CI/CD design, throughput, or promotion problems that cut across tools.

- For a container build, start with its builder guide. Open Kubernetes only when workload behavior or rollout depends on the cluster. For Argo CD, a sync can succeed before the workload or user path is ready.
- For an HTTP issue, start with the server or proxy the request actually reaches. Add the managed platform guide when it owns traffic, certificates, or promotion.
- For alerts, use Prometheus for metric shape, rules, and query evaluation; use Grafana for panels, alert routing, or investigation. Load both only when both affect the decision.
- Treat provider guides as routers to the actual service and its documented limits. GCS covers object storage; do not assume Cloud Run, GKE, or an unrelated cloud service follows the same model.

Deploy owns the rollout and served behavior. Preparation and publication still require the [distribution workflow](../../execute/references/VersionedDistribution.md); [Migrate](../../migrate/SKILL.md) owns persistent state changes, and [Audit](../../audit/SKILL.md) owns independent review findings. Match commands, features and defaults to the installed versions and the project's authority.
