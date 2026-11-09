---
name: imagine
description: "Use when generating a visual reference for an interface from an agreed image brief, with implementation if requested. Use Design when the reference already exists."
---

# Imagine

Deliver a generated visual reference for the requested interface. If implementation is authorized, translate it into a working interface. For a supplied reference to reproduce as-is, use [Design](../design/SKILL.md).

## Agree on the brief

1. Inspect the product, authorized references and earlier decisions. For a redesign, view and capture the [live baseline and invariants](../design/references/direction-and-composition.md#capture-the-redesign-baseline); if the existing interface cannot be viewed, stop the redesign until it is visible and report the blocker.
2. Prepare the image brief: audience and primary task, screen hierarchy and actions, approved content and assets, visual direction (type, color, imagery and brand), target sizes and states, and accessibility or behavior constraints. Specify the reference views needed for the decision. Ask only about consequential gaps the available evidence cannot resolve.
3. Present the brief for explicit agreement before generating. Reuse explicit approval of the same brief. If the direction, scope or a material constraint changes, get agreement on the revised brief before generating again.

## Generate the visual direction

4. Use a capable tool in the current host with the agreed brief and authorized input images. Keep working images you generate or copy into the project in `.work/temp/<task>/` under the [workspace rules](../../references/workspace.md). Start with the fewest legible views that answer the brief. Add a detail view, a distinct state or a narrow layout only when an unresolved decision needs it; keep type, palette and components consistent. If a required reference or tool is unavailable, report the gap and bring any material fallback decision to the human.
5. Inspect the generated images against the brief and show the proposed direction. Identify drift or ambiguity. When implementation is authorized, proceed with an output consistent with the agreed direction; ask the human if choosing among outputs would materially change that direction. The approved brief does not authorize unrelated implementation.

## Turn the image into code

6. If the image is the whole deliverable, pass the final image and brief to [Critique](../critique/SKILL.md) and stop after delivery. Identify any generated stand-in that could be mistaken for real product material.
7. For authorized implementation, use [reference fidelity](../design/references/reference-fidelity.md) to extract visible detail, separate trusted material from generated placeholders, and record inferences and required departures. Apply [Design's develop-and-deliver steps](../design/SKILL.md#develop-and-deliver) with that evidence and the agreed brief. This route hands the visual comparison to Critique once and keeps behavior evidence separate.

**Done:** Deliver the inspected reference generated from the agreed brief and, if requested, the implementation with comparison evidence. Report any unresolved visual, functional or tool limits.
