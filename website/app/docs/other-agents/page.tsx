import DocsNavigation from "../../../components/DocsNavigation";
import RepoMarkdown from "../../../components/RepoMarkdown";
import StructuredData from "../../../components/StructuredData";
import {otherAgentsPath, readSource} from "../../../lib/content";
import {docsBreadcrumb, otherAgentsPage, pageGraph, pageMetadata} from "../../../lib/discovery";

export const metadata = pageMetadata(otherAgentsPage);

export default function OtherAgents() {
  return <main className="docs-layout wrap">
    <StructuredData data={pageGraph(otherAgentsPage, [docsBreadcrumb, ["Other agents", otherAgentsPage.path]])}/>
    <DocsNavigation current="other-agents" source={otherAgentsPath} sections={[
      ["install-the-shared-catalog", "Install the catalog"],
      ["verify-in-your-agent", "Verify in your agent"],
      ["update-or-remove-the-catalog", "Update or remove"],
    ]}/>
    <div className="docs-content">
      <RepoMarkdown markdown={readSource(otherAgentsPath)} source={otherAgentsPath}/>
    </div>
  </main>;
}
