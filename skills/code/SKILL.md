---
name: code
description: "Use for language, framework, or database best practices when implementing, reviewing, or maintaining an identified stack."
---

# Code

Open the matching guide in the [stack index](references/README.md) when stack-specific guidance can affect a decision or prevent a defect. Confirm the project's versions, runtime, and local conventions from manifests, configuration, and nearby code first. Use an adjacent guide only for a boundary the task crosses, such as React's component model and Next.js's server boundary.

Keep compatible project patterns unless a concrete problem justifies changing them. Prefer the simplest supported construct. Treat style and architecture choices as tradeoffs; confirm version-sensitive claims in the guide's upstream sources. Do not introduce a dependency, migration, or broad rewrite to satisfy a preference.

Code supplies domain guidance to the work already underway. Use [Architect](../architect/SKILL.md) for system choices, [Debug](../debug/SKILL.md) for unexplained failures, [Refactor](../refactor/SKILL.md) for structural changes, and [Test](../test/SKILL.md) for verification. Check the affected behavior with the project's own tools.
