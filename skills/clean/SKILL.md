---
name: clean
description: "Clean up task files, check changed deliverables, or review an authorized commit."
---

# Clean

Skip delivery cleanup for answers with no changes or artifacts. Combine cleanup with final verification.

## Before delivery

- Check only the requested scope or the task's diff, direct references and outputs. Fix affected guidance and move needed stray scratch files into `.work/temp/<task>/`. Keep required checks unless coverage is demonstrably equivalent and the change is authorized.
- Preserve unrelated edits and records or evidence still in use. Delete only verified task leftovers or explicitly authorized paths after confirming exact recovery or regeneration. For irreplaceable content, make and verify a targeted [recovery copy](../execute/references/Workspace.md) with restore instructions.
- Reuse evidence that covers the final result. Run missing required checks and report remaining limits in the reply or existing task record.

## Before an authorized commit

- Reuse delivery checks and review nearby docs and agent instructions. Hold the commit for inconsistencies caused or worsened by the task. Report other material pre-existing issues.
- Inspect staged and unstaged changes, including plans, briefs and decisions. Isolate authorized hunks only when the intended commit can be verified and other staged and unstaged work preserved. Stop for overlapping hunks or uncertain preservation.
- Staged files under `.work/temp/`, `.work/recover/`, `.work/stashes/` or `.work/routines/` require an explicit exception for the exact path. With the guard active and commit authority established, acknowledge completed review in a standalone literal command such as `MIRKET_CLEANUP_DONE=1 git -C "/absolute/worktree" commit ...`.
