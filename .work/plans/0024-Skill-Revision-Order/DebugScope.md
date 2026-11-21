# Debug: scope for revision 10

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Debug](../../../skills/debug/SKILL.md) as the owner of causal investigation and the smallest authorized fix. Use the available evidence to start. Bring in another skill only when it answers a distinct question.

- **Fix directly when the cause is clear.** When a focused check confirms the failure and the code directly explains it, make the smallest fix and rerun the check. Skip a separate orientation or investigation pass.
- **Trace unclear causes.** Compare a working run with a failing one and trace the relevant path to the first point where their behavior diverges. After two plausible hypotheses fail, pause the investigation. Report what was ruled out, where the evidence stops, and the next check you recommend.
- **Distinguish a proven defect from an intermittent report.** If the reported failure won't reproduce, fix an independently proven defect when it's in scope. Leave the original report unverified until evidence connects it to the same cause.
- **Respect the request's boundary.** A clearly reported bug authorizes an in-scope fix. Stop at diagnosis when that's what the human asked for, and ask before changing agreed behavior.
- **Reuse verification.** Reuse an existing check that catches the failure. Extend an existing test when the regression case fits naturally. Add a separate test if it needs different setup or would make the existing test unclear.
- **Deliver partial evidence honestly.** When the original check can't run, deliver the in-scope fix and report what passed. Name the exact check still needed and leave that behavior unverified. Honor any explicit completion gate.
- **Use specialists for distinct work.** Debug can run a known focused check directly. Use Adapt if relevant facts are missing, Design if the intended interaction is unclear, and Test if a reliable check needs specialist work. During an incident, Operate still owns mitigation and recovery.

Representative cases: confirm and fix a slice that drops the last item with the existing test; trace a retry that may duplicate a write before editing; deliver a focus handler fix with passing unit evidence and the exact browser check still pending.
