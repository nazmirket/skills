# Host and behavioral checks

The Python tests validate local contracts and fixture preparation. They do **not** establish that a host activates hooks or that a model follows a skill. Record those two kinds of evidence separately.

## Prepare a behavioral case

[behavior_cases.json](behavior_cases.json) contains reusable cases covering all 20 skills. Each specifies the prompt and source context, expected owner and actions, allowed and prohibited writes, stopping condition, and evidence that should be reused. Expectations are reviewer criteria, not text to require the model to repeat.

```sh
python3 -B tests/prepare_host_smoke.py --list
python3 -B tests/prepare_host_smoke.py --case audit-read-only --output /absolute/disposable/trial-01
python3 -B tests/prepare_host_smoke.py --cases /absolute/evaluator/holdouts.json --case sample-07 --output /absolute/disposable/trial-02 --results-dir /absolute/evaluator/results
```

The [preparer](prepare_host_smoke.py) takes a new or empty absolute workspace path. Choose an opaque name, including its parent directories. It writes only the prompt, context and project files there. The evaluator record starts unverified. By default it is a sibling such as `trial-01.result.json`. Use `--results-dir` to put it under a separately permissioned evaluator directory. Existing inputs and prior results are preserved. Give the host access to the workspace and runtime plugin. Keep the result, private case catalog, transcripts and credentials outside its reading scope.

For a blind routing trial, supply an unpublished case catalog using `--cases`. Use the same JSON shape as `behavior_cases.json`. Set `include_sample_app` to false for cases that do not use the starter Python module and tests. Split by scenario before tuning descriptions and keep held-out prompts and rubrics outside the source checkout, installed plugin and agent workspace. The public catalog is for development and smoke checks. A full root marketplace install can contain those public answers. For a committed candidate, stage only the runtime files for development trials as shown below. For a working-tree candidate, stage the same paths including the intended edits, and compare their contents with source.

```sh
mkdir /absolute/disposable/runtime
git archive HEAD -- .agents/plugins .claude-plugin .codex-plugin assets hooks references skills LICENSE | tar -x -C /absolute/disposable/runtime
```

Launch the intended host in the prepared workspace with the candidate plugin. Submit `Prompt.md`. Record host, model, candidate identity, plugin path, enabled hooks and trust. Start without optional global Mirket instructions when testing the package alone. Use a fresh workspace for each run.

For Codex, a separate disposable `CODEX_HOME` keeps the candidate marketplace and plugin settings apart from the normal installation. Use the host's normal sign-in mechanism if that home needs authentication; never put credentials in the fixture or evidence. Use a clean candidate checkout or export containing only the files intended for distribution. A local root package can copy ignored files, so keep private workspace notes, dependencies and build output outside the candidate directory. With the disposable Codex environment selected, register the candidate and install it through the CLI:

```sh
codex plugin marketplace add /absolute/clean-mirket-candidate
codex plugin add mirket@mirket
```

After editing a candidate at the same version, use `codex plugin remove mirket@mirket` and reinstall in that disposable home, then compare installed files with source. Do not modify the cache directly. For Claude Code, `claude --plugin-dir /absolute/clean-mirket-candidate` loads the local candidate for that session. Keep unrelated MCP/capture configuration out of disposable evaluations, and review hook trust through the host; do not bypass it. A successful plugin install or unauthenticated startup only establishes discovery/startup evidence, not model behavior.

A case may exercise a particular skill without explicitly naming it. Record the skill actually loaded from the transcript, not just the skill the response claims to have used. If the host cannot expose that evidence, mark ownership unverified. A scenario's hypothetical unavailable capability is a constraint for that case; do not install a tool merely to erase the test.

## Assess the observed run

After the host stops, compare the transcript, commands and resulting files with the case's criteria. The fixture hashes in the evaluator result establish the starting content; inspect newly created files too. An attempted forbidden write is a failure even if host permissions block it. Read-only cases should not create execution plans. Substantive implementations may create appropriate workspace records when the case permits them.

In the evaluator record, capture actual skill and reference reads, the primary owner, additional skills, writes, commands, evidence reused and stopping reason. When the case depends on a guide, check its path in the transcript or record where the same guidance was already supplied. Mark unobservable reads unverified. Grade unnecessary specialist reads, the lowercase backticked selection announcement and the delivered outcome separately. Review the transcript for access to the rubric, evaluator result or another run's answers. Set `rubric_exposure` to `clear`, `exposed` or `unverified`. Exclude exposed and unobservable runs from blind accuracy and report their counts. Keep explicitly named invocations and implicit discovery in separate totals. A failed criterion makes the case fail. Use `unverified` for missing evidence, with a reason and a link to the evidence available.

