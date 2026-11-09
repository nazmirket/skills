> Historical record from the initial catalog design. It describes the project at that time; see the [current README](../../README.md) for the maintained catalog.

# Review of Mirket's 18 parent skills

This is an assessment of the [reference catalog](https://github.com/nazmirket/skills/blob/247a2bdc83ef5c6445234026e892eb7a64510cd4/catalog.json), not a request to reproduce it. Each parent is locally composed; [sources.json](https://github.com/nazmirket/skills/blob/247a2bdc83ef5c6445234026e892eb7a64510cd4/sources.json) records its stated influences. Recommendations below are starting hypotheses, not tested claims about what your eventual skills must do.

| Existing parent | Value and boundary | Recommendation for your collection |
| --- | --- | --- |
| `pick-skills` | Chooses workflows and resolves overlaps; the other parents do the work. Its always-on mechanism requires a reliable host bootstrap. | **Later:** add a router only when multiple real skills cause selection conflicts; first test native discovery. |
| `resolve-intent` | Separates user choices from facts the agent can investigate. Overlaps with planning's initial discovery. | **Early candidate:** start with a short reusable decision method; make standalone only if needed in many workflows. |
| `plan` | Turns substantial work into steps and evidence; distinct from executing them. Its persistent ledger adds operational weight. | **Early candidate:** author a lightweight planning skill for a real recurring task; add persistence only when sessions need it. |
| `review-plan` | Challenges a plan with a separate perspective; distinct from writing it. Independence depends on actual host capability. | **Later:** add a review branch to planning first; separate it if independent review is commonly needed. |
| `design-get-inspiration` | Uses real examples to inform a new visual direction, before design decisions. | **When needed:** keep separate from `design-interface` if research is reused independently; otherwise combine. |
| `design-interface` | Converts a direction into hierarchy, states and a concrete design. It stops before full implementation. | **When needed:** author around your own design decisions and artifacts; link to inspiration and feedback rather than duplicating them. |
| `design-implement` | Builds the agreed interface with functional states and accessibility. Different from proposing the design. | **When needed:** build one vertical slice; hand visual review to QA without duplicating the full process. |
| `design-unslop` | Critiques visual craft and removes defects in a rendered interface. Its scope overlaps with visual QA. | **Later:** start as focused critique criteria within visual QA; split only if standalone critique is useful. |
| `design-qa` | Verifies changed visual states in rendered views. Different from automated tests and design preference. | **When needed:** make visible evidence and unverified states explicit; combine with craft critique initially. |
| `get-feedback` | Checks a representative partial result before expensive expansion; can apply to design or other work. | **Later:** use as a checkpoint inside a larger workflow until independently valuable. |
| `scaffold` | Sets up a minimal project foundation and its first working path. Planning decides what to do; this shapes the implementation. | **When needed:** author if you repeatedly start comparable projects; avoid generic empty layers. |
| `delegate` | Assigns bounded independent work and integrates results. It is not guaranteed to be available or permitted on every host. | **Later:** add capability checks and a sequential fallback only after a real multi-agent use case. |
| `refactor` | Improves working code while preserving its behavior; different from feature work and reviewing. | **Early candidate:** useful if you frequently clean up code; define the preserved contract and focused checks. |
| `review-code` | Reports evidence-backed defects in an understood scope; distinct from automatically fixing them. | **Early candidate:** use one bounded change and define findings, evidence and read-only behavior. |
| `test` | Selects checks according to risk and reports actual evidence; shared across many workflows. | **Early candidate:** consider a compact common verification method before building a separate router. |
| `author-document` | Routes structured artifact work to format-specific processes. Its format tools and render requirements are host-dependent. | **When needed:** start with your most-used format, with a clear fallback if rendering is unavailable. |
| `create-diagram` | Matches the diagram to a question and validates its relationships and export. It does not substitute for general document authorship. | **When needed:** author for a concrete diagram type or recurring communication problem. |
| `report-results` | Makes outcomes, evidence and limitations readable. It cuts across all workflows rather than representing a domain task. | **Early candidate:** start as a concise shared writing convention; make it a skill only if it proves useful. |

## Suggested sequence

1. Pick **one** of intent, planning, code review, refactoring, or verification based on a task you actually repeat. Establish its baseline, then write and evaluate it in both hosts.
2. Add adjacent skills only when one method has a distinct trigger and deliverable. Keep overlaps explicit: planning/review, visual critique/QA, and QA/test are likely boundaries to test.
3. Add a router, policy, persistent planning, hooks, or delegation only after the collection demonstrates a specific need. These are orchestration choices, not prerequisites for authoring a useful native skill.

The present repository uses a composed catalog: for example, it associates planning with Superpowers, Matt Pocock and Planning with Files, design with Impeccable and UIZZE, and testing with Superpowers, Ponytail and Anthropic. Consult the exact entry and its licenses before reusing implementation or text. General inspiration is different from copying or adapting material; preserve attribution and comply with applicable license terms for actual reuse.
