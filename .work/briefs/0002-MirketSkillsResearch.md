# Mirket skills, routing, design and hooks

**Research brief · 19 November 2026 · Mirket 0.5.1 · revision `33de42d`**

Three changes have the clearest payoff. Hide the expected skill from the agent during routing tests. Move two Python imports off the cleanup hook’s ordinary shell path. Give Design worked references for charts, multilingual interfaces and form recovery. The first corrects a measurement defect, the second has a measured local benefit, and the third fills gaps in decisions the existing guides already ask agents to make.

The catalog’s physical wiring is healthy. All 20 skills are represented in the 48 behavior cases, all 175 packaged Markdown references are reachable by following local links from skill entry points, and all 42 repository tests passed. The installed Codex CLI reported all 20 descriptions and all three Mirket hooks enabled and trusted. The remaining questions concern which instructions the model chooses, what it does with them and what the host can observe. [Audited revision][rev] · [Host evaluation guide][smoke]

## Defects and ambiguities in 0.5.1

| Priority | Finding and consequence | Correction and check |
| --- | --- | --- |
| High for evaluation | **Routing fixtures disclose the expected owner.** The preparer writes `Result.json` into the agent’s working directory. Its `case_id` starts with the expected owner in **46 of 48** cases. I prepared `architect-unresolved` in a neutrally named directory and read the label while the observed owner was still empty. I also verified that the installed 0.5.1 package includes the complete `tests/behavior_cases.json` rubric. Past runs would need transcript evidence to establish whether the agent saw either. [Preparer][preparer] · [Evaluator instructions][smoke] | Keep results, case IDs and rubrics on the evaluator side. Give the agent an opaque working directory. Use unpublished held-out prompts for full-package tests, and mark trials contaminated if the transcript shows evaluator data was read. Verify actual skill reads or host events. |
| Medium for implementation | **The CSS guide omits a cascade tie-breaker.** It goes from specificity to source order. In Chromium 151.0.7922.34, equal-specificity rules under nested `@scope` roots rendered the inner element blue even though the outer red rule came later. An outer-only element and an unscoped source-order control both rendered red. The current diagnostic can point an agent toward an unnecessary selector override. [Mirket CSS guide][css-local] · [Chrome’s scoped cascade explanation][css-chrome] | Add scoping proximity between specificity and order of appearance when scoped rules compete. Use the nested case as the acceptance example. |
| Medium for routing | **Two discovery descriptions understate what their owners do.** Architect explicitly owns design-time threat modeling, but its discovery description omits it while Audit advertises security and privacy. Search describes communities, traction, competitors and history, while the project assigns it external research. Technical documentation, fact-checks and paper syntheses have no explicit trigger in its description or routing row. These are confirmed omissions. Their effect on selection requires host trials. [Architect][architect] · [Search][search] · [Routing guide][routing] · [Contributor contract][contrib] | Add a short intent phrase to each description and give Search’s routing row the same scope. Test an audit of a fixed proposal beside a choice between two designs, and a literature question beside a question about local code. |
| Medium for write scope | **Architect’s draft instruction and the evaluator allow different readings.** For an open decision needing its own comparison, the skill directs the agent to keep a private draft. Two comparison cases declare an empty write allowance and expect the answer in chat. A side-by-side assessment may naturally meet both descriptions. [Draft instruction][architect-draft] · [Storage comparison][arch-case] · [Threat-model case][threat-case] | Make the destination conditional on a comparison needing a durable record. Test a recommendation-only request with zero writes and a request for a reusable draft with one authorized write. Preserve the existing ADR path for a settled decision. |
| Low for readability | **Three measurement steps render as a paragraph.** In `MeasuredImprovement.md`, the list resumes at `3.` directly after a paragraph. The repository’s own Remark/GFM parser classified lines 10–13 as a single paragraph. The corrective workflow loses its list structure in rendered Markdown. [Measurement guide][measure] | Insert a blank line before step 3. Check that the parsed node is an ordered list starting at 3 with three items. |

## What the research says about effectiveness

