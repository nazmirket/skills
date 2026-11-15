# Host and behavioral checks

The Python tests validate local contracts and fixture preparation. They do **not** establish that a host activates hooks or that a model follows a skill. Record those two kinds of evidence separately.

## Prepare a behavioral case

[behavior_cases.json](behavior_cases.json) contains 45 reusable cases covering all 20 owners. Each specifies the prompt and source context, expected owner and actions, allowed and prohibited writes, stopping condition, and evidence that should be reused. Expectations are reviewer criteria, not text to require the model to repeat.

```sh
python3 -B tests/prepare_host_smoke.py --list
python3 -B tests/prepare_host_smoke.py --case audit-read-only --output /absolute/disposable/mirket-audit
```

The [preparer](prepare_host_smoke.py) requires a new or empty absolute directory and refuses symlinked paths or existing work. It creates local source material, `Context.md`, `Prompt.md`, and `Result.json` with every verdict **unverified**. It does not start an agent, initialize Git, install anything, change host settings, or grant access. Use separate directories for each host/case/run. Keep credentials outside the fixture.

Launch the intended host in that fixture with the candidate plugin, using its supported local-plugin mechanism if available. Start without optional global Mirket instructions so the package is what supplies the guidance. Record the host version, model, candidate revision (and dirty snapshot when applicable), plugin path, hook trust and activation. Verify that it loaded the candidate, not a previously cached version. Submit only `Prompt.md`; keep the expected-owner criteria and `Result.json` outside the model's requested reading context. Do not add extra permission to the scenario.

For Codex, a separate disposable `CODEX_HOME` keeps the candidate marketplace and plugin settings apart from the normal installation. Use the host's normal sign-in mechanism if that home needs authentication; never put credentials in the fixture or evidence. Use a clean candidate checkout or export containing only the files intended for distribution. A local root package can copy ignored files, so keep private workspace notes, dependencies and build output outside the candidate directory. With the disposable Codex environment selected, register the candidate and install it through the CLI:

```sh
codex plugin marketplace add /absolute/clean-mirket-candidate
codex plugin add mirket@mirket
```

After editing a candidate at the same version, use `codex plugin remove mirket@mirket` and reinstall in that disposable home, then compare installed files with source. Do not modify the cache directly. For Claude Code, `claude --plugin-dir /absolute/clean-mirket-candidate` loads the local candidate for that session. Keep unrelated MCP/capture configuration out of disposable evaluations, and review hook trust through the host; do not bypass it. A successful plugin install or unauthenticated startup only establishes discovery/startup evidence, not model behavior.

A case may exercise a particular skill without explicitly naming it. Record the skill actually loaded from the transcript, not just the skill the response claims to have used. If the host cannot expose that evidence, mark ownership unverified. A scenario's hypothetical unavailable capability is a constraint for that case; do not install a tool merely to erase the test.

## Assess the observed run

After the host stops, compare the transcript, commands and resulting files with the case's criteria. The fixture hashes in `Result.json` establish the starting content; inspect newly created files too. An attempted forbidden write is a failure even if host permissions block it. Read-only cases should not create execution plans. Substantive implementations may create appropriate ignored workspace records when the case permits them.

Fill in the observed owner, loaded skills, writes, commands, evidence reused and stopping reason. Link the transcript and evidence. For each criterion use `pass`, `fail`, `unverified`, or `not_applicable` with a reason. A missing host, blocked prerequisite or inaccessible transcript is **unverified**, never a pass. Leave the overall result unverified until every applicable criterion has evidence; any failed criterion makes the case fail. Fixture generation and unit-test success never change these behavioral verdicts.

Repeat ambiguous routing cases with hooks disabled to assess linked guidance, and repeat with optional global instructions when testing those instructions specifically. Keep the settings and results distinct. Rerun only the cases affected by a correction or newly identified risk. One successful run supports that observed case and model; it does not prove universal compliance.

## Boundaries covered

