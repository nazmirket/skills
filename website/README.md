# Mirket skills website

The local, static Next.js site for skills.mirket.dev. Its content and installation commands come from `docs/README.md` and the Mirket skills in the repository’s root `skills/` directory. The catalog, skill pages, navigation, sitemap and social previews are derived from those sources.

```sh
cd website
npm install
npm run dev
```

Open the local URL printed by Next.js. Run `npm run build` to create the deployable static export in `out/`. No server-side services or deployment configuration are required.

The homepage uses packaged skill names and its own [card descriptions](data/skill-cards.json). Each skill page opens with a [quick start](data/skill-pages.json) and one example prompt. Expand **Full skill instructions** to read the packaged `SKILL.md`. The docs index renders [the repository guide](../docs/README.md).

The homepage diagrams and the repository README SVGs share [one source](data/workflows.json). The first shows when the owning skill asks for help or a human decision; the second follows an illustrative bug fix from request to evidence. Keep both aligned with the packaged routing guide. After changing the data, run `npm run docs:diagrams` to refresh the SVGs.

Each catalog card has a 10 × 10 [pixel icon](components/PixelIcon.tsx) drawn on the same grid. Add a distinct icon under the skill slug when adding a skill.

## Search and share previews

The static export includes canonical metadata, JSON-LD, and a page-specific 1200 × 630 PNG for each public page. [Page discovery data](lib/discovery.ts) supplies the metadata, social previews, and sitemap. The docs' install commands and prompts come from [the repository guide](../docs/README.md). The crawler policy allows public pages and links to the sitemap; `llms.txt` is an optional plain-text guide to the same canonical pages.

Run `npm run build` and `npm run seo:check` to validate the exported HTML, PNGs, and discovery files. To preview cards locally, open the PNGs in `out/social/`. When the card artwork changes, update the filename version in the discovery data so sharing services can fetch a new image URL.

The export produces an indexable page and social preview for each skill, plus the home and documentation pages. Verify new skill routes, catalog navigation and long summaries at desktop and narrow mobile widths, including reduced-motion mode, before claiming visual quality. Build success alone is not rendered verification.

After deployment, verify that `/robots.txt`, `/sitemap.xml`, and the PNG URLs return 200 at the production hostname. Submit the sitemap in Google Search Console and Bing Webmaster Tools if you manage those properties. Use the platform's preview tool if an older card stays cached. Neither structured data nor `llms.txt` guarantees indexing, rankings, or inclusion in generated answers.
