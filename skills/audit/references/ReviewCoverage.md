# Coverage across reviews

Use a compact table when a review spans several boundaries or someone will revisit earlier conclusions. Identify the target revision and scope. Use the existing issue or report format when it already carries this information. A findings-only request can return the table in chat.

Give each row a stable description of the behavior under review. Cite the evidence and the condition under which it applies. Record what was checked even when the result was clear or a suspected defect was ruled out. For an open row, name the smallest check that could settle it. Count an area as examined only to the extent the evidence covers it.

### Worked example

A second review of a reporting service moves from revision A to B. The renderer at B now bundles a font. The CSV writer and its inputs are identical at both revisions.

| Area | Revision and evidence | Conclusion | Follow-up |
| --- | --- | --- | --- |
| CSV row count | At A, the two-page fixture produced all 51 rows. At B, the writer, pagination caller, and fixture match A. | The earlier missing-row report was ruled out for this path. | Reopen if the writer, caller, or pagination contract changes. |
| Report size | At A, the largest supported report fit the delivery limit with the old font. At B, the renderer embeds a different font. | The previous size conclusion is open at B. | Export the largest supported report at B and compare its byte size with the current delivery limit. |
| Scheduled delivery | Neither review had a run from the scheduler. The manual export exercises a different entry point. | Unexamined. | Inspect a scheduled run at B before assessing this path. |

On the next review, compare the evidence's dependencies as well as the named file. Changes to a caller, configuration, fixture, runtime, or data contract can invalidate a conclusion even when the reviewed lines are identical. Preserve the revision and reason for a superseded verdict so the next reviewer can follow the change. Keep sensitive evidence in its authorized location and reference only what the report needs.
