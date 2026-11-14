# Responsive design

Use when the same material must work across viewports or containers. Preserve meaning and action priority as space changes.

## Reflow around content

Decide what wraps, changes arrangement, stays visible or needs a local scroll region. Set transitions where the content no longer fits; preserve reading order, meaning and access to important actions. Use the actual context for navigation: a component embedded in a narrow panel may need a different layout even on a wide screen.

Inspect the narrow, wide and first awkward intermediate view, plus any important short viewport. Try long or translated labels, missing media, text enlargement and zoom. Check clipped popovers, sticky bars over focus or controls, offscreen actions, cropping and accidental horizontal scroll. Dense tables or canvases may need local scrolling; make the scroll area discoverable and keep surrounding controls usable. Preserve direction, order and reachability for right-to-left layouts when supported.

## Choose how the layout adapts

Start with fluid sizing and wrapping. Add a breakpoint where content or interaction actually breaks; use container size when the component can live in different layouts. Inspect visual order against reading and focus order after reflow. Keep one source of truth for behavior across sizes when possible.
