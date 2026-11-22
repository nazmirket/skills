# Accessibility

Use to make content and actions perceivable and usable with the relevant inputs, preferences and assistive technology. A screenshot or automated scan cannot establish conformance.

## Provide equivalent ways to act

- Start with semantic controls and native behavior. Give controls usable names, roles and states. Follow the focus order through the task and check that focus stays visible and unobscured. In a modal dialog, check initial focus, Tab and Shift+Tab cycling inside it, Escape dismissal and focus returning to the invoking control or the next logical step.
- Make important operations usable with keyboard, touch and pointer. Keep targets easy to acquire at real scale, with space between neighboring actions. Offer a visible alternative to dragging, swiping or hover when it carries a meaningful action. Test a direct tap or click as well as keyboard for drag alternatives.
- Communicate status, selection and error with more than color or motion. Give meaningful images a context-appropriate alternative, keep decorative images out of the reading path, and make important chart information available as text or data. Announce status changes when they matter without repeating every render.
- Honor reduced motion and applicable display preferences. Check contrast against the actual surrounding surfaces, including imagery and supported themes. Verify visual and semantic disabled, busy and selected states. For native or embedded experiences, honor safe areas, text scaling, platform conventions and permission or offline states.

## Check the applicable standard

For an editable combobox with a listbox popup, distinguish the active suggestion from the committed value. Exercise typing, arrow navigation, Enter to accept and Escape to dismiss. Check the expanded state and accessible option as focus moves, including implementations that keep DOM focus on the input with `aria-activedescendant`. Verify dismissal preserves the value specified by that interaction. For multi-field validation, exercise the [form recovery sequence](UX.md#review-the-whole-task).

Identify the target level and scope of the project's applicable standard. For web content evaluated against WCAG 2.2 AA, normal text generally needs 4.5:1 contrast and large text 3:1. Large text here means at least 18 pt, or 14 pt bold. Apply the relevant criterion and exceptions to the actual state. Also assess non-text contrast, target size, reflow, focus obstruction and alternatives to dragging where applicable. Use platform conventions for native surfaces.

Run the important path with the relevant inputs, preferences and difficult content in the actual preview. Record observed behavior and measurements. Use [Critique](../flows/Critique.md) when the request includes a design assessment. Name material gaps in assistive technology, device, state or criteria coverage.
