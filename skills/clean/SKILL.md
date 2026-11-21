---
name: clean
description: "Use for requested cleanup, relevant delivery checks, or a review of an authorized commit."
---

# Clean

Clean owns requested cleanup and delivery or pre-commit checks. Skip the delivery pass for an answer that made no changes and produced no artifacts.

## Before delivery

- Inspect the task's changes, direct references and temporary output, or the scope named in a cleanup request. Check for scratch files this task left outside `.work/temp/<task>/` and move any still needed there. Fix stale references in docs and agent instructions. Remove a redundant step only when its replacement demonstrably covers it. Seek approval for changes to verification requirements outside the authorized scope.
- Delete only verified temporary files from this task unless other deletions are authorized. Preserve unrelated edits, plans, handoffs, historical records and screenshots still needed for delivery, review or handoff. Before deletion, verify that the exact content is recoverable from Git or can be regenerated. Otherwise make and verify a targeted [recovery copy](../execute/references/Workspace.md) with restore instructions.
- Check the resulting diff and references. Record the checks, results and material limits in the reply or existing task record.

## Before an authorized commit

- Reuse delivery checks that cover the content being committed. Also inspect nearby docs and agent instructions. Fix inconsistencies the task caused or worsened. Hold the commit while any such issue remains. Report other material pre-existing issues and proceed when the commit checks pass.
- Inspect staged and unstaged changes. If unrelated work is staged, isolate authorized hunks, even within a shared file, only when you can verify the intended commit and preserve the human's staged and unstaged changes. Stop and show the conflict when hunks overlap or preservation is uncertain.
- Review staged plans, briefs and decisions with the other project changes. Staged files under `.work/temp/`, `.work/recover/`, `.work/stashes/` or `.work/routines/` require an explicit exception for the exact path. With Mirket's guard active, acknowledge the completed review in a standalone literal command such as `MIRKET_CLEANUP_DONE=1 git -C "/absolute/worktree" commit ...`. The commit itself requires existing authority.
