import {mkdirSync, readFileSync, writeFileSync} from "node:fs";

const workflows = JSON.parse(readFileSync(new URL("../data/workflows.json", import.meta.url), "utf8"));
const output = new URL("../../docs/diagrams/", import.meta.url);
mkdirSync(output, {recursive: true});

const escape = (value) => value.replace(/[&<>"]/g, (char) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[char]));

for (const {asset, title, figure, stages} of Object.values(workflows)) {
  const cards = stages.map(([label, detail], index) => {
    const x = 18 + index * 193;
    return `  <g transform="translate(${x},58)">
    <rect width="173" height="87" fill="#120e13" stroke="#67434c"/>
    <rect width="173" height="3" fill="#b22222"/>
    <text x="12" y="27" font-size="12" fill="#ff717d">0${index + 1}</text>
    <text x="12" y="50" font-size="16" font-weight="bold" fill="#fff2e9">${escape(label)}</text>
    <text x="12" y="71" font-size="12" fill="#c2aeb2">${escape(detail)}</text>
  </g>${index < stages.length - 1 ? `\n  <path d="M${x + 178} 102h9m-4-4 4 4-4 4" fill="none" stroke="#ff717d"/>` : ""}`;
  }).join("\n");
  const description = stages.map(([label, detail]) => `${label}: ${detail}`).join("; ");
  writeFileSync(new URL(asset, output), `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 788 163" width="788" height="163" role="img" aria-labelledby="title description">
  <title id="title">${escape(title)}</title>
  <desc id="description">${escape(description)}</desc>
  <rect x="0.5" y="0.5" width="787" height="162" fill="#191217" stroke="#67434c"/>
  <path d="M1 1h786v42H1z" fill="#22171d"/>
  <path d="M1 43h786" stroke="#67434c"/>
  <rect x="18" y="17" width="9" height="9" fill="#b22222"/>
  <g font-family="ui-monospace, monospace">
    <text x="38" y="26" font-size="15" font-weight="bold" fill="#fff2e9">${escape(title)}</text>
    <text x="770" y="26" font-size="12" text-anchor="end" fill="#ff717d">FIG. ${figure}</text>
${cards}
  </g>
</svg>
`);
}
