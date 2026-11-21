# Hook improvements

Execution authorized; this written plan has not been separately approved.

1. Identify supported host events and existing behavior, then write focused regression tests with isolated repositories.
2. Improve shell recognition warnings, add staged workspace index inspection and assess safe handling of shared Stop state.
3. Run focused and project checks, inspect scope and report remaining host and enforcement limits.

## Current status

Implemented warnings for recognizable unsupported commit forms and target-index inspection for supported direct commits, including exact human-authorized `.work` exceptions. Denied recognized compound commit commands to prevent a preceding shell command from changing the inspected index or working directory. Nineteen synthetic tests pass; `git diff --check` passes. Host activation and live behavior remain unverified. Shared Stop continuation state and the extra continuation on simple responses remain unresolved: Claude's Stop event does not document a turn ID, and no safe cross-host condition has been established to distinguish another hook's continuation or safely skip cleanup. No independent review was performed.
