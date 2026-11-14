---
name: preflight
description: "Use when asked to check environment readiness, when a tool fails to run, or when evidence points to a setup blocker."
---

# Preflight

Check whether the environment can support the task. Skip routine prechecks for ordinary work.

## Diagnose the blocker

- Identify where the work or check must run and which capabilities it needs. For a handoff from [Equip](../equip/SKILL.md), use the chosen tool, target environment, and required capabilities. Inspect only what's relevant, using read-only checks. Do not expose secrets or change the environment during inspection.
- Use the configuration that governs the task, such as the container, lockfile, or CI job. If a setup guide disagrees, flag misleading guidance. Ask when the conflict changes what can be done or affects an explicit requirement.
- Report what is ready, missing, incompatible, or unknown and what the evidence establishes. Block only the work that depends on the missing capability. Continue independent authorized implementation and available checks. Name the exact blocked check and leave it unverified.

## Use equivalent evidence

- Use a fallback within existing authority when it proves the same requirement. Report where and how it ran. Ask before using a weaker or uncertain substitute. A host browser can exercise the same build if the container browser isn't required; screenshots can't prove keyboard operation.
- A local run using CI's pinned image, dependencies, and test command can establish readiness if other requirements for the task also match. Say where it ran and that the test itself has not run in CI.

## Set up and hand back

- Verify the documented setup command and explain what it changes. Wait before installing or changing the environment unless that setup is already authorized. If fresh environments routinely lack a tool needed for normal project checks, recommend fixing the shared setup and get approval before editing it.
- After approved setup, check the tool's basic function in the target environment. For a browser, launch it and open the app. Return the readiness evidence and blockers to the workflow responsible for the work; the verification owner runs the change's acceptance checks. For lifecycle work, return environment evidence to [Deploy](../deploy/SKILL.md) or [Migrate](../migrate/SKILL.md) as appropriate.
