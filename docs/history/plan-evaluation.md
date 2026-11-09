> Historical evaluation of an earlier plan skill draft. These observations are not a current catalog-wide test.

# Plan skill evaluation

These are isolated simulated exercises with independent agents, not tests of plugin installation or automatic discovery. The samples are illustrative, not statistical reliability estimates.

## Baseline: conflicting shipping rule and undefined loyalty discount

Fixture: `src/shipping.js` applies free shipping at a subtotal of $50 or greater. The simulated user asserted that the existing threshold is $35, requested free shipping over $35, and mentioned a loyalty discount without defining its terms.

The baseline agent inspected the fixture and identified the $50 discrepancy. It asked for loyalty terms and the subtotal basis, but proposed proceeding with a strict over-$35 rule while the qualifying subtotal was unresolved, included release as an action, and created no plan or agreement files.

## Guided exercise: discrepancy and pending business choices

With the draft skill loaded explicitly, a separate agent created `.plans/checkout-shipping-loyalty/Plan.md`, `Outcome.md`, and `Agreement.md`. It reported the $50 discrepancy, left the loyalty details and plan approval pending, and did not change application code. On rechecking, the agent reported a sequence limitation: it inspected the fixture before creating the three planning files, despite the instruction to keep them during investigation.

## Guided exercise: intentional hypothetical and unchanged fee

A second user prompt explicitly described $35 as a hypothetical demo threshold and distinguished the real $50 threshold. The first guided run correctly separated hypothetical and observed behavior, but treated an existing $8 fee as an agreed demo requirement without confirmation. A revision told the agent to propose preserving an existing rule until confirmed; one fresh retest still carried $8 into the acceptance criteria as settled.

The skill was revised again to give a concrete example and require a cross-check across all three files. In a further fresh run, an agent created all three required files, distinguished the observed $50 rule from the hypothetical $35 rule, and marked the below-threshold fee and related acceptance check pending in each file. It left approval pending and did not implement the demo. This single passing run does not prove consistent behavior.

## Validation limits

- Frontmatter was parsed with Ruby's YAML library and checked for the expected name, description, and nonempty body.
- The installed `quick_validate.py` could not run because its Python environment lacks PyYAML. Claude Code CLI is unavailable here.
- No Codex or Claude Code marketplace installation, native discovery, automatic triggering, or cross-host execution was tested. Test the skill in fresh sessions on both hosts before relying on it.
