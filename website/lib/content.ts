import {readFileSync, readdirSync} from "node:fs";
import {resolve} from "node:path";
import {parse} from "yaml";
import skillPages from "../data/skill-pages.json";

type SkillPage = (typeof skillPages)[keyof typeof skillPages];
const pagesBySlug: Partial<Record<string, SkillPage>> = skillPages;

export const repo = "https://github.com/nazmirket/skills";
export const guidePath = "docs/README.md";
export const otherAgentsPath = "docs/OtherAgents.md";
export const skillsPath = "skills";
const root = resolve(process.cwd(), "..");

export function readSource(path: string) {
  return readFileSync(resolve(root, path), "utf8");
}

export function getInstallGuide() {
  const source = readSource(guidePath);
  const snippets = new Map([...source.matchAll(/^```(?:text|sh) ([a-z-]+-(?:setup|install))\r?\n([\s\S]+?)\r?\n```[ \t]*$/gm)].map(([, key, value]) => [key, value]));
  function getSnippet(key: string) {
    const value = snippets.get(key);
    if (!value) throw new Error(`Missing ${key} snippet in ${guidePath}`);
    return value;
  }
  return [["Codex", "codex"], ["Claude Code", "claude-code"], ["OpenCode", "opencode"]].map(([name, id]) => ({
    name,
    prompt: getSnippet(`${id}-setup`),
    commands: getSnippet(`${id}-install`),
  }));
}

export function getSkills() {
  return readdirSync(resolve(root, skillsPath), {withFileTypes: true})
    .filter(entry => entry.isDirectory() && /^[a-z][a-z0-9-]*$/.test(entry.name))
    .map(({name: slug}) => {
      const page = pagesBySlug[slug];
      if (!page?.cardDescription) throw new Error(`Missing website copy for skill: ${slug}`);
      const path = `${skillsPath}/${slug}/SKILL.md`;
      const markdown = readSource(path);
      const frontmatter = /^---\r?\n([\s\S]*?)\r?\n---\r?\n/.exec(markdown);
      if (!frontmatter) throw new Error(`Missing skill frontmatter: ${path}`);
      const skill = parse(frontmatter[1]);
      const {interface: metadata} = parse(readSource(`${skillsPath}/${slug}/agents/openai.yaml`));
      return {
        slug,
        page,
        path,
        name: metadata.display_name as string,
        summary: metadata.short_description as string,
        description: skill.description as string,
        body: markdown.slice(frontmatter[0].length).trimStart(),
      };
    })
    .sort((a, b) => a.name.localeCompare(b.name, "en"));
}
