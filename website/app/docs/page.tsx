import type {Metadata} from "next";
import RepoMarkdown from "../../components/RepoMarkdown";
import WorkflowDiagram from "../../components/WorkflowDiagram";
import {guidePath, readSource, repo} from "../../lib/content";

export const metadata: Metadata = {
  title: "Mirket documentation",
  description: "How Mirket works: its purpose, skills, philosophy, and plugin architecture.",
};

export default function Documentation() {
  return <main className="docs-layout wrap">
    <aside className="docs-sidebar">
      <p className="eyebrow">FIELD GUIDE</p>
      <nav aria-label="Documentation sections">
        <a href="#purpose">Purpose</a><a href="#philosophy">Philosophy</a><a href="#skills">Skills</a>
        <a href="#architecture">Architecture</a><a href="#diagrams">Workflow diagrams</a>
      </nav>
      <a className="text-link" href={`${repo}/blob/main/${guidePath}`}>Markdown source ↗</a>
    </aside>
    <div className="docs-content">
      <RepoMarkdown markdown={readSource(guidePath)} source={guidePath}/>
      <section className="docs-diagrams" id="diagrams" aria-labelledby="diagram-title">
        <p className="eyebrow">ILLUSTRATED WORKFLOWS</p><h2 id="diagram-title">Workflow diagrams</h2>
        <div className="diagram-grid"><WorkflowDiagram/><WorkflowDiagram variant="example"/></div>
      </section>
    </div>
  </main>;
}
