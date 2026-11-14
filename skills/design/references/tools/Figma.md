# Figma

Use when an authorized Figma file is the design source or an editable Figma file is the requested result. Use the available editor, viewer, or integration; confirm which operations and permissions it actually exposes.

1. Open the exact file, page and frame. Record a version or status when visible, and distinguish an approved target from an exploration. Inspect the relevant variants, annotations and prototype states. If [Dev Mode inspection](https://help.figma.com/hc/en-us/articles/22012921621015-Guide-to-inspecting) is available, use it to inspect component properties, layout, variable modes and export settings.
2. For implementation, map the design's roles and variants to existing components and tokens. Treat generated code as an inspection aid. A single frame cannot establish breakpoints or behavior it doesn't show; use the brief, other states, and the running product to resolve gaps.
3. Edit the agreed frame or a clearly named draft only when authorized. Preserve shared components and variables unless changing them is in scope. Export only the needed assets at their intended size or format, then open the actual output and check for clipping, substitution and unintended backgrounds.

Hand back the exact frame or version, selected states, assets, and any meaningful differences. If access is unavailable, use an authorized export or screenshot to assess what is visible and report which source properties, versions or interactions remain unknown. Product behavior needs its own runtime check.
