# Equip: scope for revision 7

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Equip](../../../skills/equip/SKILL.md) focused on choosing tools and formats and challenging a poor fit. Debug owns incorrect behavior; Architect owns changes to shared abstractions. Use Equip in those cases only if a different tool or format is part of the decision.

- **Check before adding another workaround.** When a working tool is already causing recurring friction, first look for a supported extension or a simpler capability already in the project. Raise the issue when this check changes the recommended approach.
- **Prefer the established tool.** For a routine choice with no tool specified, follow the project's convention. Depart from it when doing so materially improves the result. When evaluating poor fit, check one credible outside option alongside the simpler path with the current stack. Stop exploring if the current stack meets the requirements.
- **Propose a pilot when the benefit is uncertain.** Show the measured cost of staying and why the alternative might help. Specify the sample, success threshold, and expected effort. Wait for approval unless testing alternatives is already authorized. Weigh the observed benefit against the full cost of switching before recommending a material change.
- **Protect hard requirements.** If the requested tool or format cannot produce the intended outcome, explain the limitation and recommend one that can. Wait for approval before substituting it. Continue preparation that works for either path.
- **Hand off after the choice.** Give [Preflight](../../../skills/preflight/SKILL.md) the chosen tool, target environment, and capabilities it must support. Preflight owns authorized setup and proves readiness with a representative run. The choice itself does not authorize setup.

Representative cases: check a supported UI kit extension before adding another brittle override; propose an import pilot when a replacement's gains are unproven; route an incorrect exact-ID match to Debug when no tool or format change is needed. Keep detailed examples in the reference and retain those that fit this boundary. Align routing and the Preflight handoff without opening Preflight's full revision.
