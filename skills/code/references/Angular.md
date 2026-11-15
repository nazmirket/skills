# Angular

Confirm Angular and tooling versions, standalone or NgModule conventions, change detection setup, and RxJS use. Fit the existing feature structure instead of migrating it by preference.

- Keep components centered on a view and its interactions. Move independent policy or infrastructure to a suitable service; choose dependency injection scope intentionally so state is shared only as far as needed.
- Use computed signals for synchronous derived values where supported. Use effects for synchronization with imperative dependencies and RxJS where stream composition or asynchronous cancellation matters. Do not convert between the models without a clear boundary.
- Keep subscription lifetimes tied to their owner using available mechanisms such as the async pipe or lifecycle-aware teardown. Match concurrency behavior to intent: a search should discard stale results, while a save may need to queue or prevent duplicate submissions.
- Prefer the repository's typed form conventions. Show disabled, pending, invalid and server rejection states intentionally. Lazy loading and newer template syntax are useful when supported and appropriate, not required migrations.

## Make the change observable

- Organize by feature and keep injection scoped to the intended lifetime. Singleton services are useful for shared coordination but can accidentally retain state that should reset on navigation. Use a pure function for a rule that needs neither lifecycle nor I/O.
- Pick a stream operator for semantics: replace outdated reads, serialize order-sensitive writes, or ignore duplicate submits while one is active. Verify the server contract when replacing a request; unsubscribing does not imply the server undid a mutation.
- Profile expensive templates or change detection before changing strategy. Track list identity by a stable key, keep costly calculations out of repeated template evaluation, and check that narrowed update rules still handle external changes.

Check template compilation and test the real user path with a fake dependency or HTTP boundary; include navigation, teardown or failed requests where they could change observed behavior.

Official: [Angular style guide](https://angular.dev/style-guide), [Signals](https://angular.dev/guide/signals).
