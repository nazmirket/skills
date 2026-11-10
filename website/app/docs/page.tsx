import DocsNavigation from "../../components/DocsNavigation";
import RepoMarkdown from "../../components/RepoMarkdown";
import StructuredData from "../../components/StructuredData";
import {guidePath, readSource} from "../../lib/content";
import {docsPage, pageGraph, pageMetadata} from "../../lib/discovery";

export const metadata = pageMetadata(docsPage);

export default function Documentation() {
  return <main className="docs-layout wrap">
    <StructuredData data={pageGraph(docsPage)}/>
    <DocsNavigation current="overview" source={guidePath} sections={[
      ["install-mirket", "Install Mirket"],
      ["purpose", "Purpose"],
      ["philosophy", "Philosophy"],
      ["skills", "Skills"],
      ["architecture", "Architecture"],
      ["optional-local-hindsight", "Hindsight opt-in"],
      ["codex-setup-prompt", "Codex prompt"],
      ["claude-code-setup-prompt", "Claude Code prompt"],
      ["common-questions", "Common questions"],
    ]}/>
    <div className="docs-content">
      <RepoMarkdown markdown={readSource(guidePath)} source={guidePath}/>
    </div>
  </main>;
}
