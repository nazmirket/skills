# Command-line interfaces

Design from a job someone will perform in a shell. Keep the project's existing command names, flag placement, exit statuses and output formats when extending a shipped tool. Make each subcommand's help sufficient to discover its inputs, effects, results and a realistic invocation.

## Work through one caller's job

Suppose an operator must find a queued report export, inspect its status and preview cancellation. The following contract supports that job.

| Invocation | Observable result |
| --- | --- |
| `reports jobs list --limit 10 --json` | A single object with an `items` array of jobs and an opaque `next_cursor`, or `null` on the last page. Each job has a stable ID. The help documents how to resume with `--cursor`. |
| `reports jobs show exp_17 --json` | A single object such as `{"id":"exp_17","state":"queued"}`. Repeated reads have no side effects. |
| `reports jobs cancel exp_17 --dry-run --json` | Shows the selected job and proposed change. The stored job stays queued. The live command checks its current state again before cancellation. |

Use stable IDs for exact reads and writes. If a display name or search matches multiple jobs, return the candidates for selection. Bound list requests and document the default ordering, page size and end-of-results signal. A multi-page walk needs a defined continuation even when names repeat.

## Make machine output predictable

- Specify the exit status and streams for successful reads, empty results, invalid input, missing objects and service failures. In this example, an empty list is a successful empty collection. An unknown job returns a nonzero status and a JSON error on stderr such as `{"code":"job_not_found","id":"exp_17"}`, with empty stdout. A documented error code gives callers a stable branch when the human-readable message changes.
- Keep prompts, colors and progress bars out of machine output. Make the success payload parseable in a pipe and define what happens without a terminal. Require enough input to choose a write target unambiguously. Use the host's credential mechanism and redact secrets from both streams.
- Document which writes can be retried after a timeout. Where the service supports an idempotency key or a conditional update, preserve that protection through the CLI. If the result is uncertain, provide an exact read that can settle the state before retrying.

Check the installed entry point from a different working directory. Starting with help alone, follow a paginated list, select one of two similarly named jobs by ID, and read it. Parse stdout as JSON on success. For an unknown ID, capture status and both streams separately and parse the documented error. For a preview, check that the fixture stays unchanged and that the test service received no write request.
