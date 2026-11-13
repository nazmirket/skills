---
name: release
description: "Use to prepare or publish a versioned release: scope, artifacts, compatibility, release notes and readiness. Use Deploy to roll an artifact out to an environment."
---

# Release

Make a specific version ready for its intended consumers and publish it when authorized. A release may be a package, application build, model, document bundle or other versioned artifact. [Deploy](../deploy/SKILL.md) owns rollout to a running environment; [Migrate](../migrate/SKILL.md) owns persistent-state transitions. See the [routing guide](../../references/Routing.md).

## Pin the candidate

1. Identify the requested version, audience, distribution channels, included changes and existing release convention. Establish whether the request authorizes preparation, publication, or both; honor clear prior authority. Pin the source revision and account for staged, unstaged and generated inputs. Preserve unrelated work and never label a dirty-source build as an exact committed release.
2. Check version and compatibility consistency across manifests, schemas, assets, documentation and upgrade instructions. Identify supported consumers, breaking changes, deprecations and prerequisites. Give state transitions to Migrate and consequential security/privacy questions to [Secure](../secure/SKILL.md). Reuse the current plan and prior validation; reopen decisions only when the candidate changes their basis.
3. Build or assemble using the project's reproducible path. Put agent-created staging and extraction copies under ignored `.work/temp/`; keep the deliverable in its designated destination. Record source, toolchain and artifact identity, including a checksum where useful. Inspect the actual distributable for missing files, private workspace material, secrets, development-only content and required notices. An in-tree test does not prove the packaged artifact contains the tested behavior.

## Verify and distribute

4. Exercise installation or consumption of the candidate artifact in an isolated representative environment. Check upgrade from a supported prior version when relevant, including retained configuration and data. For agent plugins, verify discovered skills, referenced files, installed version and hook activation/trust separately. Give [Test](../test/SKILL.md) missing checks and [Audit](../audit/SKILL.md) the fixed candidate when independent review is required.
5. Prepare release notes, known limitations, upgrade and recovery instructions, and an explicit readiness result. Identify unresolved failures and owner decisions. For a blocked release, preserve the candidate and explain the unmet condition; do not hide a failed required check under a general caveat.
6. Publish only the identified, authorized artifact through the established channel. Check whether an earlier attempt succeeded before retrying an ambiguous publication. Verify the published version and artifact identity from the consumer side. Do not overwrite an immutable version or assume a successful upload means consumers have received it.
7. If deployment is also authorized, hand Deploy the exact artifact, target constraints, compatibility requirements, checks and recovery path. Keep publication, deployment and local installation results separate. Use [Operate](../operate/SKILL.md) for post-release health and [Focus](../focus/SKILL.md) for product outcomes.

**Done:** Deliver the prepared artifact and readiness evidence, or the verified published version and channel, with actual checks and remaining limits. A release-preparation request stops before publication. Keep release records in the project's designated location and scratch artifacts under the [workspace rules](../../references/Workspace.md).
