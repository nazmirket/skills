# User experience

Use when an interaction or product task needs clearer choices, feedback, or recovery. Start from the person’s goal and the system's actual behavior. For steps spanning time, roles or channels, use [Journey](Journey.md).

## Design actions as state changes

Walk one primary journey from entry to completion and one consequential failure or interruption. For each important step, record what the person knows, what they can do, when the action takes effect, how they can undo or recover, and where focus and scroll position belong. Preserve data and task context across back navigation or retries where appropriate. Do not invent behavior or change a product rule through interface copy.

Design the states the action can actually reach: starting, loading or saving, empty or no matches, success, error, offline, denied, expired or unavailable as relevant. An empty collection and an unsuccessful search need different explanations. A delayed write needs a truthful pending or failure state; acknowledge the input promptly without claiming success early. Preserve useful controls while data updates, and avoid losing focus when replacing content.

- Use links for destinations and buttons for operations. Give controls names that match the outcome. Keep current location and a useful back path clear. Surface important actions without requiring hover or an undocumented gesture.
- Give fields persistent labels, constraints before commitment, and actionable errors by the affected inputs. Preserve valid entries and move focus predictably after failure. Where relevant, support native input types, paste, autofill, long values and international formats.
- Show consequences before irreversible or high impact actions. Prefer a safe undo when it fits the operation. Prevent accidental duplicate submissions while allowing meaningful retry or cancel.

## Review the whole task

For a long form, submit two invalid fields alongside a valid entry. A summary can take focus and link to each affected input, with matching field-level messages. Follow each link with the keyboard, correct one field, submit again and check that the remaining error is findable and the valid value survives. Adapt the pattern to the service's form length and validation timing. [GOV.UK error summary](https://design-system.service.gov.uk/components/error-summary/)

Trace the entry, user input, response, next step and recovery with realistic data. Check what the person knows before pressing an action and what becomes clear afterward. Preserve input when safe after errors, and surface consequences before hard-to-reverse actions. Avoid claiming that a plausible design has been validated with users unless that evidence exists.
