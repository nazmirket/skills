# Swift

Confirm the Swift language mode, deployment targets, package or Xcode settings and concurrency checks. Use the project's platform and framework conventions; availability is part of the interface.

- Name APIs for clarity at the call site and state the effect or mutation. Prefer value semantics when copying a value should isolate changes. Use reference types for identity or shared state when that is intentional; account for resource ownership and retention by closures.
- Represent absence as an optional and distinct outcomes as enums or thrown errors where they improve the contract. Bind or validate at boundaries rather than forcing unwraps. Preserve recoverable failures with context.
- Make concurrent ownership clear with structured tasks, actors and appropriate isolation. Treat the main actor as a UI isolation boundary, and check whether values may cross actors. Understand reentrancy across await before assuming an actor protects a multi-step operation. Bound tasks and respect cancellation.
- At API boundaries, check availability, interoperability and error bridging. Prefer localized changes to blanket concurrency annotations or unchecked overrides where the compiler points to a real ownership gap.

Run the configured build and tests on supported targets. Exercise isolation or UI lifecycle changes on the intended simulator or device where relevant, and report deployment target limitations separately.

Official: [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/), [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/).