Use identical prompts, model, host version, permissions and competing catalog within each comparison. For skill value compare with a no-Mirket baseline. For hook contribution compare the same catalog with hooks off and on. For a wording change vary only that wording. Rotate order, repeat in fresh sessions and report raw counts per host for owner, unnecessary reads, outcome, write scope and stopping point. Check owner changes across turns and whether the session pointer is available on resume. Optional global instructions get their own comparison.

For delegated execution, inspect the worker calls, assigned paths, profile settings and integrated files. Record any profile choice the host hides as unverified.

Record the observed catalog and global instructions for each condition. Exclude a nominal no-Mirket control if its transcript reads a user-installed copy. A disabled plugin entry alone cannot establish what files the agent consulted.

Check that each prompt distinguishes its intended outcome from neighboring skills. A request to choose a product priority can reasonably select Ship even when its context mentions storage. Preserve the original score if an ambiguous prompt surfaces, then test a fresh scenario that explicitly requests the technical comparison.

## Boundaries covered

| Boundary | Cases and distinguishing result |
| --- | --- |
| Orientation and diagnosis | `adapt-orientation` and `adapt-contract-conflict` check orientation. `author-bug-intake` and `debug-authorized-fix` use the same defect to distinguish a ticket draft from a verified repair. `debug-two-failed-hypotheses` checks that an authorized diagnostic continues from the last confirmed event. |
| Concurrent migration guidance | `migrate-concurrent-transition-plan`, `migrate-single-transition-plan`: load the compatibility reference only when versions or writers overlap; use the saved race and rehearsal evidence, and keep planning separate from execution. |
| External research | `search-community-trends` checks discussions and dated project activity. `search-paper-and-standard` checks the original study, its limits and applicable interaction guidance. Compare with `adapt-orientation` for internal project facts. |
| Review | `audit-read-only`, `audit-independent-review-unavailable`: return findings without edits and leave a required independence gate open when only inline review is available. |
| Repeated review | `audit-follow-up-coverage` preserves a ruled-out finding, reopens a conclusion that depends on a changed service, and identifies an unexamined path. |
| Verification | `test-evidence-only`, `test-regression-and-export-smoke`: return the failure without editing product code, and distinguish a focused regression check from a smoke check through the affected workflow. |
| Technical choice and structural change | `architect-unresolved`, `architect-reusable-comparison`, `architect-settled-boundary` and `architect-first-adr` distinguish an answer in chat, a requested decision draft and a settled ADR in an established or new collection. `refactor-preserve-behavior` and `refactor-characterize-and-fix` distinguish preserved behavior from a separately verified correction. |
| Direct work and writing review | `execute-short-answer`, `execute-direct-fix`, `author-document`, `author-review`: take the simplest complete path, verify when needed, and stop at findings for writing review. |
| Implementation and stack advice | `execute-settled-feature` checks a new capability against agreed requirements. `code-cascade-scope` checks a CSS explanation against three browser-computed colors. `code-transaction-boundary` checks the rollback design against the caller’s failure contract. |
| Choosing tools | `equip-tool-fit`, `equip-pilot-needs-approval`: rule out a format that fails hard requirements and propose a pilot without running it merely because the tool is available. |
| Visual production and review | `design-supplied-reference`, `design-no-generation-authority`, `design-redesign-baseline-blocked`, `design-visual-review`: carry over reference intent, agree on the brief before generating, require a live redesign baseline, and stop at findings for visual review. |
| Web design acceptance | `design-web-review-with-browser` exercises the keyboard path in the available browser. `design-polish-full-page` checks transcript access and matched full-resolution before/after originals. `design-viewport-evidence-gap` leaves final listing and footer acceptance open when only a top slice is available. |
| Design decisions in use | `design-regional-chart` checks the scale, missing observation and accessible comparison. `design-mixed-direction` checks both note directions, the product ID and keyboard order. `design-form-recovery` checks focus, the remaining error and preservation of a valid entry after resubmission. |
| Realistic file data | `design-stress-file-picker` compares ordinary and long filenames in the same rows and checks keyboard operation independently of text clipping. |
| Specialist boundaries | `market-brand-voice` uses approved claims and samples; `ship-product-readiness` leaves activation with its owner; `code-react-state-review` opens only the identified stack guide. |
| Product and marketing decisions | `ship-locale-launch-scope` distinguishes a working regional waitlist from unresolved purchase and recovery paths. `market-channel-payback` checks acquisition cost, payback and the limits of a young attributed cohort. |
| Testing demand before building | `ship-manual-service-pilot` asks for a manual trial within a coordinator’s weekly time budget and evidence for the next product decision. |
| Readiness and fallback | `preflight-inferior-fallback`, `preflight-equivalent-fallback`: a page load cannot establish keyboard operation; an equivalent browser can unblock the exact check without a setup change. |
| Authorization, coordination and continuity | `plan-inherited-authority`, `plan-status-read-only`, `plan-coordinate-read-only`, `plan-delegated-execution`, `brief-stale-handoff`, `stale-handoff-material-conflict`, `brief-pause`: preserve traceable authority, keep status read-only, point to current evidence, pause only work affected by a conflict, and stop on an explicit pause. |
| Cleanup | `clean-no-op`, `clean-commit-blocked-by-stale-guide`: skip answer-only cleanup; hold a commit for an unresolved inconsistency caused by the task while preserving work owned by others. |
| Security and privacy | `audit-security-read-only`, `architect-threat-model`: assess and prioritize risks without editing the target, and compare design exposure without assuming permission to implement. |
| Versioned distribution | `release-prepare-only` checks both the source tests and the example run from the extracted candidate. The work stops at preparation. |
| Deployment | `deploy-review-target`, `deploy-production-authority`: pin artifact and target, reuse matching evidence, and keep target prerequisites, recovery compatibility, and production activation authority separate. |
| Migration | `migrate-dry-run`, `migrate-resume-checkpoint`: demonstrate recovery, resume from a verified checkpoint under existing authority, and leave unmet acceptance criteria open. |
| Operations | `deploy-incident`: use Deploy's operations branch without assuming rollout or mitigation authority; separate stabilization from causal investigation. |

