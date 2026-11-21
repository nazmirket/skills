# Brief: scope for revision 23

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Brief](../../../skills/brief/SKILL.md) as the owner of handoffs and explicit pause and resume requests. [Plan](../../../skills/plan/SKILL.md) tracked progress; Orchestrate assigned and coordinated workers at the time of this revision. The [later merge](OrchestrateScope.md) moved worker coordination into Plan.

1. **Use one small core.** State the outcome, exact next action, authorized scope and its source, essential evidence, and what to recheck. Add detail only when it changes what the recipient should do. A handoff records existing authority; the recipient reuses it only while it still applies and agrees with current instructions.
2. **Point to evidence when it is accessible.** Link to the authoritative source or give its exact location. Copy only what the recipient cannot retrieve or what would materially delay the next step. Label any limits, and omit secrets and unnecessary personal information.
3. **Save for reuse or on request.** Keep immediate worker assignments and updates in the coordination channel. Save handoffs intended for later reuse and unfinished pauses; use the designated destination or a numbered brief under `.work/briefs/` as applicable.
4. **Recheck what matters to the next action.** Correct routine drift and continue within existing scope. Pause affected work if a conflict changes the goal, authority, product decision, ownership, interface, or acceptance criteria. Escalate to the human or coordinating owner as appropriate.
5. **Relay material changes to affected workers.** Orchestrate decides who needs the update. Brief says what changed, what it means for the worker, and what to do next. Report when delivery cannot be confirmed.
6. **Pause explicitly; resume from current evidence.** On a pause, stop starting work and save the minimum reliable resume point for unfinished work. Stop task-owned workers only when safe and supported. Leave unsafe-to-interrupt operations running and record their known or uncertain state. Give the human the resume location and stop. On resume, recheck current state, correct routine drift, continue already authorized work, and escalate material conflicts before acting on the affected part.

## Implementation and checks

The revision updates Brief, routing, and affected fixtures. Handoffs favor source pointers, preserve traceable authority, and pause only affected work on material conflict. The explicit pause and resume branch keeps its safety limits. Approval covered the catalog revision, not pausing or resuming an active task, launching workers, or sending messages.
