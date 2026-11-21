# Project workspace

Use `.work/` at the project root for agent-owned files. In Git, use the current worktree root (`git rev-parse --show-toplevel`), including from a nested directory; for non-Git work, use the project root selected by the human. Put every agent-created temporary artifact in `.work/temp/<task>/` from the first write. Point scratch scripts, tool output, captures, logs and intermediate exports there before running the tool. Use designated paths for deliverables, maintained fixtures and docs. Create only the directories you need.

| Path | What belongs there |
| --- | --- |
| `.work/plans/0001-Sales-Contracts/` | Durable [Plan](../../plan/SKILL.md) records: `Evidences.md`, `Scope.md`, `Outcome.md`, `Plan.md`, and `Progress.md`. Short plans can stay in chat. Use a shared project location only when the human asks or the project explicitly requires it. Link related architectural decisions. |
| `.work/decisions/` | Default location for decision drafts and accepted architecture decision records (ADRs). [Architect](../../architect/SKILL.md#record-the-decision) uses the project's existing decision directory when present. |
| `.work/routines/` | Reusable project procedures specific to this device, such as a website deployment runbook that uses a local SSH alias. Look here for an existing routine before writing one. Keep it across tasks. |
| `.work/stashes/<task>/` | Temporary file-based snapshots or patches needed to set aside work. Record what they contain and how to restore them. |
| `.work/recover/<task>/` | A targeted recovery copy of important work at risk of being lost. Record its original path and how to restore it; check the copy before removing the original. This is not a trash folder or a routine backup. |
| `.work/briefs/0001-SalesContractsHandoff.md` | Standalone handoff prompts and other briefs without a designated destination. |
| `.work/temp/<task>/` | Disposable files the agent generates or copies: scratch code, renders, test output and working drafts. Remove your leftovers when no longer needed. |

Before the first project write in a Git worktree, inspect the root `.gitignore`. Create or repair it automatically. Replace a blanket workspace exclusion with these root-relative rules and preserve unrelated entries.

```gitignore
/.work/temp/
/.work/recover/
/.work/stashes/
/.work/routines/
```

Verify the effective rules with `git check-ignore --no-index` on representative files in each listed directory and at the workspace root. The four directories listed in the ignore rules should match. Files directly under `.work/` and records under `plans/`, `briefs/` and `decisions/` should remain visible. If a broader rule also affects other project paths, preserve it and add scoped exceptions for the workspace. Use `git check-ignore -v --no-index` to locate conflicting rules. Use `git ls-files -- .work/temp .work/recover .work/stashes .work/routines` to identify already tracked files in those directories and report them before writing there. Leave existing records and the index intact. Check that the intended workspace path stays inside the worktree when resolving symlinks.

## Numbered records

Plans and briefs each have their own sequence per worktree. ADRs use the repository's ADR numbering convention; in a new ADR collection, use the same numbering method as for plans and briefs. Start at `0001`; for a new record use one more than the highest sequence number in that collection, including numbered records moved to its archive. Ignore legacy dates when counting. Use at least four digits, a hyphen and a short title. Follow the project's naming convention for Markdown titles; use PascalCase if none exists, for example `0002-NextjsRewrite.md`. Use short hyphenated titles for plan folders. Put dates inside the record if useful.

When resuming work, find and reuse its existing record. Keep its number and path. Coordinate allocations when writers are working in parallel and check the prefix is unused before linking to a new record. Preserve legacy archives and old links when migrating existing records; write only to the canonical destination.
