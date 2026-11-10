import Markdown, {defaultUrlTransform} from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeSlug from "rehype-slug";
import {guidePath, repo, skillsPath} from "../lib/content";

function resolveLink(url: string, key: string, source: string) {
  const safe = defaultUrlTransform(url);
  if (!safe || safe.startsWith("#") || /^[a-z][a-z0-9+.-]*:|^\/\//i.test(safe)) return safe;

  const target = new URL(safe, `https://source.invalid/${source}`);
  const path = target.pathname.slice(1);
  const suffix = target.search + target.hash;
  if (key === "src") return `https://raw.githubusercontent.com/nazmirket/skills/main/${path}${suffix}`;
  if (path === guidePath) return `/docs/${suffix}`;
  if (path === skillsPath || path === `${skillsPath}/`) return "/#skills";

  const skill = /^plugins\/mirket\/skills\/([a-z][a-z0-9-]*)\/SKILL\.md$/.exec(path);
  if (skill) return `/docs/skills/${skill[1]}/${suffix}`;

  const kind = path.endsWith("/") ? "tree" : "blob";
  return `${repo}/${kind}/main/${path}${suffix}`;
}

export default function RepoMarkdown({markdown, source}: {markdown: string; source: string}) {
  return <article className="prose" id="main-content" tabIndex={-1}>
    <Markdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeSlug]} urlTransform={(url, key) => resolveLink(url, key, source)}
      components={{table: ({node: _node, ...props}) => <div className="prose-table"><table {...props}/></div>}}>
      {markdown}
    </Markdown>
  </article>;
}
