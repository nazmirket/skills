---
name: code
description: "Use to answer a stack-specific coding question or support a change whose patterns, readability, testability or performance depend on the language, framework or database."
---

# Code

Code owns stack-specific advice. During implementation it advises the skill responsible for the change. For advice, explain what fits, why and how to check it. For an implementation, check affected behavior with the project's tools.

Read manifests, configuration and nearby code for the language, framework, runtime, versions and conventions. Open the most specific [stack guide](references/README.md) that could change the decision. Add another only for a distinct concern at a boundary the change crosses. Verify version-sensitive behavior against the installed stack.

Use [Engineering Practices](references/EngineeringPractices.md) for module boundaries, patterns, readability, testability or efficiency. Keep routine edits direct and compatible project patterns in place unless a concrete problem warrants a change. [Architect](../architect/SKILL.md) owns lasting system choices, [Debug](../debug/SKILL.md) unexplained failures and [Refactor](../refactor/SKILL.md) structural changes.
