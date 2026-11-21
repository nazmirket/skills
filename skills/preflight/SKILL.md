---
name: preflight
description: "Use when asked to check environment readiness, when a tool fails to run, or when evidence points to a setup blocker."
---

# Preflight

Preflight owns environment readiness and authorized setup. Use it for a readiness request or evidence of a setup blocker. Ordinary work can proceed directly.

## Diagnose the blocker

Identify the target and required capabilities. Reuse [Equip](../equip/SKILL.md)'s tool choice and requirements when available. Inspect only relevant configuration and capabilities with read-only checks that keep secrets private. Follow what actually governs execution, such as a container, lockfile or CI job. Flag conflicting setup guidance. Ask when the conflict changes feasibility or an explicit requirement.

State what is ready, missing, incompatible or unknown. Block only work that needs the missing capability. Continue independent authorized work and available checks.

## Use equivalent evidence

Use an authorized fallback directly when it proves the same requirement. Report where and how the check ran. Ask before substituting weaker or uncertain evidence. A host browser can exercise the same build when a container browser is optional. Keyboard operation requires an interaction check.

A local readiness check can use CI's pinned image, dependencies and command when other requirements also match. Identify it as local and keep the CI run unverified.

## Set up and hand back

Verify the documented setup command and explain its effects. Install or change the environment only when authorized. If fresh environments routinely lack a tool for normal checks, recommend a shared setup fix and get approval before editing it.

After setup, verify basic function in the target environment, such as launching the browser and opening the app. Return readiness evidence and the exact check still blocked, if any, to the task owner. For rollout or state transitions, that owner is [Deploy](../deploy/SKILL.md) or [Migrate](../migrate/SKILL.md). The verification owner runs acceptance checks.
