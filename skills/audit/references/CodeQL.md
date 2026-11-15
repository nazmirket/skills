# CodeQL

Start with the existing result for the reviewed SHA. Confirm the CodeQL version, languages, build mode, query suite and analysis status. For compiled languages, establish what actually entered the database. A skipped build, unsupported language, or missing target can make a clean report misleading.

- Use the result path to identify the affected input, transformations, checks and destination. Read surrounding code and framework behavior on the reviewed revision. Validate whether the reported path reaches the relevant boundary and whether an existing guard changes the finding. A reported path is evidence to review, not proof of exploitability.
- Check whether the rule and result are new, or came from a different suite, language configuration or base revision. Record the stable rule ID and exact location. Consolidate duplicate paths to the same defect while retaining distinct affected entry points when they change scope.
- Investigate missing coverage rather than trying broader queries reflexively. Confirm how generated sources, build variants and framework models were included. Prefer an already authorized analysis or a trusted build environment; a scan of untrusted changes does not authorize executing their build scripts in a privileged context.

Report confirmed defects, risks pending corroboration, and scanner limits separately. Leave configuration changes, dismissals and fixes to the authorized owner.

Upstream: [CodeQL code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning), [Build options for compiled languages](https://docs.github.com/en/code-security/reference/code-scanning/codeql/build-options-for-compiled-languages).
