# Plan — draft, execution authorized

1. Audit current production HTML and discovery files; use the installed Next docs, Open Graph, X and search-provider primary guidance. Generate canonical per-page titles and descriptions, social metadata, site/route structured data, robots.txt, sitemap.xml, and llms.txt from the static routes and packaged skill catalog.
2. Render a branded PNG for each page at build time using the existing mascot and fonts, with no external runtime. Keep cards readable after cropping. Add concise visible answers and both install command sets to the source-backed documentation and share those commands with the existing homepage installer.
3. Check the exported HTML, PNGs, route coverage and discovery artifacts, then inspect representative preview images and browser flows at desktop and phone sizes. Record deployment verification steps in the website README. Keep current origin and unrelated work unchanged.

## Result

Production audit found no canonical, OG, X, or JSON-LD metadata on the sampled pages and no robots.txt, sitemap.xml, or llms.txt. Implemented and verified the replacement locally: 23 indexable routes, 23 build-time share cards with the pixel mascot, valid canonical URLs and sitemap entries, structured data and error-page exclusions. Both install command sets and direct answers are available in exported HTML. A fresh npm ci and export passed; final build and discovery checks passed. Browser smoke passed for six crawler user agents and 320px/1366px installer layout, and all internal links and fragments resolve. Reviewed representative share images and retained the final export. 53 repository tests passed. No commit or production deployment was performed.

## Deployment

User authorized commit, push, and deployment. Commit 5880421 was pushed to origin/main. Built from a clean archive with npm ci and passed the discovery checks. Activated the versioned release and verified the previous release is still available for rollback. The public HTTPS responses for all 23 pages, 23 social cards, sitemap, robots.txt, llms.txt, and the 404 body matched the committed export byte for byte. HTTP redirection, neighboring site, and Nginx health also passed. The untracked runbook now includes discovery checks.
