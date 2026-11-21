# Installed hook execution verification

2026-11-11. Mirket 0.4.0; Codex CLI/app-server 0.167.0. Fresh actual ephemeral sessions used installed plugins and normal persisted hook trust. No trust bypass, model override, permission override, install or live configuration change was used. The inherited model was `gpt-6-astra`, approval policy `never`, and sandbox `dangerFullAccess`. Each fixture is an independent dummy Git repository; both carry an independent pre-commit safety hook that rejects any commit.

## Actual Codex results

| Case | Observed result |
| --- | --- |
| SessionStart | Passed. Installed hook completed and supplied Distill plus the installed `references/Routing.md` pointer. |
| UserPromptSubmit | Passed. Installed hook completed and supplied Distill plus the installed Clean skill pointer. |
| Standalone `git commit --dry-run` | Passed. Actual shell call exited 0 and listed only staged dummy files. |
| Acknowledged commit without absolute `-C` | Passed. Actual PreToolUse hook blocked it with the explicit-target requirement. The model did not retry or repair it. |
| Absolute second-repository target with staged `.work/private.txt` | Passed. Actual PreToolUse hook blocked that target's dummy private path, independently of the session repository. |
| Default Stop | Passed. Hook completed with empty output after one final answer; no continuation. |
| Opt-in Stop | Passed. With `MIRKET_FINAL_REVIEW=1` only in the second process environment, first Stop requested combined Distill/Clean review, one continuation emitted, and second Stop completed neutrally. The short answer `5` appeared twice, matching the documented extra-pass cost. |
| Updated global instructions | Passed for loading. Fresh thread/start listed `/Users/nazmi/.codex/AGENTS.md` in `instructionSources`. Its current fingerprint and exact lifecycle-owner, PascalCase Routing/Memory and settled-ADR guidance are recorded in the JSON. This proves source loading, not compliance with every rule. |

Both runs completed normally. `git rev-parse --verify HEAD` found no commit in any of the four fixture repositories after the runs. No real source-repository commit command was submitted.

## Evidence

- [Structured verification record](InstallHookVerification.json) includes event IDs, statuses, feedback, thread IDs, global-file fingerprint and fixture HEAD checks.
- [Default actual event stream](../../temp/HookDiscovery/installed-default-events.jsonl) and [summary](../../temp/HookDiscovery/installed-default-summary.json).
- [Opt-in actual event stream](../../temp/HookDiscovery/installed-opt-in-events.jsonl), [summary](../../temp/HookDiscovery/installed-opt-in-summary.json), and [loaded instruction sources](../../temp/HookDiscovery/installed-opt-in-start.json).
- [Runner](../../temp/HookDiscovery/verify_installed.py) records API notifications; it does not fabricate synthetic hook input for these live cases.

## Claude limits

The existing [actual Claude run](../../temp/ClaudeInstalled040.jsonl) contains successful Mirket SessionStart **and UserPromptSubmit** hook responses, both exit 0, before the model request failed with `Not logged in · Please run /login`. Claude's model-driven PreToolUse and Stop enforcement remain **unverified**. Installed-script/synthetic contract checks do not close that authentication-dependent gap.

This focused verification does not claim all 29 behavior scenarios passed, interactive TUI behavior beyond the root's separate observations, full token-cost measurement, or complete memory capture. No source changes were needed for these checks. Preserve the fixture transcripts as installation evidence.
