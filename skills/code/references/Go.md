# Go

Read the Go toolchain and module settings, build tags, supported platforms, and service conventions. Use the standard toolchain and existing package layout where sufficient.

- Keep types and interfaces small and useful. Put interfaces near consumers when that reflects what they need. Return concrete types where callers gain useful behavior from them; avoid abstraction before there is a genuine alternative.
- Handle errors where a decision can be made. Add useful operation context, preserve a cause with wrapping when callers need to recognize it, and use `errors.Is` or `errors.As` rather than comparing prose.
- Propagate `context.Context` into work that uses its deadline or cancellation. Make goroutine lifetimes, channel closing, and child work explicit. Do not spawn a worker without an exit path. Prefer a mutex or synchronous call when it makes ownership clearer than a channel.
- Keep zero values useful where practical and avoid typed nils in interface returns. Fit existing ownership and resource cleanup conventions; confirm whether a defer belongs in the current function or a per-iteration helper.

Run the relevant `go test` commands, `gofmt`, and existing vet or CI checks; use the race detector for touched concurrency if the target supports it. Check cancellation and failure, not just the happy path.

Official: [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments), [Effective Go](https://go.dev/doc/effective_go) for established idioms; verify newer APIs against the installed version.
