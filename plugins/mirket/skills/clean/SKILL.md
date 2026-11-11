---
name: clean
description: "Use when the human requests cleanup, before delivering work, or before committing changes to review relevant leftovers, stale references and project guidance."
---

# Clean

Leave the relevant work coherent and remove verified leftovers without disturbing the human's work. Cleanup requires judgment: a hook can request this review, but cannot decide on its own which files or evidence are safe to remove.

## Choose the scope

1. Identify the current request and applicable scope. Before delivery, make a quick applicability check; if the task changed no files and produced no artifacts requiring cleanup, skip further review. Otherwise review the relevant work from the current task. Before a commit, inspect the proposed commit and surrounding repository, documentation and agentic setup broadly enough to spot cleanup needs. Clean only the intended scope and report material unrelated findings. An explicit cleanup request sets its own scope.
2. Check the current working tree and staged changes where applicable. Separate pre-existing or unrelated changes from material created by the current work. Preserve the human's files, active plans, handoffs, historical decisions, useful evidence, licenses and artifacts unless the human authorized their removal. Do not automatically stage unrelated changes.

## Clean with evidence

3. Look for the task's temporary files in `.work/temp/` and check for unused artifacts, redundant output, obsolete paths, broken links and stale guidance within scope. Check whether each candidate still has a purpose. A file is not disposable merely because it is untracked, old, generated or unfamiliar. Preserve files whose purpose or safe removal is uncertain, and report material uncertainty.
4. Remove a leftover only when its ownership, obsolescence and safe removal are clear within the authorized task. Repair task-related stale references and documentation when evidence supports the correction; update project-specific agent instructions or artifacts when the work made them inaccurate. Preserve historical records as history rather than rewriting or deleting evidence that remains useful.
5. Before an authorized removal of important, hard-to-recreate work, make and verify a targeted `.work/recover/` copy according to the [workspace rules](../../references/Workspace.md). Record the original location and restore instructions; skip recovery for reproducible leftovers. A recovery copy does not authorize deletion. If deletion or a broader change could affect unrelated work, user data or uncertain evidence, resolve that with the human first. If cleanup is not applicable, make no changes.

## Verify and report

6. Inspect the resulting diff and relevant paths. Use focused checks appropriate to the changes; confirm that updated references resolve and intended behavior or records are preserved. Report material cleanup, remaining uncertainty and any unavailable verification. Never claim a hook ran or cleanup occurred without evidence.
7. Before committing, review the intended changes and check the index for private `.work/` files; only explicitly authorized exceptions may be tracked. Preserve the human's staged and unstaged work. If Mirket's commit hook is active, acknowledge the review with `MIRKET_CLEANUP_DONE=1` on the standalone commit command and name the worktree with an absolute `git -C` path. A hook request does not authorize committing, staging, publishing or modifying unrelated content.

**Done:** Relevant leftovers and stale material have been addressed within the authorized scope, project guidance reflects the work, and uncertain or preserved items are reported when material.