**A skill earns its space when it supplies a procedure the model otherwise misses.** SkillsBench v4 compared curated skills with a matched baseline on 87 tasks across eight domains and 18 model–harness configurations. Mean pass rate rose from 33.9% to 50.5%. The observed gains varied by configuration, and focused packages of up to three modules performed better than larger bundles in that study. Gloaguen and colleagues studied a different intervention, repository-wide context files for coding agents. Across their settings, task success generally failed to improve and inference cost rose by over 20% on average. These results favor putting the distinguishing decision or worked example in a selectively loaded guide. Neither study establishes an ideal module count or an expected gain for Mirket. [SkillsBench v4, June 2026][skillsbench] · [Gloaguen et al., September 2026 revision][agents-paper]

**A compact pointer can outperform an optional lookup on a narrow task.** Vercel’s January evaluation of newer Next.js APIs gave baseline and default skills 53%, an explicitly prompted skill up to 79%, and an 8 KB documentation index 100%. The skill went unused in 56% of default cases. Participants on Hacker News pointed out that the index already gave the agent the available document paths. Vercel’s LinkedIn post describes the same experiment. For Mirket, this supports testing a short pointer to the routing guide when the owner is unclear. It gives little reason to inject the whole guide into every turn. [Vercel experiment][vercel] · [Hacker News discussion][hn] · [Vercel’s LinkedIn post][linkedin]

**A high activation rate can conceal poor decisions.** Scott Spence’s Claude Code experiment found that two hook designs each achieved full activation on 44 straightforward Svelte trials. On 24 harder prompts including irrelevant ones, the forced-evaluation variant scored 75% and the model-based classifier 67%. The classifier generated four false positives. These are one practitioner’s results on one skill family. For Mirket, they make a case for including prompts where Execute alone is sufficient. [Original experiment, February 2026][spence] · [Author’s Reddit discussion][reddit]

**Small evaluation wins deserve a second sample.** Kozyrev and colleagues evaluated optimized skill documents on tasks drawn from three Kotlin repositories. A 4.9 percentage-point average gain from one optimizer could not be distinguished from run-to-run variation at their sample size. Soheil Feizi’s November X article describes mining merged changes and reverts for realistic tasks, with explicit attention to answer leakage. Mirket can use prior routing mistakes as development cases and reserve independently worded requests for a final comparison. [Kozyrev et al., September 2026 preprint][kotlin] · [Feizi’s X article][feizi]

## Skill selection and routing

The 20 discovery descriptions total **2,659 characters** before names and paths. Search, Code, Market and Ship each have one primary-owner fixture. The routing test checks that each owner appears in the table. Those checks catch a missing owner row, while a row pointing a realistic request to the wrong workflow can still pass. Both hosts also have listing budgets. Codex can shorten descriptions and eventually omit entries. Claude Code documents dropping less-used descriptions first. In a GitHub issue about apparently missing descriptions, the discussion moved from suspected name collisions to the documented budget. This makes a realistic mixed-plugin installation a valuable second test condition. [Mirket wiring test][wiring] · [Codex skill discovery][codex-skills] · [Claude Code skill discovery][claude-skills] · [GitHub issue and follow-up][issue]

Two candidate discovery phrases are short enough to test in isolation. For Search, try “Use to answer external questions with primary sources, including technical documentation, papers, practitioner discussions and project history.” For Architect, add “compare threats and privacy tradeoffs between proposed designs” alongside its existing decision and ADR triggers. Preserve the existing community, competitor and traction use cases when refining the final Search wording.

Use a few pairs with the same subject and different requested outcomes. The proposed routing below follows the present ownership rules except for the expanded external-research trigger.

