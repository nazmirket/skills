# Project workspace

Use `.work/` at the project root for agent-owned files. In Git, use the current worktree root (`git rev-parse --show-toplevel`), including from a nested directory; for non-Git work, use the project root selected by the human. Put every agent-created temporary artifact in `.work/temp/<task>/` from the first write. Point scratch scripts, tool output, captures, logs and intermediate exports there before running the tool. Use designated paths for deliverables, maintained fixtures and docs. Create only the directories you need.

| Path | What belongs there |
| --- | --- |
| `.work/plans/0001-Sales-Contracts/` | Durable [Plan](../../plan/SKILL.md) records: `Evidences.md`, `Scope.md`, `Outcome.md`, `Plan.md`, and `Progress.md`. Short plans can stay in chat. Use a shared project location only when the human asks or the project explicitly requires it. Link related architectural decisions. |
| `.work/decisions/` | First ADR collection for projects without an established location. Save drafts and subsequent ADRs in the project's designated or existing collection, following [Architect's placement and status rules](../../architect/SKILL.md#record-the-decision). |
| `.work/routines/DeploySkillsWebsite.md` | A reusable project procedure specific to this device. Store each routine directly in `.work/routines/` as one self-contained Markdown file. Give it a descriptive PascalCase filename without a numeric prefix. Include the prerequisites, steps and verification in the same file. Reuse the existing routine across tasks. |
| `.work/stashes/<task>/` | Temporary file-based snapshots or patches needed to set aside work. Record what they contain and how to restore them. |
| `.work/recover/<task>/` | A targeted recovery copy of important work at risk of being lost. Record its original path and how to restore it; check the copy before removing the original. This is not a trash folder or a routine backup. |
| `.work/briefs/0001-SalesContractsHandoff.md` | Standalone handoff prompts and other briefs without a designated destination. |
| `.work/temp/<task>/` | Disposable files the agent generates or copies: scratch code, renders, test output and working drafts. Remove your leftovers when no longer needed. |

Before the first project write in a Git worktree, check the project’s workspace policy and effective ignore rules. If the project specifies which records are private or shared, preserve that policy and check the intended scratch path against it. Use `git ls-files` to identify already tracked scratch files and report them before writing there. Leave the index and existing records intact. Resolve the intended path to verify it stays inside the worktree.

### Default Git layout

Use this layout when the project has no explicit workspace policy or has adopted Mirket’s defaults. In the root `.gitignore`, create or repair these root-relative exclusions. Replace a blanket exclusion only under this default policy and preserve unrelated entries.

```gitignore
/.work/temp/
/.work/recover/
/.work/stashes/
/.work/routines/
```

Verify the effective rules with `git check-ignore --no-index` on representative files in each listed directory and at the workspace root. Under the default layout the four directories listed in the ignore rules should match. Files directly under `.work/` and records under `plans/`, `briefs/` and `decisions/` should remain visible. If a broader rule also affects other project paths, preserve it and add scoped exceptions for the workspace. Use `git check-ignore -v --no-index` to locate conflicting rules.

## Numbered records

For an established ADR collection, continue its filename, numbering and index conventions. For the first ADR collection in a project, use the sequence below.

Plans, briefs and new ADR collections each start their own sequence at `0001`. Use one more than the highest number in the collection, including its archive. Ignore legacy dates when counting. Use at least four digits, a hyphen and a short title. Follow the project's naming convention for Markdown titles or use PascalCase, for example `0002-NextjsRewrite.md`. Use short hyphenated titles for plan folders. Put dates inside the record if useful.

When resuming work, find and reuse its existing record. Keep its number and path. Coordinate allocations when writers are working in parallel and check the prefix is unused before linking to a new record. Preserve legacy archives and old links when migrating existing records; write only to the canonical destination.
