---
name: clean
description: "Use for requested cleanup, relevant delivery checks, or a review of an authorized commit."
---

# Clean

Leave the task coherent and protect existing work. Use Clean during the ordinary delivery or commit workflow.

## Before delivery

- Skip cleanup for an answer-only task that made no changes and produced no artifacts. Otherwise inspect the task's changes, direct references, and temporary output. A cleanup request can set a different scope.
- Fix stale references in docs or agent instructions and remove steps the replacement demonstrably covers. Ask the human before changing the conditions that require verification. Check the resulting diff and affected references.
- Remove only verified temporary files made by this task unless the human has authorized other deletions. Keep unrelated edits, plans, handoffs, and historical records. Before an authorized deletion, confirm the exact content can be recovered from Git or reliably regenerated. If it cannot, make and verify a targeted [recovery copy](../../references/Workspace.md) with restore instructions before deleting.
- Record what you checked, what it showed, and material limits in the reply or existing task record. Keep screenshots needed for the requested deliverable, active review, or handoff.

## Before an authorized commit

- Also scan nearby docs and agent instructions for inconsistencies. Fix what the task caused. Hold the commit if such an inconsistency remains. Report material pre-existing issues; they do not block the commit unless the task made them worse.
- Inspect staged and unstaged changes. If unrelated work is staged, isolate the authorized hunks, even within a shared file, only when you can verify the intended commit and preserve the human's staged and unstaged changes. If hunks overlap or preservation cannot be verified, stop and show the conflict.
- Check the intended index for private `.work/` files; only explicitly authorized paths may be included. With Mirket's guard active, use a standalone literal `MIRKET_CLEANUP_DONE=1 git -C "/absolute/worktree" commit ...` after the review. The guard checks the commit request; it does not authorize one.
