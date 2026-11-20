# Choose the workflow by the result

Choose one owner for each requested outcome. Honor a named skill and the authorized scope. [Execute](../SKILL.md) applies throughout. Reuse evidence directly when it answers the question. Add support only for a distinct unresolved question, evidence gap or decision that could change the result. Give it the existing evidence and return its answer and limits to the owner. Use the [project workspace](Workspace.md) for agent-owned files.

## Understand and decide

| Requested result | Owner and stopping point |
| --- | --- |
| Understand the project, its behavior or its recorded decisions | [Adapt](../../adapt/SKILL.md) returns current project facts from read-only inspection. |
| Check an external claim, synthesize papers or technical documentation, or research communities, emerging projects, competitors or history | [Search](../../search/SKILL.md) returns sourced findings, disagreements and coverage limits. |
| Choose, keep, adjust or replace a tool or format | [Equip](../../equip/SKILL.md) recommends a choice or a bounded pilot. |
| Check whether the chosen tool or environment can run the work | [Preflight](../../preflight/SKILL.md) verifies readiness and handles authorized setup. The verification owner checks the actual behavior. |
| Decide product direction, priorities, requirements, success measures or launch readiness | [Ship](../../ship/SKILL.md) brings evidence and a recommendation to the human who owns the product decision. |
| Choose a lasting system boundary or compare design threats | [Architect](../../architect/SKILL.md) compares designs, [models threats](../../architect/SKILL.md#model-threats-during-design) where relevant, and records a settled boundary change in an ADR. |
| Sequence substantial work, coordinate workers or check progress | [Plan](../../plan/SKILL.md) records steps, checks and existing authority. Use [coordination](../../plan/SKILL.md#coordinate-workers) for assignments and integration, or [tracking](../../plan/SKILL.md#track-authorized-work) for a status-only request. |

## Produce or change the work

| Requested result | Owner and stopping point |
| --- | --- |
| Give a routine answer, make a known edit or implement settled requirements with no specialist owner | [Execute](../SKILL.md) owns the result through verification. Code can support a stack decision and Plan can coordinate substantial work. |
| Get advice on an identified language, framework or database | [Code](../../code/SKILL.md) answers the stack question. During implementation it supports the owner when stack guidance changes a decision. |
| Write or review a document, report or product copy, or triage bug reports | [Author](../../author/SKILL.md) delivers writing, editorial findings or [issue drafts](../../author/references/IssueTriage.md) with reproduction status and priority. |
| Position an offer, shape marketing claims or voice, run a campaign or measure conversion | [Market](../../market/SKILL.md) owns the marketing message, distribution and measurement. Ship owns changes to the offer and Design owns visual identity. |
| Create or critique visual work, or review how people use an interface | [Design](../../design/SKILL.md) owns the visual result and [interface concepts](../../design/references/flows/Create.md#generate-an-interface-concept). Use [critique](../../design/references/flows/Critique.md) to review keyboard navigation, form recovery or the rendered design. |
| Explain an observed failure or fix the reported behavior | [Debug](../../debug/SKILL.md) establishes the cause. A diagnosis ends with evidence. A repair request continues through the smallest fix and its check. |
| Simplify existing code as a distinct structural change | [Refactor](../../refactor/SKILL.md) verifies the observable contract before and after. Check and report a bounded contract correction separately. |
| Change persistent state when compatibility, preservation or recovery needs separate work | [Migrate](../../migrate/SKILL.md) defines the preservation contract, proves recovery and reconciles the authorized transition. Routine reversible edits stay with their owner. |

## Verify, operate and hand off

| Requested result | Owner and stopping point |
| --- | --- |
| Verify behavior or performance, or fill a gap in test evidence | [Test](../../test/SKILL.md) returns observations and failures to the owner. The owner can run known checks directly. For a requested speedup, Test supplies [comparable measurements](MeasuredImprovement.md) and the implementer owns the change. |
| Review a change, draft plan or system for technical, security or privacy findings | [Audit](../../audit/SKILL.md) reports findings and limits against a fixed target. A review-only request ends there. High-risk changes and explicit gates require [independent review](../../audit/SKILL.md#independent-review). Return [authorized hardening](#authorized-hardening) to the implementer. |
| Design CI/CD, roll out or roll back a candidate, assess health or recover a service | [Deploy](../../deploy/SKILL.md) owns pipelines, target readiness and verified rollout. Its [operations branch](../../deploy/SKILL.md#operate-and-recover) handles incidents, service health, recovery and bounded monitoring. Debug supplies causal evidence. |
| Transfer work, pause it or resume it | [Brief](../../brief/SKILL.md) hands over the next action, its authority and supporting evidence. Use its [pause or resume branch](../../brief/SKILL.md#pause-or-resume) on request. |
| Clean up, check delivery or inspect an authorized commit | [Clean](../../clean/SKILL.md) checks the affected work and removes verified leftovers within scope. |

## Work across skills

- For a [prototype](Prototype.md), Design owns visual experiments and Architect owns technical tradeoffs. Take product rules to the human. Production work needs its own authority.
- For [versioned distribution](VersionedDistribution.md), the task owner prepares the candidate and publishes within the authority granted. Execute owns a standalone preparation request. Migrate supplies state compatibility and reconciliation. Production activation needs a decision for the exact candidate and target, then Deploy verifies what is served.

## Authorized hardening

The implementer makes the smallest correction that addresses the [security or privacy finding](../../audit/SKILL.md#security-and-privacy-review). Reuse Test evidence that disallowed access is denied and legitimate behavior still works. Involve Migrate for state transitions and Deploy for rollout. Production changes and shared credential rotation require applicable authority.
