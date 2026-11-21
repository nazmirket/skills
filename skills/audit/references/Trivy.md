# Trivy

Identify the exact target and scanner mode before interpreting the report. An image scan of a registry digest, an image loaded locally, a filesystem scan, and a rendered configuration scan answer different questions. Record the platform for a multi-architecture image.

- Use the image that actually shipped when assessing runtime dependencies. Pin the digest, OS release, package inventory, Trivy version and database freshness. Check which scanners ran; a vulnerability scan does not imply secret or configuration checks ran, and a source scan does not prove what the runtime image contains.
- Separate OS and application dependency results. Cross-check the installed package and distribution advisory; an upstream version comparison can misstate a distro backport. Confirm which component and layer or package path contains the finding. Report whether the issue is present in the built image and what evidence establishes exposure.
- Review ignore rules, severity filters, and treatment of advisories lacking a fix. Keep excluded or unsupported inputs visible as limits. Prefer a scan of the exact artifact over rebuilding an approximation, and reuse equivalent results for the same digest, policy and database when that answers the question.

Return the digest or snapshot, finding ID, affected version, scope and next step. Leave updates and rebuilds to the owner. Verify an authorized replacement against its own artifact identity without claiming a clean scan establishes its overall security.
