import type {Metadata} from "next";
import DocsNavigation from "../../components/DocsNavigation";
import RepoMarkdown from "../../components/RepoMarkdown";
import {guidePath, readSource} from "../../lib/content";

export const metadata: Metadata = {
  title: "Mirket documentation",
  description: "How Mirket works: its purpose, skills, philosophy, and plugin architecture.",
};

export default function Documentation() {
  return <main className="docs-layout wrap">
    <DocsNavigation current="overview" source={guidePath} sections={[
      ["purpose", "Purpose"],
      ["philosophy", "Philosophy"],
      ["skills", "Skills"],
      ["architecture", "Architecture"],
      ["optional-local-hindsight", "Hindsight opt-in"],
      ["codex-setup-prompt", "Codex prompt"],
      ["claude-code-setup-prompt", "Claude Code prompt"],
    ]}/>
    <div className="docs-content">
      <RepoMarkdown markdown={readSource(guidePath)} source={guidePath}/>
    </div>
  </main>;
}
