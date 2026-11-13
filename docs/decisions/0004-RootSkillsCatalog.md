# 0004: Use a root skills catalog

**Status:** Accepted

The skill definitions belong in the repository root so different hosts can use the same catalog. Keep the canonical definitions in `skills/<name>/SKILL.md`, with skill-specific resources beside them and shared guidance in `references/`.

Use the repository root as the plugin package for both marketplaces. Codex declares `./skills/` in its compatibility manifest; Claude Code discovers the same directory by default. The existing hook layout and the `mirket@mirket` install ID remain in place. Future targets can package the root catalog without changing its location.

Keeping a nested package would require copying the catalog into it or relying on a link outside its package root. In an isolated Codex CLI 0.167.0 install, a nested package with symlinked skills and references lost both links when copied to the cache. Isolated installs of the root layout exposed all 25 skills and four hooks in Codex CLI 0.167.0 and Claude Code 2.1.323.

For local install checks, use a clean checkout or export. A local root install can copy ignored files along with the plugin. If future targets need smaller packages, assemble those packages from the root catalog at release time.
