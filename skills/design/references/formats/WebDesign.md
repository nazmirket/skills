# Web design

Use for a website, app or browser component in context. Critique ends with findings. A redesign starts from the live baseline. A visual check of even a small edit requires a [verified full-resolution original](../tools/Screenshot.md).

## Define the web result

Name the route, person, task and point of completion. Work with real content, approved assets and the project's components and tokens. Establish the target engines or browser policy, viewport or container range, inputs and states. Keep proposed improvements within the site's identity and existing user commitments.

| Surface | Design around | Verify in context |
| --- | --- | --- |
| Marketing or campaign | A specific offer, credible proof and useful next action | Show the offer in use and exercise its action |
| Editorial or learning | Reading order, orientation and meaningful paths onward | Open a deep link and read a dense section at narrow width |
| Store or catalog | Differences that affect a decision, availability and commitments | Compare real items and reach a relevant empty or unavailable state |
| App or workspace | The active task, familiar controls, appropriate density and feedback | Complete a real path and exercise its most consequential failure or recovery |

Choose a list for a sequence, a table for exact comparisons or a [chart](DiagramDesign.md#compare-values-and-trends) for a pattern in quantities. Show units, period and missing data. Supply labels or other cues for information conveyed by color or hover. Mark simulated controls, placeholder assets and sample data.

## Choose a supported implementation

Start from the semantic element or existing component that serves the task. Write down what must still work on the oldest supported engine. An optional animated transition can disappear there. A disclosure that contains required shipping information still needs a working way to open, read and close it.

For a newer platform capability, check the installed stack and project's actual browser targets. Prefer a working base path, then add the enhancement via a capability test or CSS feature query where needed. Verify the basic experience with the enhancement disabled and exercise the enhanced path in a supporting browser. An API's presence alone does not establish focus, dismissal or content visibility. For layout tied to a component's space, test its narrow container in a wide viewport as well as its full-page placement. Start from real content breaks, logical layout for writing direction and intrinsic media sizing. Reserve media dimensions to avoid shifting the reading position.

## Establish acceptance in the browser

- **Appearance.** For page or layout conclusions, capture a full, high-resolution original for each relevant route, state and responsive layout. For a component-only claim, capture the complete component in context at native resolution and limit the verdict to that state. Review the whole page and native-pixel details for hierarchy, crop, typography, overflow, state feedback and the final section. Match baseline and revision. Include exact viewport states for overlays and sticky elements. Follow [Screenshot capture](../tools/Screenshot.md) when panels scroll independently or the renderer truncates the document.
- **Interaction.** Exercise the affected action through feedback and recovery. Check keyboard entry, focus visibility and return, zoom, narrow widths, reduced motion, invalid or missing data and the supported fallback as they apply. A dialog image can show a clipped button. Establish Escape dismissal and focus return with the keyboard.
- **Runtime.** Use the [browser](../tools/Browser.md) to narrow a visible failure with computed style, network status or page errors. Use [Playwright](../tools/Playwright.md) when repeatability, state isolation or traces help. Measure real operating conditions for performance claims. Report whether evidence comes from a component preview, simulated prototype or actual product path.

For craft decisions consult [UX](../concepts/UX.md), [Responsive](../concepts/Responsive.md) or [Accessibility](../concepts/Accessibility.md). For a supplied source use [Figma](../tools/Figma.md) or [OpenPencil](../tools/OpenPencil.md) if that is how it can be inspected. An isolated state may use [Storybook](../tools/Storybook.md) or [Component Preview](ComponentPreview.md). Use [Mobile Design](MobileDesign.md) when device behavior governs the result.

Return the working entry point or findings, capture paths, tested build, view and state, observed behavior and material gaps. Include editable sources and approved assets when requested.
