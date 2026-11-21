# npm audit

Use when npm owns dependency resolution for the project. Confirm npm version, effective registry, workspaces, lockfile, and any dependency groups omitted from the check. Use the actual package manager or a scanner that understands its lockfile when npm does not own it.

- Start from the resolved graph rather than package manifest ranges. Trace a finding to its direct owner and transitive instances. Check overrides, workspace paths, optional dependencies and whether the affected version appears in the deployed artifact or build chain. A development dependency can still matter to CI.
- Distinguish a registry failure or incomplete advisory response from a clean result. The audit command can submit package names and versions to the configured registry; use only the project’s approved registry and workflow for private dependency data.
- Read the advisory and proposed remediation separately. A proposed fix may change resolution, introduce compatibility work, or require a major upgrade. For review, use audit reporting without automatic fixes; `npm audit fix` can run an install and change the dependency tree. Do not use forced upgrades to clear a review finding.

Return the advisory and resolved path, actual scope, and a targeted next step. After an authorized change, review the lockfile diff and run the relevant compatibility check as well as the advisory check.
