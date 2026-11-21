# Glassmorphism

Use translucent layering when the relationship between foreground and background matters, such as a transient panel above an active canvas.

## Build the visual language

Use a small number of translucent surfaces. Tune opacity, blur, border and shadow together so the layer reads over representative backgrounds. Make critical information rest on a stable surface.

## Avoid the cliché

Avoid stacking multiple blurred layers, losing focus indication, or making texture the only cue that an overlay is active. Provide a legible opaque fallback for incompatible or demanding settings.

## Check it in use

Check busy, light and dark backgrounds and focus states in the real viewport. Measure if large moving blur regions introduce visible slowdown.

Try an inspection panel above a pale map, a dark photograph and a busy plotted route. Compare the translucent panel with its opaque fallback in each state. Check the label, focus indicator and selected row when the background changes beneath them.
