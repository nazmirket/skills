# Azure

Confirm tenant, subscription, resource group, region, service and target slot or resource. Separate control-plane status from the service the caller reaches. Verify the effective identity; prefer scoped short-lived federation or managed identities where appropriate rather than universal credentials.

- For App Service, check plan support, slots, which settings remain with the slot, and which travel with a swap. Warm the candidate under the intended configuration, and validate runtime access and dependencies before exposing traffic. Reverse a swap only after checking compatibility with current state.
- For container workloads, clarify whether App Service, Container Apps, or AKS owns rollout and traffic. For Container Apps, check revision mode and traffic weights; for AKS use [Kubernetes](Kubernetes.md) in addition to Azure identity, networking or monitoring guidance when needed.
- Stage exposure using the relevant service's supported mechanism. Choose health thresholds and time for traffic to produce useful evidence. Investigate capacity quotas, cold start, startup time, scaling delays and downstream saturation before widening parallelism or raising capacity. Verify private networking, regional dependencies and public ingress as separate paths where relevant.

Verify the active resource or revision, App Service slot or traffic weight if applicable, and a real request through the production hostname. Use service logs and Azure Monitor to compare the changed path's health. Keep the previous healthy artifact and restore only within approved scope; a resource or slot rollback does not reverse persistent-state changes.

Upstream: [Safe deployment strategies](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments), [App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots), [Container Apps revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions).
