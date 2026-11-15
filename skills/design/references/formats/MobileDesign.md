# Mobile design

Use for a native app surface or a web experience whose mobile task and device behavior drive the design. Use [Responsive](../concepts/Responsive.md) when the work is primarily layout reflow. Consult the shared [mobile interaction principles](../concepts/Mobile.md) for task reach, touch and platform conventions.

## Establish the device and task

Identify the platform, main task and starting point, supported device or window sizes, and input or accessibility conditions. Preserve established navigation, meaningful state and platform conventions. For an existing interface redesign, inspect the affected path in the live runtime before proposing changes.

Decide what must remain reachable when system UI changes the available space. For example, in a short checkout view, a sticky action should not cover the focused field, hide its error, or make the next step unreachable when the keyboard is open. Decide how back, dismissal and interruption handle entered data. Use established components and provide a visible alternative when a gesture carries an important action.

## Verify the task in context

Run the main task and the most revealing adverse state in the intended app or mobile browser. Include relevant cases such as system text enlargement, a long label, a software keyboard, a safe-area edge, or an interruption and return. Exercise orientation, connectivity, assistive technology, or alternate inputs when the task depends on them. For example, confirm that a retry makes progress clear and preserves input when the connection drops mid-flow.

Use a representative physical device when hardware, input, system behavior or performance changes the result. Report simulator or [browser emulation](../tools/Browser.md) evidence as such. Deliver the build, prototype or design source requested, with the path and states checked, environment, and known gaps. A phone-sized capture shows layout; it does not prove the task worked.
