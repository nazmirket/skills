# Mirket skills website

The local, static Next.js site for skills.mirket.dev. Its content and installation commands are based on the repository README and the Mirket plugin skills.

```sh
cd website
npm install
npm run dev
```

Open the local URL printed by Next.js. Run `npm run build` to create the deployable static export in `out/`. No server-side services or deployment configuration are required. The workflow illustration is an editable Remotion composition embedded with `@remotion/player`; reduced-motion visitors see a still frame.

The homepage reads the packaged skill display metadata. The docs index renders [the repository guide](../docs/README.md), and each skill page renders its packaged `SKILL.md`. Changes to these Markdown sources appear in the next static export.

The animated workflow diagrams and the repository README diagrams share [one set of steps](data/workflows.json). After changing those steps, run `npm run docs:diagrams` from this directory to refresh the checked-in SVGs.

## Search and share previews

The static export includes canonical metadata, JSON-LD, and a page-specific 1200 × 630 PNG for each public page. [Page discovery data](lib/discovery.ts) supplies the metadata, social previews, and sitemap. The docs' install commands and prompts come from [the repository guide](../docs/README.md). The crawler policy allows public pages and links to the sitemap; `llms.txt` is an optional plain-text guide to the same canonical pages.

Run `npm run build` and `npm run seo:check` to validate the exported HTML, PNGs, and discovery files. To preview cards locally, open the PNGs in `out/social/`. When the card artwork changes, update the filename version in the discovery data so sharing services can fetch a new image URL.

After deployment, verify that `/robots.txt`, `/sitemap.xml`, and the PNG URLs return 200 at the production hostname. Submit the sitemap in Google Search Console and Bing Webmaster Tools if you manage those properties. Use the platform's preview tool if an older card stays cached. Neither structured data nor `llms.txt` guarantees indexing, rankings, or inclusion in generated answers.
