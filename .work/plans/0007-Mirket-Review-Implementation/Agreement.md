# Agreement: Astra review follow-up

## Confirmed by the human

- Convert the independent Astra High repository review into an implementation plan. Sequence the pre-commit hook first, Design routing second, and the skill guidance changes third.
- Include both previously optional recommendations: one default communication skill for routine replies and a compact single-file format for small plans.
- On 2026-11-10 the human approved the reviewed implementation plan and execution with “Okay go ahead.”

## Technical choices

- **Hook boundary:** Keep direct-command coverage and staged-index inspection, but separate recognition from execution. Recommend a trusted Git path and fixed probe arguments with a narrow allowlist for target selection. Deny a recognizable direct commit when its target cannot be safely checked, with a supported retry where possible. Continue the documented warning behavior for detectable indirect forms outside coverage. Forwarding arbitrary Git flags preserves more syntax but caused the helper-execution defect; replacing the hook with a full shell parser or a repository-installed Git hook changes scope and trust requirements.
- **Plan records:** Let new small plans use one file with the same three types of information; preserve separate files for substantial work and do not migrate historical records. This narrows the prior three-file convention only where the human approved the simplification.
- **Communication:** Keep Distill as the default and Author for substantive writing and triage. Change what the prompt hook requests, retaining its event, wiring and Clean reminder. This is the approved change to the earlier combined-pass convention, rather than removing either skill or the hook.

The hook uses system Git from /usr/bin or /bin and requires the --no-lazy-fetch capability before inspecting a target. See the [decision record](../../decisions/0001-Mirket-Pre-Commit-Index-Probe.md) for the compatibility tradeoff.

## Evidence and review

- Implementation review: Astra High pinned the hook and regression test files, passed the 22 focused cleanup tests with system Git 2.54.0, and found no material issues. An unsupported no-fetch capability was verified with a mock; no partial-clone remote or live host was exercised. The integrated plugin and memory suites each passed 23 tests.

- Astra High audited commit `29645ec` independently. Baseline checks in that audit: 19 hook tests, 23 memory tests, and resolution of relative Markdown file targets. Root also reproduced the hook’s selection of `./git` using a mocked subprocess and confirmed a Git trace invoked a benign fsmonitor helper via a forwarded `-c` option. No live host behavior was established.
- Astra High independently reviewed this draft against the original findings. It identified a gap: a staged-index probe does not cover commit modes that change which files are included. Outcome H1 and Plan step 1.2 now explicitly bound the guarantee and call for unsupported-mode checks. Astra High confirmed the draft correction in a focused recheck.

> 🧠 **From Hindsight memory (Improve Mirket lifecycle hooks)** — The prior intent was to check the selected staged index, preserve exact named exceptions, and document unsupported forms and host limits. The committed hook and existing isolated tests corroborate the intended baseline.

> 🧠 **From Hindsight memory (Revise Mirket Plan skill)** — The prior revision kept three planning records. The current user approval allows a compact record for smaller plans.

> 🧠 **From Hindsight memory (Revise Mirket Distill skill)** — The prior revision preserved the prompt hook’s behavior. The current user approval changes the default communication request; the hook and Clean reminder stay.
