# Prototype method

Use under [Design](../skills/design/SKILL.md) for a visual or interaction question, [Focus](../skills/focus/SKILL.md) for a product rule or workflow, or [Architect](../skills/architect/SKILL.md) for a technical model or boundary. Deliver a disposable experiment and the evidence needed for a decision.

## Bound the experiment

1. Name the decision, the alternatives, and the observable result that would favor one. Choose the smallest artifact the decision maker can run or inspect. Set a stopping point: what cases will be enough, when to stop if the result is inconclusive, and when to remove or retain the experiment.
2. Keep the entire experiment outside production: routes, entry points, variant code, controls, fixtures and assets. Use `.work/temp/<task>/` under the [workspace rules](workspace.md) for a standalone artifact or isolated preview unless the project has a designated sandbox. Exclude it from deployment and production build inputs. Hiding a switcher is insufficient if a query parameter or import still reaches experiment code. Use labeled synthetic or approved, sanitized fixtures; default to in-memory state and stubbed writes. If persistence is the subject, use a disposable scratch store with an explicit reset.

## Choose one branch

- **Visual or interaction comparison:** Show a small number of meaningfully different options with the same representative content, context and states. Change the variable under test; hold the rest steady. Make any interactive switching clear and keyboard operable. Let the user reset or replay a motion or interaction comparison from the same initial state. Identify each variant and any assumptions so the user can point to a specific result.
- **Logic or state experiment:** Put the rule or model behind a small deterministic boundary, separate from the demo or harness. Expose inputs, actions and resulting state in the decision maker's language. Let them reset and explore freely, and provide repeatable walkthroughs for a normal case, a consequential adverse case and an illegal action. Record what happened and what was supposed to happen; observed behavior does not establish a business rule.

## Close with evidence

Provide a runnable link or instructions, the question, cases actually tried, observations and limitations, and the recommendation or outstanding decision. Check that the promised scenarios run and reset before handing them over. Retain the decision and enough evidence to understand it even if the artifact is discarded. A chosen variant or model may inform separately authorized production work; it does not ship the experiment. Close or remove the preview at the agreed stop point. Commit the prototype or post it to an external service only with authorization.
