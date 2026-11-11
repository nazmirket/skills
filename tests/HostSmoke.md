# Host and behavioral checks

The Python tests validate local contracts and fixture preparation. They do **not** establish that a host activates hooks or that a model follows a skill. Record those two kinds of evidence separately.

## Prepare a behavioral case

[behavior_cases.json](behavior_cases.json) contains 29 reusable cases covering all 25 owners. Each specifies the prompt and source context, expected owner and actions, allowed and prohibited writes, stopping condition, and evidence that should be reused. Expectations are reviewer criteria, not text to require the model to repeat.

```sh
python3 -B tests/prepare_host_smoke.py --list
python3 -B tests/prepare_host_smoke.py --case audit-read-only --output /absolute/disposable/mirket-audit
```

The [preparer](prepare_host_smoke.py) requires a new or empty absolute directory and refuses symlinked paths or existing work. It creates local source material, `Context.md`, `Prompt.md`, and `Result.json` with every verdict **unverified**. It does not start an agent, initialize Git, install anything, change host settings, or grant access. Use separate directories for each host/case/run. Keep credentials and optional memory capture outside the fixture; do not expand capture permissions for an evaluation.

Launch the intended host in that fixture with the candidate plugin, using its supported local-plugin mechanism if available. Start without optional global Mirket instructions so the package is what supplies the guidance. Record the host version, model, candidate revision (and dirty snapshot when applicable), plugin path, hook trust and activation. Verify that it loaded the candidate, not a previously cached version. Submit only `Prompt.md`; keep the expected-owner criteria and `Result.json` outside the model's requested reading context. Do not add extra permission to the scenario.

For Codex, a separate disposable `CODEX_HOME` keeps the candidate marketplace and plugin settings apart from the normal installation. Use the host's normal sign-in mechanism if that home needs authentication; never put credentials in the fixture or evidence. With that environment selected, register the repository and install the candidate through the CLI:

```sh
codex plugin marketplace add /absolute/mirket-repository
codex plugin add mirket@mirket
```

After editing a candidate at the same version, use `codex plugin remove mirket@mirket` and reinstall in that disposable home, then compare installed files with source. Do not modify the cache directly. For Claude Code, `claude --plugin-dir /absolute/mirket-repository/plugins/mirket` loads the local candidate for that session. Keep unrelated MCP/capture configuration out of disposable evaluations, and review hook trust through the host; do not bypass it. A successful plugin install or unauthenticated startup only establishes discovery/startup evidence, not model behavior.

A case may exercise a particular skill without explicitly naming it. Record the skill actually loaded from the transcript, not just the skill the response claims to have used. If the host cannot expose that evidence, mark ownership unverified. A scenario's hypothetical unavailable capability is a constraint for that case; do not install a tool merely to erase the test.

## Assess the observed run

After the host stops, compare the transcript, commands and resulting files with the case's criteria. The fixture hashes in `Result.json` establish the starting content; inspect newly created files too. An attempted forbidden write is a failure even if host permissions block it. Read-only cases should not create execution plans. Substantive implementations may create appropriate ignored workspace records when the case permits them.

Fill in the observed owner, loaded skills, writes, commands, evidence reused and stopping reason. Link the transcript and evidence. For each criterion use `pass`, `fail`, `unverified`, or `not_applicable` with a reason. A missing host, blocked prerequisite or inaccessible transcript is **unverified**, never a pass. Leave the overall result unverified until every applicable criterion has evidence; any failed criterion makes the case fail. Fixture generation and unit-test success never change these behavioral verdicts.

Repeat ambiguous routing cases with hooks disabled to assess linked guidance, and repeat with optional global instructions when testing those instructions specifically. Keep the settings and results distinct. Rerun only the cases affected by a correction or newly identified risk. One successful run supports that observed case and model; it does not prove universal compliance.

## Boundaries covered

