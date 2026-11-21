# Apache HTTP Server

Identify the active instance and configuration, enabled modules, Multi-Processing Module (MPM), virtual hosts and app handler. Use the distribution's service tooling and confirm the installed Apache major.

- Use the active instance's config test and virtual-host listing (commonly `apachectl configtest` and `apachectl -S`) before a graceful reload. Inspect base config and includes together. Preserve TLS, rewrites, access rules, and any deliberate delegated `.htaccess` overrides. Verify the externally served host rather than only the default vhost.
- Set worker limits using measured memory, connection behavior and downstream capacity. Separate slow app handlers, slow clients, backend connection pools and disk costs. Consider a different MPM only if the loaded modules and app runtime support it; changing it alters the process and connection model.
- Avoid enabling per-directory overrides, heavyweight logging, broad rewrites or compression merely from a checklist. Measure which phase costs time. If a proxy or FastCGI service is involved, check queues, timeouts and error behavior there as well.

Confirm the prior config is recoverable and note whether an operation can interrupt long requests. After reload check the logs, rendered virtual host response, app path, TLS, and representative concurrent traffic when tuning capacity. Verify neighboring vhosts when shared configuration changed.
