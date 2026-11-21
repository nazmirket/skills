# Spline

Use when a Spline scene is the source or the requested result is a Spline viewer or embed. Confirm the project and scene, available access, and whether the task calls for an editable scene, a preview, or a published result. A request to inspect or edit does not authorize publishing or changing link visibility.

1. Inspect the intended scene and starting camera or state. Read the relevant objects, events, state transitions and inputs. Observe the scene in play or preview mode; editor appearance alone cannot establish an interaction.
2. If authorized to edit, work in the agreed scene or a duplicate. Exercise affected triggers, repeated actions and reset behavior. Keep unrelated objects and settings intact. For a web scene, test pointer events, focus and scrolling inside the actual viewer embed.
3. Check the actual intended container where available. Test sizing, loading, pointer or touch behavior, and relevant scroll or event scope. If the embed depends on device resources, verify on a representative device and exercise the agreed fallback when it matters. For a slow scene, isolate geometry, textures and animation in turn, then measure the same interaction on the target device.

Return the scene or approved preview, target container and states exercised. Use [Browser](Browser.md) to inspect an existing authorized embed when the editor is unavailable; leave editability, unpublished states and untested devices unverified. A supplied image shows appearance only.
