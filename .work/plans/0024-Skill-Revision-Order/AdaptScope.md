# Adapt: scope for revision 2

**Status:** The user authorized implementation from the survey, and the [packaged skill](../../../skills/adapt/SKILL.md) is revised in the working tree.

Adapt is the read-only skill for discovering and understanding project facts. It builds or refreshes enough context to know how the project works, what decisions and rules govern it, and where current implementation diverges from intent. Adapt passes findings to the skill responsible for acting on them.

## When and how to orient

- On a new codebase, make a broad pass over the main subsystems before changing it. Use representative paths to establish the project shape; a full file-by-file read was not specified.
- In a familiar project, reuse verified context. Refresh when a relevant fact, convention, or constraint is missing or stale. A different feature, worktree, or changed evidence can invalidate earlier orientation. Refresh only the affected scope.
- Consult sources in this order: project documentation, architecture decision records (ADRs), relevant project memory, then the codebase. Consult available project memory early on substantial or resumed work and skip it for routine tasks. Check remembered facts that affect the next step against the current project.
- Treat the order as a way to find context. Docs and ADRs describe intended behavior and decisions; the code and checks establish what is implemented. If they disagree and the work depends on which contract is intended, show the discrepancy and ask the user before proceeding on that part.

## What to carry forward

- Carry architectural decisions, solution patterns, system design direction, and enforced rules. Treat a one-off correction as local; apply it as a project default only when the user repeats or confirms it. Treat inferred patterns as leads and label them accordingly.
- Adapt stays read-only. When a durable rule would help, propose the exact wording and destination and wait for approval before it is written. Finding an issue or a preference does not authorize a fix, a persistent profile, or wider memory access.
- Give the user an orientation summary only when requested or when a finding needs their decision. If a finding changes the approach to already authorized work, give one line and continue. Pass evidence to the appropriate skill; use [Debug](../../../skills/debug/SKILL.md) when a finding explains the requested problem and a fix is authorized. Handoff means routing the evidence to the owner; it does not require a separate agent.

## Acceptance examples

- New project: explain how its main subsystems fit and identify the relevant constraints before any edit.
- Familiar project in another worktree: verify the facts that may differ and reuse the rest.
- Docs and implementation disagree on a contract the fix depends on: show intended versus observed behavior, then ask the user which contract should govern.
- Orientation reveals the cause of an authorized fix: pass the finding to Debug, give a one-line update if it changes the approach, and continue without another approval.
- An earlier correction looks reusable: treat it as local or tentative until repeated or confirmed; propose the wording and destination before saving it as a standing rule.

## Verification

All 41 Python tests passed. The new contract-conflict fixture establishes that the written sources disagree and that current behavior includes negative values. The site build and discovery checks passed; the catalog summary, source order, and handoff links were checked in a browser at desktop and mobile widths. The fixture does not establish live agent behavior.
