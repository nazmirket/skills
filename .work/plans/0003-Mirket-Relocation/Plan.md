# Move and install native Mirket

The user authorized replacing the old Projects checkout with the Desktop checkout and installing the new plugin.

1. Verify both Git roots, uncommitted and ignored files, active symlinks, global instructions, marketplace source, and Hindsight mappings.
2. Save a verified Git bundle of the retired checkout under ignored `.work/recover`, the existing global instructions, and the old Hindsight path mappings. The ignored legacy plan selection pointer is obsolete; the tracked plans are in the bundle. Stage the old checkout under ignored `.work/stashes`. Replace only the dangling global skills symlink with a real directory containing the separately installed Hindsight skill, verified byte for byte. Remove the staged checkout after verification.
3. Move the Desktop checkout and its private workspace into Projects. Register that path with `codex plugin marketplace add .` and install `mirket@mirket-native-marketplace` with `codex plugin add`. The old marketplace has no installed plugin and is separate from the new one. Do not install an absent host or bypass hook trust. Replace the old Mirket-only global prompt with the shipped native prompt. Move the Desktop bank's exact mapping to the new path in the registry and seed map, leaving both banks intact; preserve the rest of the Hindsight settings.
4. Verify Git identity, workspace, plug-in inventory, standalone Hindsight skill and fresh Hindsight mapping. Remove the retired checkout once verified; confirm the old Desktop path is gone.

## Current status

Completed. The native checkout is now `~/Projects/skills` at `5f9d738`, with a clean Git working tree. Codex lists `mirket@mirket-native-marketplace` 0.1.0 as installed and enabled from that path, and its cached package matches the checkout. Installed the native global Codex instructions. The retired tree and Desktop path are gone; the old reachable Git history and three prior configuration files are in the ignored recovery directory. The Hindsight skill was preserved byte for byte and a fresh MCP process resolved the new path to the native checkout's former bank. No banks were deleted, and no hook trust or live skill behavior was tested.
