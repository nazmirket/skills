# Web design

Use for a website, browser-based product surface, or web component whose result needs to work in context. If the request is a critique, use the checks below to collect findings and stop there. For redesign, the live baseline still comes first. A small fix with a clear check does not need a new acceptance plan.

## Define the web result

Identify the affected routes or component entry points, the person using them, and what they should be able to do or understand. Use real content, approved assets, and the project's existing primitives and tokens. Pin the browser support policy, relevant viewport or container ranges, input methods, and states worth preserving. If support is unspecified, report which environments you checked without assuming a support matrix.

| Surface | Design toward | Prove with |
| --- | --- | --- |
| Marketing, product, or campaign | A specific proposition, credible proof, and a clear next action | An actual product view or example, enough context to decide, and a working action |
| Editorial, documentation, or learning | Legible reading order, orientation, and useful paths onward | A deep link and a realistic dense or long section |
| Store or catalog | Useful distinctions, accurate availability, and clear commitments | A representative comparison or filter, and a relevant empty or unavailable state |
| App, admin, or workspace | The active task, familiar controls, useful density, and clear feedback | A real completion or recovery path, including the state most likely to fail |

Make the surface recognizable through the subject, material, or task. Keep claims and product facts traceable; label stand-in assets, sample data, and simulated actions. Use a list for sequence, a table for exact comparisons, or a chart for a relationship worth seeing. Give important data its units, time period, and meaningful missing-value treatment. Keep essential information available without hover or color alone.

## Choose a supported implementation

Start with an established component or native primitive that meets the interaction, access, and compatibility requirements. For a meaningful browser API choice, check the project's required engines and versions and verify the supported fallback where needed. [Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance/get-started#baseline) is an optional source for a specific capability, not a step for every task. Use [Equip](../../../equip/SKILL.md) if the decision is whether to replace a dependency. Keep design-source differences that affect behavior or appearance visible in the handoff.

## Establish acceptance in the browser

Pick a primary path with realistic content and the smallest set of adverse conditions that might change the conclusion. An isolated component preview is useful evidence for that component; inspect the actual app path if you claim production behavior. For a prototype, identify what is simulated and verify only what the prototype promises.

- **Visual:** Open the actual result at representative sizes. Inspect hierarchy, legibility, layout, cropping, and assets. Try the awkward width or difficult content that matters. Compare before and after with the same data, state, viewport and zoom wherever possible.
- **Behavior:** Exercise the affected action through feedback and recovery. Where relevant, check keyboard entry, focus visibility and return, scrolling, motion preferences, invalid or missing data, and the supported fallback. For example, an open dialog screenshot says nothing about Escape or the focus after dismissal. Reuse current [Test](../../../test/SKILL.md) results that cover the same case.
- **Runtime:** For gaps a render cannot answer, check the relevant browser errors, failed requests or traces in the tested environment. A clean console does not prove the flow works, and a performance improvement needs comparable measurements.

Use [Browser](../tools/Browser.md) for a direct check, [Playwright](../tools/Playwright.md) when replayable interaction would add evidence, or [Screenshot](../tools/Screenshot.md) to record a visual state. Choose only what the evidence calls for. For craft decisions that change the result, consult [UX](../concepts/UX.md), [Responsive](../concepts/Responsive.md), or [Accessibility](../concepts/Accessibility.md).

When implementing a supplied design, use [Figma](../tools/Figma.md) or [OpenPencil](../tools/OpenPencil.md) if that is how the source can be inspected. Use [Storybook](../tools/Storybook.md) if an existing story can isolate a state that matters.

Give the working entry point or the requested review findings, with the tested revision or build, relevant view and state, and what was observed. Hand over editable source or approved assets when part of the deliverable. List meaningful departures and say which runtime, device, assistive technology, or fallback was not checked when that limits the claim.
