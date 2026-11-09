# Adaptive and accessible design

Use when an experience must work across devices, input methods, abilities, languages or display conditions. Apply the standards and platform requirements relevant to the actual task; do not claim formal conformance from a visual review alone.

## Responsive behavior

Start with the content and task at the available size. Determine what can wrap, stack, collapse, scroll within a bounded region or move to a different navigation pattern. Choose transitions where the content stops fitting rather than relying only on device labels. Preserve reading order and access to the same important operations across sizes.

Inspect narrow and wide layouts, meaningful intermediate widths, orientation changes and short viewports. Check overflow, overlapping sticky elements, clipped controls, image cropping and the reachability of primary actions. Test text enlargement and zoom where supported. Do not use fixed heights to hide overflow or disable zoom to force the layout to fit.

## Semantic and keyboard access

- Use the platform's semantic controls and landmarks for their intended roles. Give every interactive control an accessible name and expose relevant state, such as expanded or selected, through supported semantics.
- Follow the actual focus order through the flow. Focus must remain visible and not be hidden behind fixed elements. Provide a keyboard path for every essential action and return focus sensibly when an overlay closes.
- For dialogs and menus, ensure opening, navigation, dismissal and focus behavior are appropriate for the chosen pattern. Do not add ARIA that conflicts with native behavior.
- Give meaningful images text alternatives; omit redundant descriptions for decorative media. Communicate errors, selection and status through more than color. Announce dynamic changes when needed without repeatedly interrupting the user.
- Ensure controls are usable by touch and pointer, with appropriate target size and spacing for the platform and the applicable requirements. Do not make hover the only way to access an action or important information.

## Reading, preferences and locale

Check contrast in actual component states and themes. Respect reduced-motion and other relevant system preferences. Support variable content, localization and right-to-left layouts where the product requires them; mirror directional elements intentionally and do not assume that every icon should reverse. Check whether fonts cover the required scripts and whether translations expand or wrap safely.

## Native and embedded surfaces

When targeting a native or embedded platform, use its controls, safe areas, navigation, text scaling and interaction conventions instead of treating it as a resized webpage. Account for device input, system overlays, offline or interrupted states and platform-specific permissions where relevant.

## Evidence

Provide the affected sizes, states and accessibility expectations to [Critique](../../critique/SKILL.md) for rendered review. Use [Test](../../test/SKILL.md) for keyboard, device or accessibility behavior checks where appropriate. Automated checks alone cannot establish the complete experience. Report unavailable assistive technology or device verification explicitly.
