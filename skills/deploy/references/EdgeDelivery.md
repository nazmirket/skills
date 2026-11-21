# Edge delivery

Use for a release or incident where a public hostname reaches a worker, cached asset or origin through an edge service. Identify the project's existing CLI and configuration, account, environment and target hostname. A preview can use different routing rules, runtime settings or backing resources from the public route.

| What changed | Evidence to collect |
| --- | --- |
| Route or worker | Match the host and path to the deployed rule, then identify the version actually receiving traffic. Check a representative request and its expected result. |
| Runtime binding | Resolve the application name to its resource ID in the target environment. Confirm the access and consistency the operation needs with a safe representative read or an authorized fixture write. Local emulators and remote preview bindings can produce different results. |
| Static content or cache policy | Check the entry document and one referenced asset on the public hostname, including version, content type and intended cache scope. Compare a fresh request with a repeated one using the relevant cache evidence. Keep private or personalized content scoped to its intended audience. |
| Background work | Follow an authorized test event from producer through delivery to the consumer's observable effect. Record the handling of retries or duplicate delivery when that affects correctness. |

For example, a preview might read the correct catalog while the public domain still returns yesterday's prices. Compare the active route and worker version, the bound catalog identity and the response's cache age or status. Change only the layer the evidence implicates, within rollout authority.

Check that the prior runtime can use the current resources before shifting traffic back. Recheck the public route and any affected cached content or queued work after recovery. [Migrate](../../migrate/SKILL.md) owns persistent-state recovery.
