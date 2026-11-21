# Release: scope for revision 20

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Retire Release as a standalone skill. The task owner prepares the versioned candidate, decides readiness against the project’s existing criteria, and publishes the identified artifact when authorized. Use the shared [versioned distribution guide](../../../references/VersionedDistribution.md) without transferring ownership.

- **The task owner prepares and publishes.** Apply the project’s release conventions. Identify the source inputs, version, artifact, and distribution channel. Inspect what actually ships, record readiness and unresolved conditions, and include release notes and upgrade or recovery guidance where relevant. Preparation alone does not authorize publication. Verify the published version and artifact from the consumer side. Resolve ambiguous publication state before retrying; do not overwrite an immutable version.
- **Test supplies verification evidence.** Check the exact distributable through representative installation or consumption and supported upgrades where relevant. Return actual results and gaps to the task owner. Source checks alone do not verify the packaged artifact.
- **Audit supplies findings.** Review the fixed candidate when needed and preserve the existing independence rule for high-risk work or an explicit gate. Findings go back to the task owner; Audit does not publish.
- **Deploy keeps environment activation.** When activation is authorized, hand [Deploy](../../../skills/deploy/SKILL.md) the exact artifact, target constraints, compatibility, checks, and recovery path. [Migrate](../../../skills/migrate/SKILL.md) still owns substantive state transitions. Ongoing health was assigned to Operate and later [merged into Deploy](DeployScope.md). Report preparation, publication, and activation separately.

## Open choices

Only ownership was answered. Questions 2–10 remain open: when to use a distinct workflow, candidate identity, readiness evidence, handling failed or missing checks, release notes, publication authority, ambiguous attempts, completion evidence, and handoff. Carry forward the current rules without creating a new approval or release gate.

## Implementation and checks

The merge moves release guidance to a shared reference, removes the standalone entry and metadata, and aligns both hosts with the same 18-skill catalog. The prepare-only fixture remains with the task owner and stops before publication and deployment. Approval covers only the catalog revision.
