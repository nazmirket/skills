# Project workspace

Use `.work/` at the project root for agent-owned files. In Git, use the current worktree root (`git rev-parse --show-toplevel`), including from a nested directory; for non-Git work, use the project root selected by the human. Use the designated destination for actual deliverables, maintained fixtures and docs. Create only the directories you need.

| Path | What belongs there |
| --- | --- |
| `.work/plans/0001-Sales-Contracts/` | The task's outcome, agreement, plan, status and supporting evidence. Small plans may keep the record in one file; see [Plan](../skills/plan/SKILL.md). Link related architectural decisions. |
| `.work/decisions/0001-Project-Cleanup.md` | Architectural decision records after decisions are made. |
| `.work/stashes/<task>/` | Temporary file-based snapshots or patches needed to set aside work. Record what they contain and how to restore them. |
| `.work/recover/<task>/` | A targeted recovery copy of important work at risk of being lost. Record its original path and how to restore it; check the copy before removing the original. This is not a trash folder or a routine backup. |
| `.work/briefs/0001-Sales-Contracts-Handoff.md` | Standalone handoff prompts and other briefs without a designated destination. |
| `.work/temp/<task>/` | Disposable files the agent generates or copies: scratch code, renders, test output and working drafts. Remove your leftovers when no longer needed. |

In Git projects, keep `/.work/` ignored unless the human explicitly names an exception. Before the first write, check the destination with `git check-ignore` and check `git ls-files -- .work` for tracked records. Establish a missing rule in `.gitignore` when authorized, or the repository's local Git exclude when appropriate. If the path is tracked, redirects through a symlink, or cannot be kept private, surface the problem before writing. Verify the staged paths again before committing; a general request to commit is not permission to force-add workspace files.

## Numbered records

Plans, decisions, and briefs each have their own sequence per worktree. Start at `0001`; for a new record use one more than the highest sequence number in that collection, including numbered records moved to its archive. Ignore legacy dates when counting. Use at least four digits and a short hyphenated title, for example `0002-Nextjs-Rewrite.md`. Put dates inside the record if useful.

When resuming work, find and reuse its existing record. Keep its number and path. Coordinate allocations when writers are working in parallel and check the prefix is unused before linking to a new record. Preserve legacy archives and old links when migrating existing records; write only to the canonical destination.
