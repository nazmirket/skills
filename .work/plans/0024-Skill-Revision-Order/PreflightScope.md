# Preflight: scope for revision 8

**Status:** Approved and implemented. See [Progress](Progress.md) for verification.

Keep [Preflight](../../../skills/preflight/SKILL.md) as the owner of environment readiness and authorized setup. Equip chooses the tool and hands off the target environment and required capabilities.

- **Start when there is a reason.** Skip a routine precheck before ordinary work. Use Preflight when asked, when a tool fails to run, or when evidence points to a setup blocker. Inspect only the capabilities the task needs.
- **Block only what depends on the missing capability.** Continue authorized implementation and available checks when possible. Name the exact check that remains blocked and leave its result unverified.
- **Inspect before installing.** Verify the documented setup command and explain what it changes. Wait unless that setup is already authorized. If fresh environments routinely lack a tool required for normal checks, recommend fixing the shared setup and get approval before editing it.
- **Use equivalent fallbacks within existing authority.** Use another environment or method if it proves the same requirement, and say where and how it ran. Ask before using a weaker fallback or one whose equivalence is uncertain.
- **Follow the setup that runs the task.** If the README and actual container or CI disagree, use the configuration that governs the task. Flag misleading guidance. Ask when the conflict affects the work or an explicit requirement.
- **Separate readiness from execution evidence.** A local run using CI's pinned image, dependencies, and test command can establish readiness for the task. State that the test itself has not run in CI. After setup, check that the tool can do the basic job it was installed for; leave acceptance checks to the workflow verifying the change.

Representative case: a fresh dev container cannot launch the browser needed to verify a keyboard-focus fix. Continue the fix and available checks. A host browser can provide the keyboard evidence if it serves the same build and the container browser is not part of the requirement. Otherwise leave the exact keyboard check blocked. If the browser is required for normal project checks, propose adding the pinned browser to shared container setup. Once authorized setup is done, verify that the browser launches and opens the app; the verification owner tests the changed focus behavior.
