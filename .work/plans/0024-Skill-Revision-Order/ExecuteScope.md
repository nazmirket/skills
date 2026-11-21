# Execute: scope for revision 1

**Status:** Implemented in the working tree at [skills/execute](../../../skills/execute/SKILL.md). Installed plugins and the live website have not been changed.

## Purpose

Execute is the default working posture of Mirket. Finish the assigned outcome with the least friction that preserves quality. Keep communication to what the human needs to decide, act on, or assess the result. Apply the posture across skills rather than creating a second workflow for work they already own.

Execute replaces Distill outright, with no alias. It keeps concise, factual reporting and adds solution choice, scope discipline, and when to rethink the approach. Plan still structures substantial work, Equip owns material tooling choices, and Test owns verification.

## Working rules from the survey

1. **Work from the outcome.** Know what completion looks like. Distinguish requirements from assumptions. Make routine, authorized decisions directly. When a suggested method is flexible, use a simpler route that preserves the outcome. Report the switch only if it matters. Mention unrelated findings only when consequential; finding an issue does not authorize fixing it.
2. **Take the direct route unless it has a concrete maintenance cost.** Reuse what fits. Extract a shared abstraction when duplicated rules are likely to diverge. For infrastructure architecture and big-picture decisions, give the wider system and consequences the attention they need. Simplicity is a property of the solution, not an excuse to skip analysis. Use the narrowest check that can catch a meaningful failure, plus required checks.
3. **Rethink assumptions without taking over the decision.** After two attempts fail for the same reason, revisit the assumption and try a different check that can resolve it. Where changing the framing of a widely used project could break an existing feature or ecosystem, get the human's approval before proceeding under the new framing. In creative work, surface consequential assumptions or alternatives without imposing the agent's taste as the answer.
4. **Speak only when it helps.** For a straightforward, authorized fix, start without a kickoff unless there is a material assumption to surface or the host requires an update. Skip narration of ordinary steps, unformed thoughts, and settled details that do not affect what the human does next. Report a recovered detour only if the human needs to act or expectations change. Lead the final reply with the result and the most useful verification; retain material limits.

The user named Karpathy Skills, Ponytail, Caveman, KISS, and Clean Code as influences. Use them as orientation for focus, simplicity, economy, and readability. Derive the wording and acceptance cases from the user's examples.

## Hooks and limits

The [session and prompt hooks](../../../hooks/execute.py) inject short guidance. The existing [Stop hook](../../../hooks/cleanup.py) can request one extra review when opted in. Prompt injection can make guidance present where hooks run. A supported Stop continuation can request another pass; it cannot retract text already shown or guarantee that a model followed the guidance. Host trust and support still apply.

Inject Execute guidance at session start and prompt submission. Do not add an automatic extra pass. A stronger intervention needs a concrete, detectable violation and a clear correction; no particular rule or blocking mechanism was specified. Do not add a general verbosity gate.

Clean and pre-commit behavior are unchanged. The existing opt-in Stop review now names Execute in its reply guidance. Active routing, documentation, and tests use the new name; historical records may keep the old name.

## Candidate acceptance cases

- A small, authorized edit takes the direct path and reports the result and the check without a running narrative.
- A flexible implementation suggestion creates a maintenance burden. The agent uses a simpler route, but asks before changing the framing of a widely used project where a feature or ecosystem could break.
- Two attempts fail for the same reason. The agent revisits the assumption and takes a discriminating next step instead of repeating it.
- A tempting simplification would change behavior, weaken a check, or omit a material limit. The agent preserves quality and reports the relevant evidence.
- A consequential blocker is raised in time for the human to act. A trivial detour that was resolved does not become a status update.
- Creative work exposes two valid directions. The agent raises the choice rather than silently choosing a new direction.
- Hook checks distinguish guidance delivery, existing opt-in behavior, and observed agent behavior in each host.

## Verification

All 41 local tests passed, including hook and package checks. The new direct-fix fixture's heading check failed against the starting file and passed after the literal fix. The website build and discovery checks passed, and the rendered pages exposed Execute at desktop and mobile widths; the old Distill route returned 404. An isolated Codex install discovered Execute among 25 skills and all four hooks. Synthetic runs of the installed hook script returned guidance for both events. Live agent behavior and a fresh Claude Code install were not verified for this revision.