| First request and proposed owner | Closely related request and proposed owner | Evidence to grade |
| --- | --- | --- |
| “What do the published studies and current specification say about this interaction?” → Search | “Which behavior does our checkout implement today?” → Adapt | Primary external evidence in the first answer and the local implementation in the second. |
| “Compare two proposed designs for handling account identifiers.” → Architect | “Assess the privacy risks in this fixed proposal.” → Audit | A design choice with open tradeoffs versus findings against the supplied target. Either target can be a draft. |
| “Draft the ticket for the missing last item.” → Author | “Fix the missing last item.” → Debug | The first stops at a ticket. The second verifies the repaired behavior. |
| “Prepare the versioned package and release notes.” → Execute as standalone task owner in the existing fixture | “Assess whether this artifact can roll out to staging.” → Deploy | Inspect the candidate package versus the target environment. Preserve the authority granted in each request. |
| “Correct this literal heading.” → Execute | “Why does the heading change after hydration?” → Debug | A direct edit and focused check versus an investigation of an unexplained failure. |

One ownership question deserves a maintainer decision. The user guide calls the owner of a new implementation “the implementer,” Code explicitly supports the current owner, and Execute names routine answers and known edits. A nonvisual backend feature inside an agreed architecture can fall between these descriptions. One economical interpretation is to name Execute as the default implementation owner once requirements are settled, with Code supporting stack-specific decisions and Plan supporting coordination. Test that interpretation on a new feature before changing the public contract. [User guide][implementer] · [Code][code] · [Execute][execute]

For trials, score the primary owner, unnecessary specialist reads, the requested outcome, allowed writes and the stopping point separately. Include a two-turn owner change, an implicit request and an Execute-only control. Two existing prompts expressly name Migrate. Count these as invocation tests. Preserve the accepted lowercase, backticked selection announcement and grade substance independently of its surrounding prose. [Behavior cases][cases]

For efficacy, compare the ordinary host with the released catalog. For hook contribution, compare the same catalog with hooks off and on. For a wording change, compare the release with that change alone. Hold model, permissions, competing catalog and optional global instructions constant within each pair. Split development and holdout cases by scenario so paraphrases cannot leak across the split. Repeat in fresh sessions, rotate order and report pass counts and unobservable outcomes by host. The Agent Skills guides and Anthropic’s open-source evaluator provide working examples. [Trigger evaluation][trigger] · [Output evaluation][eval-quality] · [GitHub evaluator][creator]

## Design vocabulary with a job to do

Mirket already has 7 design flows, 17 concepts, 16 formats, 13 styles and 9 tool guides, excluding indexes. It covers modal keyboard behavior, drag alternatives, contrast, localization stress and chart units. The 13 style guides contain no outbound specimen links. Keep the existing flow, format, concept, style and tool structure. Add references at the point where they change a decision an agent can demonstrate. [Design reference decision][adr-design] · [Concept index][concepts] · [Format index][formats] · [Style index][styles]

| Priority and location | Vocabulary and use | An example that would demonstrate the improvement |
| --- | --- | --- |
| First · extend Diagram Design with a chart branch | **Marks, encoding channels, scale, small multiples, uncertainty and missingness.** The current guide gives quantities a single chart row. A reader comparing regional trends needs guidance on comparable scales and a meaningful alternative to color. | Give the agent three regional series with one missing quarter. Check common scales where comparison requires them, an explicit gap and a text or table equivalent that answers the comparison. [Current chart guidance][diagram] · [Vega-Lite authors][vega] · [ONS small multiples][ons] · [W3C complex images][complex] |
| First · concept shared by Responsive and Typography | **Base direction, bidirectional isolation, logical start/end and script fallback.** Translated text length already appears in the guides. An Arabic interface containing an English product ID and punctuation exercises a different failure. | Render an Arabic invoice containing a Latin SKU, an amount and a mixed-direction note. Check the visual order of the ID and punctuation, field direction for unknown input, and keyboard progression. [W3C direction guidance][bidi] |
| First · extend UX and Accessibility | **Error summary, field-level error, focus destination, committed value and active option.** Use a concrete recovery sequence for long forms and a separate example for an editable combobox. | Submit two invalid fields, follow each summary link and check preservation of valid answers. For a combobox, inspect keyboard navigation and dismissal in its actual implementation. GOV.UK supplies a tested service pattern and APG supplies the widget interaction contract. [GOV.UK error summary][govuk] · [WAI-ARIA combobox][apg] |
| Next · add specimens to Composition and Styles | **International Typographic Style, asymmetric grid, typographic hierarchy and negative space.** Use Müller-Brockmann’s Zürich concert poster to discuss how blocks relate and where the reader enters. | Arrange one event program at poster and phone sizes. Keep date, venue and event legible through the change in geometry. Compare with the actual specimen. [Swiss National Library][swiss] · [MoMA collection object][moma] |
| Next · add a contrasting specimen to Art or Illustration Design | **Ukiyo-e woodblock composition, foreground scale, silhouette and a restricted palette.** Hokusai’s print makes the distant mountain read inside the shape of the wave. That relationship is more instructive than a generic style adjective. | Ask for two compositions of a new subject with the same content. Judge whether foreground and distance establish the intended emphasis at thumbnail size. [The Met collection object][met] |
| When exchanging a system across tools · extend Design System | **Semantic alias, primitive value and type.** The present guide already assigns semantic roles. A worked interchange case would explain what must survive an export. | Change a shared color value, resolve an alias and inspect the affected focus treatment in both themes. Keep the example optional for projects that exchange tokens. [Design Tokens Community Group format, 2025.10][tokens] |

