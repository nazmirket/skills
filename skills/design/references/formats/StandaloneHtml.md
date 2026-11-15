# Standalone HTML

Use when an HTML file the recipient can open is the deliverable: an explainer, report, wireframe, demo, or small interactive prototype. Use [Web Design](WebDesign.md) for a surface that belongs in a running product. Add [Presentation Design](PresentationDesign.md) or [Diagram Design](DiagramDesign.md) only when that deliverable brings its own requirements.

## Define what the file must do

Agree on how the recipient will open it: directly from disk, from a supplied local server, or from another specified environment. Confirm whether it needs to work offline and whether the delivery must be a single file. Use local or embedded assets when portability requires them; if companions are allowed, keep their paths portable. Document any required network resources and what still works without them.

Match fidelity to the decision. A wireframe should make structure easy to compare; an interactive prototype should let someone complete the relevant path and reach its important alternate states. Use representative data, clearly distinguish simulation from actual operations, and avoid controls that imply a submission or external effect they cannot perform. Keep the file usable with ordinary navigation, keyboard input, and browser zoom. For variants, use the [prototype method](../../../execute/references/Prototype.md).

## Open the delivered copy

Open the actual file by the agreed method from a fresh location or browser session. Check essential content, narrow and wide layouts, and the representative interaction, including reset or recovery if applicable. Check missing assets or browser errors when they could explain a failure. If offline behavior is part of the contract, verify it without the network and without relying on a warm cache. A preview server does not establish that double-clicking the file works.

Deliver the requested file or folder with the entry point, dependencies if any, and a short note on simulated behavior and checks. Use [Browser](../tools/Browser.md) for direct inspection or [Playwright](../tools/Playwright.md) if repeatable evidence is needed.
