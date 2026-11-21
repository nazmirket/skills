# Critique: scope for revision 17

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Retire Critique as a standalone skill. Move its useful review guidance into the skills that already own the work. Keep the review step for substantial visual work.

- **Design owns visual critique.** Use its [distinct branch](../../../skills/design/SKILL.md#visual-critique) for visual review requests and for substantial visual work. For substantial work, keep the first inspection, then review the brief and the actual preview or export in its intended medium. Judge how the work looks, feels to use, and communicates. Keep the [interface stress guidance](../../../skills/design/references/UiStress.md) with Design, and recheck material visual corrections before delivery. Review-only requests end with findings.
- **Author owns writing quality.** Use the existing workflow to judge whether a document, report, or substantive copy serves its reader and purpose. Review-only requests end with findings about clarity, structure, and material claims. Preserve Author’s current verification and issue triage guidance.
- **Audit owns technical review.** Use its existing findings workflow for integration risks and unnecessary complexity when they impose a meaningful cost. Reuse [Test](../../../skills/test/SKILL.md) evidence for behavior and performance claims. Keep Audit’s independent review rule for high-risk work or explicit gates.

## What the draft leaves open

Only ownership was answered. Questions 2–9 remain open: any additional review triggers, judgment criteria, evidence requirements, coverage, which findings to include, who resolves matters of taste, who can hold delivery, and who rechecks corrections. Carry forward existing owner rules where they apply. Preserve Design’s approved review step and the current authorization boundary for corrections. The merge proposes no new delivery gate or independence requirement.

## Implementation and checks

Move the guidance before removing the standalone entry and its agent metadata. Update routing, live references, the catalog and website, and the affected behavior fixtures. Check that both hosts package the same 20 skills, that active guidance points to the receiving owners, that the writing review fixture stops at findings, and that Design still calls for a distinct review for substantial visual work. Keep historical decisions as records.
