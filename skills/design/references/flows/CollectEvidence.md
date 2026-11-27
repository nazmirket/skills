# Collect design evidence

Establish the target, decision it will inform and relevant conditions. Return traceable observations, reproducible inputs and gaps.

## Check an interaction

For a specific behavior question, identify the starting state, input and expected outcome. Reuse a matching observed interaction or exercise it through the real controls. For example, open a dialog by keyboard, press Escape and observe both whether it closes and which control receives focus. Report the sequence and result. To judge how the indicator looks, [capture the focused control in context](../tools/Screenshot.md).

## Collect visual evidence

- Open the actual artifact or runtime. Record its location or version, entry point, content and state, input, viewport or physical size. Distinguish direct observations from supplied images, reports and inferences.
- Reuse or obtain a [verified original covering the claim](../tools/Screenshot.md) for each reviewed state. Record any gap in coverage, state or density.
- Use the matching [tool guide](../tools/README.md) before giving a requested procedure or attempting an unfamiliar operation. For example, a Figma handoff procedure uses [Figma](../tools/Figma.md). A tool name in already sufficient evidence adds no procedure of its own.
- Inventory available content, approved assets, brand cues, interaction conventions and known constraints. Record source, permissions and freshness of material assets. For a redesign, inspect the current interface live before editing. Gather the primary path and important navigation, feedback, error and access states. If the runtime is unavailable, leave the live baseline open.

## Stress content

Use valid lengths, counts, missing values and language conditions from the actual model. For a member row, file list or numeric table, select a pair from the [content stress fixtures](../../assets/content-stress.json). Use the same component, viewport, locale, theme and input method for both states. Load the values through a local story, test adapter or safe override. Keep the fixtures out of production.

| Fixture | What the adverse data can expose | Check in the running component |
| --- | --- | --- |
| Member row | A name beginning with a joined emoji can produce a broken avatar initial. A long name and address can push the row action out of reach. | With the avatar absent, inspect the fallback. Tab to the member action at the narrow supported width and activate it. Confirm which member it acts on. |
| File list | Two filenames share a long prefix and differ near the extension. End truncation can make them look identical. | Using the supported input, identify the signed copy before opening it. Open it and confirm the file ID. Check whether the full name is available on keyboard and touch where supported. |
| Numeric table | A negative amount, true zero and missing amount can collapse to the same display. Grouped digits can lose their sign, unit or column alignment. | Format the integer amounts as USD cents in the target locale. Read each row with its label and unit. Confirm the negative remains negative, zero remains zero and the missing amount is visibly distinct. |

Map only fields and values that the product accepts. If its range or nullability differs, choose its nearest valid boundary. Report the exact value, affected action and observed outcome with the matched [captures](../tools/Screenshot.md).
