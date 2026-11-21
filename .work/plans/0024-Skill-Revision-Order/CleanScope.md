# Clean: scope for revision 5

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Clean](../../../skills/clean/SKILL.md) as a focused delivery and commit check. It does no cleanup for answer-only work that produced no artifacts.

- **Review scope.** Before delivery, check the task's changes, direct references, and temporary output. Before a requested commit, also scan nearby docs and agent instructions. Fix inconsistencies caused by the task. Flag material unrelated issues and hold the commit if an inconsistency caused by this task cannot be resolved. A pre-existing issue that the task did not worsen does not block the commit.
- **Deletion and recovery.** Without separate deletion authority, remove only verified temporary files made by the current task. Leave older files in place even if they look obsolete. Before an authorized deletion, use an existing reliable recovery path when available (the exact content in Git or reproducible output). Otherwise save and verify a targeted copy in `.work/recover/` with restore instructions before deleting.
- **Guidance.** Fix stale commands in docs and agent instructions. Remove steps when evidence shows the replacement already covers them. Ask before changing the conditions that require verification.
- **Mixed staged changes.** If the requested commit can be isolated, verify the exact intended hunks and preserve the user's staged and unstaged changes, including separable changes in the same file. Stop and show the overlap if isolation cannot be verified. Keep the existing commit guard.
- **Verification evidence.** Record what was checked, what it showed, and any material limits. Keep screenshots only when requested or needed by an active handoff.
- **No extra pass.** Remove the opt-in `Stop` review and its `MIRKET_FINAL_REVIEW` path. Clean still applies before delivery, and the existing commit guard stays in place. Update affected references and checks.

Representative check: a command rename leaves the old command in a contributor guide. Clean fixes the reference if it can. If someone else owns the edit and the inconsistency remains, Clean holds the commit. A nearby unrelated issue is reported without blocking it. Hook checks should confirm that Mirket no longer requests a `Stop` continuation and that the existing commit guard still behaves as before.
