# Motion and gestures

Use to design, tune or remove motion, coordinate several moving elements, or specify direct manipulation. Start with the action or story the movement serves. Time and movement are design materials, not requirements.

## Decide what should move

Start from a before and after state. Name what motion would help a person notice: immediate feedback, origin and destination, change in relationship, a process, or an expressive beat the work calls for. Rank opportunities by the confusion or friction they would resolve. Leave movement out when placement, a visible state or clear language already does the job. Repeat a proposed transition several times; a useful first-run moment can slow a frequent task.

| Intent | Useful starting treatment | Avoid |
| --- | --- | --- |
| Acknowledge input | Immediate state change, optionally with a short emphasis | Waiting for a flourish before the action registers |
| Connect two states | Carry one recognizable element, edge or origin through the change | Moving unrelated regions together or inventing a false spatial relationship |
| Guide attention | Change emphasis or sequence the few elements that need an order | Introducing each item one by one when they can be read together |
| Explain or express | Use a storyboard with a clear opening, development, pause and ending | Animation that obscures the idea, text or controls |

Record just enough to build or evaluate it: trigger; logical change; initial, interrupted and final appearances; timing and easing; whether actions remain available; reduced-motion treatment. Reuse a product's motion conventions when they express the same behavior.

## Set timing and choreography

- Start when the input is received. As a starting point for everyday UI, try roughly a tenth of a second for a small cue and a few tenths for an ordinary transition. Adjust for distance, perceived weight, repetition and readability. A longer explanatory sequence has a different job. These are tuning suggestions, not acceptance thresholds.
- Easing describes how speed changes. A quick response that settles gently often works for arrival; continuous progress should reflect the underlying process. A spring can carry momentum after release or interruption when that helps; excess bounce or settling time can make a direct control feel imprecise.
- Use a shared origin or coordinated progress when elements describe one change. Overlap related motion, stagger only when reading order or causality benefits, and cap the total delay across a group. Make the usable state available as soon as its logical state allows it. Let navigation direction follow the actual hierarchy and locale.
- For stand-alone animation, storyboard the key poses or frames and give viewers time to absorb important information. Preview at actual duration and frame size. Plan for a legible still or poster frame, meaningful loop boundary or ending, and captions or a textual alternative where the content calls for them.

## Preserve state during interruption

Treat an animation as a view of state. Commit the action, expose semantic state and manage focus independently of a successful animation event. Design cancel, reverse and retarget paths from the current appearance. Cancel outdated work so a late callback cannot hide a reopened panel or overwrite a more recent state. Keep exiting content out of interaction and focus when it is logically closed, even if it remains visible for a short exit.

Honor the user's motion preference. Reduce or remove travel, scaling, parallax, repeated motion and decorative sequencing where they are not essential. Replace them with immediate updates or quieter cues when helpful. Preserve the same outcome, status information and control. Provide pause, stop or equivalent controls for persistent movement where required; avoid flashing or reading interference. Verify both preference paths and a preference change during use where relevant.

## Track the gesture; settle on release

1. **Start deliberately.** Pick an appropriate handle or affordance, identify the active pointer, and decide which direction or threshold claims the gesture. Preserve ordinary taps, scrolling and zoom until the gesture actually owns the input.
2. **Follow input.** While held, let the visual response track the pointer directly, with intentional boundaries or resistance. Derive related layers from the same progress. Avoid easing that makes a handle lag behind the person.
3. **Resolve once.** On release, decide commit or return using clear thresholds; direction and recent velocity can help when they reflect intent. Settle from the current position. Specify lost capture, pointer cancellation, extra touches and interruption of settling; a canceled gesture must not commit inadvertently.
4. **Offer another path.** Pair meaningful drag or swipe actions with visible tap or click controls and a keyboard path. A reorder handle can coexist with Move up and Move down actions. Preserve resulting feedback and focus for each input.

Example: An item can be moved by dragging or by pressing a move action. Show its destination before a drop; announce or visibly confirm its new position after commit. When canceled, keep the original order. A settling animation can clarify placement, but removing it must leave ordering and feedback intact.

## Measure and remove safely

Prefer explicit animated properties and a small moving region. Transforms and opacity often avoid layout work, but do not promise smoothness. Transforming scale does not change surrounding layout; opacity alone does not remove an element from focus. Use actual layout transitions when necessary and measure their cost. Inspect expensive painting, large blurred layers, repeated layout reads and writes, and whole-view work on every input event before choosing a new tool. Reuse built-in or established primitives; a library change needs a real capability gap.

If removing movement, look for initial hidden styles, queued timers and completion handlers, deferred removal, focus changes and assumptions in tests. Keep useful status cues and confirm content is visible and usable without the transition. Remove helpers and dependencies only when no remaining path needs them.

Give [Critique](../../critique/SKILL.md) the preview in normal use and the cases that could expose confusing movement. Reproduce rapid activation, interruption, cancel, repeated use and reduced motion as applicable. Use slow playback to investigate a sequence, normal playback to judge it, and representative hardware and content to check comfort and performance. [Test](../../test/SKILL.md) owns repeatable behavior and measurements; use [Debug](../../debug/SKILL.md) when there is a concrete stutter or gesture failure. Report the devices and paths that were actually exercised.
