# Project workspace

Use `.work/` at the project root for agent-owned files. In Git, use the current worktree root (`git rev-parse --show-toplevel`), including from a nested directory; for non-Git work, use the project root selected by the human. Use the designated destination for actual deliverables, maintained fixtures and docs. Create only the directories you need.

| Path | What belongs there |
| --- | --- |
| `.work/plans/<task>/` | The task's plan, decisions, status and supporting evidence. |
| `.work/stashes/<task>/` | Temporary file-based snapshots or patches needed to set aside work. Record what they contain and how to restore them. |
| `.work/recover/<task>/` | A targeted recovery copy of important work at risk of being lost. Record its original path and how to restore it; check the copy before removing the original. This is not a trash folder or a routine backup. |
| `.work/briefs/` | Standalone handoff prompts and other briefs without a designated destination. |
| `.work/temp/<task>/` | Disposable files the agent generates or copies: scratch code, renders, test output and working drafts. Remove your leftovers when no longer needed. |

In Git projects, keep `/.work/` ignored unless the human explicitly names an exception. Before the first write, check the destination with `git check-ignore` and check `git ls-files -- .work` for tracked records. Establish a missing rule in `.gitignore` when authorized, or the repository's local Git exclude when appropriate. If the path is tracked, redirects through a symlink, or cannot be kept private, surface the problem before writing. Verify the staged paths again before committing; a general request to commit is not permission to force-add workspace files.
