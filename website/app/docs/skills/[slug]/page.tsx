import type {Metadata} from "next";
import Link from "next/link";
import {notFound} from "next/navigation";
import DocsNavigation from "../../../../components/DocsNavigation";
import RepoMarkdown from "../../../../components/RepoMarkdown";
import StructuredData from "../../../../components/StructuredData";
import {getSkills} from "../../../../lib/content";
import {docsBreadcrumb, pageGraph, pageMetadata, skillPageInfo} from "../../../../lib/discovery";

type Props = {params: Promise<{slug: string}>};

export function generateStaticParams() {
  return getSkills().map(({slug}) => ({slug}));
}

export const dynamicParams = false;

export async function generateMetadata({params}: Props): Promise<Metadata> {
  const {slug} = await params;
  const skill = getSkills().find(item => item.slug === slug);
  return skill ? pageMetadata(skillPageInfo(skill)) : {robots: {index: false}};
}

export default async function SkillPage({params}: Props) {
  const {slug} = await params;
  const skills = getSkills();
  const skill = skills.find(item => item.slug === slug);
  if (!skill) notFound();

  const page = skillPageInfo(skill);
  const index = skills.indexOf(skill);
  const previous = skills[index - 1];
  const next = skills[index + 1];

  return <main className="docs-layout wrap">
    <StructuredData data={pageGraph(page, [docsBreadcrumb, ["Skills", "/docs/#skills"], [skill.name, page.path]])}/>
    <DocsNavigation current="skill" source={skill.path} skills={skills} activeSkill={slug}/>
    <div className="docs-content">
      <nav className="docs-breadcrumb" aria-label="Breadcrumb">
        <Link href="/docs/">Docs</Link><span aria-hidden="true">/</span>
        <Link href="/docs/#skills">Skills</Link><span aria-hidden="true">/</span>
        <span aria-current="page">{skill.name}</span>
      </nav>
      <article className="prose skill-overview" id="main-content" tabIndex={-1}>
        <h1 id={slug}>{skill.name}</h1>
        <h2 id="when-to-use">When to use it</h2>
        <p>{skill.page.when}</p>
        <h2 id="what-it-adds">What it adds</h2>
        <p>{skill.page.adds}</p>
        <h2 id="example-prompt">Example prompt</h2>
        <blockquote><p>{skill.page.prompt}</p></blockquote>
      </article>
      <details className="skill-instructions" id="full-instructions">
        <summary>Full skill instructions</summary>
        <RepoMarkdown markdown={skill.body.replace(/^# [^\r\n]+\r?\n/, "").trimStart()} source={skill.path} id="skill-instructions"/>
      </details>
      <nav className="skill-pagination" aria-label="Adjacent skills">
        {previous && <Link href={`/docs/skills/${previous.slug}/`}><span>← Previous</span>{previous.name}</Link>}
        {next && <Link className="skill-next" href={`/docs/skills/${next.slug}/`}><span>Next →</span>{next.name}</Link>}
      </nav>
    </div>
  </main>;
}
