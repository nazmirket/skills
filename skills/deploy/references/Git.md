# Git

Use for delivery provenance, release revision selection, and recovery in systems that deploy from Git. Identify the authoritative remote, branch or tag, and exact commit; inspect the worktree and index before acting.

- Pin the commit in the release or environment record. Use a signed or annotated tag when required by the project, and verify it resolves to the intended commit. Build with the inputs the pipeline actually needs, including submodules, large files, generated assets, and version metadata. A shallow checkout can be faster but may omit history or tags expected by version and comparison logic.
- Prefer a new revert commit on a shared branch when reversing intent. A source revert does not move traffic by itself or undo database, storage or third-party effects. Trace which workflow consumes the revert, whether it creates a different artifact, and what revision actually serves users.
- Use a temporary worktree or clean archive when it isolates build inputs without disturbing local edits. Check sparse or shallow fetching against the actual build and use realistic measurements before optimizing fetch size. Preserve branch protections and normal review; use [Clean](../../clean/SKILL.md) for an authorized commit.

Verify that the artifact's source SHA matches the intended Git object and that the platform actually serves its expected artifact digest or revision. Keep previous artifact identity even if a tag or branch moves.

Upstream: [Git worktree](https://git-scm.com/docs/git-worktree), [Git revert](https://git-scm.com/docs/git-revert), [Git clone options](https://git-scm.com/docs/git-clone).
