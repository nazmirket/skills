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
