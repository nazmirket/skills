# CSS

Read the site's cascade, tokens, layers, supported browsers, and ownership model before adding overrides. Use the existing system unless a concrete gap calls for a change.

- Resolve cascade problems at their source: origin, importance, layer, then selector specificity and order. Keep selectors scoped and predictable. Check interaction with unlayered styles before layering one component; normally declared unlayered author rules have higher priority than normally declared layered rules.
- Use grid for coordinated tracks and flex for arrangement along an axis when they fit the content. Build for min/max constraints, intrinsic sizes and wrapping instead of fixed widths or heights that fail with long text or zoom. Use logical properties where writing direction matters.
- Preserve visible focus, usable contrast, reduced-motion behavior and access to content without hover. Respect system settings where supported. Use container queries or other newer features when the support target or fallback permits them, not to force a change in architecture.
- Share intentional tokens or values with a common meaning; a one-off equality does not imply a new abstraction. Inspect computed styles and layout before adding specificity, another breakpoint or an animation.

Exercise realistic short and long content, narrow and wide layouts, zoom and keyboard focus. Check the actual browser and fallback when a new feature is load-bearing.

Standards: [CSS Cascading and Inheritance](https://www.w3.org/TR/css-cascade-5/). Reference: [MDN cascade layers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers).
