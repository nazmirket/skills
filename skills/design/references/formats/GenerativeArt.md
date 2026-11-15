# Generative art

Use when rules or an algorithm produce the artwork and the result is a selected still, animation, interactive piece, or reusable generator. A single generated image can be material for [Illustration Design](IllustrationDesign.md); it does not by itself require a generator handoff.

## Tie variation to the visual idea

Decide what the process should express and which relationships make the outputs recognizable as a family. Translate that intent into rules about elements, space, time and change. For example, if the piece shows currents converging, vary path density or direction while keeping the region where they meet legible. Keep variation that contributes to the idea and constrain variation that erases it.

Make a small set of sample outputs before adding controls. Separate stable rules from meaningful parameters; choose useful defaults and bounded ranges. Offer named controls, reset or replay only if someone will use them. Use a seed when selection or reproduction matters. Record the selected settings and relevant runtime, version or assets; a seed alone cannot account for fonts, time or rendering differences. Use original rules and approved assets and distinguish outputs from factual imagery.

## Verify the range and selected result

Inspect the default, the selected result, and boundary combinations likely to fail. Adjust rules that regularly produce empty, clipped, unreadable or overly costly results. For live work, check representative device performance and the needed control or fallback, such as a still or reduced-motion path. Use [Motion Design](MotionDesign.md) if timed playback is a separate deliverable.

Reopen the exported still or animation and check dimensions, background and end or loop behavior as relevant. If reproducibility was promised, regenerate the selected result from the saved settings under the defined conditions. Deliver the requested artwork or generator, plus seed, parameters, source and environment details when applicable. A standalone viewer or framework belongs in the handoff only if the brief needs it.
