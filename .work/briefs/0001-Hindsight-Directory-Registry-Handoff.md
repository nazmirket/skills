# Resume Hindsight directory isolation

> Relocation note: the native checkout now lives at `~/Projects/skills`. The state below is a historical snapshot; inspect the active Hindsight setup before following any unfinished steps.

Resume the interrupted work: remove obsolete Impeccable hooks and make Hindsight healthy with one memory bank per project directory. First inspect the current state; this handoff is historical context, not new authorization. If the current configuration or user instructions differ, adapt before acting.

## User decisions and boundaries

- The user chose separate memory for different project directories even when their folder names match. Subdirectories within a Git project share that project’s memory. Linked Git worktrees are intended to share their project identity.
- `/Users/nazmi/Desktop/skills` is the active authored Mirket repository and contains `memory/` as the source of installation guidance and scripts. Do not store the memory database in the repository. `/Users/nazmi/Projects/skills` was the original reference repository and must not be changed unnecessarily; preserve all existing uncommitted work in both locations.
- Continue to defer behavioral testing of the authored Mirket skills until the catalog is ready. Isolated tests of infrastructure and Hindsight itself are allowed.
- Honor current host and repository skill routing and planning instructions. User-level Codex hook changes require the host’s normal trust review; do not bypass it.

## Completed and verified

- Removed exactly the old Impeccable `PostToolUse` and `Stop` registrations from `/Users/nazmi/.codex/hooks.json`. Hindsight hooks were preserved. The legacy Impeccable skill itself was not removed.
- Hindsight coding-agents 0.8.6 is installed, configured to use the local daemon and `openai-codex` provider. It was healthy at `http://127.0.0.1:9077/health` at the last check. The service and its embedded database are persistent user infrastructure, not a background task to terminate merely because this work pauses.
- Earlier a temporary Hindsight bank successfully retained and recalled a synthetic fact, and the temporary bank was removed.
- The two existing explicit mappings in `/Users/nazmi/.hindsight/coding-agent.json` preserve `coding-agent::desktop-skills` for the Desktop checkout and `coding-agent::projects-skills` for the Projects checkout. Do not delete or migrate any existing banks. A bank list showed `coding-agent::projects-skills` contained recorded facts; verify live state before acting.
- `/Users/nazmi/Desktop/skills/memory/project_registry.py` and `test_project_registry.py` contain an unactivated draft registry wrapper. At last run 15 isolated tests passed, covering equal names, nested repos, linked worktrees including separate Git dirs, concurrent registry updates, aliases, broken Git metadata, Git environment isolation and byte-exact hook input forwarding. An independent reviewer rechecked the latest Codex-scoped alias guard. `memory/README.md` describes the proposed behavior.
- A separate live MCP experiment with a temporary config and fresh processes verified that Hindsight’s Codex-specific empty `mapPathToBank` override and per-process bank environment resolve two equal-named Git projects and a nested repo to distinct banks while retaining an exact-root legacy bank. This did not activate the wrapper.

## Crucial unfinished work

**The directory registry has not been activated.** No registry wrapper has yet been installed under `~/.hindsight/mirket`, the live Hindsight config has not been changed to the Codex-specific empty map override, and the Hindsight hook and MCP commands still point to the original upstream scripts. The two manual mappings do not protect every future same-named project; do not describe global directory isolation as working.

1. Read `/Users/nazmi/Projects/skills/.work/plans/archive/2026-11-09-hindsight-memory/task_plan.md`, especially Phase 6, and inspect the actual source and current user config. The independent review recommended guarding routing aliases in both global and Codex-scoped `banks` and `paths`; the latest code includes this. Re-run the focused registry tests if anything has changed.
2. Finish careful activation: preserve all user hooks, Hindsight config, MCP settings and existing banks. Intended order: stage the wrapper under Hindsight’s user data directory and seed a private, concurrency-safe registry with the existing exact-root mappings; route only the three Hindsight Codex hooks and the Hindsight MCP server through it while preserving the explicit provider and desktop-safe paths; then apply a Codex-only `mapPathToBank: {}` and `autoUpdate: false` override. Validate all input shapes and version 0.8.6; perform changes atomically with safe rollback or explicitly report partial state. Avoid changing other agents or hooks. Verify the design again before applying: the wrapper fails closed for conflicting bank overrides, bank aliases, bad project identity or unsupported runtime versions.
3. Verify fresh, actual MCP processes resolve the two existing checkouts to their preserved banks and temporary same-named repos, nested repos, subdirectories, symlinks and linked worktrees to expected isolated banks. Test exact hook forwarding and verify daemon health and disposable retain/recall. Do not confuse a direct MCP round trip with proof that Codex lifecycle hooks are trusted or have run.
4. Explain that moving to another project in an existing session requires a new session because MCP binds a bank on startup. Changed Hindsight hooks need the user’s review/trust in Codex; Codex app computer-use access was denied, so do not claim to have trusted them.

## Expensive-to-rediscover findings

- Hindsight’s default `bankIdTemplate` uses repository basename and can merge separate same-named repositories. `mapPathToBank` matches prefixes and precedes per-process bank IDs; a parent mapping can capture a nested repository. The Codex-only empty map override is intended to prevent this without altering the global maps or other agent harnesses.
- Hindsight config files override environment variables; wrapper supplies `HINDSIGHT_BANK_ID` and `HINDSIGHT_DYNAMIC_BANK_ID=false`, validates conflicting settings, disables Codex runtime auto-update, and fails closed on versions other than 0.8.6. Other harnesses could still update the shared runtime; version validation is necessary.
- MCP bank selection occurs when the MCP process starts, but hook routing occurs per event. The draft wrapper uses an anonymous temporary file plus `dup2` and `exec` to preserve exact hook stdin and process signals. It uses Hindsight’s existing session-root marker for non-Git contexts and skips cross-project hook transitions.
- The two `skills` checkouts have the same basename. The currently running MCP process previously reported the old cached `coding-agent::skills` bank even after config changed; a new process picked up the manual path mappings. Always verify with fresh processes.
- `/Users/nazmi/.agents/skills` is a symlink to `/Users/nazmi/Projects/skills/skills`; the upstream Hindsight installer created the untracked `/Users/nazmi/Projects/skills/skills/hindsight-coding-agent/` through it. It is an active installed companion skill, not an arbitrary disposable file. Preserve it unless deliberately resolving the user’s original-repository constraint without breaking Hindsight.
- Relevant source: https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/coding-agents/README.md. Current installed runtime source: `/Users/nazmi/.hindsight/coding-agents/dist/`.

## Delegation and current state

The independent `registry_research` and `registry_plan_review` agents finished; no delegated work is known to remain active. Hindsight’s local daemon remains running intentionally. Review `git status` in both repositories and reread the selected plan before resuming.
