# Go

Read the Go toolchain and module settings, build tags, supported platforms, and service conventions. Use the standard toolchain and existing package layout where sufficient.

- Keep types and interfaces small and useful. Put interfaces near consumers when that reflects what they need. Return concrete types where callers gain useful behavior from them; avoid abstraction before there is a genuine alternative.
- Handle errors where a decision can be made. Add useful operation context, preserve a cause with wrapping when callers need to recognize it, and use `errors.Is` or `errors.As` rather than comparing prose.
- Propagate `context.Context` into work that uses its deadline or cancellation. Make goroutine lifetimes, channel closing, and child work explicit. Do not spawn a worker without an exit path. Prefer a mutex or synchronous call when it makes ownership clearer than a channel.
- Keep zero values useful where practical and avoid typed nils in interface returns. Fit existing ownership and resource cleanup conventions; confirm whether a defer belongs in the current function or a per-iteration helper.

## Scope changes to packages and workloads

- Expose behavior callers actually need. Table tests can cover multiple outcomes without creating another interface; use an external package test for a public contract or an integration check for a real adapter. Preserve context when wrapping errors, and decide which wrapped errors are part of the API.
- Separate shared state ownership from goroutine count. Use a bounded work queue only when independent jobs benefit from overlap. Exercise cancellation while sending or waiting and verify shutdown can finish even when a consumer stops early.
- Use a benchmark with realistic payloads and report allocation cost when relevant. Use execution or contention profiles to tell copying, blocking and algorithmic cost apart; avoid pools or preallocation until size distribution and measurements justify them.

Run the relevant `go test` commands, `gofmt`, and existing vet or CI checks; use the race detector for touched concurrency if the target supports it. Check cancellation and failure, not just the happy path.

Official: [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments), [Effective Go](https://go.dev/doc/effective_go) for established idioms; verify newer APIs against the installed version, [Go diagnostics](https://go.dev/doc/diagnostics).