## Lifecycle hook checks

Run these in fresh Codex and Claude Code sessions against the candidate, using disposable projects and dummy data. Record actual hook events and decisions when the host exposes them. These checks supplement the behavioral cases.

A loopback model stub can request fixed tool calls to check native dispatch and enforcement reproducibly. Label the model as scripted and inspect the host's event and tool result for each call. Use real model sessions to grade skill selection, the delivered result and the stopping point.

| Case | Expected observation |
| --- | --- |
| Start a session and explicitly invoke Mirket Audit. | All 20 skills are discoverable, the session hook points to installed Execute, and Audit loads from the candidate plugin. |
| Ask for a ticket draft, then ask for the repair in the same session. | Observe whether the host moves from Author to Debug and applies Clean to delivery of the edit. Verify that Mirket registers only SessionStart and PreToolUse. |
| Resume the session in the host. | Verify the session hook supplies the Execute pointer when the host dispatches SessionStart on resume. |
| Request a standalone supported `git commit --dry-run`. | It remains a preview and needs neither cleanup acknowledgment nor an absolute target. |
| Submit a guarded commit without an absolute target. | Hook denies it and explains the explicit-target requirement. No actual commit is required to observe denial. |
| Force-add a dummy `.work/temp/private.txt` in a second disposable repository, then submit an acknowledged literal commit with that repository's absolute `-C` target. | The hook examines that target and denies the staged private path. A different session directory must not change this result. Never stage real private material for a test. |
| Inspect an explicit-path exception using synthetic events, or a separately authorized disposable host run. | Only the named path is excepted; another staged scratch path remains denied. The assertion marker is not proof of human authorization. |

For the paired guard check, record a permitted read-only shell call and the host's actual denial on the same installed revision. In a disposable repository, an independent pre-commit hook that always exits unsuccessfully can prevent an unintended commit if the host guard is inactive. Record which layer denied the call and verify HEAD and the index afterward. For startup or timeout failures, record the native host outcome and the effect on ordinary shell operations. The shared matcher applies to all Bash calls. Host outage policy and protected-branch merge rules are separate operator decisions.

When assessing advisory noise, distinguish a hook warning from a denial. Count warnings out of the observed ordinary shell calls, record the command category (for example a benign here-document) and note whether the command proceeded.
