# Agreement: revise the Mirket skill catalog

Status: approved for catalog authoring. The user replied “I approve” to the independently reviewed revision proposal, then supplied a superseding list of 19 skills.

| Status | Decision | Alternatives and rationale |
| --- | --- | --- |
| Requested | Review the 16 references against the 14 authored Desktop skills and cover all nine requested scopes. | The separate reference checkout is outside this revision. The catalog and reference index establish the inventory. |
| Requested | Canonical skill IDs use a single commanding verb. Substantial influence from strong upstream work is welcome. | Record substantial adaptations, source revisions and notices; avoid giving imported conventions universal authority. |
| Approved | Keep narrow verbs with separate outputs. Add capabilities in waves. | A skill for every job title duplicates workflows; expanding Critique, Plan and Design into catch-alls obscures triggers. Splitting every check into its own skill would create unnecessary routing. |
| Approved | Rename `cleanup` to `clean`, and `handoff` to `brief`. | Cut over active in-repository callers and document the replacement IDs. The Desktop README records host installation as outstanding, and the caller audit found internal links and hooks, not a consumer that requires a shim. Preserve historical documents and the hook acknowledgment marker. Actual host migration remains unverified. |
| Superseded | Author Build, Test, Review, Triage, Author, Architect, Scope and Track. | The 22-skill revision was implemented and reviewed before the user reduced the catalog. Prototype and measured improvement remain references. |
| Approved | Keep exactly the 19 skills the user listed. Rename Discover to Preflight, Review to Audit, and Scope to Focus. Embed Triage in Author and Track in Plan. Remove Build as a standalone skill. | Use one entry point per retained workflow; Author keeps the issue intake, drafting and tracker authorization boundaries, and Plan keeps read-only status requests and its existing plan record. Direct implementation remains available within ordinary task authorization. |
| Approved | Keep automatic lifecycle behavior limited to the existing Distill and Clean intent. | Do not make substantive work or review automatic on every turn; trigger based on the task and actual host capabilities. |
| Existing constraint | Defer behavioral skill testing until the catalog is ready. | Structural validation and targeted hook checks can run during implementation; record any missing host check rather than treating it as passed. |

Host installation and behavioral evaluation remain a separate gate. No external release or change to user-level host settings is part of this approval.

## Independent review

`revision_plan_reviewer` independently reviewed the four draft files and the relevant existing skill and hook contracts. The reviewer found three material gaps:

1. Plan could call Review, but Orchestrate required an approved plan. The proposal now separates authorized read-only draft review from execution and reports the gate unmet if independence is unavailable.
2. The coverage table depended on conditional skill IDs. The proposal now assigns existing owners for each first-release prototype and optimization route and requires direct-use evidence before promotion.
3. The rename did not account for hook compatibility. The proposal now preserves `MIRKET_CLEANUP_DONE`, checks the migrated hook path, and defers actual host refresh, old-ID and trust checks to the authorized evaluation phase.

The reviewer also requested a single owner for overlapping QA requests, examples for the four new role skills, and self-contained packaging for adapted guidance. The proposal now assigns those owners, includes those examples, and maps each adaptation to its pinned source while excluding unshipped dependencies.

The same independent reviewer rechecked the repairs and reported no remaining blockers. Two optional wording suggestions were incorporated: use the shared method names where standalone IDs may not ship, and make the cache experiment a choice between proposed designs.

## Implementation review

`catalog_implementation_review` reviewed the implemented package, manifests, README, provenance and synthetic hook assertions. The reviewer found that a draft without independent review could still appear to qualify for execution and that a measurement-only request could fall into the product-change procedure. The fixes explicitly gate readiness and execution on required review, require authorized dispatch, and stop the measurement-only branch before edits. The reviewer rechecked both repairs and reported no remaining material findings. Host evaluation remains deferred.

`reduction_review` independently checked the subsequent 19-skill catalog against the user's exact list, including metadata, links, provenance and the two merged workflow boundaries. No material findings were reported.
