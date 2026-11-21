# Swift

Confirm the Swift language mode, deployment targets, package or Xcode settings and concurrency checks. Use the project's platform and framework conventions; availability is part of the interface.

- Name APIs for clarity at the call site and state the effect or mutation. Prefer value semantics when copying a value should isolate changes. Use reference types for identity or shared state when that is intentional; account for resource ownership and retention by closures.
- Represent absence as an optional and distinct outcomes as enums or thrown errors where they improve the contract. Bind or validate at boundaries rather than forcing unwraps. Preserve recoverable failures with context.
- Make concurrent ownership clear with structured tasks, actors and appropriate isolation. Treat the main actor as a UI isolation boundary, and check whether values may cross actors. Understand reentrancy across await before assuming an actor protects a multi-step operation. Bound tasks and respect cancellation.
- At API boundaries, check availability, interoperability and error bridging. Prefer localized changes to blanket concurrency annotations or unchecked overrides where the compiler points to a real ownership gap.

## Check boundaries across suspension

- After an await, recheck any actor state a concurrent operation could have changed before applying a result. Give a task an owner that can cancel it when a view disappears or a newer request wins. Keep expensive non-UI work out of UI-isolated paths.
- Move deterministic work into a value or small function. Pass in the clock, store, or service where an effect crosses a boundary. Avoid protocol wrappers when a direct unit test or a real integration check covers the behavior with less indirection.
- Profile an optimized build on the device or simulator appropriate to the claim. Investigate main-thread stalls, avoidable repeated copying and retained objects rather than assuming value semantics or an async declaration makes a hot path cheap.

Run the configured build and tests on supported targets. Exercise isolation or UI lifecycle changes on the intended simulator or device where relevant, and report deployment target limitations separately.
