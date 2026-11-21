# SSH

Identify the actual destination, account, host-key source, authentication and network path. Use approved access. Treat changes to SSH itself as a separate rollout with a tested recovery route.

- Inspect resolved client configuration with `ssh -G` for the intended alias. Use noninteractive automation with known host keys and a specific identity; fail closed when the identity or key changes unexpectedly. Verify a rotated host key through an independent trusted channel. Prefer a dedicated deploy identity with narrowly scoped server permissions. Avoid agent forwarding unless explicitly needed and approved.
- Use the established artifact transfer and privilege boundary. Verify the checksum on the remote side before activation, keep staging separate from live files, and use a versioned switch on the same filesystem when the established layout supports it. Never retry a disconnected mutation until remote state establishes what happened.
- Compare connection/authentication time, upload throughput, and remote execution separately. Reuse connections for repeated small operations only when identity, permission and socket ownership stay scoped. Prefer a bounded transfer and safe checksum retry to repeatedly copying finished artifacts.

For a server config change, validate with the target's `sshd -t` and keep a known working session or recovery console. Prove a second authorized connection and the intended command scope before relinquishing the first. For application deploys, verify the served path over its normal client interface too.
