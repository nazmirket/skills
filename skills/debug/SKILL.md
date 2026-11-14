---
name: debug
description: "Use to find the cause of a concrete failure or unexpected behavior and make the smallest authorized fix."
---

# Debug

Start with what should happen, what actually happened, and the best evidence already available. Use [Adapt](../adapt/SKILL.md) if relevant facts are missing. Bring in other skills only for a distinct question, such as [Design](../design/SKILL.md) for unclear interaction intent or [Test](../test/SKILL.md) when a reliable check needs specialist work.

## Find the cause

- **Fix directly when the evidence is clear.** If a focused check confirms the failure and the code directly explains it, make the smallest authorized fix and rerun the check. Skip a separate orientation or investigation pass.
- **Trace an unclear cause.** Use the smallest safe reproduction. Compare a working run with a failing one and trace the relevant path to the first point where their behavior diverges. For each plausible cause, choose a check that can rule it out. After two plausible hypotheses fail, pause the investigation. Report what you ruled out, where the evidence stops, and the next check you recommend.
- **Keep intermittent reports separate.** If the reported failure will not reproduce, record the conditions and what remains unknown. Fix an independently proven, in-scope defect if you find one. Leave the reported failure unverified until evidence connects it to that cause.

## Fix and verify

- A clearly reported bug authorizes an in-scope fix. Stop at diagnosis when requested, and ask before changing agreed behavior. An orientation finding alone does not authorize a repair.
- Reuse a focused check that catches the failure. If a regression case needs coverage, extend an existing test when it fits naturally. Add a separate test if it needs different setup or would make the existing test unclear. Run the required project checks and verify affected behavior.
- Report the cause, fix, and actual results. If the original check cannot run, deliver the in-scope fix with the evidence you have, name the exact check still needed, and leave that behavior unverified. Honor explicit completion gates. Use [Preflight](../preflight/SKILL.md) for setup blockers and its rules for weaker fallbacks.

During an incident, [Deploy’s operations branch](../deploy/SKILL.md#operate-and-recover) owns mitigation and recovery. Give it causal evidence and any authorized fix. Use [Audit](../audit/SKILL.md#security-and-privacy-review) for a separate security or privacy review and [Migrate](../migrate/SKILL.md) for persistent state transitions.
