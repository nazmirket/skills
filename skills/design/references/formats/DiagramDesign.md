# Diagram design

Use when the deliverable explains relationships, sequence, state, ownership, or quantities through a visual model. Establish what readers must infer, and what level of detail their decision requires. Use the responsible domain owner for the underlying facts; a diagram can clarify a system without establishing its architecture or policy.

## Model the relationship before drawing

Capture the entities and the meaning of connections, directions and boundaries. Mark observed, intended and unknown parts when they differ. Choose the organizing relationship first:

| Reader's question | Useful form |
| --- | --- |
| What happens next, or under which condition? | Flowchart or state diagram with conditions and outcomes |
| Who sends what to whom, and in what order? | Sequence or swimlane with meaningful handoffs |
| What contains, depends on, or connects to what? | Grouped topology, hierarchy, or dependency diagram |
| How much, how often, or how has it changed? | Chart with a stated measure, units, scale and data source |

Let position, shape, labels or line treatment encode stable meanings. Give connectors room, minimize unnecessary crossings and make direction explicit where it matters. Keep one reading path dominant; split an overview from detail when the notation, labels or decisions can no longer be read comfortably at the target size. Use [Composition](../concepts/Composition.md) for hierarchy and [Vector](../concepts/Vector.md) for editable geometry.

## Verify meaning and export

Walk a representative path from entry to outcome against the actual source. Check branch labels, edge endpoints, actor responsibilities, boundaries and any scale or quantities. Check the real export for clipped text and arrowheads, hidden or ambiguous connectors, and type at intended size. For example, crossing arrows in a service diagram must stay visually distinct from a junction where paths actually join.

Use labels or another visible cue alongside color when meaning depends on a distinction. Provide a short description and, for a complex diagram, a text account of the essential relationships or data as appropriate; see [W3C guidance on complex images](https://www.w3.org/WAI/tutorials/images/complex/). Deliver the requested rendering and editable source when needed. Identify deliberate omissions, unverified relationships and any rendering limitations.