Measure visual improvement on the same content and viewport with a blinded comparison of hierarchy, fidelity and readability. Exercise the task separately for claims about interaction or recovery. Design2Code’s 484-page benchmark combined rendered comparisons with human evaluation. Its screenshot-to-code task is evidence for judging visual fidelity. Mirket’s dialog and form cases also need keyboard observations. [Design2Code, NAACL 2025][design2code] · [Existing Mirket browser case][design-case]

## Hook efficiency and host enforcement

The manifest starts a fresh isolated Python process for session start, user prompt and each matching Bash tool call. The shared guidance is **590 characters**. Using checkout paths, the session context was 871 characters and the turn context 714. On a session’s first prompt their common 590 characters are delivered twice. The installed paths change the totals. Character counts describe the payload. Billed tokens, cache behavior and the effect on adherence require host measurements. [Hook manifest][manifest] · [Generated guidance][execute-hook]

| Path on the unmodified checkout | Median | p95 |
| --- | ---: | ---: |
| Python startup control, `python3 -I -c pass` | 13.17 ms | 19.49 ms |
| SessionStart | 18.77 ms | 26.62 ms |
| UserPromptSubmit | 18.80 ms | 25.77 ms |
| PreToolUse with `git status --short` | 29.56 ms | 42.13 ms |

I measured process launch through completion on macOS 27.2 arm64, Python 3.15.2, with five warmups and 80 observations per path in shuffled order. Hook inputs were synthetic. An ordinary shell heredoc containing only `hello` also produced a cleanup advisory by design. That is a candidate for measuring warning frequency during everyday work before changing the treatment of uncertain commands. [Cleanup hook][cleanup-hook]

**One optimization has experimental support.** In disposable copies I moved only the `shutil` and `subprocess` imports into the existing staged-index inspection function. In 100 randomized pairs after 12 warmup pairs, the ordinary shell-call median fell from **28.53 to 21.89 ms** and p95 from **29.01 to 22.34 ms**. The trial copy was faster in 100 of 100 pairs. Both copies passed all 25 cleanup-hook tests. This is a 23.3% reduction for that subprocess path on this machine. Interactive host latency, the index-inspection path’s latency and other Python versions remain unmeasured. This is the first hook change I would consider. [Import site and inspection function][cleanup-imports] · [Hook tests][hook-tests]

**A shorter turn reminder is a separate experiment.** The candidate below is 291 characters with the same checkout path, down from 714. Replace the placeholder with the installed Clean path.

> Apply Execute. Choose one owner per outcome. Announce selected skills with lowercase backticked names, as in “I’ll use `execute` and `design` skills.” Read selected skills missing from context. For edits or artifacts, apply CLEAN_PATH before delivery.

