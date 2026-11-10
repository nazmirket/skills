import type {Metadata} from "next";
import Link from "next/link";
import {notFound} from "next/navigation";
import RepoMarkdown from "../../../../components/RepoMarkdown";
import {getSkills, repo} from "../../../../lib/content";

type Props = {params: Promise<{slug: string}>};

export function generateStaticParams() {
  return getSkills().map(({slug}) => ({slug}));
}

export const dynamicParams = false;

export async function generateMetadata({params}: Props): Promise<Metadata> {
  const {slug} = await params;
  const skill = getSkills().find(item => item.slug === slug);
  return skill ? {title: `${skill.name} — Mirket skill`, description: skill.description} : {};
}

export default async function SkillPage({params}: Props) {
  const {slug} = await params;
  const skills = getSkills();
  const skill = skills.find(item => item.slug === slug);
  if (!skill) notFound();

  const skillIndex = skills.map(item => <Link key={item.slug} href={`/docs/skills/${item.slug}/`} aria-current={item.slug === slug ? "page" : undefined}>{item.name}</Link>);

  return <main className="docs-layout wrap">
    <aside className="docs-sidebar">
      <Link className="text-link" href="/docs/">← Docs overview</Link>
      <div className="skill-index-desktop">
        <p className="eyebrow">SKILL INDEX</p>
        <nav aria-label="Skill index">{skillIndex}</nav>
      </div>
      <details className="skill-index-mobile">
        <summary>Browse all {skills.length} skills</summary>
        <nav aria-label="Skill index">{skillIndex}</nav>
      </details>
    </aside>
    <div className="docs-content">
      <div className="docs-source"><p className="eyebrow">MIRKET / SKILL</p><a className="text-link" href={`${repo}/blob/main/${skill.path}`}>Markdown source ↗</a></div>
      <RepoMarkdown markdown={skill.body} source={skill.path}/>
    </div>
  </main>;
}
