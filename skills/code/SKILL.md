---
name: code
description: "Use for engineering principles, code structure, testability and performance, and for advice on languages, frameworks, runtimes, databases and CLI contracts."
---

# Code

Code owns engineering advice. Apply [Engineering Practices](references/EngineeringPractices.md) to the affected code. The implementer checks the diff against the applicable principles, corrects in-scope violations and verifies the affected contract before delivery. For advice or read-only review, explain what the caller would observe and how to check it.

Choose the reference by the decision. For a [command-line contract](references/CommandLineInterfaces.md), start with the caller, commands, output and exit status. When the answer depends on a particular stack, identify the language, framework, runtime, versions and conventions from available project evidence and open the most specific [stack guide](references/README.md). Add another only for a distinct concern at a boundary the change crosses. Verify version-sensitive behavior against the installed stack.

[Architect](../architect/SKILL.md) owns lasting system choices, [Debug](../debug/SKILL.md) unexplained failures and [Refactor](../refactor/SKILL.md) behavior-preserving structural changes.
