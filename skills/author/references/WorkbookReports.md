# Workbook reports

Start with the question the reader will answer, the source rows and the values they may change. Use the project's spreadsheet or host workflow. Keep the requested sheet names, headers, units, date ranges and rounding conventions.

- **Editing a workbook.** Locate its input cells and inspect both formulas and displayed values before editing. Check which features the round trip must preserve, such as named ranges, validations, charts or macros. Use an editor that preserves them. A values-only import is suitable for inspecting numbers. Save edits through a formula-preserving view.
- **Building a report.** Keep source inputs distinguishable from derived figures. Put assumptions and units beside the values they govern. Use formulas for totals or rates the reader expects to update. For a fill-in template, identify editable cells and show the expected input format.
- **Checking the delivered file.** Recalculate changed formulas in a compatible engine, save, and reopen the deliverable. Inspect affected formulas, their displayed results and downstream summaries for new errors or stale values. Reconcile a result independently against the source. On a scratch copy, change one consequential input and check the expected change downstream.

For example, if a total excludes cancelled orders, check one included order, one cancelled order and the resulting total. Increase the included amount by 10 on the scratch copy and verify that the total increases by 10 in the same units. A numeric result alone can conceal a wrong range.

Inspect the final labels, number formats and charts at reading size. Identify any calculation the available engine could not evaluate and the affected results. For a flat data export, verify column types on reimport, row count and representative values such as leading-zero IDs.
