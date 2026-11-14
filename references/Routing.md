# Choose the workflow by the result

Choose one primary owner for each requested result. Respect an explicitly requested skill and the authorized scope. Add a supporting skill only for a distinct deliverable or missing evidence. Give it the question and the evidence already available; it returns its result and limits to the owner without restarting the workflow or taking over execution.

[Execute](../skills/execute/SKILL.md) applies across these workflows: take the simplest complete path, preserve quality, and report what matters.

Use the [project workspace](Workspace.md) for any agent-owned files the workflow creates.

| Request | Owner and stopping point |
| --- | --- |
| Discover or refresh project facts | [Adapt](../skills/adapt/SKILL.md): read-only orientation; pass findings to the skill responsible for acting on them. |
| Check readiness on request or investigate a setup blocker | [Preflight](../skills/preflight/SKILL.md): evidence about the needed capability, authorized setup if needed, and a basic readiness check. Return acceptance checks to the verification owner. |
| Choose a tool or format, or challenge one that falls short or works at a material cost | [Equip](../skills/equip/SKILL.md): evidence for keeping, adjusting, piloting, or switching. Once chosen, [Preflight](../skills/preflight/SKILL.md) owns authorized setup and readiness. Use [Debug](../skills/debug/SKILL.md) for unexpected failures. |
| Assess architecture or change a lasting system boundary | [Architect](../skills/architect/SKILL.md): evidence and a recommendation while open; a self-contained ADR once a lasting boundary change is settled. Plan uses the ADR for steps and checks. |
| Agree how to execute a substantial change | [Plan](../skills/plan/SKILL.md): evidence, human decisions, review when available, and a truthful record of authorization. A substantial review without an execution request belongs to Audit; it does not need a Plan record. |
| Implement a known change | Do the authorized work and incidental simplification directly. Use [Plan](../skills/plan/SKILL.md) for substantial work and [Test](../skills/test/SKILL.md) when verification needs specialist work. |
| Simplify existing code as distinct structural work | [Refactor](../skills/refactor/SKILL.md): preserve the observable contract with focused before-and-after evidence. Verify and report any bounded contract fix separately. |
| Assess security or privacy, model design threats, or harden a target | [Audit](../skills/audit/SKILL.md#security-and-privacy-review) returns risk findings without editing. [Architect](../skills/architect/SKILL.md#model-threats-during-design) models threats for design decisions. The implementer owns [authorized hardening](#authorized-hardening); Deploy owns active incidents. |
| Prepare or publish a versioned artifact | The task owner follows [versioned distribution](VersionedDistribution.md), with Test and Audit evidence as needed. Preparation does not authorize publication. |
| Change persistent state when preservation, compatibility, or recovery needs separate work | [Migrate](../skills/migrate/SKILL.md): preservation contract, simplest authorized cutover, proved recovery and reconciliation. Keep routine reversible changes with the task owner. |
| Activate or roll back an artifact or configuration in a shared running environment | [Deploy](../skills/deploy/SKILL.md): target readiness, authorized rollout, acceptance evidence, and recovery. Production activation requires a distinct decision for the exact candidate and target. Migrate owns state transitions. |
| Maintain service health, respond to an incident or recover a workflow | [Deploy’s operations branch](../skills/deploy/SKILL.md#operate-and-recover): observed health, mitigation, recovery, and bounded monitoring. Debug investigates causes; Migrate owns persistent-state transitions. |
| Sort incoming reports; diagnose an observed failure | [Author](../skills/author/SKILL.md) uses its issue triage branch for intake, reproduction status, and priorities. [Debug](../skills/debug/SKILL.md) owns causal investigation and the smallest authorized fix. Reuse a focused check directly; add supporting skills only for distinct work or missing evidence. |
| Verify behavior on request, fill an evidence gap, or measure performance | [Test](../skills/test/SKILL.md): checks, results, and gaps. The task owner can run known checks directly. Return failures to the owner or Debug without starting a repair. For a requested speedup, Test owns comparable measurements and the implementer owns the change. |
| Review a change, plan, module, system or repository | [Audit](../skills/audit/SKILL.md): material findings and coverage limits against a fixed target. High-risk changes and explicit gates require independent review. Corrections need separate authorization. |
| Direct, produce or review visual work | [Design](../skills/design/SKILL.md) owns visual direction and production, including supplied references and [interface concepts from an agreed brief](../skills/design/SKILL.md#generate-an-interface-concept). Use [visual critique](../skills/design/SKILL.md#visual-critique) for review-only requests and substantial visual work. |
| Resolve uncertainty cheaply | Use the [prototype method](Prototype.md). Design owns visual experiments and Architect owns technical tradeoffs. The human decides product rules and authorizes production work separately. |
| Write or review a document or substantive copy, or triage issues | [Author](../skills/author/SKILL.md) owns the content and its audience. Writing review-only requests end with findings. |
| Report where authorized work stands, or coordinate its workers | [Plan’s tracking branch](../skills/plan/SKILL.md#track-authorized-work) owns the status snapshot; its [coordination branch](../skills/plan/SKILL.md#coordinate-workers) owns assignments and integration. |
| Transfer, pause, or resume work | [Brief](../skills/brief/SKILL.md): the next action, traceable authority, and relevant evidence. Brief [handles explicit pause and resume](../skills/brief/SKILL.md#pause-or-resume); Plan tracks progress and coordinates workers. |
| Remove verified leftovers | [Clean](../skills/clean/SKILL.md) owns cleanup within scope. |

For work spanning the product lifecycle, use the requested outcome to assign ownership and name each handoff. Migrate supplies compatibility and reconciliation; the task owner identifies any distributable; Deploy owns activation, target verification, and service health. Use the steps the work needs.

## Authorized hardening

The implementer makes the smallest correction that addresses the evidenced risk. Reuse [Test](../skills/test/SKILL.md) evidence that disallowed access is denied and legitimate access and behavior still work. Use [Migrate](../skills/migrate/SKILL.md) for persistent-state transitions and [Deploy](../skills/deploy/SKILL.md) for rollout when relevant. Findings alone do not authorize production changes or shared credential rotation.
