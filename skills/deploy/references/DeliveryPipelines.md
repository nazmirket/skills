# Delivery pipeline practices

Use this guide to design, review, or improve a delivery pipeline across build, check, and promotion stages. Read the installed system's guide for concrete syntax and controls.

## Preserve the identity of what ships

- Trace source revision → build inputs → immutable artifact digest → target environment → served revision. Use a manifest or platform record that can answer which source and inputs a deployment used. Promote the tested artifact when its configuration model permits. If each environment requires a separate build, track and verify each artifact separately.
- Separate checks that can run before merge from permissions needed to publish or activate. Keep a distinct promotion step with clear human approval for production where required. Use job-scoped access, short-lived credentials where supported, and immutable dependency references where practical. Keep an untrusted contribution path outside privileged runners and credentials.
- A dependency cache saves work; it is not the release artifact or a test pass. Scope cache keys by compatibility inputs. Make correctness hold on a cold cache, verify artifact integrity across jobs, and avoid reusing outputs from an untrusted context.

## Reduce wait without losing evidence

- Measure queue time, setup, the critical path, retries, and deploy verification separately. Start with slow runs that reflect normal usage; compare cold and warm cases. Remove repeated builds and unnecessary transfers before adding runners or parallel jobs.
- Keep fast independent checks early. Split work only when it shortens the critical path and still gives meaningful failure evidence. Avoid matrix growth without a coverage reason; cap parallelism to protect scarce runners and shared services.
- Cancel obsolete checks when safe; serialize mutations to a shared environment. Do not cancel a deployment midway if the system cannot reconcile that state. Give steps explicit deadlines and retry only transient failures where the step can safely replay.

## Verify promotion and recovery

Preserve the last known good artifact and the procedure that restores traffic. Pin expected checks and stop conditions before activation. Confirm what users actually receive, including a dependency or one end-to-end path; a successful pipeline job alone is not enough. For state changes verify compatibility with [Migrate](../../migrate/SKILL.md). Compare meaningful outcomes such as time to feedback, flake rate, throughput, and recovery time before calling a pipeline faster or safer.

Upstream examples: [GitHub deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments), [Jenkins pipeline best practices](https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/), [Azure safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments).
