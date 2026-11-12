import Link from "next/link";
import {getSkills, repo} from "../lib/content";

type SkillLink = {slug: string; name: string};

type Props = {
  current: "overview" | "skill";
  source: string;
  sections?: ReadonlyArray<readonly [id: string, title: string]>;
  skills?: SkillLink[];
  activeSkill?: string;
};

export default function DocsNavigation({current, source, sections, skills = getSkills(), activeSkill}: Props) {
  return <aside className="docs-sidebar">
    <p className="eyebrow">DOCUMENTATION</p>
    <nav aria-label="Documentation">
      <Link href="/docs/" aria-current={current === "overview" ? "page" : undefined}>Overview</Link>
      <Link href="/docs/#skills">Skill reference</Link>
    </nav>

    {sections && <div className="docs-section-links">
      <p className="eyebrow">ON THIS PAGE</p>
      <nav aria-label="On this page">{sections.map(([id, title]) => <a key={id} href={`#${id}`}>{title}</a>)}</nav>
    </div>}

    <details className="docs-skill-index">
      <summary>Browse {skills.length} skills</summary>
      <nav aria-label="Skill index">
        {skills.map(({slug, name}) => <Link key={slug} href={`/docs/skills/${slug}/`} aria-current={slug === activeSkill ? "page" : undefined}>{name}</Link>)}
      </nav>
    </details>
    <a className="text-link" href={`${repo}/blob/main/${source}`}>Markdown source ↗</a>
  </aside>;
}
