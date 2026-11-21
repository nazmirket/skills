# Architect: scope for revision 9

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Architect](../../../skills/architect/SKILL.md) for consequential technical decisions. Write a project architecture decision record (ADR) when a settled choice changes a lasting boundary, such as where hosts get their skill definitions. Keep behavior-preserving changes within an existing boundary in the diff or plan.

- **Compare enough to decide.** Compare the current approach with the strongest viable alternative. Explain why serious contenders were ruled out and stop once the evidence supports a recommendation.
- **Separate requirements from technical choices.** Trace the affected behavior, then ask the human about any unresolved requirement that determines the design. An experiment can test whether a design meets a requirement; it cannot decide what the requirement is. Make technical choices within the approved outcome and bring material tradeoffs that need human judgment to the human.
- **Review without prematurely replacing a decision.** If an original assumption plausibly changed, note that the decision is under review and identify the check that would settle it. Keep the current decision in force. Reopen it only when evidence challenges its rationale. Preserve the accepted record and link any successor.
- **Draft privately.** When an unresolved comparison needs its own document, save a draft under `.work/decisions/` and link it from the active plan. Create the project ADR when the decision is settled. Keep recommendations distinct from decisions and attribute authority accurately.
- **Make the ADR stand on its own.** Follow the project's ADR format and location. Include the context and constraints, alternatives considered, choice and rationale, test setup and observed results where applicable, consequences, and any known condition for revisiting. Give maintainers enough detail to understand the decision and reproduce the checks without relying on the private plan. Supplement with links when useful; label unverified claims.
- **Hand off the ADR.** Give the decision record to Plan when execution planning is needed. Plan derives the steps and checks. The decision record does not grant implementation authority.

Representative cases: Mirket's root skills catalog changed a lasting boundary; reorganizing a loader while preserving its inputs and outputs did not. A host release note can prompt review of the compatibility manifest decision; only evidence from a relevant comparison can reopen it. If concurrent writes would determine the storage design, trace the write paths and ask whether overlap must be supported before testing designs against that requirement.
