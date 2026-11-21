# Final catalog review — Astra Max

Reviewed baseline `0e29f6c98c5f14bbd26fac708a58bbddab543479` and the local patch on 2026-11-15. The user authorized bounded corrections, with no commit, publication or activation. The coordinating agent owns integration and final host/site verification; this reviewer owned the first tracked patch.

## Findings resolved

### Concurrent migration guidance left the most consequential sequence implicit

`skills/migrate/SKILL.md` correctly required compatibility, checkpoints and recovery, but did not explain how to preserve changes arriving during a backfill or order the compatible expansion, synchronization, data copy and consumer switch. A completion status alone can hide a stale update or resurrected deletion. This was a guidance gap, not a demonstrated defect in an application migration.

Added the selectively loaded `skills/migrate/references/ConcurrentTransitions.md`. It covers the overlap contract, compatible expansion, ongoing inserts/updates/deletes, replay-safe bounded work, reconciliation against a defined write boundary, and the handoff to Deploy. Authority, preservation and retirement remain with Migrate. The guide does not prescribe an online migration when an authorized pause suffices, and does not assume a particular database mechanism.

The method was checked against the original [Parallel Change description](https://martinfowler.com/bliki/ParallelChange.html), [GitLab's compatibility examples](https://docs.gitlab.com/development/database/avoiding_downtime_in_migrations/), and [GitLab's background migration completion, isolation and idempotence guidance](https://docs.gitlab.com/development/database/batched_background_migrations/). These informed original Mirket guidance; their framework code, helper APIs and release schedules were not imported.

Added one saved-evidence behavioral case for the unresolved concurrent transition and a control for a simple offline conversion. They start unverified and require actual host observation before being called passing evaluations.

### Initial ownership cues permitted unnecessary peer entrypoint reads

The previous committed-revision suite recorded four sessions with extra peer skill reads. In several, Deploy+Audit or Test+Audit were opened in the first batch, before guide selection. The evidence therefore supports improving initial ownership cues; it does not show that a tool guide caused scope expansion. Every session still selected the expected technology guides and stayed within its operational bounds.

Clarified Test's description to include interpreting test results. The shared routing guide now states that a cross-skill link or reused result does not itself require loading another skill. SessionStart asks the agent to read the owning skill if absent from context and add support only for distinct unresolved questions. This introduces no new hook event, review pass or permission gate. Whether it changes model choices needs fresh sampled host evidence; source wording alone cannot establish that outcome.

### Generic regression proof was repeated in runner guides

Test owns the requirement to prove that a new regression case fails against the original code and passes against the fix. Playwright, pytest and Vitest repeated the same logical rule. Removed those copies and linked the runner index to Test's existing check-selection and regression method. Kept runner-specific environment, selection, isolation, retry and reporting guidance. No verification condition was weakened.

### Maintained references were reached through compatibility indirection

SessionStart and optional global instructions pointed to root reference wrappers, requiring another read to reach the maintained instructions. README also linked the routing guide twice. Pointed those active entrypoints directly to `skills/execute/references/`, removed the duplicate README navigation, and retained every root compatibility wrapper. Updated path-contract validation so both legacy and maintained reference forms are actually checked, including a nonempty-match assertion.

## Reviewed and intentionally preserved

- Read all 20 skill entrypoints and the ownership/routing contracts, shared workflow references, contribution rules, package manifests, all hook source, and hook/package/fixture tests. Reviewed the added Test and Audit guide sets and relevant Design, Code, Deploy and issue-triage boundaries. This was a catalog and targeted-reference assessment, not a fresh exhaustive validation of every technology fact in every guide.
- Reviewed the prior 16-session routing report and the actual command records for extra loads. Existing evidence was reused rather than presented as a new evaluation.
- Debug's two-hypothesis pause is a recorded human choice, reinforced by a behavioral fixture. It was preserved. Execute already defers to an owning workflow's pause.
- Hook commit detection remains deliberately limited to documented literal forms. The staged probe uses system Git, disabled helpers, an explicit target and bounded subprocesses. No reproducible correctness defect was found within the reviewed supported forms. The known heredoc warning can be noisy, but removing it without a reliable recognizer would conceal a coverage gap. No parser or enforcement rule was changed.
- Compatibility manifests, root reference wrappers, the packaged license, and historical ADRs have continuing purposes. Catalog/link checks pass, no tracked `.work/` files or generated temporary leftovers were found, and no deletion was justified. Private work records were untouched except for this new review note.

## Verification performed by this reviewer

- Before edits: `python3 -B -m unittest discover -s tests` — 41 tests passed.
- After edits: the same required repository suite — 41 tests passed.
- `git diff --check` — passed.
- `git ls-files .work` — empty; `git check-ignore .work/temp` — ignored.
- Reviewed the resulting diff, all changed reference targets and the unchanged compatibility surfaces. No files were staged, committed, pushed or published.

The local patch was frozen for the coordinating agent's exact-candidate packaging. Site build, rendered pages and fresh live routing/hook results belong to that integration record, not to the tests above. The new migration cases are synthetic guidance checks; no real data migration, rollout or recovery was executed.

## Material limits

The installed Mirket 0.4.0 cache in this session is older than the current source for some guides. Installed skills governed the work, while current tracked sources were the audit target. The cache was not edited. This review does not establish updated installation behavior, Claude Code activation, universal model compliance, or complete scanner/security coverage. Hooks remain advisory guardrails with the documented unsupported-command and trust limitations.
