import {readFileSync, readdirSync} from "node:fs";
import {resolve} from "node:path";
import {parse} from "yaml";

export const repo = "https://github.com/nazmirket/skills";
export const guidePath = "docs/README.md";
export const memoryGuidePath = "memory/README.md";
export const skillsPath = "plugins/mirket/skills";
const root = resolve(process.cwd(), "..");

export function readSource(path: string) {
  return readFileSync(resolve(root, path), "utf8");
}

export function getInstallGuide() {
  const source = readSource(guidePath);
  const snippets = new Map([...source.matchAll(/^```(?:text|sh) ((?:codex|claude-code)-(?:setup|install))\r?\n([\s\S]+?)\r?\n```[ \t]*$/gm)].map(([, key, value]) => [key, value]));
  function getPair(kind: "setup" | "install") {
    const codex = snippets.get(`codex-${kind}`);
    const claude = snippets.get(`claude-code-${kind}`);
    if (!codex || !claude) throw new Error(`Missing ${kind} snippet in ${guidePath}`);
    return {Codex: codex, "Claude Code": claude};
  }
  return {prompts: getPair("setup"), commands: getPair("install")};
}

export function getSkills() {
  return readdirSync(resolve(root, skillsPath), {withFileTypes: true})
    .filter(entry => entry.isDirectory() && /^[a-z][a-z0-9-]*$/.test(entry.name))
    .map(({name: slug}) => {
      const path = `${skillsPath}/${slug}/SKILL.md`;
      const markdown = readSource(path);
      const frontmatter = /^---\r?\n([\s\S]*?)\r?\n---\r?\n/.exec(markdown);
      if (!frontmatter) throw new Error(`Missing skill frontmatter: ${path}`);
      const skill = parse(frontmatter[1]);
      const {interface: metadata} = parse(readSource(`${skillsPath}/${slug}/agents/openai.yaml`));
      return {
        slug,
        path,
        name: metadata.display_name as string,
        summary: metadata.short_description as string,
        description: skill.description as string,
        body: markdown.slice(frontmatter[0].length).trimStart(),
      };
    })
    .sort((a, b) => a.name.localeCompare(b.name, "en"));
}
