# pip-audit

Identify the Python interpreter, environment, project requirements or lock input, package indexes, and which dependency groups and platform markers apply. A developer environment is not necessarily the environment used in a deployed image.

- Prefer an already resolved inventory or the matching installed environment when available. Treat requirement paths, indexes and source distributions as inputs with their own trust boundary. Auditing unresolved requirements can require resolving or building package metadata; do not run that process against untrusted inputs in a privileged environment.
- Confirm the installed distribution name and version. Read the advisory range and the suggested fixed versions, then trace the relevant dependency owner. Record skips and unsupported or privately patched packages. Check how the specific build and production extras differ from local tooling before prioritizing.
- Check which advisory service, indexes and network policy actually apply. Keep private dependency data within approved services. An absent match says only that the scanner did not find a known advisory for the inventory it covered. Avoid automatic fixes during a read-only review.

Report the affected resolved package, advisory and environment, severity in context, and the smallest remediation candidate or remaining check. After an authorized update, verify the deployed inventory and affected behavior.
