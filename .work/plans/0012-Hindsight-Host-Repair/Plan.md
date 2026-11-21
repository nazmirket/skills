# Plan — draft, execution authorized

1. Stage official Claude Code and Hindsight 1.2.1, verifying the release contains the parser correction. Confirm upstream Claude-only installation effects and keep private rollback snapshots.
2. Switch the same local daemon profile and provider to the fixed release. Recheck health, bank inventory, raw recall and real refresh; refresh the Mirket survey from its canonical checkout.
3. Wire only Claude Code without replacing Codex adapters. Scope Claude to this checkout with a dedicated bank. Check Claude auth and run real fresh turns across both hosts, or report and isolate the sign-in dependency while completing all other verification.
4. Compare doctor, live APIs and logs, check the stale/failed/pending state and original bank coverage. Keep recovery and leave existing website work untouched.

## Current status

- Hindsight daemon 1.2.1 started on the original loopback endpoint and profile with the original provider. A private PostgreSQL dump was validated before migration; all ten pre-existing banks are present afterward. Profile and daemon log permissions are owner-only. Recovery files are under ~/.hindsight/mirket/backups/host-repair-53y3830u/.
- A fresh Codex CLI session wrote its own tagged conversation into the correct bank; an independent raw chat recall found its synthetic label in that exact document. The Component map page refresh completed on the new daemon. All four survey findings were updated from committed HEAD 8a05fdc in a clean linked worktree.
- Claude Code 2.1.311 and the pinned Hindsight 0.8.6 hooks, skill, and MCP registration are installed. The registered MCP connects to a separate Mirket bank and exposes zero tools outside the configured project scope. No authenticated Claude conversation or capture/recall test was performed at the user's request.
- The 30 focused memory tests passed; the shared Codex adapter and registry integrity checks passed. Existing repository edits and the index were preserved.
- A second fresh Codex CLI session retrieved the exact synthetic label using its configured Hindsight MCP, without shell or file access. The survey receipt for 8a05fdc is tagged complete and all four document timestamps independently confirm a fresh survey. The temporary clean worktree was removed with Git after both runs.
- Final readiness on 1.2.1: all 23 pages current, 24 post-upgrade refreshes completed, zero failed or active refreshes, and no response parser errors in the post-upgrade daemon log. Hindsight was still consolidating new records in the background. Disposable verification files were removed; recovery snapshots were kept private.
