# Product requirements

Write the agreement needed to make and verify the next product decision. Reuse the same source of truth when it already exists. A small change may need only a behavior statement and a few acceptance cases; a multi-team dependency may need a more durable specification.

- State the problem, target user and situation, evidence, desired outcome, and what is outside this version. Name the decision owner and unresolved material choices. Separate assumptions from established rules.
- Specify observable behavior: allowed actors and starting states, inputs and transitions, visible results, invalid or abandoned paths, access, and any data, accessibility, compatibility or performance constraints that affect acceptance. Leave implementation open unless a real contract constrains it.
- Add acceptance cases for the normal path, the likely failure and any material boundary. Give starting condition, action and observable result. If a requirement is ambiguous under retry, concurrent changes or a rollout, ask before making up the product rule.
- Record baseline and success evidence. Mark whether something is required to ship, experiment-only, or explicitly deferred. Give the approved outcome and acceptance evidence to Plan and Test.

For an oversized requirement, cut a usable path by actor, scenario or rule. A first release could let a dispatcher assign one open shift, handle a conflicting assignment and show the confirmed result to both people. Defer bulk assignment and recurring schedules explicitly. Verify that someone can complete the smaller job end to end and that its exclusions still fit the agreed outcome.

Before handoff, ask whether two readers could implement and assess the same intended behavior. Resolve contradictions and leave genuinely unmade decisions open. An accepted product requirement does not grant authority to deploy.
