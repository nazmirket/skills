# Screenshot capture

For page critiques, layout changes or whole-artifact conclusions, capture the full surface using the procedure below. For a component-only question, capture the complete component and enough surrounding context at native resolution to see the specific condition (for example, keyboard focus and any clipping at a panel edge). Inspect the original at actual pixels and identify the build, viewport, state and bounds reviewed. If the effect can extend beyond those bounds, expand the capture before drawing a wider conclusion.

For responsive work include the desktop and narrow layouts in scope. Match baseline and revision conditions for comparisons. Reuse originals when build, coverage, state and capture settings match.

## Capture the full surface

1. Pin the build, route or artifact, CSS viewport or artboard size, content, UI state, theme and zoom. Use authorized test data throughout the surface, including below the fold. Keep saved evidence free of private overlays, credentials and unrelated windows.
2. On the web, keep the intended **layout width and viewport height** and render at **device pixel ratio 2 or greater**, with browser zoom at 100% unless zoom itself is under review. Use a lossless PNG at device scale. A 390 CSS-pixel layout at 2× has 780 physical pixels across when there is no horizontal overflow. Enlarging the viewport selects a different breakpoint. Upscaling a saved bitmap adds no detail.
3. Prepare the actual state. Let fonts settle. Traverse a long document to bring lazy images, charts and deferred sections into view. Wait for meaningful content or the intended error state, including the last item. Restore the intended scroll/state and recheck readiness. Note sticky elements, overlays, virtual lists and independently scrolling panels.
4. Record the document's full width and height in CSS pixels at capture time, including overflow. Capture **from the first pixel to the last** using native full-page mode. For a nested scrolling surface, also capture its complete scoped contents. A full document shot records only the visible part of that panel. For a fixed header, keyboard focus, dialog or a sticky failure, include the exact viewport state as a companion to the full capture.
5. For a slide, canvas, printable page, design frame or artwork, export the entire frame or sheet from its native renderer. Keep a vector or print master where applicable and render a legible lossless inspection image at 2× the intended logical viewing size or higher. For a native app, capture the whole screen at its native high density and cover the full scrollable content. For motion, retain full frames at key states and exercise actual playback. For supplied raster-only material, preserve and inspect its complete native original. Record a resolution or coverage gap when it lacks the detail needed for the verdict.

## Verify the file

Read the saved image dimensions. For a browser capture they must equal measured document width and height times the **actual** capture DPR, allowing integer rounding for fractional densities. For example, a 1,280 × 2,400 CSS-pixel document at 2× yields 2,560 × 4,800 px. A 2,560 × 1,600 viewport shot misses content even though its width is correct.

With Node available, the bundled [PNG geometry checker](../../scripts/full-page.mjs) takes the original file and *independently observed* CSS width, CSS height and DPR. Resolve the script relative to the installed Design folder. An equivalent native image inspector can perform the same check.

```sh
node "$DESIGN_DIR/scripts/full-page.mjs" review.png 1280 2400 2
```

Open the saved original. Inspect the whole composition at fit, then read the top, middle, bottom and every cited defect at actual pixels. Verify expected content, last row/footer, assets, overlays and legibility. Matching dimensions alone cannot detect blank regions, duplicated content or a stitched image with missing rows.

**Large or constrained surfaces.** When the native renderer truncates the image, use a capable renderer or capture ordered, overlapping lossless tiles at the same density and layout width. Record actual scroll offsets, stitch at device-pixel coordinates, reconcile overlap and repeated sticky elements, and inspect the full stitched original. For a virtual list, verify item continuity against the finite fixture. For an infinite feed, define the last item or finite state being assessed. Keep the outer-page context. If a tool only offers thumbnails, the reconstruction is unreliable, or content is inaccessible, return supported observations and mark the visual check incomplete.

Give the reviewer the full original path, target/build, state, browser or renderer, viewport, measured surface, output dimensions and density. Link useful detail crops alongside the original. Save comparison images under distinct names. Preserve review evidence through handoff. See [Browser](Browser.md) for direct inspection and [Playwright](Playwright.md) for repeatable capture.
