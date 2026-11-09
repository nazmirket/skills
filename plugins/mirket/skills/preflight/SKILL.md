---
name: preflight
description: "Use when checking whether the current execution environment is ready for a project's development work, including missing tools, incompatible versions, and setup blockers."
---

# Preflight

Determine whether the environment where the agent will actually work can support the requested project work. Base the assessment on the project's requirements and observed environment; do not change the environment during inspection.

## Identify what the project needs

1. Identify the project, the requested work, and where commands will run: the local device, a container, remote machine, or another available execution environment. State when the agent cannot inspect the relevant environment.
2. Read the relevant setup documentation, project instructions, manifests, lockfiles, version pins, configuration, and existing development or CI commands. Identify the tools, runtimes, versions and services required for the requested work, as well as optional components. Respect the project's existing setup and conventions. If a requirement is unclear or sources conflict, report the uncertainty instead of inventing a requirement.

## Inspect and compare

3. Use focused, read-only checks appropriate to the operating system and execution environment. Identify the active executable or service, its version and availability, and compare them with the project's stated requirements. Check the capabilities relevant to this work rather than collecting an unrelated inventory. Avoid exposing credentials, secrets, or unnecessary personal data.
4. Classify each material requirement as **ready**, **missing**, **incompatible**, or **unknown**, and distinguish required components from optional ones. A command that cannot be inspected or executed is not necessarily absent; describe the observed failure and limits. Report the project evidence and actual observations supporting each blocker. Do not claim readiness when a required capability remains unknown.

## Resolve blockers with the human

5. For a missing required component, propose a specific installation that fits the project and current platform. For a breaking mismatch, explain the expected and observed setup, its impact, and a concrete project-compatible fix. Describe the relevant command or changes, scope and meaningful effects so the human can review the proposal. If more than one valid approach exists, show the tradeoff and recommendation. Ask for confirmation before any installation or environment change, unless the human has already explicitly authorized that specific action.
6. When a required component is missing, incompatible or cannot be verified, stop work that depends on it. Present the proposed fix before proceeding with the affected project work. Continue independent read-only investigation where useful, and do not call a proposed fix complete until it has actually been applied and checked.
7. If a preferred or project-required tool is unavailable, do not silently substitute an inferior method. An alternative is inferior when it reduces required capability, correctness, reliability, security, project fidelity or verification coverage for the task. Explain what the alternative would change and ask for explicit confirmation before using it. If its quality relative to the required method is unclear, explain that uncertainty and ask before substituting. Earlier explicit authorization for that specific alternative remains valid.
8. After an approved change, recheck the affected requirement and report the actual result. Return readiness evidence and blockers to the person or workflow responsible for the affected work. A proposal does not authorize an environment change.

**Done:** Report a concise readiness assessment, evidence for material findings, the effects and approval needed for each proposed fix or inferior fallback, and any remaining unknowns. The affected work remains blocked until its requirements are met or the human explicitly accepts an identified alternative.
