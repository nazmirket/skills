import {getSkills, repo} from "../../lib/content";
import {canonicalUrl, docsPage, homePage, skillPageInfo} from "../../lib/discovery";

export const dynamic = "force-static";

export function GET() {
  const docs = canonicalUrl(docsPage.path);
  const lines = [
    "# Mirket",
    "",
    `> ${homePage.description}`,
    "",
    "Mirket provides reusable Markdown workflows, not a model or a standalone coding agent.",
    "",
    "## Start here",
    "",
    `- [Mirket](${canonicalUrl(homePage.path)}): Workflow examples, installer and skill catalog.`,
    `- [Documentation](${docs}): Purpose, philosophy, architecture and common questions.`,
    `- [Install Mirket](${docs}#install-mirket): Commands for Codex and Claude Code.`,
    "",
    "## Skill reference",
    "",
    ...getSkills().map(skill => `- [${skill.name}](${canonicalUrl(skillPageInfo(skill).path)}): ${skill.summary}.`),
    "",
    "## Source",
    "",
    `- [GitHub repository](${repo}): Plugin source, Markdown guides and marketplaces.`,
    `- [MIT License](${repo}/blob/main/LICENSE): Terms for use and redistribution.`,
    "",
  ];
  return new Response(lines.join("\n"), {headers: {"Content-Type": "text/plain; charset=utf-8"}});
}
