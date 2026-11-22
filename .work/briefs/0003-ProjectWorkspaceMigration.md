# Migrate this project to the Mirket workspace layout

Carry out the migration in the current Git worktree. Start at `git rev-parse --show-toplevel`. Read the project's instructions and inspect Git status, including staged, unstaged, untracked and relevant ignored files. Map each candidate's old path, new path and consumers before moving it. Use file contents and actual usage to classify it. Keep unrelated edits and merge conflicts intact. A second run should find the same records at the same paths.

## Move and reshape the records

- **Plans** — Use one folder per plan, for example `.work/plans/0007-Website-Rollout/`. Reshape the source material into `Evidences.md` (starting state, evidence and gaps), `Scope.md` (boundaries and constraints), `Outcome.md` (intended result and acceptance checks), `Plan.md` (ordered work and dependencies), and `Progress.md` (completed work, verification and open items). Preserve dates, approvals, quotations and evidence links. Mark missing information as unrecorded. Keep supporting material with its plan when it is needed to understand or verify the record.
- **Architecture decisions** — Consolidate existing ADRs under `.work/decisions/`, including ADRs currently in a dedicated docs directory. This task explicitly selects the new destination. Use one descriptive file per decision, for example `0004-StaticSiteHosting.md`. Preserve existing IDs, status, context, decision, rationale, consequences and supersession links. Keep drafts identifiable as drafts.
- **Numbering and names** — Keep established IDs and archive relationships. Allocate missing plan and ADR numbers independently, using at least four digits and checking active and archived records before choosing the next number. Use short hyphenated titles for plan folders. Use descriptive PascalCase titles for ADRs and ordinary Markdown files. Resolve collisions without overwriting either source. Rename the actual files and folders, including case-only changes on case-insensitive filesystems.
- **Device-specific routines** — Put each reusable procedure directly under `.work/routines/` as one self-contained Markdown file with a descriptive, unnumbered PascalCase name, such as `DeployProjectWebsite.md`. Bring its prerequisites, device-specific setup, steps, verification and applicable recovery steps into that file. Keep credential values in their existing secret store. Preserve shared deployment scripts, CI entry points and team runbooks that other machines need.
- **Temporary artifacts** — Move disposable scripts, logs, renders, intermediate exports and scratch output into `.work/temp/<task>/`. Direct future scratch output there too. Keep maintained fixtures, published assets and required evidence at a durable destination.
- **Local backups** — Move recovery copies to `.work/recover/<task>/`. Preserve their contents, record the original path and restore procedure, and verify the copy before removing the original. Preserve existing `.work/stashes/` and `.work/briefs/` records.

## Fix Git rules and consumers

Before the first project write, create or repair the root `.gitignore`. Preserve unrelated rules, remove any blanket workspace exclusion, and apply these root-relative directory rules:

```gitignore
/.work/temp/
/.work/recover/
/.work/stashes/
/.work/routines/
```

Keep `.work/` itself, plans, decisions and briefs visible to Git. An ignore rule alone does not untrack a file. When moving a tracked file to a local-only destination, verify the local copy and account for removal of the old tracked path. Preserve any distinct staged edits. Keep device-private details out of Git-visible records.

Update incoming and outgoing references: relative links, anchors, indexes, cross-plan and ADR links, agent instructions, templates, generators, scripts, CI, build and packaging config, tests and path-based discovery. Update both writers and readers so the next run uses the new location. Check assumptions about the current directory and paths assembled at runtime. Shared builds and CI must work in a fresh checkout where ignored files are absent. Preserve externally used URLs or entry points when needed and record any external reference you cannot update.

## Verify and report

Search for old paths, basenames, IDs and globs. Resolve active references and distinguish intentional historical mentions. Check both sides of relative links. Use `git check-ignore -v --no-index` on representative paths and `git ls-files` on the four ignored directories. Verify that local-only files exist on disk and durable records are visible to Git. Run the affected entry points, link checks and required project tests. Use a preview or dry run for operational routines.

Report the old-to-new paths, changes to content and wiring, checks that actually ran, and any unresolved collisions or external references. Carry out the authorized local changes in this task. Commit, push, publish or deploy only when separately requested.
