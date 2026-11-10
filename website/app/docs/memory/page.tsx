import type {Metadata} from "next";
import DocsNavigation from "../../../components/DocsNavigation";
import RepoMarkdown from "../../../components/RepoMarkdown";
import {memoryGuidePath, readSource} from "../../../lib/content";

export const metadata: Metadata = {
  title: "Local Hindsight — Mirket documentation",
  description: "Optional local Hindsight setup for Codex and Claude Code.",
};

export default function MemoryGuide() {
  return <main className="docs-layout wrap">
    <DocsNavigation current="memory" source={memoryGuidePath} sections={[
      ["recommended-local-daemon", "Codex setup"],
      ["directory-based-memory-registry", "Project registry"],
      ["coverage-and-recovery", "Coverage and recovery"],
      ["claude-code-with-the-upstream-installer", "Claude Code setup"],
      ["other-self-hosting-options", "Other options"],
    ]}/>
    <div className="docs-content">
      <RepoMarkdown markdown={readSource(memoryGuidePath)} source={memoryGuidePath}/>
    </div>
  </main>;
}
