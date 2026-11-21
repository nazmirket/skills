# Chrome DevTools

Confirm the affected route, browser version, expected action, deployed build, and any extensions, service worker, or cache state. Use the panel that answers the current question.

- **Network:** Reproduce one action and follow the relevant request's initiator, redirects, timing and response. Separate connection setup, waiting for headers, transfer, and client processing. A successful HTTP status can still contain the wrong data. Compare warm and cold loads only if cache behavior is in question; disabling cache with DevTools open changes the experiment.
- **Performance:** Record a short window around the action and select the expensive interval. Separate input delay, JavaScript, style and layout, paint, and network waits. Follow the call tree to the code doing work; use bottom-up cost to find repeated hot functions. Compare the same interaction on the same build mode, viewport, and CPU/network settings.
- **Sources or Memory:** Confirm source maps match the running assets before trusting line numbers. Use a focused breakpoint for a control-flow question, not for timing. For suspected retention, compare heap snapshots after repeating and then undoing the same action; inspect what retains objects instead of interpreting any heap growth as a leak.

For a fix, repeat the original action on the intended runtime and one adjacent path. Report the observed request, event, or timing and its conditions. Remove credentials, query data, response bodies or user details before sharing a HAR, screenshot or trace.
