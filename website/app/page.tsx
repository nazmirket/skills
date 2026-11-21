import Link from "next/link";
import Install from "../components/Install";
import Mascot from "../components/Mascot";
import PixelIcon from "../components/PixelIcon";
import StructuredData from "../components/StructuredData";
import WorkflowDiagrams from "../components/WorkflowDiagram";
import {getInstallGuide, getSkills} from "../lib/content";
import {homePage, pageGraph, pageMetadata} from "../lib/discovery";

export const metadata = pageMetadata(homePage);

export default function Home() {
  const skills = getSkills();
  return <main id="main-content" tabIndex={-1}>
    <StructuredData data={pageGraph(homePage)}/>
    <section className="hero wrap">
      <div className="hero-copy">
        <p className="eyebrow"><span className="status-dot" aria-hidden="true"/> MIRKET / AGENT SKILLS</p>
        <div className="hero-title">
          <Mascot/>
          <h1>Good work,<br/><span className="accent">on repeat.</span></h1>
        </div>
        <p className="hero-description">Mirket gives <strong>Codex</strong> and <strong>Claude Code</strong> reusable playbooks: what to inspect first, when to ask you for a decision, and how to verify the result.</p>
      </div>
      <Install {...getInstallGuide()}/>
    </section>

    <section id="diagrams" className="section wrap" aria-labelledby="diagram-title">
      <header className="diagram-heading">
        <p className="eyebrow">MIRKET IN PRACTICE</p>
        <h2 id="diagram-title">What changes with Mirket</h2>
      </header>
      <WorkflowDiagrams/>
    </section>

    <section id="skills" className="section wrap">
      <div className="section-heading">
        <div><p className="eyebrow">THE TOOLBOX / {skills.length} SKILLS</p><h2>Pick a skill</h2></div>
        <Link className="text-link catalog-link" href="/docs/">Read the docs <span aria-hidden="true">→</span></Link>
      </div>
      <div className="skill-grid">
        {skills.map(({slug, name, page}) => <Link className="skill-card" key={slug} href={`/docs/skills/${slug}/`}>
          <span className="skill-glyph"><PixelIcon glyph={slug}/></span>
          <div><h3>{name}</h3><p>{page.cardDescription}</p></div>
          <span className="skill-arrow" aria-hidden="true">→</span>
        </Link>)}
      </div>
    </section>
  </main>;
}
