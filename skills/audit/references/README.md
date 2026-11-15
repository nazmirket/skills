# Audit tool guides

Start with the pinned revision, artifact, or dependency inventory and the question the review must answer. Use existing evidence when it covers that target. Open only the guide for the review surface or scanner you’re using. If a different question needs separate evidence, select that guide at the point of need.

| Review question | Guide |
| --- | --- |
| What changed in a Git diff or GitHub pull request, and how should findings be grounded? | [Git and GitHub code review](GitHubReview.md) |
| What does an existing CodeQL result or database cover? | [CodeQL](CodeQL.md) |
| Is a Semgrep pattern match or data-flow finding material? | [Semgrep](Semgrep.md) |
| Did the scoped change expose a credential or other secret? | [Gitleaks](Gitleaks.md) |
| Which known findings apply to the built image, filesystem, or its configuration? | [Trivy](Trivy.md) |
| Which resolved components in a lockfile or SBOM match advisories? | [OSV-Scanner](OSVScanner.md) |
| What does npm’s advisory report say about the installed dependency tree? | [npm audit](NpmAudit.md) |
| Which Python packages in the selected environment or input have known advisories? | [pip-audit](PipAudit.md) |
| What does GitHub’s dependency graph show about an alert or dependency change? | [Dependabot and dependency review](Dependabot.md) |

Use the project’s existing tools, policy and result format. Verify what the scanner analyzed, plus its version, rules or advisory data and coverage. Treat tool output as a lead: corroborate material findings against the reviewed target and distinguish affected code or packages from demonstrated impact. Report skipped or unsupported inputs even when the tool returned no findings. Keep review read-only; do not apply fixes, run untrusted builds, upload private source or dependency data, or post findings without the applicable authority.
