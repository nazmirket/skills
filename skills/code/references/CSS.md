# CSS

Read the site's cascade, tokens, layers, supported browsers, and ownership model before adding overrides. Use the existing system unless a concrete gap calls for a change.

- Inspect origin, importance and cascade layers before comparing selectors. Among otherwise tied rules, compare specificity, then scoping proximity, then order of appearance. For matching rules under nested `@scope` roots, the closer root wins a specificity tie even if the outer rule appears later. Check the computed value both inside and outside the inner scope. Normal unlayered author declarations take priority over normal layered author declarations. [Scoped cascade](https://developer.chrome.com/docs/css-ui/at-scope)
- Use grid for coordinated tracks and flex for arrangement along an axis when they fit the content. Build for min/max constraints, intrinsic sizes and wrapping instead of fixed widths or heights that fail with long text or zoom. Use logical properties where writing direction matters.
- Preserve visible focus, usable contrast, reduced-motion behavior and access to content without hover. Respect system settings where supported. Use container queries or other newer features when the support target or fallback permits them, not to force a change in architecture.
- Share intentional tokens or values with a common meaning; a one-off equality does not imply a new abstraction. Inspect computed styles and layout before adding specificity, another breakpoint or an animation.

## Diagnose layout and rendering cost

- Inspect the containing block, intrinsic sizes, overflow ancestors, and stacking contexts before overriding a width or z-index. A grid or flex item can refuse to shrink because of its automatic minimum; fix the sizing relationship where it originates.
- Keep reusable layout rules independent of page-specific selectors. Prefer named tokens where values have shared meaning and an intentional cascade layer where an override policy is part of the design. Avoid making a local fix depend on unrelated DOM depth or source order.
- If an interaction is slow, record it in the browser and identify style recalculation, layout, painting, or asset cost. Avoid interleaving synchronous layout reads with DOM writes in a hot loop. Check the actual target device before changing visual behavior for a presumed gain.

Exercise realistic short and long content, narrow and wide layouts, zoom and keyboard focus. Check the actual browser and fallback when a new feature is load-bearing.

Standards: [CSS Cascading and Inheritance](https://www.w3.org/TR/css-cascade-5/). Reference: [MDN cascade layers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers).
