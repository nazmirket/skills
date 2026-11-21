# Production website deployment — Mirket 0.4.0

Deployed committed `cf41945c46bde6fd581b25379733143794f02762` to **https://skills.mirket.dev/** on November11,2026 (Europe/Istanbul).

Built a clean full Git archive with `npm ci`, `npm run build` and `npm run seo:check`. The static export passed28-page/28-social-image checks. SHA-256 of the transferred archive: `4d96f9ec50cdc42b032e49904443a248441f6cf5659b4b7192e6ad8bb640596f`. The server verified that checksum before extraction, published a new deploy-owned immutable directory and atomically switched `/opt/skills.mirket.dev/current`. No Nginx configuration, DNS, certificate, plugin or memory-runtime changes were required.

Active release: `/opt/skills.mirket.dev/releases/cf41945c46bde6fd581b25379733143794f02762`.
Previous release, retained and readable for rollback: `/opt/skills.mirket.dev/releases/b47b89f5bbd14456ff4ccc549addedc6abeafd5c`.

## Live acceptance

- Homepage lists exactly the25 source skill slugs; all25 skill routes return200 and byte-match the clean export.
- Installation guide contains current Codex and Claude commands. Live mobile installer host/method controls display both correct command sets.
- Hindsight guide contains the latest freshness profile, bounded recovery, pending/processing guard, capture/freshness distinctions, existing-initiative update and durable bank-scoped query recovery guidance. Browser-rendered text confirms those updates.
- All71 checked HTML, social images, fingerprinted assets and Next navigation payload responses return200 and exactly match the export. The28 social images and all28 indexable pages are included.
- HTTP redirects to the same HTTPS path; a missing route returns404. Fingerprinted assets use immutable caching; navigation payloads use no-cache. The neighboring mirket.dev homepage remains byte-identical to its pre-deploy baseline.
- Real browser navigation from homepage to Secure and then Local Hindsight succeeds. Desktop1440px and mobile320px have no document horizontal overflow. Screenshots were inspected. Console reports zero errors/warnings.
- The first automation attempt to check an underlying styled radio was intercepted by its visible label span; clicking the visible label succeeded and selected the expected radio/commands. This was a locator adjustment, not a site failure.
- A final repeat of homepage, docs, memory and Deploy content parity passed after the browser checks. Nginx remains active. Existing runbook rollback can atomically restore the retained previous release if needed.

## Evidence and cleanup

`WebsiteDeployment.json` pins source, artifact and remote release. `WebsiteLiveVerification.json` records71 response hashes/statuses; `WebsiteDeploymentFileHashes.json` records the full export. Activation/checksum logs, browser evaluation, desktop and mobile screenshots accompany this report. Task-owned upload files were removed after activation; the disposable local clean build and dependency tree were removed after verification. Browser snapshots were moved into ignored workspace scratch. The source worktree remains clean; no new source commit was needed.
