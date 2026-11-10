# Choose the workflow by the result

Choose one primary owner for each requested result. Add a second skill only for a different deliverable or evidence the owner needs. A supporting skill returns that result to its caller; it does not restart the caller's workflow.

Use the [project workspace](workspace.md) for any agent-owned files the workflow creates.

| Request | Owner and stopping point |
| --- | --- |
| Understand the code and its conventions | [Adapt](../skills/adapt/SKILL.md): evidence-backed orientation. Use [Preflight](../skills/preflight/SKILL.md) for environment readiness and blockers. |
| Find why the current tool or method cannot deliver the result or needs repeated workarounds | [Equip](../skills/equip/SKILL.md): evidence for the mismatch and the smallest better fit. Use Preflight when the chosen method fits but its required environment is missing or misconfigured. |
| Decide what problem to prioritize, or compare outside options | [Focus](../skills/focus/SKILL.md): product brief with the decisions for the human. [Curate](../skills/curate/SKILL.md) owns sourced discovery and comparison of options. |
| Decide how to change a system boundary | [Architect](../skills/architect/SKILL.md): alternatives, consequences, and a recommendation or draft decision record. |
| Agree how to execute a substantial change | [Plan](../skills/plan/SKILL.md): evidence, human decisions, review when available, and a truthful record of authorization. |
| Implement a known change | Execute the authorized work directly. Use [Plan](../skills/plan/SKILL.md) for substantial work and [Test](../skills/test/SKILL.md) for verification. [Refactor](../skills/refactor/SKILL.md) owns behavior-preserving simplification. |
| Sort incoming reports; diagnose an observed failure | [Author](../skills/author/SKILL.md) uses its issue triage branch for intake, reproduction status, and priorities. [Debug](../skills/debug/SKILL.md) owns causal investigation and any authorized fix. |
| Exercise behavior or measure performance | [Test](../skills/test/SKILL.md): actual checks, results and gaps. For a requested speedup, the implementer owns the authorized change and Test owns comparable measurements. |
| Review a change, plan, module, system or repository | [Audit](../skills/audit/SKILL.md): prioritized findings against the specified target. An audit request does not itself authorize corrections. |
| Judge work against its brief during implementation or before delivery | [Critique](../skills/critique/SKILL.md): evidenced quality findings; reuse relevant Test results. |
| Establish or implement visual direction | [Design](../skills/design/SKILL.md) owns direction, redesigns, supplied references and non-interface visual artifacts. [Imagine](../skills/imagine/SKILL.md) owns generated interface references from an agreed brief. Critique owns rendered QA. |
| Resolve uncertainty cheaply | Use the [prototype method](prototype.md). Design owns visual experiments, Focus product logic, Architect technical tradeoffs. Production implementation is a separate decision. |
| Write a document or substantive copy, or triage issues | [Author](../skills/author/SKILL.md) owns the content and its audience. Use [Distill](../skills/distill/SKILL.md) for routine replies and clear communication throughout. |
| Report where authorized work stands, or coordinate its workers | [Plan’s tracking branch](../skills/plan/SKILL.md#track-authorized-work) owns the status snapshot; [Orchestrate](../skills/orchestrate/SKILL.md) owns assignments and integration. |
| Transfer work, or pause it | [Brief](../skills/brief/SKILL.md) prepares the transfer. [Sleep](../skills/sleep/SKILL.md) persists it and stops work until asked to resume. |
| Remove verified leftovers or improve a response | [Clean](../skills/clean/SKILL.md) owns cleanup within scope. [Distill](../skills/distill/SKILL.md) applies to communication. |
