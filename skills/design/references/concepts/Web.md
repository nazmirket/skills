# Web design

Use for websites and browser-based product surfaces. Design for browser behavior and real content, then inspect in the browser.

## Shape the surface around the job

| Surface | Lead with | Check early |
| --- | --- | --- |
| Marketing, campaign or product page | A specific proposition, a concrete example or useful proof, and the next action when the visitor is ready | Does the page show what is actually offered? Do details answer the objections that would block action? |
| Editorial, documentation or learning | An orientation, readable sequence and useful routes back into the content | Can someone arrive at a deep link, know where they are and find what comes next? |
| Store or catalog | Useful distinctions, comparable information and clear action costs | Can a person narrow choices, understand availability and see what they are committing to? |
| App, admin or workspace | The active work, stable navigation, useful density and unambiguous feedback | Can a returning person repeat a task, pick up interrupted work and recover from failure? |

Adapt these choices to the project. A transactional screen inside a marketing site should behave like a transaction. A quiet, familiar table may be the right answer; a generic hero or ornamental dashboard may have nothing to do with the work.

## Let real content make decisions

Give a heading or link enough context to make sense on its own. Use the audience's terms and stable labels for the same object or action. Lead with what happened and what to do next. Distinguish approved claims and actual data from illustrative copy. Do not invent endorsements, prices, metrics, features or stock availability.

Choose a list for order, a table for exact comparison, or a chart for a relationship worth seeing. Use real units, clear time periods, honest axes and useful treatment of missing values. Provide access to essential values without hover or color alone. Test constrained layouts with long values, realistic row counts, optional fields and screen enlargement.

## Build in the project's own language

Start with native or established primitives and tokens. Use the least complex implementation that expresses the design and provides real semantics, focus and behavior. A new library is useful only if it materially closes a gap in the current stack; if a choice is needed, compare relevant components and behavior, styling fit, performance cost, maintenance and migration effort through [Equip](../../../equip/SKILL.md). A visual refresh does not by itself justify replacing the stack.

Build the real action and its critical states alongside its appearance. For a standalone demonstration, label synthetic data and mocked behavior; use the [prototype method](../../../../references/Prototype.md) if the point is to settle a question. A production change must be exercised through its actual path.

Match any new browser primitive to the browser support the project requires. Check actual focus, navigation, layout and fallback behavior in the browsers you claim to support.
