# Dart

Read the SDK constraint, analysis options, target platforms, and package's public exports. Use [Flutter](Flutter.md) for widget lifecycle, layout, and frames.

- Keep the public library surface intentional. Make required inputs and nullability reflect real contracts; parse external values once and keep internal models typed. Use enums or sealed types for fixed cases when the SDK supports them. Keep collection ownership clear: a final reference does not make a list immutable.
- Choose the async contract by result shape. A `Future` gives one result or failure; a `Stream` exposes a sequence with a lifetime. Cancel owned subscriptions, close owned controllers, and distinguish single-subscription and broadcast streams before changing consumption. Bound concurrent work; throwing from one operation does not automatically stop independent futures.
- Keep pure transformations free of framework state. Prefer direct constructors and functions; add a dependency seam when time, I/O, or a platform adapter makes the boundary hard to exercise. Reserve isolates for CPU work that needs separation; measure messaging and transfer overhead and verify target support.
- Watch repeated iterable traversal and materialization. Lazy work is useful when consumers stop early, but repeated traversal may repeat expensive operations. Materialize once when consumers need a stable reusable snapshot and the size fits.

Use the package's analyzer and tests. Exercise malformed input and stream completion, error or cancellation when affected. Compare production-like builds and representative input sizes before claiming a performance gain.
