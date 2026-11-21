# Agreement

The user explicitly authorized SSH as admin with this device's existing key and deploying the site to the domain they pointed at the server. Use the matching SSH alias with strict host-key checking. The written plan is a draft; execution is authorized. Production is committed HEAD 74e33b9. Public DNS points to the provided IPv4 address; there is no existing site configuration or matching TLS lineage. Follow mirket.dev's /opt/<domain>/releases/<commit> and atomic current symlink, the deploy account and Nginx sites-available/sites-enabled pattern, and the host's existing Certbot Nginx integration. No server-side Node runtime, Docker container, DNS edits, or changes to sibling sites.

## Independent audit

The reviewer found no blocker. Adopted atomic GNU rename for the release and current symlink, hostname-specific Certbot flags, preservation of the new release/certificate on first-deploy rollback, and verification of the actual Next.js navigation payload as well as ordinary HTML, assets, and sibling-site health.
