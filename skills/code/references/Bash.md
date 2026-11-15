# Bash

Check the actual interpreter, minimum Bash version, and host tools. If the contract is POSIX sh, avoid Bash-only syntax. macOS or CI images can provide older Bash and different utility flags.

- Quote expansions that represent one argument. Use arrays for argument lists and pass arguments directly rather than constructing commands as strings. Preserve boundaries with `"$@"`; use a supported option terminator when passing arbitrary filenames. Do not evaluate untrusted text as shell code.
- Handle exit status deliberately. Test expected failures in conditionals. Understand what `errexit` ignores and whether `pipefail` fits the pipeline; strict options do not replace success or error handling. Keep diagnostics on stderr and stdout usable for callers.
- Check paths and inputs before mutation and scope cleanup to scratch paths the script owns. Use a secure temporary directory and register cleanup only after successful creation. Prefer a plan or explicit dry run where the action is hard to undo.
- Keep shell for glue. Move complex parsing, concurrency or persistent state into a language better suited to it. Reuse known portable primitives instead of complex one-liners.

Run `bash -n` and existing lint, such as ShellCheck if present. Try spaces, leading hyphens, empty input, a failing command, and the target host's utilities.

Sources: [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html), [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) for practical patterns and tradeoffs.
