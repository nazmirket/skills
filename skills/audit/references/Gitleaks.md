# Gitleaks

Pin the scan surface: staged or changed files, a directory, or reviewed Git history. Choose the smallest scope that answers the question. Use the installed scanner’s supported mode and check the project rules and baseline.

- A finding is a pattern or entropy match. Establish whether it resembles a fixture, placeholder, or credential using its context and classification. Do not test a suspected credential against a live service. Do not paste it in review comments, prompts, tickets, or logs.
- Enable the installed version’s redaction for scan output and verify reports are also redacted before sharing. Record the file or commit, rule or credential type, and exposure scope without retaining the full value. A baseline can hide known results; state which prior findings or paths it excludes.
- For history, distinguish when the value appeared, whether the commit remains reachable, and whether the scan had enough history. A shallow checkout or working-tree scan cannot answer a history question. Deleting the current line does not revoke a credential or remove copies already distributed.

Hand off suspected disclosure through the approved incident or credential owner path. Revocation, rotation, and rewriting shared history are separate actions. Verify any authorized cleanup by rechecking the same scope without re-exposing the value.
