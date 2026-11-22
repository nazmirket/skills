# AWS

Confirm the AWS account, role, region, service and exact deployment target. Check quotas and dependencies for that target. Use account- or environment-scoped short-lived credentials where supported, and verify the caller identity before a mutating operation.

## Follow the service that controls traffic

- **ECS:** Pin task definition revision and image digest. Check desired, running and healthy tasks as well as load-balancer targets. Use supported alarms or a deployment circuit breaker only after confirming the rollout strategy and rollback prerequisites. Check deployment events and the known-good revision before retrying.
- **Lambda:** Publish versions and control the caller path through an alias where appropriate. Confirm the event source or API invokes that alias. Use compatible versions and runtime configuration for weighted routing; observe version-specific errors, throttles and latency with enough traffic to interpret them.
- **S3 and CloudFront:** Keep assets immutable where practical. Publish new assets before referring to them from entry documents, then check caching behavior at both origin and CDN. Scope invalidations to changed routes when needed. Keep prior assets available through the rollback window.

Separate build time from provisioning, target health, traffic exposure and propagation. Check capacity, placement, throttles, warm/cold latency and cost before increasing parallel work or reserved capacity. Use the service's documented operation ID and end states, then verify a representative request or event through the target environment's consumer path. An artifact rollback cannot reverse durable state or downstream writes.
