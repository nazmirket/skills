# Choose the workflow by the result

Choose one primary owner for each requested result. Respect an explicitly requested skill and the authorized scope. Add a supporting skill only for a distinct deliverable or missing evidence. Give it the question and the evidence already available; it returns its result and limits to the owner without restarting the workflow or taking over execution.

Use the [project workspace](Workspace.md) for any agent-owned files the workflow creates.

| Request | Owner and stopping point |
| --- | --- |
| Understand the code and its conventions | [Adapt](../skills/adapt/SKILL.md): evidence-backed orientation. Use [Preflight](../skills/preflight/SKILL.md) for environment readiness and blockers. |
| Choose or obtain a tool, or challenge a tool, format, representation, abstraction, or workflow that falls short or works at a material cost | [Equip](../skills/equip/SKILL.md): evidence for the mismatch, the benefit and cost of changing, and guidance for authorized setup. Use Preflight when a suitable tool is missing or misconfigured in the target environment, and Debug when a suitable tool unexpectedly fails. |
| Decide what problem or product option to prioritize | [Focus](../skills/focus/SKILL.md): product brief with the decisions for the human. |
| Discover or compare outside options without making an adoption decision | [Curate](../skills/curate/SKILL.md): sourced comparison. When the decision is whether to adopt or replace a tool, return this evidence to Equip. |
| Decide how to change a system boundary | [Architect](../skills/architect/SKILL.md): alternatives, consequences, and a recommendation or draft decision record. |
| Agree how to execute a substantial change | [Plan](../skills/plan/SKILL.md): evidence, human decisions, review when available, and a truthful record of authorization. A substantial review without an execution request belongs to Audit; it does not need a Plan record. |
| Implement a known change | Execute the authorized work directly. Use [Plan](../skills/plan/SKILL.md) for substantial work and [Test](../skills/test/SKILL.md) for verification. [Refactor](../skills/refactor/SKILL.md) owns behavior-preserving simplification. |
| Assess security/privacy or harden an authorized target | [Secure](../skills/secure/SKILL.md): threat and data-flow evidence, prioritized risks, or verified hardening. Audit remains the owner of a general review; Operate owns an active incident. |
| Prepare or publish a versioned artifact | [Release](../skills/release/SKILL.md): identified candidate, packaging/compatibility evidence, release notes and verified distribution when authorized. Preparing a release does not itself authorize publishing it. |
| Change persistent data, schema, formats or configuration | [Migrate](../skills/migrate/SKILL.md): invariants, compatibility sequence, rehearsed recovery and reconciled state when execution is authorized. |
| Roll a known change into an environment or roll it back | [Deploy](../skills/deploy/SKILL.md): exact artifact and target, rollout, served-path verification and recovery. Release prepares the artifact; Migrate owns state transitions. |
| Maintain service health, respond to an incident or recover a workflow | [Operate](../skills/operate/SKILL.md): observed health, mitigation/recovery and bounded monitoring. Debug returns causal evidence; Deploy and Migrate execute their scoped changes. |
| Evaluate a shipped feature or product experiment | [Focus](../skills/focus/SKILL.md#learn-from-shipped-work): evidence quality, observed outcomes and a continue/change/retire recommendation. Operate supplies operational evidence; live changes require their own authority. |
| Sort incoming reports; diagnose an observed failure | [Author](../skills/author/SKILL.md) uses its issue triage branch for intake, reproduction status, and priorities. [Debug](../skills/debug/SKILL.md) owns causal investigation and any authorized fix. |
| Exercise behavior or measure performance | [Test](../skills/test/SKILL.md): actual checks, results and gaps. If Debug is already investigating, return a failing result to Debug. For a requested speedup, the implementer owns the authorized change and Test owns comparable measurements. |
| Review a change, plan, module, system or repository | [Audit](../skills/audit/SKILL.md): prioritized findings against the specified target. An audit request does not itself authorize corrections. |
| Judge work against its brief during implementation or before delivery | [Critique](../skills/critique/SKILL.md): evidenced quality findings; reuse relevant Test results. |
| Direct or produce visual work | [Design](../skills/design/SKILL.md) owns visual direction and production for UI, web, brand, illustration, motion, slides and other visual artifacts, including fidelity to a supplied reference. [Imagine](../skills/imagine/SKILL.md) owns generating an interface concept image from an agreed brief; a UI build does not require one. [Critique](../skills/critique/SKILL.md) owns visual assessment, including review-only requests. |
| Resolve uncertainty cheaply | Use the [prototype method](Prototype.md). Design owns visual experiments, Focus product logic, Architect technical tradeoffs. Production implementation is a separate decision. |
| Write a document or substantive copy, or triage issues | [Author](../skills/author/SKILL.md) owns the content and its audience. Use [Distill](../skills/distill/SKILL.md) for routine replies and clear communication throughout. |
| Report where authorized work stands, or coordinate its workers | [Plan’s tracking branch](../skills/plan/SKILL.md#track-authorized-work) owns the status snapshot; [Orchestrate](../skills/orchestrate/SKILL.md) owns assignments and integration. |
| Transfer work, or pause it | [Brief](../skills/brief/SKILL.md) prepares the transfer. [Sleep](../skills/sleep/SKILL.md) persists it and stops work until asked to resume. |
| Remove verified leftovers or improve a response | [Clean](../skills/clean/SKILL.md) owns cleanup within scope. [Distill](../skills/distill/SKILL.md) applies to communication. |

For work spanning the product lifecycle, use the requested outcome as the owner and name each handoff. Secure supplies risk evidence; Migrate supplies compatibility and reconciliation; Release identifies a distributable; Deploy verifies it in the target; Operate checks its continuing health; Focus evaluates whether it helped users. These are conditional responsibilities, not a mandatory sequence for every change.
