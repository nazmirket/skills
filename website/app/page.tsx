import Link from "next/link";
import Install from "../components/Install";
import Mascot from "../components/Mascot";
import PixelIcon, {type PixelGlyph} from "../components/PixelIcon";
import StructuredData from "../components/StructuredData";
import WorkflowDiagram from "../components/WorkflowDiagram";
import {getInstallGuide, getSkills} from "../lib/content";
import {homePage, pageGraph, pageMetadata} from "../lib/discovery";

export const metadata = pageMetadata(homePage);

const glyphs: Record<string, PixelGlyph> = {
  adapt: "target", architect: "plan", audit: "inspect", author: "prompt",
  brief: "signal", clean: "clean", critique: "inspect", curate: "target",
  debug: "bug", design: "design", distill: "signal", equip: "prompt",
  focus: "target", imagine: "design", orchestrate: "signal", plan: "plan",
  preflight: "check", refactor: "clean", sleep: "plan", test: "check",
};

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
        <p className="hero-description">Mirket is a free, open-source skills plugin for <strong>Codex</strong> and <strong>Claude Code</strong>. Use it to plan changes, debug failures, design interfaces, and verify results.</p>
      </div>
      <Install {...getInstallGuide()}/>
    </section>

    <section id="diagrams" className="section wrap" aria-labelledby="diagram-title">
      <div className="section-heading"><h2 id="diagram-title">How it Works</h2></div>
      <div className="diagram-grid"><WorkflowDiagram/><WorkflowDiagram variant="example"/></div>
    </section>

    <section id="skills" className="section wrap">
      <div className="section-heading">
        <div><p className="eyebrow">THE TOOLBOX / {skills.length} SKILLS</p><h2>Pick a skill</h2></div>
        <Link className="text-link catalog-link" href="/docs/">Read the docs <span aria-hidden="true">→</span></Link>
      </div>
      <div className="skill-grid">
        {skills.map(({slug, name, summary}) => <Link className="skill-card" key={slug} href={`/docs/skills/${slug}/`}>
          <span className="skill-glyph"><PixelIcon glyph={glyphs[slug] ?? "prompt"}/></span>
          <div><h3>{name}</h3><p>{summary}</p></div>
          <span className="skill-arrow" aria-hidden="true">→</span>
        </Link>)}
      </div>
    </section>
  </main>;
}
