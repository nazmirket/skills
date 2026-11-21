# Orchestrate: scope for revision 24

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Fold Orchestrate into [Plan’s coordination branch](../../../skills/plan/SKILL.md#coordinate-workers). Plan sequences work, tracks progress, and coordinates workers when delegation is allowed. [Brief](../../../skills/brief/SKILL.md) still owns handoff content and continuity. [Audit](../../../skills/audit/SKILL.md#independent-review) still owns review criteria and independence.

1. **Prefer parallel work for substantial independent scopes.** Keep tightly coupled work inline. The root assigns workers directly, resolves conflicts, and owns integration. Workers report to the root and do not delegate further. Follow the human's instructions and the host's delegation rules. If delegation is unavailable, continue authorized work inline and leave any required independence or isolation gate open.
2. **Settle the shared plan before dispatching implementation.** Pin the outcome, shared interfaces, integration order, and execution authority. Authorized, bounded read-only investigation or review of a fixed target can happen earlier. Use Brief for assignments.
3. **Split along established ownership boundaries.** Follow existing modules, artifacts, or roles. Keep changes that cross those boundaries together unless the shared contract is clear. Give concurrent workers exclusive write paths or isolated workspaces; sequence changes that would write to the same state.
4. **Match capability to judgment.** Prefer stronger capabilities for consequential, creative, or ambiguous work. Reserve cheaper options for bounded deterministic work. Use only settings the host supports.
5. **Report on completion unless coordination is needed.** Surface a dependency, scope conflict, or material decision as soon as it affects the plan. Correct routine drift within scope. Escalate changes to authority, ownership, interfaces, or acceptance and pause only the affected work.
6. **Check and integrate returned work.** The root inspects the work and evidence before accepting it. Keep substantial repairs with workers; the root can make a bounded integration correction after handback and once write ownership is clear. Verify the integrated result and use independent review of the fixed target when required or materially useful. If a qualified reviewer is unavailable, keep the required gate open. Self-review cannot satisfy it.

## Implementation and checks

The merge moves coordination into Plan, removes the standalone skill and metadata, and aligns routing, references, catalog, website, and the read-only coordination fixture. Approval covered guidance and local verification, not delegation or live host evaluation.
