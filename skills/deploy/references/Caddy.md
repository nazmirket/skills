# Caddy

Identify the running binary and modules, config adapter, config source, admin endpoint, and who owns persistent certificate state. An API-managed config and a file-managed config should not silently overwrite each other.

- Adapt and validate the intended config using the deployed binary and modules; use the installed service manager or supported reload path. Treat the admin API as privileged access. Keep certificate storage available as required by the deployment; verify challenge reachability through the actual DNS, proxy and load-balancer path. Don't repeatedly request production certificates merely to test a routing change.
- Select routes and upstreams explicitly. Trusted forwarding headers should come only from configured trusted proxies; confirm real source IPs and headers across the deployed chain. Choose active or passive health checks for the upstream behavior and validate streaming, client cancellation or WebSocket use when affected.
- Measure proxy time, upstream latency, compression cost and connection churn before adding buffering, compression, or load distribution rules. Compare on realistic payloads and a request that crosses the external proxy as well as a local test.

Verify the active route, TLS certificate and redirects, plus upstream success and failure through the hostname users reach. Keep previous validated config and check observable behavior after restoring it. Retaining config does not by itself back up keys or certificate storage.
