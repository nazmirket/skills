---
name: code
description: "Use for practical coding patterns, readability, testability, and performance in an identified language, framework, or database."
---

# Code

Read the project's manifests, configuration, and nearby code to identify the language, framework, runtime, versions, and conventions. Open the most specific guide in the [stack index](references/README.md) when it can change a decision. Open another stack guide only for a distinct concern at a boundary the change crosses.

For decisions about module boundaries, patterns, readability, testability, or efficiency, use [Engineering Practices](references/EngineeringPractices.md). Keep routine changes direct. Keep compatible project patterns unless a concrete problem justifies changing them, and verify version-sensitive behavior against the installed stack.

Code supplies guidance to the current task owner. Use [Architect](../architect/SKILL.md) for lasting system decisions, [Debug](../debug/SKILL.md) for unexplained failures, [Refactor](../refactor/SKILL.md) for distinct structural work, and [Test](../test/SKILL.md) when verification needs separate work. Check affected behavior with the project's own tools.