| Boundary | Cases and distinguishing result |
| --- | --- |
| Orientation and diagnosis | `adapt-orientation`, `adapt-contract-conflict`, `debug-authorized-fix`, `debug-two-failed-hypotheses`: orient in source order when needed, fix a clear cause directly, and pause after two failed hypotheses without inventing a cause. |
| External research | `search-community-trends`: follow actual discussions and dated project activity beyond familiar names; distinguish evidence of traction from visibility without switching to internal discovery or tool adoption. |
| Review | `audit-read-only`, `audit-independent-review-unavailable`: return findings without edits and leave a required independence gate open when only inline review is available. |
| Verification | `test-evidence-only`, `test-regression-and-export-smoke`: return the failure without editing product code, and distinguish a focused regression check from a smoke check through the affected workflow. |
| Technical choice and structural change | `architect-unresolved`, `architect-settled-boundary`, `refactor-preserve-behavior`, `refactor-characterize-and-fix`: clarify design requirements, record settled boundary changes, and distinguish behavior preserved by a refactor from a separately verified defect correction. |
| Direct work and writing review | `execute-short-answer`, `execute-direct-fix`, `author-document`, `author-review`: take the simplest complete path, verify when needed, and stop at findings for writing review. |
| Choosing tools | `equip-tool-fit`, `equip-pilot-needs-approval`: rule out a format that fails hard requirements and propose a pilot without running it merely because the tool is available. |
| Visual production and review | `design-supplied-reference`, `design-no-generation-authority`, `design-redesign-baseline-blocked`, `design-visual-review`: carry over reference intent, agree on the brief before generating, require a live redesign baseline, and stop at findings for visual review. |
| Web design acceptance | `design-web-review-with-browser`: match before and after conditions and use the available browser to verify an interaction without requiring Playwright or changing the target. |
| Specialist boundaries | `market-brand-voice` uses approved claims and samples; `ship-product-readiness` leaves activation with its owner; `code-react-state-review` opens only the identified stack guide. |
| Readiness and fallback | `preflight-inferior-fallback`, `preflight-equivalent-fallback`: a page load cannot establish keyboard operation; an equivalent browser can unblock the exact check without a setup change. |
| Authorization, coordination and continuity | `plan-inherited-authority`, `plan-status-read-only`, `plan-coordinate-read-only`, `brief-stale-handoff`, `stale-handoff-material-conflict`, `brief-pause`: preserve traceable authority, keep status read-only, point to current evidence, pause only work affected by a conflict, and stop on an explicit pause. |
| Cleanup | `clean-no-op`, `clean-commit-blocked-by-stale-guide`: skip answer-only cleanup; hold a commit for an unresolved inconsistency caused by the task while preserving work owned by others. |
| Security and privacy | `audit-security-read-only`, `architect-threat-model`: assess and prioritize risks without editing the target, and compare design exposure without assuming permission to implement. |
| Versioned distribution | `release-prepare-only`: the task owner prepares an identified candidate and readiness evidence without publishing or deploying. |
| Deployment | `deploy-review-target`, `deploy-production-authority`: pin artifact and target, reuse matching evidence, and keep target prerequisites, recovery compatibility, and production activation authority separate. |
| Migration | `migrate-dry-run`, `migrate-resume-checkpoint`: demonstrate recovery, resume from a verified checkpoint under existing authority, and leave unmet acceptance criteria open. |
| Operations | `deploy-incident`: use Deploy's operations branch without assuming rollout or mitigation authority; separate stabilization from causal investigation. |

## Lifecycle hook checks

Run these in fresh Codex and Claude Code sessions against the candidate, using disposable projects and dummy data. Record actual hook events and decisions when the host exposes them. These checks supplement the behavioral cases.

| Case | Expected observation |
| --- | --- |
| Start a session and explicitly invoke Mirket Audit. | All 20 skills are discoverable; the session hook supplies the routing pointer; Audit loads from the candidate plugin. |
| Answer a short question, then perform an edit. | User-prompt Execute guidance is present and Clean still applies to relevant delivery work. Mirket registers no Stop hook and requests no extra pass. |
| Request a standalone supported `git commit --dry-run`. | It remains a preview and needs neither cleanup acknowledgment nor an absolute target. |
| Submit a guarded commit without an absolute target. | Hook denies it and explains the explicit-target requirement. No actual commit is required to observe denial. |
| Stage a dummy `.work/private.txt` in a second disposable repository, then submit an acknowledged literal commit with that repository's absolute `-C` target. | The hook examines that target and denies the staged private path. A different session directory must not change this result. Never stage real private material for a test. |
| Inspect an explicit-path exception using synthetic events, or a separately authorized disposable host run. | Only the named path is excepted; another staged `.work/` path remains denied. The assertion marker is not proof of human authorization. |

Hook activation and agent behavior are separate observations. Do not label an unobserved host or a disabled/untrusted hook as working.
