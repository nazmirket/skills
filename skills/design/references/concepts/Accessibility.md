# Accessibility

Use to make content and actions perceivable and usable with the relevant inputs, preferences and assistive technology. A screenshot or automated scan cannot establish conformance.

## Provide equivalent ways to act

- Start with semantic controls and native behavior. Give controls usable names, roles and states. Follow the focus order through the task and check that focus stays visible and unobscured. For overlays, check focus on entry, dismissal and return. In a modal dialog, Tab and Shift+Tab should cycle inside and Escape should close it. [W3C modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#keyboardinteraction)
- Make important operations usable with keyboard, touch and pointer. Keep targets easy to acquire at real scale, with space between neighboring actions. Offer a visible alternative to dragging, swiping or hover when it carries a meaningful action. Test a direct tap or click as well as keyboard for drag alternatives.
- Communicate status, selection and error with more than color or motion. Give meaningful images a context-appropriate alternative, keep decorative images out of the reading path, and make important chart information available as text or data. Announce status changes when they matter without repeating every render.
- Honor reduced motion and applicable display preferences. Check contrast against the actual surrounding surfaces, including imagery and supported themes. Verify visual and semantic disabled, busy and selected states. For native or embedded experiences, honor safe areas, text scaling, platform conventions and permission or offline states.

## Check the applicable standard

For an editable combobox with a listbox popup, distinguish the active suggestion from the committed value. Exercise typing, arrow navigation, Enter to accept and Escape to dismiss. Check the expanded state and accessible option as focus moves, including implementations that keep DOM focus on the input with `aria-activedescendant`. Verify dismissal preserves the value specified by that interaction. For multi-field validation, exercise the [form recovery sequence](UX.md#review-the-whole-task). [WAI-ARIA combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

For web work, identify the target level and scope of [WCAG 2.2](https://www.w3.org/TR/WCAG22/) or the project's applicable standard. For example, AA generally requires 4.5:1 contrast for normal text and 3:1 for large text; use the actual criterion and its exceptions. Check non-text contrast, target size, reflow, focus obstruction and an alternative to dragging as applicable. Use platform guidance where web criteria do not govern the surface. Aim for comfortable use, not just a minimum measurement.

Run the important path with the relevant inputs, preferences and difficult content in the actual preview. Use [Test](../../../test/SKILL.md) for distinct measurable behavior and follow [review and delivery](../flows/Critique.md) for visual assessment. Name the assistive technologies, devices, states or criteria that were not checked.
