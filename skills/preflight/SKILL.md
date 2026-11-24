---
name: preflight
description: "Use when asked to check environment readiness, when a tool fails to run, or when evidence points to a setup blocker."
---

# Preflight

## Diagnose the blocker

Identify the target and required capabilities, using existing [tool requirements](../equip/SKILL.md) where available. Check the configuration that actually governs execution, such as the container, lockfile or CI job. Inspect relevant capabilities without exposing secrets. Flag conflicts that affect feasibility or requirements. Block only dependent work and report what is ready, missing, incompatible or unknown.

## Use equivalent evidence

Use an authorized fallback directly if it proves the same requirement, such as a host browser exercising the same build. Ask before substituting weaker or uncertain evidence. Give the verifier the working browser and [interaction check](../design/references/flows/CollectEvidence.md#check-an-interaction) for keyboard behavior. Report where the check ran. Label a matched local run as local and keep CI execution unverified.

## Set up and hand back

Verify the setup command and its effects before authorized changes. For recurring missing capabilities, identify the shared setup fix and apply it only under authority for that shared environment. Verify basic function in the target. Return readiness evidence and any blocked acceptance check to its owner, including [Deploy](../deploy/SKILL.md) or [Migrate](../migrate/SKILL.md) where applicable.
