# Design systems

Use for shared tokens, component rules, variants, themes and guidelines that need to survive reuse.

## Define rules in use

Keep one authoritative home for repeatable decisions. Name shared roles by the job they do, and point them at the existing values or tokens. Add a component-level override only when the exception is intentional, used and costly to express otherwise. A small site may need a handful of shared variables and native controls. Use the project's existing design system where it solves the same problem.

For a reusable component, describe its job, content, sizes or variants that actually occur, and how people operate it. Specify the relevant combinations of states: an invalid field still needs a visible focus indicator; a busy focused control needs feedback without losing its place; selection must remain recognizable on hover. Explain which rule takes priority where two treatments compete. Check the component in a realistic host, with different widths, themes and inputs, before updating all callers.

Document when a rule is global, when a product surface may vary it and which existing uses a change affects. Prefer a local repair over changing a global token to correct one outlier. Favor gradual adoption through representative cases over rebuilding every surface for symmetry.

## Apply themes and carry identity across media

A theme maps roles to an intentional set of treatments. Define foreground, surface, action, focus, feedback and data roles together. Test their applied combinations with real content and imagery in each supported theme, including selected, busy, invalid and disabled states. A beautiful palette sample can fail when used for small text, over an image or on an alternate layer.

Use the same recognizable ideas across media without freezing their geometry: an editorial voice, particular use of color and recurring image treatment can survive a compact product view, a slide and a poster. Let the medium determine density, scale, crop and interaction. Keep wording consistent where it refers to the same thing, and adapt tone to the moment.

Deliver only the guidance someone needs to repeat the result: intent, roles and locations, relevant component examples, exceptions, and editable assets when requested. Show at least one real application and state which themes, sizes or asset uses remain unverified.

## Validate the system in use

When tokens move between tools, follow one semantic alias through export and import. This DTCG example gives the focus ring a color type and a reference to the palette. [Design Tokens Community Group format](https://www.designtokens.org/tr/2025.10/format/)

```json
{
  "palette": {
    "ink": {"$type": "color", "$value": {"colorSpace": "srgb", "components": [0.12, 0.18, 0.34]}}
  },
  "focus": {
    "ring": {"$type": "color", "$value": "{palette.ink}"}
  }
}
```

Change the referenced color in one theme and inspect the focused control in each supported theme. Check the recipient's exported token still contains the alias and type when editability is part of the handoff. Flattening the alias to its current color loses that relationship.

Inspect representative real components and combinations, including dense content and conflicting states. Check tokens at the semantic role rather than copying one raw value everywhere. Document what is stable, which extension is allowed, and what is an exception.
