# Component preview

Use when the result is an isolated preview, state gallery, story, or comparison for a component. A quick inspection of a component in its real page may only need [Web Design](WebDesign.md). Choose [Storybook](../tools/Storybook.md) if it already fits the project; an isolated preview can serve the same decision without it.

## Make the relevant states reproducible

Name the component, audience of the preview, and the decision it should support. Render the real component through its normal inputs. Reuse the project's theme, tokens, providers and layout constraints where those affect the view. Mock at a clear input or data boundary and label what is simulated. Do not build an imitation of the component and present it as implementation evidence.

Expose only states that matter: for example, default and long content, selected and disabled, or loading, empty and recovery. Give each state or variant a stable name or entry point. Keep the inputs the same across comparisons except for the value under test. For interactions, provide a clear way to reset. Keep preview fixtures and controls outside the production surface.

## Check and hand off

Open each included case. Inspect the rendered state at the size and theme where the decision matters. Exercise the relevant input or transition: a labeled error example can confirm layout, while a failed action followed by a successful retry is evidence about the isolated behavior. Check the real application separately before claiming its routing, data, providers or surrounding layout work.

Return the preview entry point and state names, fixtures or editable source as requested, and any differences from production. Stop when the requested states are observable and the preview answers the stated question. For variants, use the [prototype method](../../../../references/Prototype.md) to carry the decision forward.
