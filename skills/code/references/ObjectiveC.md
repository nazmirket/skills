# Objective-C

Check the SDK and minimum deployment target, ARC status, framework conventions and Swift or C interoperability. Preserve existing public selectors and binary or archive compatibility where relied on.

- Verify object ownership and property attributes rather than assuming ARC removes lifetime risks. Use copy where snapshot semantics are needed, such as a published string or block property; use weak references where a relationship must not keep its counterpart alive. Check block capture and callback lifetimes before adding a weak capture or a strong cycle.
- Declare nullability and lightweight generics on exposed interfaces where supported. Do not assume a message to nil reports a failure; validate required objects at boundaries. Follow the project's error conventions and own the branch that consumes a nullable result or error object.
- Respect Cocoa and platform threading contracts. UI work belongs on the required main thread or queue; communicate async completion queue and ownership. For Core Foundation bridging, match the API's ownership rules rather than applying a cast mechanically.
- Preserve conventions for categories, delegates and protocols. Avoid side effects or conflicting methods in categories; prefer changes visible to both Objective-C and Swift callers.

Build for the actual deployment target and test the affected entry point and error path. Check callback release and Swift-imported signatures where relevant, using the project's leak or lifecycle tools if ownership changed.

Official: [Apple's Programming with Objective-C archive](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html), [Working with Blocks](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithBlocks/WorkingwithBlocks.html). Check current SDK headers for API availability.
