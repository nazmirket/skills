# Typeface design

Use for creating or revising a typeface that will be used as a font. Use [Typography](../concepts/Typography.md) for choosing and applying existing fonts, and [Logo Design](LogoDesign.md) for one-off lettering in a mark.

## Define the font to be delivered

Agree on the reading or display purpose, actual sizes, target environments, supported scripts and languages, and required characters and features. Make coverage explicit: include the punctuation, figures, marks, and locale-specific characters people will need. Distinguish a lettering sample, a functional single face, and a family. Define required styles and outputs; add a variable axis only if the intended use calls for it. Identify source and distribution rights and whether you are extending an existing family whose names, metrics or coverage must remain compatible.

## Draw, space, and build

1. **Set the system with real text.** Draw representative glyphs for each agreed script and appropriate test strings. Establish proportions, stroke logic, counters, vertical metrics and spacing rhythm at intended sizes before completing the glyph set. Choose constructs that belong to the script; a Latin control string cannot establish quality for another script.
2. **Expand and shape.** Extend the system to the required characters and marks. Set sidebearings before correcting exceptional pairs with kerning. Implement the necessary anchors, substitutions and positioning for the supported text; prove combinations and writing directions that depend on them. Proof a repeated sample word before and after changing a sidebearing, then check a single exceptional pair before applying kerning.
3. **Build the requested binaries.** Keep editable sources and a repeatable export configuration. Set family and style names, version, character mapping and relevant layout features. For variable fonts, check source compatibility and define axis ranges, defaults and named instances against the font’s compatible masters. Export the agreed desktop and/or web formats for the target consumers.

## Proof the exported font

| Check | Evidence |
| --- | --- |
| Coverage and shaping | Compare character coverage with the agreed set. Render representative words, numbers, punctuation and marks per script; check for silent fallback, incorrect joining or positioning, and clipping. |
| Appearance and metrics | Set real text at intended sizes. Check repeated spacing problems, difficult pairs, line height, and style selection in the target application or browser. For a revision, compare with the existing family under the same settings. |
| Variations and binary integrity | Try endpoints, default, named instances and revealing intermediate or combined settings. Check that exports build, load and show the expected names. Use the relevant checks from FontBakery or the project's validator as appropriate. A validator does not establish readability or shaping quality. |

Deliver the agreed font files, version and coverage notes, a specimen rendered from the binaries, and editable sources or build instructions when requested. Include the license or permitted-use notes and name untested scripts, apps or platforms. A specimen alone is evidence of appearance, not of a usable font.
