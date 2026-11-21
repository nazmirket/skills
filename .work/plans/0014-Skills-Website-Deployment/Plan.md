# Plan — draft, execution authorized

1. Verify clean committed static export with npm ci and npm run build, then upload only the export into a private incoming release under /opt/skills.mirket.dev/releases. Check contents and use atomic rename and current symlink switch.
2. Add one static virtual host from the prepared configuration under sites-available and enable it. Test Nginx configuration before reload. Verify correct HTTP response, then issue a dedicated certificate using Certbot's Nginx installer with HTTPS redirect.
3. Check HTTP redirect, HTTPS certificate validation, selected pages, a fingerprinted asset, a missing URL, and the adjacent mirket.dev virtual host. Check Certbot renewal wiring. Record the exact deploy/update/rollback procedure in .work/routines/DeploySkillsWebsite.md; preserve original release/config if a step fails.

## Result

A clean Git archive at 74e33b9 built all 25 Next.js pages. The archive and configuration matched their SHA-256 checksums after SSH transfer. Published the deploy-owned release and enabled the new Nginx vhost, then obtained its own Let's Encrypt certificate with Certbot. Nginx configuration passed validation; the adjacent vhost configurations were byte-for-byte unchanged. Public verified HTTPS returned byte-matched HTML, CSS, navigation payload and error page; HTTP redirected to the same HTTPS path. Playwright confirmed host switching and documentation navigation on mobile without page errors. The untracked runbook is .work/routines/DeploySkillsWebsite.md.

The hostname-specific Certbot renewal dry run passed. Rechecked Nginx syntax and compared all neighboring configuration hashes after the dry run. Removed the deployment staging files on both machines. The guide is ignored, no .work paths are tracked, and the repository remains clean.
