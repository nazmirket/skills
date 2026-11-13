# Adaptive and accessible design

Use when a design must survive changes in space, device, input, ability, language or user preference. Check the applicable requirements for the medium and project. A render or automated scan alone cannot establish conformance.

## Reflow around the content

Decide what wraps, changes arrangement, stays visible or needs a local scroll region. Set transitions where the content no longer fits; preserve reading order, meaning and access to important actions. Use the actual context for navigation: a component embedded in a narrow panel may need a different layout even on a wide screen.

Inspect the narrow, wide and first awkward intermediate view, plus any important short viewport. Try long or translated labels, missing media, text enlargement and zoom. Check clipped popovers, sticky bars over focus or controls, offscreen actions, cropping and accidental horizontal scroll. Dense tables or canvases may need local scrolling; make the scroll area discoverable and keep surrounding controls usable. Preserve direction, order and reachability for right-to-left layouts when supported.

## Keep equivalent ways to act

- Start with semantic controls and native behavior. Give controls usable names, roles and states. Read the focus sequence through the task; keep it visible and unobscured. For overlays, test where focus goes on open, how to dismiss, and where it returns.
- Make important operations usable with keyboard, touch and pointer. Keep targets easy to acquire at real scale, with space between neighboring actions. Offer a visible alternative to dragging, swiping or hover when it carries a meaningful action. Test a direct tap or click as well as keyboard for drag alternatives.
- Communicate status, selection and error with more than color or motion. Give meaningful images a context-appropriate alternative, keep decorative images out of the reading path, and make important chart information available as text or data. Announce status changes when they matter without repeating every render.
- Honor reduced motion and applicable display preferences. Check contrast against the actual surrounding surfaces, including imagery and supported themes. Verify visual and semantic disabled, busy and selected states. For native or embedded experiences, honor safe areas, text scaling, platform conventions and permission or offline states.

## Apply the right benchmark

For web work, identify the target level and scope of [WCAG 2.2](https://www.w3.org/TR/WCAG22/) or the project's applicable standard. For example, AA generally requires 4.5:1 contrast for normal text and 3:1 for large text; use the actual criterion and its exceptions. Check non-text contrast, target size, reflow, focus obstruction and an alternative to dragging as applicable. Use platform guidance where web criteria do not govern the surface. Aim for comfortable use, not just a minimum measurement.

Run the important path with the relevant inputs, preferences and difficult content in the actual preview. Use [Test](../../test/SKILL.md) for measurable behavior and [Critique](../../critique/SKILL.md) to judge the rendered result. Name the assistive technologies, devices, states or criteria that were not checked.
