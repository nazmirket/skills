# Plan — draft; execution authorized

1. Compare the current skill and packaged hooks with the requested behavior and current host event contracts.
2. Rewrite the skill around action, evidence, and a short result. Register compact SessionStart and UserPromptSubmit context. Make final Distill and Clean use the same guarded Stop response.
3. Verify the JSON event contracts, no second Stop continuation, and package/website integrity; report actual checks without claiming measured model token savings.

## Result

Rewrote Distill to act first, minimize narration and tool-output repetition, and report results with evidence and material limits. Added SessionStart guidance and a short per-prompt reminder that does not require rereading the skill. The first guarded Stop response now requests Distill and relevant Clean together, with no additional hook or continuation. The PreToolUse path and pending Equip changes were preserved.

All 56 repository tests passed, including synthetic event envelopes, invalid input, and single-Stop checks. Claude package validation passed with existing listing advisories. The website build and discovery check passed. No fresh authenticated host run, measured model token savings, installation, commit, or publication.