| Boundary | Cases and distinguishing result |
| --- | --- |
| Orientation, diagnosis, checks and review | `adapt-orientation`, `debug-authorized-fix`, `test-evidence-only`, `audit-read-only`: findings/checks return to their owner; an audit cannot silently become a fix. |
| Technical choice and structural change | `architect-unresolved`, `refactor-preserve-behavior`: unresolved recommendations remain proposals; refactoring preserves the contract. |
| Documents, routine replies and quality review | `author-document`, `distill-short-answer`, `critique-report`: durable content, routine communication and assessment have distinct outputs. |
| Product and tool decisions | `focus-outcome-learning`, `curate-internal-options`, `equip-tool-fit`: compare actual outcomes/options without inventing causation, adoption or product approval. |
| Visual production and concept generation | `design-supplied-reference`, `imagine-no-generation-authority`: reproduce the supplied target; honor an explicit request to agree the brief before generation. |
| Readiness and fallback | `preflight-inferior-fallback`: source review cannot establish keyboard operation; dependent work stops for the specific missing capability. |
| Authorization, coordination and continuity | `plan-inherited-authority`, `plan-status-read-only`, `orchestrate-bounded-read-only`, `brief-stale-handoff`, `stale-handoff-material-conflict`, `sleep-pause`: reuse authority, keep status read-only, correct routine stale facts, escalate material conflicts, and actually stop on pause. |
| Project memory | `memory-scope-conflict`, `memory-capture-not-proven`: ambiguous identity prevents writes; queryability, manual notes and page timestamps do not prove automatic capture or freshness. The packaged [memory contract](../plugins/mirket/references/Memory.md) supplies the general guidance. |
| Cleanup | `clean-no-op`: no changes or artifacts means no cleanup work is manufactured. |
| Security and privacy | `secure-read-only`: identify trust/data risks without unauthorized probing or hardening. |
| Release | `release-prepare-only`: prepare an identified versioned artifact and readiness evidence without publishing or deploying. |
| Deployment | `deploy-review-target`: pin artifact and environment; define rollout/rollback checks without treating candidate preparation as rollout authority. |
| Migration | `migrate-dry-run`: rehearse a state transition, reconcile invariants and preserve a usable recovery source; no production authority is inferred. |
| Operations | `operate-incident`: prioritize recovery and verification; separate mitigation from later causal diagnosis and rollout mechanics. |

## Lifecycle hook checks

Run these in fresh Codex and Claude Code sessions against the candidate, using disposable projects and dummy data. Record actual hook events and decisions when the host exposes them. These checks supplement the behavioral cases.

| Case | Expected observation |
| --- | --- |
| Start a session and explicitly invoke Mirket Audit. | All 25 skills are discoverable; the session hook supplies the routing pointer; Audit loads from the candidate plugin. |
| Answer a short question, then perform an edit with final review disabled. | User-prompt guidance is present. Default Stop remains neutral. Clean still applies to relevant delivery work. |
| Repeat with `MIRKET_FINAL_REVIEW=1` inherited at host launch. | At most one combined Distill/Clean continuation; a shared Stop-loop flag may mean another hook already consumed it. Record that outcome rather than claiming Mirket ran. |
| Request a standalone supported `git commit --dry-run`. | It remains a preview and needs neither cleanup acknowledgment nor an absolute target. |
| Submit a guarded commit without an absolute target. | Hook denies it and explains the explicit-target requirement. No actual commit is required to observe denial. |
| Stage a dummy `.work/private.txt` in a second disposable repository, then submit an acknowledged literal commit with that repository's absolute `-C` target. | The hook examines that target and denies the staged private path. A different session directory must not change this result. Never stage real private material for a test. |
| Inspect an explicit-path exception using synthetic events, or a separately authorized disposable host run. | Only the named path is excepted; another staged `.work/` path remains denied. The assertion marker is not proof of human authorization. |

If measuring final-review cost, record model requests, token counts when available, wall time, duplicated output and any material issue the review caught. Hook activation, behavioral quality and cost are separate observations. Do not label an unobserved host or a disabled/untrusted hook as working.
