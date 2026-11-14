# Gestures

Use for direct manipulation such as dragging, swiping and reordering. Define the underlying action, its alternate controls, and the interruption and cancellation rules before choosing animation.

## Track input and settle on release

1. **Start deliberately.** Pick an appropriate handle or affordance, identify the active pointer, and decide which direction or threshold claims the gesture. Preserve ordinary taps, scrolling and zoom until the gesture actually owns the input.
2. **Follow input.** While held, let the visual response track the pointer directly, with intentional boundaries or resistance. Derive related layers from the same progress. Avoid easing that makes a handle lag behind the person.
3. **Resolve once.** On release, decide commit or return using clear thresholds; direction and recent velocity can help when they reflect intent. Settle from the current position. Specify lost capture, pointer cancellation, extra touches and interruption of settling; a canceled gesture must not commit inadvertently.
4. **Offer another path.** Pair meaningful drag or swipe actions with visible tap or click controls and a keyboard path. A reorder handle can coexist with Move up and Move down actions. Preserve resulting feedback and focus for each input.

Example: An item can be moved by dragging or by pressing a move action. Show its destination before a drop; announce or visibly confirm its new position after commit. When canceled, keep the original order. A settling animation can clarify placement, but removing it must leave ordering and feedback intact.

## Check touch, pointer and keyboard

Check intent thresholds, scroll coexistence, interruption, cancellation, focus and feedback. Exercise both the direct gesture and the visible alternative. When settling motion is used, read [Motion](Motion.md) for timing and interruption.
