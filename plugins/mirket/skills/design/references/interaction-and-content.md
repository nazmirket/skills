# Interaction and content

Use for screens, components, flows, navigation, forms, dashboards and data-rich interfaces. Design the task and its states, not just the initial view.

## Map the journey

Describe the user's starting point, goal, information required, decisions and exit. Trace the primary path and the meaningful alternatives: cancellation, back navigation, interruptions, permission denial, retries and recovery. Respect the platform's navigation patterns and preserve work where appropriate.

For each action, determine what it changes, whether it can be reversed, what feedback is needed and where focus moves. Use a destructive confirmation only when the action and its consequences warrant interruption. Distinguish an action that changes data from a link that navigates.

## Forms and input

- Give inputs persistent labels, useful instructions and suitable input types. Indicate required fields and constraints before submission rather than relying on placeholder text.
- Validate at a useful point in the workflow. Put an actionable error next to the relevant input and provide an overview for longer forms when useful. Preserve valid entries and move focus predictably after failure.
- Show submission progress and prevent unintended duplicate actions without trapping the user. Support cancellation, retry and success; explain what happened and what the person can do next.
- Consider autofill, paste, password managers, international names, long values, multiple locales and input method differences where relevant. Do not create requirements or claims the product has not established.

## Navigation and controls

Give labels that describe the destination or action. Make the current location or selected state clear, preserve a coherent back path, and keep related operations together. Ensure visible controls produce their stated outcome; a decorative mock interaction is not finished functionality. Use familiar patterns when they reduce learning cost, and make unusual interaction discoverable.

## Data, lists and charts

Determine the question the data must answer before choosing a display. Use lists for ordered content, tables when precise comparison matters, and charts when a visual relationship helps. Keep units, labels, time range and missing values clear. Avoid visual encodings that distort the underlying values. Provide a text or tabular alternative when meaningful, and do not rely solely on color, hover or a tooltip to convey essential information.

For lists and tables, account for empty results, loading, error, long values, sorting or filtering where applicable, and the difference between no data and no matches. Keep actions identifiable on touch and keyboard.

## Interface writing

Use the audience's vocabulary. Name the actual action, object or outcome consistently across controls and feedback. Keep error messages specific about the problem and a useful next step; use an empty state to explain what is absent and how to proceed. Avoid invented metrics, customer endorsements, guarantees, prices or product capabilities. When real copy is missing, mark a placeholder rather than presenting it as verified fact.
