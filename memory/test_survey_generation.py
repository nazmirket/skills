"""Survey receipts require fresh findings for their pending generation."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import project_registry as registry


IDS = ["repository-component-map", "repository-core-concepts", "repository-conventions-and-patterns", "repository-tech-stack-and-features"]


@unittest.skipUnless(shutil.which("node"), "Node is required for generated runtime checks")
class SurveyGenerationTest(unittest.TestCase):
    def execute(self, source):
        result = subprocess.run(["node", "--input-type=module", "-e", source], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def evidence(self, fresh=4, fail=False, behind=0, changed=False):
        marker = "survey-baseline:" + "a" * 40
        documents = {marker: {"id": marker, "tags": ["source:survey-baseline"], "updated_at": "2026-11-11T09:00:00Z"}}
        for index, identity in enumerate(IDS):
            documents[identity] = {"id": identity, "tags": ["source:upload"],
                "updated_at": "2026-11-11T09:01:00Z" if index < fresh else "2026-11-10T09:01:00Z"}
        script = "const SURVEY_DOC_IDS=" + json.dumps(IDS) + ";\n" + registry.SURVEY_EVIDENCE_JS
        script += 'const REPO="fixture", gitHeadSha=()=>"a".repeat(40);\n'
        script += "const documents=" + json.dumps(documents) + ";\n"
        script += f"const fail={json.dumps(fail)}, changed={json.dumps(changed)}; let reads=0;\n"
        script += '''const client = {bankUrl: value => value, req: async (method, path) => {
          if (fail) throw new Error("API unavailable");
          const id = decodeURIComponent(path.slice("/documents/".length));
          const document = {...documents[id]};
          if (id.startsWith("survey-baseline:")) {
            reads++;
            if (changed && reads > 1) document.updated_at = "2026-11-11T09:02:00Z";
          }
          return {ok: true, json: async () => document};
        }};
        '''
        script += "console.log(JSON.stringify(await mirketSurveyEvidence(client," + json.dumps({"id": marker, "sha": "a" * 40, "behind": behind}) + ")));"
        return self.execute(script)

    def test_old_findings_cannot_complete_new_receipt(self):
        self.assertIsNone(self.evidence(fresh=0))

    def test_partial_current_generation_cannot_complete_receipt(self):
        self.assertIsNone(self.evidence(fresh=3))

    def test_all_current_findings_produce_revision_and_timestamp_evidence(self):
        evidence = self.evidence()
        self.assertEqual(evidence["mirket_survey_revision"], "a" * 40)
        self.assertEqual(evidence["mirket_survey_started_at"], "2026-11-11T09:00:00Z")
        self.assertEqual(set(json.loads(evidence["mirket_survey_finding_updates"])), set(IDS))

    def test_api_failure_does_not_produce_completion(self):
        self.assertIsNone(self.evidence(fail=True))

    def test_later_findings_cannot_complete_unrelated_historical_receipt(self):
        self.assertIsNone(self.evidence(behind=1))

    def test_retry_during_evidence_read_invalidates_completion(self):
        self.assertIsNone(self.evidence(changed=True))

    def test_incomplete_current_receipt_does_not_suppress_retry(self):
        source = '''const counts=[];
              for (const id of markers) {
                counts.push(distances[id]);
              }
              const sinceLast=counts.length ? Math.min(...counts) : null;
              const findingsAbsent=false;
              return ''' + registry.SURVEY_CADENCE + ";"
        adapted = registry.survey_cadence(source)
        old, current = "survey-baseline:" + "a" * 40, "survey-baseline:" + "b" * 40
        for completed, expected in (([old], True), ([], True), ([old, current], False)):
            with self.subTest(completed=completed):
                script = ('const markers=new Set(' + json.dumps([old, current]) + '), distances=' + json.dumps({old: 1, current: 0}) + ', cfg={surveyRefreshCommits:1}; '
                          'const SURVEY_BASELINE_PREFIX="survey-baseline:", cwd="fixture", gitLocal=()=>""; '
                          'const client={listDocumentIds:async()=>new Set(' + json.dumps(completed) + ')}; '
                          'console.log(JSON.stringify(await(async()=>{' + adapted + '})()));')
                self.assertEqual(self.execute(script), expected)

    def test_descendant_receipt_is_not_current_head_or_an_ancestor(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            def git(*args):
                return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True).stdout.strip()
            git("init", "-q")
            for message in ("older", "newer"):
                git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "--allow-empty", "-qm", message)
                if message == "older":
                    older = git("rev-parse", "HEAD")
            newer = git("rev-parse", "HEAD")
            git("checkout", "-q", "--detach", older)
            self.assertEqual(git("rev-list", "--count", newer + "..HEAD"), "0")
            prefix = ('import {execFileSync} from "node:child_process"; const REPO=' + json.dumps(str(root)) + '; '
                      'const gitLocal=(repo,...args)=>execFileSync("git",["-C",repo,...args],{encoding:"utf8",stdio:["ignore","pipe","pipe"]}); '
                      'const gitHeadSha=repo=>gitLocal(repo,"rev-parse","HEAD").trim(); const SURVEY_DOC_IDS=[]; ')
            script = prefix + registry.SURVEY_EVIDENCE_JS + 'console.log(JSON.stringify(await mirketSurveyEvidence({},' + json.dumps({"sha": newer, "behind": 0}) + ')));'
            self.assertIsNone(self.execute(script))
            cadence = '''const counts=[];
              for (const id of markers) {
                counts.push(Number(gitLocal(cwd,"rev-list","--count",id.slice(SURVEY_BASELINE_PREFIX.length)+"..HEAD").trim()));
              }
              const sinceLast=counts.length ? Math.min(...counts) : null;
              const findingsAbsent=false;
              return ''' + registry.SURVEY_CADENCE + ";"
            script = (prefix + 'const cwd=REPO, SURVEY_BASELINE_PREFIX="survey-baseline:", cfg={surveyRefreshCommits:1}; '
                      'const markers=new Set(' + json.dumps(["survey-baseline:" + newer]) + '), client={listDocumentIds:async()=>markers}; '
                      'console.log(JSON.stringify(await(async()=>{' + registry.survey_cadence(cadence) + '})()));')
            self.assertTrue(self.execute(script))

    @unittest.skipUnless(os.environ.get("MIRKET_TEST_RUNTIME"), "Set MIRKET_TEST_RUNTIME for pinned adapter contract checks")
    def test_actual_pinned_adapters_parse_and_guard_receipt_writes(self):
        dist = Path(os.environ["MIRKET_TEST_RUNTIME"]) / "dist"
        adapted = registry.adapters(dist)
        for name, source in adapted.items():
            with self.subTest(name=name):
                subprocess.run(["node", "--check", "--input-type=module"], input=source, text=True, capture_output=True, check=True)
        worker = adapted[registry.DEEPEN_ENTRY]
        self.assertIn("if (mirketEvidence)", worker)
        self.assertIn("metadata: {...stamp.metadata, ...mirketEvidence}", worker)
        self.assertIn("if (!completedMarkers.has(id)) continue;", adapted[registry.SURVEY_ENTRY])
