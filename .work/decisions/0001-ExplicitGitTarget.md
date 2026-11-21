# 0001: Require an explicit Git target for guarded commits

**Status:** Accepted

Mirket checks the staged index before a supported agent-issued commit. Codex supplies a session directory to its hook, but a shell command may run in another directory. An index inspection based on the session directory can therefore give the wrong result. The [Codex hook contract](https://learn.chatgpt.com/docs/hooks#common-input-fields) does not promise the shell's effective directory.

To implement the authorized audit fix, Mirket requires the first literal `git -C` to specify an absolute directory for guarded commits in both hosts. Later literal `-C` values resolve from that target. The check probes the same target from a fixed starting directory. Supported explicit dry runs do not need this target or cleanup acknowledgment.

Using session state would keep commit commands shorter but can inspect the wrong index. Splitting the shared hook by host would preserve shorter commands where a reliable directory is available, at the cost of two contracts. A single explicit target adds one argument and works without inferring host identity. If a supported host later supplies a trustworthy execution directory, revisit the requirement with a cross-worktree regression.
