---
name: code
description: "Use for language, framework, runtime or database advice, CLI contracts, and engineering decisions about code structure, testability or performance."
---

# Code

Code owns stack and engineering advice. During implementation it advises the skill responsible for the change. For advice, explain what fits, why and how to check it. For an implementation, check affected behavior with the project's tools.

Choose the reference by the decision. For a [command-line contract](references/CommandLineInterfaces.md), start with the caller, commands, output and exit status. When the answer depends on a particular stack, identify the language, framework, runtime, versions and conventions from available project evidence and open the most specific [stack guide](references/README.md). Add another only for a distinct concern at a boundary the change crosses. Verify version-sensitive behavior against the installed stack.

Use [Engineering Practices](references/EngineeringPractices.md) for module boundaries, patterns, readability, testability or efficiency. Keep routine edits direct and compatible project patterns in place unless a concrete problem warrants a change. [Architect](../architect/SKILL.md) owns lasting system choices, [Debug](../debug/SKILL.md) unexplained failures and [Refactor](../refactor/SKILL.md) structural changes.
