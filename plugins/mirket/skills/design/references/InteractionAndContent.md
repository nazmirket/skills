# Web, UI and content

Use to organize a website, product surface or workflow. Decide what the person is trying to accomplish before choosing a visual pattern or a component.

## Shape the surface around the job

| Surface | Lead with | Check early |
| --- | --- | --- |
| Marketing, campaign or product page | A specific proposition, a concrete example or useful proof, and the next action when the visitor is ready | Does the page show what is actually offered? Do details answer the objections that would block action? |
| Editorial, documentation or learning | An orientation, readable sequence and useful routes back into the content | Can someone arrive at a deep link, know where they are and find what comes next? |
| Store or catalog | Useful distinctions, comparable information and clear action costs | Can a person narrow choices, understand availability and see what they are committing to? |
| App, admin or workspace | The active work, stable navigation, useful density and unambiguous feedback | Can a returning person repeat a task, pick up interrupted work and recover from failure? |

Adapt these choices to the project. A transactional screen inside a marketing site should behave like a transaction. A quiet, familiar table may be the right answer; a generic hero or ornamental dashboard may have nothing to do with the work.

## Design actions as state changes

Walk one primary journey from entry to completion and one consequential failure or interruption. For each important step, record what the person knows, what they can do, when the action takes effect, how they can undo or recover, and where focus and scroll position belong. Preserve data and task context across back navigation or retries where appropriate. Do not invent behavior or change a product rule through interface copy.

Design the states the action can actually reach: starting, loading or saving, empty or no matches, success, error, offline, denied, expired or unavailable as relevant. An empty collection and an unsuccessful search need different explanations. A delayed write needs a truthful pending or failure state; acknowledge the input promptly without claiming success early. Preserve useful controls while data updates, and avoid losing focus when replacing content.

- Use links for destinations and buttons for operations. Give controls names that match the outcome. Keep current location and a useful back path clear. Surface important actions without requiring hover or an undocumented gesture.
- Give fields persistent labels, constraints before commitment, and actionable errors by the affected inputs. Preserve valid entries and move focus predictably after failure. Where relevant, support native input types, paste, autofill, long values and international formats.
- Show consequences before irreversible or high impact actions. Prefer a safe undo when it fits the operation. Prevent accidental duplicate submissions while allowing meaningful retry or cancel.

## Let real content make the decisions

Give a heading or link enough context to make sense on its own. Use the audience's terms and stable labels for the same object or action. Lead with what happened and what to do next. Distinguish approved claims and actual data from illustrative copy. Do not invent endorsements, prices, metrics, features or stock availability.

Choose a list for order, a table for exact comparison, or a chart for a relationship worth seeing. Use real units, clear time periods, honest axes and useful treatment of missing values. Provide access to essential values without hover or color alone. Test constrained layouts with long values, realistic row counts, optional fields and screen enlargement.

## Build in the project's own language

Start with native or established primitives and tokens. Use the least complex implementation that expresses the design and provides real semantics, focus and behavior. A new library is useful only if it materially closes a gap in the current stack; if a choice is needed, compare relevant components and behavior, styling fit, performance cost, maintenance and migration effort through [Curate](../../curate/SKILL.md). A visual refresh does not by itself justify replacing the stack.

Build the real action and its critical states alongside its appearance. For a standalone demonstration, label synthetic data and mocked behavior; use the [prototype method](../../../references/Prototype.md) if the point is to settle a question. A production change must be exercised through its actual path.
