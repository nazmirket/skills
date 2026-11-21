# Scene design

Use for a 3D asset, scene, still render, or interactive viewer. Identify the actual deliverable and where it will be used: a good render does not establish that an asset imports correctly or that a scene runs within budget.

## Set the target and prove the shape

Name the consumer, expected scale and framing, and any constraints on format, device, asset size or performance. For an editable or runtime asset, record units, up direction, origin or pivot, and which of geometry, materials, lights, cameras or animation must survive handoff. Agree on what the reference establishes and label unobserved views or inferred measurements.

Block out the important shapes and camera first. Compare their silhouette and proportions from the intended view and an alternate view that would reveal a mismatch. For example, a product can match a front reference and still have the wrong depth in an orbit view. Check contact, light and material separately before adding small detail: make sure surfaces read under neutral light, then judge mood in the final lighting. Match level of detail to real display size and budget.

## Verify in the intended consumer

| Deliverable | Evidence |
| --- | --- |
| Render or shot | Open the actual export; inspect framing, silhouette, materials, shadows, depth cues and clipping at intended size. Check motion at speed when delivered. |
| Reusable asset | Open the export in the target viewer or importer; compare scale, axes, pivot, normals, textures and materials, and animation when required. A successful export command proves only that a file was written. |
| Interactive scene | Exercise representative input, camera bounds and reset; check loading, failure or fallback, and any relevant motion or input alternative. Verify budgets on the intended device or report the tested substitute. |

Use [Gestures](../concepts/Gestures.md) for direct manipulation and [Motion Design](MotionDesign.md) when a sequence is a separate result. For interchange, test the exported scene in the receiving viewer. Verify the active camera, coordinate scale, materials and any animation clips needed there. Give the requested render, asset, or playable entry point, plus editable source and necessary dependencies where in scope. Name the consumer and settings used, and report import, interaction, or performance checks you could not run.

Use [Blender](../tools/Blender.md) when the source or export work belongs there, or [Spline](../tools/Spline.md) when the result is a Spline scene or embed.
