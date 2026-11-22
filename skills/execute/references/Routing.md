# Choose the workflow by the result

Choose one owner per requested outcome. Honor named skills and existing authority. Apply [Execute](../SKILL.md) throughout. Reuse available evidence. Bring in support when a distinct question, evidence gap or decision could change the result. Give the owner the answer and its limits. Keep agent-owned files in the [project workspace](Workspace.md).

## Understand and decide

| Requested result | Owner and stopping point |
| --- | --- |
| Understand a project or its recorded decisions | [Adapt](../../adapt/SKILL.md) returns facts from read-only inspection. |
| Check an external claim or research papers, documentation, communities, trends or history | [Search](../../search/SKILL.md) reports sourced findings, disagreements and limits. |
| Choose, keep, adjust or replace a tool or format | [Equip](../../equip/SKILL.md) recommends a choice or bounded pilot. |
| Check tool or environment readiness | [Preflight](../../preflight/SKILL.md) verifies readiness and handles authorized setup. The verification owner checks behavior. |
| Set product direction, priorities, requirements, success measures or launch readiness | [Ship](../../ship/SKILL.md) recommends an option. The human makes the product decision. |
| Choose a lasting system boundary or compare design threats | [Architect](../../architect/SKILL.md) compares designs, [models threats](../../architect/SKILL.md#model-threats-during-design) and records settled boundary changes in an ADR. |
| Sequence substantial work, coordinate workers or check progress | [Plan](../../plan/SKILL.md) records steps, checks and authority. Use [coordination](../../plan/SKILL.md#coordinate-workers) for assignments and [tracking](../../plan/SKILL.md#track-authorized-work) for status. |

## Produce or change the work

| Requested result | Owner and stopping point |
| --- | --- |
| Give a routine answer, make a known edit or implement settled requirements without a specialist owner | [Execute](../SKILL.md) delivers and verifies the result. |
| Get language, framework, database or CLI contract advice | [Code](../../code/SKILL.md) answers the implementation question or advises the implementer. |
| Write or review a document, report or in-product instructions, or turn a bug report into a ticket | [Author](../../author/SKILL.md) delivers writing, editorial findings or an [issue draft](../../author/references/IssueTriage.md) with reproduction status and priority. |
| Position an offer, write marketing copy, plan a campaign or measure conversion | [Market](../../market/SKILL.md) owns the message, distribution and measurement. Ship handles offer changes and Design owns visual identity. |
| Create visual work or review an interface | [Design](../../design/SKILL.md) delivers the visual result, an [interface concept](../../design/references/flows/Create.md#generate-an-interface-concept) or a [critique](../../design/references/flows/Critique.md) of the rendered design and interactions. For a specific input and outcome, use the [interaction check](../../design/references/flows/CollectEvidence.md#check-an-interaction). |
| Diagnose or fix an observed failure | [Debug](../../debug/SKILL.md) reports the cause and evidence. A repair request continues through the smallest fix and its check. |
| Simplify existing code | [Refactor](../../refactor/SKILL.md) checks behavior before and after. Report defects discovered during a refactor. Verify a correction separately when the request authorizes it. |
| Change persistent state with compatibility or recovery requirements | [Migrate](../../migrate/SKILL.md) defines what to preserve, proves recovery and reconciles the transition. Routine reversible edits stay with their owner. |

## Verify, operate and hand off

| Requested result | Owner and stopping point |
| --- | --- |
| Verify behavior or performance, or fill a test evidence gap | [Test](../../test/SKILL.md) reports observations and failures. Owners can run known checks. For speedups, Test supplies [comparable measurements](MeasuredImprovement.md) and the implementer owns the change. |
| Review a change, plan or system for technical, security or privacy risks | [Audit](../../audit/SKILL.md) reports findings and limits for a fixed target. High-risk changes and explicit gates require [independent review](../../audit/SKILL.md#independent-review). The implementer owns [authorized hardening](#authorized-hardening). |
| Design CI/CD, roll out or roll back a candidate, assess health or recover a service | [Deploy](../../deploy/SKILL.md) owns pipelines, target readiness and rollout verification. Its [operations branch](../../deploy/SKILL.md#operate-and-recover) covers incidents, health, recovery and bounded monitoring. Debug investigates causes. |
| Hand off, pause or resume work | [Brief](../../brief/SKILL.md) carries forward the next action, its authority and evidence. Use [pause or resume](../../brief/SKILL.md#pause-or-resume) on request. |
| Clean up, check delivery or inspect an authorized commit | [Clean](../../clean/SKILL.md) reviews affected work and removes verified leftovers within scope. |

## Work across skills

- For a [prototype](Prototype.md), Design owns visual experiments, Architect owns technical tradeoffs and the human decides product rules. Production work needs its own authority.
- For [versioned distribution](VersionedDistribution.md), the task owner prepares the candidate and publishes when authorized. Execute owns standalone preparation. Migrate covers state compatibility and reconciliation. Production activation needs a decision on the exact candidate and target. Deploy verifies the served version.

## Authorized hardening

The implementer makes the smallest correction that addresses the [finding](../../audit/SKILL.md#security-and-privacy-review). Reuse Test evidence that disallowed access is denied and legitimate behavior still works. Use Migrate when the fix requires a persistent-state transition, and Deploy when rollout is in scope. Production changes and shared credential rotation require applicable authority.
