# Direction and composition

Use for a new visual direction, substantial redesign, page structure or composition. Keep explicit references and approved design decisions authoritative.

## Frame the work

Write down the person using the result, what they need to do or understand, where they encounter it, and what success looks like. Inventory the actual material: product capabilities, names, approved claims, images, data, brand assets and required content. Separate unknowns from facts. Ask the human only for gaps that change the direction; if authorized to decide, state the decision rather than presenting it as a fact supplied by them.

For an unsettled direction, inspect a small number of relevant examples from comparable products or media. Record the pattern that serves the user's task and the context that makes it work; treat a mood reference as inspiration unless the human asks for fidelity.

## Capture the redesign baseline

Before changing an existing interface, open the affected flow in a browser or its native runtime. Capture representative before views at relevant sizes and states. Record the entry point, environment, viewport and inputs so the same case can be reproduced. Record what must survive: approved content and data, brand assets, key actions and destinations, navigation, state changes and feedback, and accessibility or platform requirements. Separate a pre-existing problem from a regression risk and identify any behavior change the human requested.

If the existing interface cannot be viewed, stop the redesign and report the blocker; resume after the baseline is visible and captured. Available source or documentation can support orientation but cannot replace viewing the baseline. Pass the before evidence and invariants to [Critique](../../critique/SKILL.md) for the rendered comparison; use [Test](../../test/SKILL.md) to substantiate preserved behavior when it matters.

## Set the emphasis

Choose a composition based on the visitor's immediate job:

- **Decide or act:** reveal the offer, supporting evidence and the next action in a coherent sequence. Show the actual thing when that helps explain it.
- **Operate:** prioritize scanning, task continuity and clear feedback. Familiar placement and information density can matter more than decoration.
- **Read or learn:** organize content for orientation, sustained reading and retrieval; keep navigation available without competing with the text.
- **Experience:** let the work, image or interaction carry the message; keep controls clear and subordinate to the content.

A single project may have different surfaces with different priorities. Do not turn these categories into a fixed template.

## Compose the surface

1. List the essential content and actions in the order a person needs them. Remove unsupported claims and mark missing inputs. Choose one focal point that expresses the task's strongest real material.
2. Sketch the structural relationships: navigation, entry point, content groups, primary action and closing or next step. Decide which elements share an edge, which occupy full width, and where the eye moves next. Use columns, a list, a grid, a split or an open canvas only when it suits the content.
3. Set a hierarchy for each region. Use size, position, spacing, contrast and imagery together so a heading, data value or action is emphasized for a reason. Items that belong together should read as a group; separate different ideas enough to be distinguishable.
4. Vary repeated structures only when their content or role changes. A repeated pattern can aid scanning; excessive uniformity can hide differences. Conversely, decorative variety can make a workflow harder to learn.
5. Check the proposal with real copy, long labels, sparse content and dense content. Determine what should reflow, stack, crop or remain reachable as available space changes. Do not force fixed viewport-height sections if content can overflow or users need text enlargement.

## Make the direction specific

Describe a small set of intentional choices—tone, visual emphasis, type behavior, color roles, material and motion—and connect each to the audience or subject. Compare the proposal to the existing brief: would these choices still make sense if the product name changed? If so, look for a more specific expression of the actual content or use case. Distinctive does not have to mean loud, complex or novel at the expense of usability.

Show a bounded direction or representative slice when it resolves a consequential choice before broad implementation. Record which parts the human chose or authorized. A text description or wireframe can communicate intent but cannot prove the final appearance.
