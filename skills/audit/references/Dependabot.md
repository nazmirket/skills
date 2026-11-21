# Dependabot alerts and GitHub dependency review

Identify the repository, alert status, advisory, manifest path, and the relevant Git revision. Use Dependabot alerts for known advisories in the dependency graph; use dependency review for changes between the intended base and head. Neither proves which packages the deployed artifact contains.

- Check how GitHub’s graph was populated and what it covers. Supported static manifests and lockfiles, dependency submissions and build-specific inputs can differ. An unchanged dependency can receive a new advisory, and a pull request can introduce an affected transitive package without changing a top-level name.
- Trace the resolved version to the introducing change and identify whether it ships, runs during builds, or affects another approved environment. Check the advisory range, affected path, and fixed candidate. Verify any automated update’s actual lockfile and behavioral impact; a proposed update or green scanner does not establish compatibility.
- Keep dismissals and policy exceptions reviewable. Record evidence, scope and a recheck condition when an exception is approved. Reviewing an alert does not authorize dismissal, changing repository settings or opening a public comment.

Report the affected revision and manifest, advisory, resolved path and what the GitHub view misses. If artifact or workspace coverage differs, request the missing evidence from its owner.
