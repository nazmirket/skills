# OSV-Scanner

Use for known advisories against a resolved dependency inventory. Identify the ecosystem, scanner version and input: a supported lockfile, package inventory, or SBOM. If the question concerns a released artifact, check that the inventory describes what actually shipped.

- Verify input recognition and supported dependency formats. Distinguish declared ranges from selected versions, and check which workspaces, optional targets and transitive dependencies the input includes. An SBOM without usable component names, versions or ecosystem identifiers can miss relevant results.
- Check the advisory’s aliases, affected version ranges and fixed versions. Confirm the selected package and dependency path in the project or artifact. Group aliases for one issue while keeping distinct affected instances. A version match identifies a candidate finding; it does not establish that the affected feature is reachable.
- Record the advisory data source or snapshot and whether an offline mode was used where supported. Use the project’s allowed source and trust boundary. Before comparing two runs, account for advisory data changes; a newly reported finding may reflect a new advisory rather than a new dependency.

Report the package, resolved version, advisory ID, dependency path and limits of the match. Leave dependency changes to the owner and verify the resulting resolved inventory after an authorized fix.
