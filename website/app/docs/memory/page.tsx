import Link from "next/link";
import DocsNavigation from "../../../components/DocsNavigation";
import RepoMarkdown from "../../../components/RepoMarkdown";
import StructuredData from "../../../components/StructuredData";
import {memoryGuidePath, readSource} from "../../../lib/content";
import {docsBreadcrumb, memoryPage, pageGraph, pageMetadata} from "../../../lib/discovery";

export const metadata = pageMetadata(memoryPage);

export default function MemoryGuide() {
  return <main className="docs-layout wrap">
    <StructuredData data={pageGraph(memoryPage, [docsBreadcrumb, ["Local Hindsight", memoryPage.path]])}/>
    <DocsNavigation current="memory" source={memoryGuidePath} sections={[
      ["recommended-local-daemon", "Codex setup"],
      ["directory-based-memory-registry", "Project registry"],
      ["coverage-and-recovery", "Coverage and recovery"],
      ["claude-code-with-the-upstream-installer", "Claude Code setup"],
      ["other-self-hosting-options", "Other options"],
      ["project-freshness-and-bounded-recovery", "Freshness and recovery"],
      ["real-host-capture-acceptance", "Capture acceptance"],
    ]}/>
    <div className="docs-content">
      <nav className="docs-breadcrumb" aria-label="Breadcrumb">
        <Link href={docsBreadcrumb[1]}>Docs</Link><span aria-hidden="true">/</span>
        <span aria-current="page">Local Hindsight</span>
      </nav>
      <RepoMarkdown markdown={readSource(memoryGuidePath)} source={memoryGuidePath}/>
    </div>
  </main>;
}
