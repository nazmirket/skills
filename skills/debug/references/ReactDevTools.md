# React Developer Tools

Identify the React version, intended renderer, root, dev/production mode, and whether an SSR or hydration boundary is involved. Pick Components for ownership and state, Profiler for React work, and the browser profiler for whole-interaction cost.

- Trace the affected component through props, state, hooks and providers. Check which ancestor owns the value and which update initiated the render. Inspect keys and identity when rows reorder or state resets. DevTools edits can test a hypothesis about the view, but repeat the real interaction to establish causality.
- Record a short repeatable interaction in the Profiler. Compare commits, costly subtrees, and update causes where that profiling mode exposes them. Separate React render work from network, layout, paint and other main-thread work. Development Strict Mode can deliberately add renders or effect checks; confirm behavior with the appropriate build.
- Tune the measured source first: narrow ownership, avoid duplicated derived state, or reduce work in expensive subtrees. Avoid adding memoization solely because a component renders. If using a profiling-enabled build, account for instrumentation overhead and validate on the intended production mode too.
- For an SSR mismatch, check server output and initial client input before interpreting the later component tree. Source maps and the deployed build must match.

Repeat the same interaction after a change and check the affected state and inputs. Record the profiler's build, mode and sample. When component timing leaves a gap, trace the interaction on the affected runtime. For a Chromium browser use [Chrome DevTools](ChromeDevTools.md).
