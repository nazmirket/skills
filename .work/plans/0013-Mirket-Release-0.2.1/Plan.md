# Mirket 0.2.1 release — draft; execution authorized

## Outcome

Ship the pending website and documentation changes and synchronized patch version on origin/main. Verify a clean Codex reinstall and a fresh Claude Code install from the pushed Git marketplace. Preserve Hindsight wiring, banks, unrelated plugin preferences, and private .work records.

## Agreement

The user explicitly asked to commit and push everything, bump the version, and install the latest plugin on this device. 0.2.1 is a patch after 0.2.0 because the pending work is site and setup guidance, with no plugin API change. Prior versions were released by manifest bump on main; no separate tag or deployment is implied.

## Plan

Review the complete pending diff, synchronize both manifests and correct any material setup guidance left by the preceding repair. Run repository tests, build and check the static site, validate the plugin and marketplace, and inspect the staged file list before committing and pushing. Confirm origin/main matches the commit. Refresh the Git marketplaces, reinstall Mirket on Codex and install it on Claude Code; check installed versions and files and keep Hindsight intact.

## Independent review

No release blocker. Adopted the reviewer's guard against staging the pinned Hindsight runtime from npx, and the check of the pushed Codex marketplace snapshot before removing the old install. Claude's validation gives existing listing advisories and succeeds. The release does not include a host login or a signed-in Claude turn.

## Checks before release

23 hook and 30 memory tests passed. Next.js built a static export. Playwright verified desktop and mobile installer tab height, Claude opt-in prompt and manual commands, reduced-motion diagrams, local memory docs anchors and adjacent skill navigation. Both Claude validators and Git whitespace/index checks passed.

## Result

Pushed 74e33b9 to origin/main and verified the remote head. Removed the old Mirket Codex install with the host CLI and installed 0.2.1 from the refreshed marketplace. Added the same Git marketplace and installed Mirket 0.2.1 in Claude Code. Both report enabled and contain the exact 65 committed package files with no older cache version. Hindsight configuration and hook hashes did not change; Codex doctor and the Claude MCP connection passed. The temporary static preview server was stopped and the Git worktree is clean.