Keep the fuller session-start guidance in the comparison. Test owner changes, required verification, Clean on artifact delivery and host-supported resume or compaction. Existing unit tests assert exact phrases in the shipped reminder. Agree on the behavioral results a shorter variant must preserve before changing those assertions. Only the character saving has been measured. [Execute hook tests][execute-tests] · [Host smoke checks][smoke]

| What the plugin needs to establish | What can establish it |
| --- | --- |
| The plugin is discoverable and eligible to run | On this installation, read-only Codex CLI 0.167.0 `skills/list` returned 20 enabled Mirket skills with descriptions. `hooks/list` returned SessionStart, UserPromptSubmit and PreToolUse, all enabled and trusted. A release smoke run should also capture execution of each event. Keep the compatibility manifest until another layout passes that comparison. [Codex trust and events][codex-hooks] · [Mirket packaging decision][adr-host] |
| The model followed a workflow | Observe the skill read or invocation, the produced artifact or answer, and its task-specific check. A skill announcement is a self-report. The hook fields used at session and turn start supply model context. [Mirket event output][execute-hook] · [Claude hook protocol][claude-hooks] |
| A supported tool action was stopped | Use the host’s synchronous PreToolUse decision. Pair a supported denial with an ordinary read-only operation that should proceed and verify actual host outcomes in a disposable project. Codex documents unified exec matching `Bash`. Keep the current explicit-target index check and the normal host trust review. The cleanup acknowledgment records an assertion. [Codex tool coverage][codex-hooks] · [Mirket commit contract][contrib] |
| A hook startup failure or timeout should stop work | This is a maintainer policy choice. Claude Code documents `onFailure` for command and HTTP hooks from 2.1.295. Mirket’s matcher currently covers all Bash calls, so failing closed there could interrupt unrelated reads during a runtime outage. Test a supported host/version and its availability cost before adopting host-specific configuration. [Claude failure semantics][claude-failure] · [Shared manifest][manifest] |
| A rule must hold for changes merged into a protected branch | A repository-owned required check can inspect the proposed change and honor explicitly named project exceptions. That control applies at merge time. The Markdown-only installations provide skills without Mirket hooks. Decide whether a repository wants that additional control independently of its plugin installation. [GitHub rulesets][rulesets] · [Mirket’s other-host installation contract][other] |

## Order of investment

1. **Make the results trustworthy.** Move evaluator metadata outside the agent-visible fixture. Keep source/expected labels, explicit-name runs and implicit runs distinguishable. Use the existing 48 cases as the starting asset.
2. **Take the inexpensive, verified corrections.** Correct the CSS and Markdown defects and evaluate the deferred imports on the supported host runtimes. Tighten the two underdescribed discovery triggers against the paired requests above.
3. **Run the three design trials.** Start with chart comparison, mixed-direction input and form-error recovery. A new reference earns its place when the agent makes a better observable decision or catches a defect the baseline misses.
4. **Spend additional enforcement effort where evidence warrants it.** Compare the shorter reminder against 0.5.1 on each native host. Report raw counts, cost and forbidden actions separately. Product decisions remain open on default feature ownership and on what should happen during a hook outage.

**Verification limits.** I inspected the released checkout, its discovery text and reference graph, prepared a neutral-name fixture, ran the repository suite, checked installed Codex metadata, reproduced the CSS and Markdown cases, and benchmarked isolated hook processes. Of 259 distinct literal external links in packaged skill Markdown, 258 returned HTTP 200 to the direct check. The Khronos glTF registry returned HTTP 403 to that client, which leaves that endpoint inconclusive. Accuracy was checked for the cited findings. The investigation included official documentation, papers, GitHub source and discussion, X, Reddit, LinkedIn and Hacker News. Fresh model-operated Codex and Claude comparisons are still needed to establish the behavioral effect of the routing, design and enforcement proposals. The delivered work is this private brief.

