# Outcome: revise the Mirket skill catalog

Status: catalog authoring approved; behavioral evaluation is deferred. The final target is the user's exact 19-skill list. Retain issue triage under Author and approved-work status tracking under Plan. The original catalog audit remains a historical record of the larger proposal.

Give Mirket clear workflows across Software Engineering, QA Engineering, Document Authoring, Design, Product Management, Software Architecture, Optimization, Project Management, and Team Management. Keep skill IDs portable, lowercase, and composed of one commanding verb, with the `mirket:` namespace supplied by the plugin.

## Acceptance for this proposal

- Account for all 16 copied references and all 14 authored entry points in the Desktop checkout.
- For each reference, identify what to borrow, where it belongs, and what to omit or qualify. For each current skill, recommend a concrete revision or explain why its contract stays.
- Give every new skill a distinct trigger, output and stopping point. Map all nine scopes without treating job titles as skill names.
- Sequence additions, revisions and migration so the catalog stays usable. Identify human decisions and provide a testable definition of the eventual result.
- Link evidence to the copied reference and existing catalog. Preserve upstream provenance for substantial adaptations.

## Implementation acceptance

- New canonical IDs match their folder, frontmatter and display label. The old cleanup and handoff routes have a documented compatibility decision. The cleanup hook points to the new skill and retains its existing acknowledgment marker; synthetic checks cover the migrated path. Host refresh and applicable hook trust checks happen during the later authorized evaluation.
- Representative prompts route to the correct workflow; closely related counterexamples do not trigger redundant work. Agent writes, external issue creation and acceptance changes respect authorization.
- Substantial draft plans can receive independent read-only review before approval. An unavailable reviewer leaves the gate unmet; execution still requires human approval.
- Catalog structure and relative links validate; the applicable hook checks pass. Skill behavior and discovery are evaluated in both hosts at the end of the catalog revision, after the user confirms the catalog is ready for behavioral testing.
