# Agreement

**Status: catalog order proposed; Execute authorized.** The user asked for a step-by-step revision order. After settling the first skill in the survey, they explicitly authorized implementing [Execute](ExecuteScope.md), replacing Distill outright, updating session and prompt guidance, and preserving Clean without adding an automatic extra pass. This does not approve the entire plan or authorize work on the remaining skills, publication, or changes to installed plugins.

## Working principles already documented

| Principle to carry forward | Evidence |
| --- | --- |
| Act directly within existing authority. Ask about a decision that changes the outcome. Put the result first and report the checks actually performed and the limits. | The user's current working instructions; [Distill revision agreement](../0017-Distill-Lifecycle/Agreement.md) |
| Give each outcome one owner. Use narrow verbs and bring in supporting guidance only for a distinct result or evidence. Keep the direct implementation path available for ordinary work. | [Catalog agreement](../0001-Skill-Catalog-Revision/Agreement.md), [lifecycle agreement](../0020-Product-Lifecycle-And-Memory/Agreement.md), [current routing](../../../references/Routing.md) |
| Keep product priorities, business rules, and consequential choices with the human. Plan substantial work with evidence and a written outcome; keep routine work direct and review-only work read-only. | The user's current working instructions and [previous answers](../0005-Remaining-Skill-Revisions/Agreement.md) |
| Challenge a tool that works poorly with evidence and switching costs. Honor specific authority for tool or environment changes; an inferior fallback needs explicit agreement. | [Equip agreement](../0016-Equip-Rewrite/Agreement.md) and [previous answers](../0005-Remaining-Skill-Revisions/Agreement.md) |
| A reported bug authorizes an in-scope fix unless diagnosis only was requested. Use focused checks, add regression coverage when it earns its keep, and disclose missing evidence. | [Previous answers](../0005-Remaining-Skill-Revisions/Agreement.md) |
| For redesign, see the existing interface first. For image concepts, agree on the detailed brief before generating. Verify visual results in the rendered medium. | [Previous answers](../0005-Remaining-Skill-Revisions/Agreement.md) and the user's current working instructions |
| Keep artifact preparation, publication, rollout and continuing operations separate. Record settled architecture decisions at the project's ADR location, and preserve unrelated work. | The user's current working instructions, [lifecycle decision](../../../docs/decisions/0002-LifecycleOwnership.md), [routing and hook agreement](../0019-Routing-And-Hook-Hardening/Agreement.md) |

These are starting constraints, not proof of how every edge case should work. The sequence in [Plan.md](Plan.md) proposes specific cases to surface exceptions. A current user answer takes precedence over old agreements. Old catalog counts and packaging paths in historical records are not current. No automatic expansion of memory, hooks, or behavioral testing is implied.

A flat alphabetical pass would be easy to track but would revisit the same boundaries repeatedly. A single rewrite would hide the user's choices in a large diff. The proposal groups skills by shared decisions and revises one entry at a time, adjusting the later order when the work exposes a dependency.

## Review

Checked inline against the root catalog, the routing guide, the existing behavioral cases, and the previous agreements above. No independent reviewer participated in this planning turn.

## Focus removal

The user directed removing Focus as redundant. Leave product priorities and business rules with the human. Plan already surfaces unresolved choices that affect implementation; Curate and Operate continue to supply comparison and operational evidence within their own scope. The sequence keeps the removed position as a record.

## Design and Brief merges

The user authorized merging Imagine into Design and Sleep into Brief as simple branches, and removing both standalone entries. Design keeps explicit brief agreement before generation and separate implementation authority. Brief keeps explicit pause and resume behavior. The catalog has 22 skills. The sequence retains the old positions for traceability; Plan is next.
