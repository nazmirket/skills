---
name: design
description: "Use to direct, create, redesign, implement or review visual work, including interface concepts, supplied mockups, UI, websites, brands, illustration, motion, slides and visual prototypes."
---

# Design

Own visual direction, production, and review. When the requested outcome changes how work looks, feels, or communicates, agree with the human on the intended effect and what the identity must preserve. Within those boundaries, choose the composition, visual language, and execution. Deliver the direction, artifact, or working implementation the human asked for.

## Choose the job

- **New direction or scoped refinement:** Start with the project's own material. Look outside only when comparison could resolve an open direction or pattern. Show two or three materially different [approaches](references/DirectionAndComposition.md) before developing an open direction. For a scoped refinement, use one approach within the established direction.
- **Redesign an existing interface:** First view and capture the [live baseline](references/DirectionAndComposition.md#capture-the-redesign-baseline). If it cannot be viewed, pause the redesign and name the blocker. Preserve working behavior and established identity. Ask before altering interactions, access, content meaning, or distinctive identity unless already authorized.
- **Translate a supplied mockup or screenshot:** Carry over hierarchy, tone, and relationships by default. [Match literal details](references/ReferenceFidelity.md) when the human explicitly makes them part of the target. If the work redesigns an existing interface, capture the live baseline first.
- **Generate an interface concept image:** Use [the concept branch](#generate-an-interface-concept).
- **Review visual work:** Use [visual critique](#visual-critique). Review-only requests end with findings.
- **Compare visual or interaction approaches:** Use the shared [prototype method](../../references/Prototype.md) to isolate the decision. Keep the experiment outside production.

Read only what changes the work:

| Design question | Reference |
| --- | --- |
| What should lead, and how should the composition express the idea? | [Direction and composition](references/DirectionAndComposition.md) |
| How should type, color, spacing, surfaces and imagery work together? | [Visual language](references/VisualLanguage.md) |
| How should a website, product screen, workflow or component work? | [Web, UI and content](references/InteractionAndContent.md) |
| How should it adapt to space, input, accessibility needs and locale? | [Adaptive and accessible design](references/AdaptiveAndAccessible.md) |
| How should identity, tokens, components or themes stay coherent? | [Identity and design systems](references/IdentityAndSystems.md) |
| What should move, how should it respond to a gesture, and when should motion go away? | [Motion and gestures](references/MotionAndGestures.md) |
| How should an illustration, icon, poster, slide deck or visual asset be composed and produced? | [Visual artifacts and assets](references/ArtifactsAndAssets.md) |
| How should an algorithm or set of parameters create the artwork? | [Generative work](references/GenerativeWork.md) |
| What evidence will make the result reviewable and usable? | [Review and delivery](references/ReviewAndDelivery.md) |

## Generate an interface concept

1. Inspect the product and authorized references. For a redesign, capture the [live baseline](references/DirectionAndComposition.md#capture-the-redesign-baseline) first; stop if you cannot see it. Agree on a brief covering the audience, main action, hierarchy, content, visual direction, target views and constraints. Get explicit agreement before generating; reuse approval of the same brief and ask again only if direction, scope, or a material constraint changes.
2. Use a capable tool with approved inputs. Generate the fewest views needed to answer the brief. Inspect them against the brief and show the proposed direction, flagging drift or placeholders. If the image is the deliverable, apply the delivery checks below and stop after delivery.
3. If the agreed brief also authorizes implementation, proceed with a concept that fits it. Ask before adopting a concept that changes direction or scope. Permission to generate alone does not authorize implementation. Use [reference fidelity](references/ReferenceFidelity.md) to translate the concept, separate trusted content from generated placeholders, and record meaningful departures.

## Develop and deliver

1. **Read the context.** Identify the audience, what they should do or understand, the medium and constraints. Inspect existing work, content, assets and approved decisions. Separate supplied requirements from assumptions and inspiration.
2. **Choose an approach.** Use the structure that serves the job and give one meaningful thing priority. Decide what stays familiar and where a specific visual choice adds value. Tie that choice to the actual content or use; if the same design could serve an unrelated project after swapping the name, revisit the structure before adding polish.
3. **Prove the consequential part first.** Use a representative section, task, state, crop or sequence with realistic material. For an open direction, make the alternatives comparable; for a scoped refinement, develop the single approach. Ask about consequential direction or product choices that remain unresolved; honor decisions and authority already given. For a local edit, make the edit directly.
4. **Deliver in the intended medium.** Use the existing stack, approved assets and real content where available. Carry the direction through the relevant states, formats and input methods. Label assumptions and placeholders. Keep intermediates in `.work/temp/<task>/` under the [workspace rules](../../references/Workspace.md).
5. **Inspect and substantiate.** Inspect the result in its intended medium. For substantial visual work, follow the initial inspection with a distinct [visual critique](#visual-critique) using the brief, actual preview or export, and [relevant cases](references/ReviewAndDelivery.md). Recheck material corrections before delivery. Give the human the result and relevant editable sources, with key decisions and unverified conditions.

**Done:** The requested result works in its intended context to the extent verified, with evidence and any material gaps stated.

## Visual critique

1. Inspect the actual preview or export in its intended medium against the brief, relevant reference, and project conventions. Judge how it looks, feels to use, and communicates. Choose [representative cases](references/ReviewAndDelivery.md), including [realistic interface stress cases](references/UiStress.md) when they could change the judgment. Reuse [Test](../test/SKILL.md) evidence for behavior and measurements; a static image cannot establish live interaction or accessibility.
2. Give the location or condition, evidence, impact on use or communication, and a next step. Distinguish observed problems from inferences and matters of taste. State what remains unverified, and ask when a choice would materially change the agreed direction or outcome.
3. Stop at findings for review-only requests. When corrections are authorized, recheck the changed render before delivery. For a stress-related fix, recheck normal and adverse cases.
