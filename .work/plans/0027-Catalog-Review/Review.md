# Mirket catalog and hook review

Two independent GPT-6 Astra reviewers at high effort reviewed base `467912c`: one covered all 20 skill entries, local references and shared routing; the other covered repository wiring, lifecycle hooks, tests, and stale or redundant files. The lead reconciled their findings, applied the bounded corrections below, and verified a candidate from the resulting diff.

| Area | Finding and disposition |
| --- | --- |
| Entry points and depth | Preserve the rich Design workflow, format and tool references. Preserve concise routing rules that live checks showed were necessary, such as reading Ship Prioritization on its own when the outcome is set. Plan and Deploy are the longest entry points; no demonstrated friction justified splitting them in this pass. |
| Opinion and stopping rules | The Debug pause after two failed hypotheses is a prior human decision. Execute now defers to an owning workflow's stopping rule instead of implying it should always try one more check. |
| Ownership and mid-task support | The shared routing rule now allows a specialist to answer a distinct question, fill a gap, or guide a decision that arises during an existing task. The owner and scope stay in place. Aligned Author and the two opt-in templates with Market's ownership of messaging/claims and Ship's ownership of requirements. Design applies approved brand voice while Market owns decisions about voice itself. |
| Visual evidence | Whole-page review now calls for coverage from top to bottom, using a full-page image or clearly ordered overlapping sections. Keep a readable original, add high-resolution details and representative viewport states where needed, and link specific findings to the corresponding capture and state. Local evidence remains sufficient for local issues. The format and flow state this independently of capture-tool choice; tool guides remain optional unless requested or needed. Clean keeps evidence needed for review and handoff. |
| Repository cleanup | Removed stale present-tense hook counts from current instructions and clarified superseded lifecycle owners in the historical ADR without erasing the decision history. The scan found no broken local links, tracked private workspace files, orphan skill directories, or obsolete configs safe to delete. The identical instruction templates and the separate logo assets are used. Existing ignored work records and build dependencies were left alone. The stale old owner names and Memory reference in this chat's external instructions are separate from the repository templates. |

## Hooks: sufficient in design; a live enforcement gap

| Event | Verified result |
| --- | --- |
| SessionStart | Live Codex returned the Execute context plus the shared ownership/routing pointer. |
| UserPromptSubmit | Live Codex returned the Execute reminder and conditional Clean instruction. |
| Bash PreToolUse | The authored contract covers literal standalone commit previews and inspections of the explicitly named Git target. Source and payload tests passed for the supported paths, including staged private-path handling. The live host listed the installed hook as trusted and enabled, but every attempted execution reported “plugin contents changed; hook approval required.” No live guard decision was observed. |
| Stop | No authored handler or automatic extra pass. |

The live test used the normally installed package and matched the three hook files byte for byte against the repository. The target was a separate disposable repository with a staged dummy private path and a pre-commit failure guard; no commit occurred. The shell attempts failed under the read-only sandbox, which does not verify Mirket's decisions. Trust settings and hook source were left unchanged. Reapprove through Codex and rerun the actual preview and denial cases before relying on the guard. Claude Code live activation was not verified because the CLI was unavailable. The hooks are intentionally advisory and limited to documented command forms; they do not guarantee compliance or prove authorization. See [host event evidence](Evidence/HookSmoke.json).

## Checks on the corrections

- 40 repository tests passed, including lifecycle payloads, Git index targeting, packaged wiring, local links and fixtures. Diagram generation, website build and SEO passed. Author, Clean and Execute docs were inspected in Chrome at 360 and 1280 CSS px.
- Six live Codex routing/capture sessions ran against an isolated candidate with hooks disabled. Market opened its messaging guide; Ship opened requirements; Plan read a new handoff, added Code guidance on Next.js and React, and remained the planning owner. No fixture content was changed.
- A real browser tool returned a [complete 1280 × 1884 landing page](Evidence/full_page-1280-1x.png) and a [2560 × 1020 pricing section](Evidence/section-pricing-1280-2x.png) at 2×. The overview showed top through footer; the detail showed the deliberately faint pricing terms in context. Two narrow mobile requests each returned one 360 × 640 viewport, including a run that explicitly required the Screenshot guide. See [routing and PNG metadata](Evidence/RoutingAndCaptures.json).

This was a catalog-wide review with representative live checks, not a live test of all guides or external sources. Changes are local and uncommitted.
