# Nginx

Identify the effective config, includes, active master, downstream TLS and upstream protocol. Static files, reverse proxying, and streaming do not need the same settings. Check the packaged version before using directives from newer docs.

- Validate with `nginx -t` using the runtime's config path and service context before reload. Scope edits to the affected virtual host. For proxy changes, verify host and forwarded headers, path rewriting with and without a trailing slash, client-IP trust, and WebSocket or streaming behavior where applicable.
- Choose buffering, request body limits, and timeouts based on the real traffic path. Disabling buffering may help streaming but can keep upstream connections open longer; raising every timeout can hide saturation. Keep cache keys and cacheability rules aligned with authentication, variants, and freshness. Do not reuse a personalized response as a public cache entry.
- Compare request and upstream timing, status distribution, connection reuse, disk writes, and resource pressure. Use warm and cold paths and a realistic payload. Tune the hop that is actually slow; do not equate a large worker limit with higher throughput.

Reload through the established service process and check its logs; acceptance of a reload signal does not prove the new config became active. Verify TLS and the actual request, including adjacent hosts or paths affected by shared includes. Keep prior config and restore via validation and reload if needed.

Upstream: [Controlling nginx](https://nginx.org/en/docs/control.html), [Proxy module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html), [Request processing](https://nginx.org/en/docs/http/request_processing.html).
