---
name: execute
description: "Apply throughout Mirket work. Own routine answers, known edits and authorized implementation of settled requirements when no specialist owns the result."
---

# Execute

Execute owns routine answers, known edits and authorized implementation when requirements and architecture are settled and no specialist owns the result. Choose one owner per outcome and apply these working rules throughout. Add support for a distinct question and return its evidence to the owner. Consult the [routing guide](references/Routing.md) when ownership is unclear. Use [Code](../code/SKILL.md) for stack decisions and [Plan](../plan/SKILL.md) when risk or coordination warrants it. Execute owns [standalone release preparation](references/VersionedDistribution.md).

Keep all agent-created temporary artifacts in `.work/temp/<task>/`. Before the first project write, follow the [workspace rules](references/Workspace.md) to check and repair the project’s `.gitignore`.

1. Establish what completion requires. Separate requirements from assumptions and make routine choices within existing authority. When the method is flexible, take the simplest complete path. Raise unrelated findings only when consequential. Fix them only within scope.
2. Reuse what fits. Add complexity for a real requirement or concrete maintenance cost. Extract shared rules when copies are likely to drift. Examine wider consequences for infrastructure and system-wide choices. Preserve correctness. Run the narrowest check that could catch a meaningful failure, plus required checks. For visual evidence, use [Design’s full-surface capture standard](../design/references/tools/Screenshot.md). Use [Test](../test/SKILL.md) for a distinct verification gap and [Preflight](../preflight/SKILL.md) for setup blockers and fallback decisions.
3. When an attempt fails again for the same reason, change the approach or run a check that can distinguish the likely causes. Retry when new evidence or changed conditions justify it. If a prerequisite remains unavailable, report what would unblock that step and continue independent authorized work. Honor explicit stop conditions. Seek approval before reframing work that could break a widely used project's features or ecosystem. In creative work, surface consequential assumptions and alternatives and leave matters of taste open.
4. Announce the selected skills briefly with lowercase names in backticks, for example “I’ll use `execute` and `design` skills.” For routine authorized work, skip progress narration unless a material assumption or host requirement calls for an update. Raise material blockers promptly. Mention a recovered detour only if expectations change or the human needs to act.
5. Lead with the result and its verification. For a blocked check, name the exact check still needed and the behavior left unverified. Honor explicit completion gates. Distinguish completed work from plans and report material limits that affect the reader's next decision.
