# Typography

Use to give text a reading order, a voice and readable form at its actual size. Use [Typeface Design](../formats/TypefaceDesign.md) if the task is to produce a font.

## Assign type roles

Assign roles to display type, headings, body, labels and data. Make adjacent roles distinguishable by a few deliberate changes in weight, size, spacing or position. Give long text a comfortable measure and line height; keep dense labels readable. Test real scripts, weights, fallback fonts, long labels and text enlargement. Use tabular numerals when aligned values help comparison. Check the type at actual viewing size; a zoomed canvas hides reading problems.

Use an established face when it carries the identity. Introduce a display face only if its letterforms do work the brief needs, such as distinguishing the title of a publication from dense catalog entries. Check permitted use, available weights and glyph coverage before committing to it.

## Check real text

For mixed scripts, inspect both glyph shaping and [directional isolation](Responsive.md#check-mixed-direction-content). Use the actual fallback fonts at the intended size.

Compare an ordinary sample, long text, and a dense or localized case at the target size. Watch widows, clipping, baseline drift, awkward wrapping and silent changes in fallback. Fix hierarchy using roles, measure and spacing before adding another typeface.

For a short headline on the web, try `text-wrap: balance` against ordinary wrapping at the first awkward width. Keep the natural wrap when it reads better or the feature is unavailable. Avoid hard-coded line breaks that split translated text. In a data row, check whether units, signs and decimals still belong to the correct value.

Inspect the same heading and nearby action during a cold font load and with the custom font blocked. If wrapping moves the action or clips a label, select a closer local fallback. When the stack supports font metric overrides, fit its size and line metrics to the actual face. Check the rendered fallback and loaded state with zoom and real text.
