# Marketing measurement

Start with the decision the number should change. Define who is eligible, the metric numerator and denominator, event and time window, direction of improvement and downstream guardrails. A signup count and signups per eligible visit answer different questions.

1. **Trace the inputs.** Identify the source of truth, event meaning and trigger, identity boundary, redaction or consent behavior, deduplication, and handling of blocked clients or missing data. Validate a successful path and an excluded path using sanctioned test data. Confirm event payloads and reporting independently where practical.
2. **Make comparisons fair.** Align time zone, windows, inclusion rules, campaign parameters and currency. Check cohort size and traffic mix when interpreting movement. State whether revenue is booked, paid, or net of refunds. Check disagreement between platform reports and internal measures before reconciling or summing them.
3. **Handle attribution honestly.** Document the model and lookback. Platform credit is descriptive; it does not establish what would have happened without the campaign. For a material causal decision, consider an appropriate holdout or grouped test and document overlap and spillover.
4. **Decide prospectively.** Set the primary metric, guardrails, minimum meaningful effect and stop rule before exposure. Report absolute and relative effect alongside uncertainty and data quality limits. Do not declare a winner because a proxy improved or a dashboard moved early.

For a conversion event, state the confirmed business transition, unique event key, permitted fields, system of record and expected reporting delay. For a trial booking, an accepted reservation may count once by booking ID. A rejected form counts zero, and a duplicate callback for the same booking counts once. A later cancellation belongs in a separately defined reversal or net-bookings measure. Trace these cases from fixture to report. Respect collection permissions when reconciling analytics with business totals.

Return a concise measurement or tracking plan with event definitions, QA steps, owner and decision rule, or the observed result and limits. Give evidence about the value of a product change to [Ship](../../ship/references/ProductReview.md) for the product owner's decision.
