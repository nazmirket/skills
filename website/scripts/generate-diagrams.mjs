import {mkdirSync, readFileSync, writeFileSync} from "node:fs";

const {routing, example} = JSON.parse(readFileSync(new URL("../data/workflows.json", import.meta.url), "utf8"));
const output = new URL("../../docs/diagrams/", import.meta.url);
mkdirSync(output, {recursive: true});

const escape = (value) => value.replace(/[&<>"]/g, (char) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[char]));
const width = 788;
const innerWidth = 750;
const lineHeight = 19;

function wrap(value, limit) {
  return value.split(" ").reduce((lines, word) => {
    const last = lines.at(-1);
    if (last && last.length + word.length + 1 <= limit) lines[lines.length - 1] += " " + word;
    else lines.push(word);
    return lines;
  }, []);
}

function textLines(lines, x, y, style = "detail") {
  return lines.map((line, index) => `<text class="${style}" x="${x}" y="${y + lineHeight * index}">${escape(line)}</text>`).join("\n");
}

function card(x, y, w, h, label, detail, featured = false) {
  return `<rect class="${featured ? "featured" : "card"}" x="${x}" y="${y}" width="${w}" height="${h}"/>
  ${featured ? `<rect x="${x}" y="${y}" width="3" height="${h}" fill="#ff717d"/>\n  ` : ""}${textLines([label], x + 14, y + 25, "card-title")}
  ${textLines(detail, x + 14, y + 47)}`;
}

function routingArt() {
  const fullCopyWidth = 87;
  const branchWidth = 368;
  const start = wrap(routing.start.detail, fullCopyWidth);
  const end = wrap(routing.finish.detail, fullCopyWidth);
  const branchText = routing.branches.map(({detail}) => wrap(detail, 42));
  const startY = 80;
  const startHeight = 40 + start.length * lineHeight;
  const forkY = startY + startHeight + 31;
  const branchY = forkY + 10;
  const branchHeight = 40 + Math.max(...branchText.map(lines => lines.length)) * lineHeight;
  const joinY = branchY + branchHeight + 10;
  const endY = joinY + 14;
  const endHeight = 40 + end.length * lineHeight;
  return {
    height: endY + endHeight + 19,
    description: [routing.start, ...routing.branches, routing.finish].map(({label, detail}) => `${label}: ${detail}`).join(" "),
    art: `${card(19, startY, innerWidth, startHeight, routing.start.label, start, true)}
  <path class="connector" d="M394 ${startY + startHeight}V${endY - 2}m-4-5 4 5 4-5"/>
  <path class="branch" d="M203 ${branchY}v-10h382v10 M203 ${joinY - 10}v10h382v-10"/>
  <rect x="327" y="${forkY - 20}" width="134" height="17" fill="#191217"/>
  ${textLines([routing.branchCue], width / 2, forkY - 7, "label centered")}
  ${routing.branches.map(({label}, index) => card(19 + index * 382, branchY, branchWidth, branchHeight, label, branchText[index])).join("\n")}
  ${card(19, endY, innerWidth, endHeight, routing.finish.label, end, true)}`,
  };
}

function exampleArt() {
  const prompt = wrap(example.prompt, 87);
  const promptY = 80;
  const promptHeight = 40 + prompt.length * lineHeight;
  let y = promptY + promptHeight + 17;
  const steps = example.steps.map(({label, role, detail}, index) => {
    const lines = wrap(detail, 83);
    const height = 34 + lines.length * lineHeight;
    const body = `<rect x="23" y="${y + 4}" width="18" height="18" fill="#3b1922"/>
  ${textLines([String(index + 1)], 32, y + 17, "label centered")}
  ${textLines([`${label} / ${role}`], 53, y + 18, "card-title")}
  ${textLines(lines, 53, y + 39)}`;
    y += height;
    return body;
  });
  const report = wrap(example.report, 87);
  const reportHeight = 40 + report.length * lineHeight;
  return {
    height: y + reportHeight + 19,
    description: `You ask: ${example.prompt} ${example.steps.map(({label, detail}) => `${label}: ${detail}`).join(" ")} What you get back: ${example.report}`,
    art: `${card(19, promptY, innerWidth, promptHeight, "YOU ASK", prompt)}
  ${steps.join("\n")}
  ${card(19, y, innerWidth, reportHeight, "WHAT YOU GET BACK", report, true)}`,
  };
}

for (const [data, {height, description, art}] of [[routing, routingArt()], [example, exampleArt()]]) {
  writeFileSync(new URL(data.asset, output), `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}" role="img" aria-labelledby="title description">
  <title id="title">${escape(data.title)}</title>
  <desc id="description">${escape(description)}</desc>
  <style>
    text { font-family: ui-monospace, monospace; fill: #fff2e9; }
    .label { font-size: 11px; fill: #ff717d; font-weight: bold; }
    .heading { font-size: 19px; font-weight: bold; }
    .card-title { font-size: 14px; font-weight: bold; }
    .detail { font-size: 13px; fill: #c2aeb2; }
    .centered { text-anchor: middle; }
    .card { fill: #120e13; stroke: #67434c; }
    .featured { fill: #25171d; stroke: #67434c; }
    .branch { stroke: #91646d; stroke-dasharray: 3 3; fill: none; }
    .connector { stroke: #ff717d; fill: none; }
  </style>
  <rect x=".5" y=".5" width="${width - 1}" height="${height - 1}" fill="#191217" stroke="#67434c"/>
  <path d="M1 1h786v63H1z" fill="#22171d"/>
  <path d="M1 64h786" stroke="#67434c"/>
  ${textLines([`${data.figure} / ${data.label}`], 19, 23, "label")}
  ${textLines([data.title], 19, 48, "heading")}
  ${art}
</svg>
`);
}
