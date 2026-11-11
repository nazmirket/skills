# 0003: Use Codex compatibility packaging for hook discovery

**Status:** Accepted — November 11, 2026

The user authorized installing Mirket 0.4.0 with active lifecycle hooks. A fresh Codex CLI 0.167.0 session showed the installed, enabled plugin and all 25 skills, but no Mirket hooks or trust-review prompt. Read-only app-server inspection confirmed an empty plugin hook list without parsing errors.

Controlled local comparisons used the same skill and hook configuration across manifest layouts. A portable root `plugin.json` suppressed discovery with explicit or default hook paths, including when a `.codex-plugin/plugin.json` fallback was present. Compatibility-only packages exposed the hook. Repeating the comparison with the full Mirket package exposed all 25 skills and all four hooks. These observations establish discovery, not hook execution.

Use `.codex-plugin/plugin.json` for Codex and retain `.claude-plugin/plugin.json` for Claude Code. Synchronize identity, version and description, and keep the 25 skills, hook scripts and assets shared at the package root. The Codex manifest explicitly references `./skills/` and `./hooks/hooks.json`. Omit root `plugin.json` so it cannot shadow the working compatibility manifest.

The [official packaging documentation](https://developers.openai.com/plugins/build/plugins) supports compatibility packages and also describes portable hook configuration. The observed 0.167.0 behavior disagrees with the latter. Adding another manifest while keeping the portable root did not solve it; bypassing trust cannot repair missing discovery. This decision favors the verified supported layout over portable-manifest distribution for now.

Install through the host's supported marketplace workflow, review hooks normally, and verify discovery and execution separately. Do not patch installed caches or bypass hook trust. Reconsider the portable layout after a supported host version passes an actual comparison of skill discovery, all four hook events, and their execution. Keep both host manifests and their checks aligned when changing the layout again.