[rev]: https://github.com/nazmirket/skills/tree/33de42def11deb30786cc4cb338d07a32895fc42
[smoke]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/HostSmoke.md
[preparer]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/prepare_host_smoke.py#L41-L53
[css-local]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/code/references/CSS.md#L5
[css-chrome]: https://developer.chrome.com/docs/css-ui/at-scope
[architect]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/architect/SKILL.md#L3-L19
[architect-draft]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/architect/SKILL.md#L21-L25
[arch-case]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/behavior_cases.json#L227-L245
[threat-case]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/behavior_cases.json#L799-L814
[search]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/search/SKILL.md#L3-L14
[routing]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/execute/references/Routing.md
[contrib]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/CONTRIBUTING.md
[measure]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/execute/references/MeasuredImprovement.md#L10-L13
[skillsbench]: https://arxiv.org/abs/2602.12670v4
[agents-paper]: https://arxiv.org/abs/2602.11988v3
[vercel]: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
[hn]: https://news.ycombinator.com/item?id=46809708
[linkedin]: https://www.linkedin.com/posts/vercel_were-experimenting-with-ways-to-keep-ai-activity-7422383807284125696-ELS7
[spence]: https://scottspence.com/posts/measuring-claude-code-skill-activation-with-sandboxed-evals
[reddit]: https://www.reddit.com/r/ClaudeCode/comments/1qzjy2h/claude_code_skills_went_from_84_to_100_activation/
[kotlin]: https://arxiv.org/abs/2609.12742
[feizi]: https://x.com/FeiziSoheil/status/2123466115829395525
[wiring]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/test_package_wiring.py#L179-L191
[codex-skills]: https://learn.chatgpt.com/docs/build-skills
[claude-skills]: https://code.claude.com/docs/en/skills
[issue]: https://github.com/anthropics/claude-code/issues/95582
[implementer]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/docs/README.md#L60-L70
[code]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/code/SKILL.md#L8-L12
[execute]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/execute/SKILL.md
[trigger]: https://agentskills.io/skill-creation/optimizing-descriptions
[eval-quality]: https://agentskills.io/skill-creation/evaluating-skills
[creator]: https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/run_eval.py
[adr-design]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/docs/decisions/0005-DesignReferenceLayers.md
[concepts]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/design/references/concepts/README.md
[formats]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/design/references/formats/README.md
[styles]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/design/references/styles/README.md
[diagram]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/skills/design/references/formats/DiagramDesign.md
[vega]: https://vis.csail.mit.edu/pubs/vega-lite/
[ons]: https://service-manual.ons.gov.uk/data-visualisation/chart-types/small-multiple-charts
[complex]: https://www.w3.org/WAI/tutorials/images/complex/
[bidi]: https://www.w3.org/International/questions/qa-html-dir.en
[govuk]: https://design-system.service.gov.uk/components/error-summary/
[apg]: https://www.w3.org/WAI/ARIA/apg/patterns/combobox/
[swiss]: https://www.nb.admin.ch/en/the-international-style-1950-1970
[moma]: https://www.moma.org/collection/works/6257
[met]: https://www.metmuseum.org/art/collection/search/45434
[tokens]: https://www.designtokens.org/tr/2025.10/format/
[design2code]: https://aclanthology.org/2025.naacl-long.199/
[design-case]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/behavior_cases.json#L389-L409
[cases]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/behavior_cases.json
[manifest]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/hooks/hooks.json
[execute-hook]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/hooks/execute.py#L13-L38
[cleanup-hook]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/hooks/cleanup.py#L223-L249
[cleanup-imports]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/hooks/cleanup.py#L181
[hook-tests]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/test_cleanup_hooks.py
[execute-tests]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/tests/test_execute_hook.py
[codex-hooks]: https://learn.chatgpt.com/docs/hooks
[claude-hooks]: https://code.claude.com/docs/en/hooks
[claude-failure]: https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails
[adr-host]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/docs/decisions/0003-CodexHookCompatibility.md
[rulesets]: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-status-checks-to-pass-before-merging
[other]: https://github.com/nazmirket/skills/blob/33de42def11deb30786cc4cb338d07a32895fc42/docs/OtherAgents.md#L3-L15
