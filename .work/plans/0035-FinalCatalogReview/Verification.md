# Integration and verification

Astra Max reviewed the 20 skill entry points, shared guidance, hook and package implementation, relevant specialist references, and prior live evidence against base `0e29f6c`. See the [review](AstraReview.md) for findings, sources and unchanged decisions. The lead inspected the integrated patch, corrected the fixture-count prose, and tightened prompt-time Clean guidance after a read-only live case opened Clean unnecessarily.

## Repository and site

All 41 repository tests passed on the baseline and final patch. The final diff passed whitespace checks. Diagram generation, static website build and discovery checks passed. Playwright inspected the local Migrate and Test pages at 360 and 1200 CSS pixels; full instructions, reference links, and viewport widths were correct. The website was not deployed.

## Routing and scope

Codex CLI 0.167.0 with `gpt-6.1-sol`, Mirket 0.4.0 installed from a clean export of the base plus the exact reviewed working-tree files. The installed hooks, skills and references were compared with the export. Isolated profiles were used, and web search was disabled.

- 18 sessions with hooks disabled: the complete 16-session Deploy, Debug, Test and Audit suite plus two Migrate cases. All passed exact technology-guide selection and stayed within scope. All reused the expected guide only, or none when the supplied evidence was sufficient. No extra owner or supporting skill entry was read in these 18 sessions. The earlier committed baseline suite recorded extra entries in four of its 16 sessions.
- Migrate's concurrent scenario opened the new reference and described how the saved copy lost a recent update and recreated a deletion. The offline scenario reused rehearsal evidence without opening the reference. Neither performed a migration or rehearsal.
- Initial hook-on read-only cases selected their guides; one Prometheus run also opened Clean. The lead changed the prompt hook to apply cleanup only when the task made changes or produced an artifact. Final follow-up: both Prometheus replays and the Playwright review kept the expected owner with Execute and skipped Clean; an authorized fixture edit loaded Clean and changed only the requested file. Skills and references were byte-identical across these two candidate snapshots.

[Full routing observations](../../temp/final-review-validation.2E9AHUri/RunObservations.json) and [final hook-on follow-ups](../../temp/final-review-validation.2E9AHUri/final-candidate/RunObservations.json) contain the exact prompts, reads and actions.

## Lifecycle hooks

The three hooks were approved through Codex's normal review UI in a disposable profile, without a trust bypass or changes to the normal profile. The final live host events confirmed SessionStart's direct routing pointer and conditional support rule, UserPromptSubmit's conditional cleanup reminder, and Bash PreToolUse denials for an unacknowledged commit and a staged dummy `.work/private.txt` in a separate repository. The standalone preview was allowed by the guard. The nested sandbox denied Git's index lock, and the same literal preview exited 0 through the current Codex shell in the same fixture. No fixture commit occurred. No new hook event or automatic review pass was added. [Final hook events](../../temp/final-review-validation.2E9AHUri/final-candidate/LiveHookEvents.json).

Claude Code was not available for live activation checks. Hook scope limits and intentional compatibility shims remain documented. This was a catalog review with sampled live checks, not exhaustive verification of every technology reference or universal host/model compliance. Changes remain uncommitted.
