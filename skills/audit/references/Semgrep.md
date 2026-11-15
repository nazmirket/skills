# Semgrep

Confirm the installed engine and edition, exact source revision, ruleset, languages, exclusions and whether the result came from a full or change-focused scan. Use the project’s configured rules rather than fetching an arbitrary set into a sensitive workspace.

- Distinguish a structure match from a data-flow result. Read the rule rationale and match context. For reported flows, check which inputs, guards and destinations the engine models and whether the finding crosses functions or files the selected engine can analyze. Verify ambiguous paths in the actual code before assigning impact.
- Look for parse errors, unsupported languages and ignored paths before interpreting no findings. A change-focused scan is useful for regressions but may miss the rest of the codebase or unchanged paths that the change newly connects.
- Prefer results for the exact revision. If rerunning is needed, use the narrowest relevant paths and existing rules, but keep enough context for the analysis. Record rule ID, configuration, and skipped coverage. Avoid broad suppressions or autofixes just to make a run green.

Report the actual location, condition, effect, and a narrow next step. Keep analysis local unless the project authorizes a hosted workflow for the relevant source and results.

Upstream: [Semgrep Code overview](https://docs.semgrep.dev/semgrep-code/overview), [Data-flow analysis](https://docs.semgrep.dev/writing-rules/data-flow/data-flow-overview).
