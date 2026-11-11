# Local Hindsight for Mirket

Mirket works without Hindsight. This directory contains a guarded installer for Codex and guidance for Claude Code's upstream integration. Hindsight installs its runtime, configuration, and memory data in its normal user-level locations; this repository is not the memory store.

## Recommended: local daemon

This setup uses Hindsight's coding-agents integration and a local daemon. Mirket's installer wires the Codex hooks, interactive MCP and the background survey through the same project registry so unrelated repositories with the same name stay separate. The daemon starts on demand and keeps running until stopped. The first start downloads its package and models and may not be ready for the first turn or two.

The registry uses POSIX file locking. On macOS or Linux you need Python 3.8 or newer, Node.js and npm/npx, Codex, `uvx` (from `uv`), and a current Rust toolchain on macOS. Install missing tools using their official guidance: [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Rust](https://www.rust-lang.org/tools/install). This installer does not install prerequisites or change model providers for you.

Choose the LLM deliberately. Hindsight supports your Codex subscription (`openai-codex`), local models such as Ollama, and other providers. Local memory storage does not make a remote provider local. A local model must already be running and configured; Codex provider requests use your subscription and send context to OpenAI. See [Hindsight model configuration](https://hindsight.vectorize.io/developer/models).

For example, after signing in to the Codex CLI, select the Codex provider in the shell that runs setup:

```sh
export HINDSIGHT_API_LLM_PROVIDER=openai-codex
python3 memory/install.py --check
python3 memory/install.py
```

Run these commands from the repository root. `--check` is read-only and checks whether a fresh install is safe. The install downloads the pinned coding-agents package, wires the registry, and sets Codex to page-first injection. A fresh install refuses to replace an existing Hindsight configuration, MCP registration, or service on the daemon's default port. For an existing recognized 0.8.6 Codex installation, run `python3 memory/install.py --wire` instead. It updates the wrapper and adapters without reinstalling the daemon and keeps private recovery copies under `~/.hindsight/mirket/backups/`. It refuses ambiguous or unrecognized wiring. Follow the [upstream guide](https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/coding-agents/README.md) for other installations.

For newly wired hooks and MCP, the installer records the selected provider name and installation PATH so a separately launched Codex Desktop app can find them. Credentials and provider-specific settings still have to be available to the daemon; the installer does not write secrets or change login settings. When wiring an existing setup, existing registry commands are preserved to keep their trust configuration. Verify the actual host after installation or a toolchain change.

After installation:

1. Restart Codex, review and trust the hooks as required by your host, and check `codex features list` for the `hooks` feature. If needed, use `codex features enable hooks` deliberately; see [Codex hooks](https://learn.chatgpt.com/docs/hooks).
2. Run `python3 memory/doctor.py` from the project. It reports the resolved bank, configured hooks and MCP, adapter integrity, daemon health, known local primary-session coverage, survey documents and page freshness separately. For recent conversation evidence, use `python3 memory/doctor.py --recall-chat 'your question'` against the default local daemon. A healthy daemon or a synced seed does not prove capture or recall.
3. In each host you use, record a harmless decision, open a fresh session and check that it is recalled. Verify the bank in a linked worktree and verify that a different project cannot see that evidence. This is a host integration check, separate from the doctor and unit tests.

Mirket pins the Codex integration runtime; daemon and model downloads are separate. Hindsight retains session conversations and ingests repository commit messages by default. Model processing may use subscription limits or API credits, and captured content can be sent to whichever model provider you select. Inherited `HINDSIGHT_API_*` settings can also redirect storage or other processing: review them before starting the daemon if data locality matters.

## Directory-based memory registry

The Codex-specific [project registry](project_registry.py) routes hooks and MCP to the bank assigned to the canonical project root. It records paths and bank identifiers in `~/.hindsight/mirket/projects.json`, without conversation text. Explicit project mappings are preserved. Separate same-named repositories receive different banks; subdirectories and linked worktrees share the main project bank. For a Git repository with a separate Git directory, the shared metadata directory is its identity. Non-Git sessions use their starting directory.

Hindsight's MCP server resolves its bank at session startup. Start a new Codex session when switching projects. Hooks persist the original project binding under `~/.hindsight/mirket/sessions/`; if the binding and old temporary marker are unavailable, a matching local Codex transcript can establish the original directory. A mismatched project or unverifiable resume is skipped and reported rather than routed to a new bank. The registry applies to Codex only. Other agents need equivalent routing and a separate host check.

The wrapper requires coding-agents 0.8.6 and pins Codex auto-updates off. The installer generates adapters for the pinned survey launcher and its background worker; upstream files stay intact. The survey's MCP process must resolve the same bank as its parent. The worker completes only a pending receipt for the current HEAD when all four finding documents have update timestamps strictly newer than that pending generation, and the receipt remains unchanged during the evidence read. It saves the revision and timestamps with the completed receipt. Old document IDs alone cannot complete a new survey. Cadence counts only completed receipts whose revisions are ancestors of the current HEAD; an incomplete receipt cannot suppress retries, which remain bounded by upstream's lease and attempt limit. A runtime upgrade needs an adapter review; changed hook commands need host trust review. Existing banks and mappings remain intact.

## Coverage and recovery

- Page search is the fast default. Verify recent status and decisions against a transcript or current project files. Use targeted chat recall when a page has not caught up; use deeper reflection when it adds value.
- If the 1.2.0 daemon reports `ReflectToolCallError` with extra JSON data using the Codex provider, use [Hindsight 1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1) or a later compatible release that includes the [response parser fix](https://github.com/vectorize-io/hindsight/pull/6459). Back up the database before upgrading and verify a live page refresh afterward.
- Commit messages are the default Git source. Zero diff documents under that policy is expected. Opt in to deeper Git ingestion per bank when the extra coverage justifies its processing cost.
- Archived chats are not automatically backfilled. Check the doctor's coverage count; an active session may still be waiting for its first successful Stop. Verify exact session IDs and project provenance before importing, and skip IDs already present. Copy only vetted documents from legacy banks. Keep originals until the destination has been verified.
- The installer preserves the configured capture policy. In the absence of an opt-in policy, the upstream default enables capture for projects broadly. Use explicit opt-in paths if only some projects should be retained, and check both hooks and MCP after changing policy. Loopback storage does not make LLM processing local.

## Claude Code with the upstream installer

Claude Code uses [Hindsight's Coding Agents integration](https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/coding-agents/README.md#claude-code). Mirket's `memory/install.py`, doctor, and project registry are for Codex.

1. Check for existing Hindsight hooks, an MCP registration, and a daemon or server configuration before installing. Choose the [model provider](https://hindsight.vectorize.io/developer/models) and [which projects may be captured](https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/coding-agents/README.md#opt-in-only). Local storage does not make a hosted provider local.
2. For a fresh setup, follow the [upstream local daemon requirements](https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/coding-agents/README.md#local-daemon-mode), then install only the Claude Code integration:

   ```sh
   npx @vectorize-io/hindsight-coding-agents install claude-code --server daemon
   ```

   If Mirket already manages Hindsight for Codex, don't run the `npx` command above. Even with the same version pinned, it can replace the shared runtime and remove Mirket's adapters. With the recognized 0.8.6 runtime, run its already installed installer instead:

   ```sh
   node ~/.hindsight/coding-agents/dist/installer.js install claude-code
   ```

   Before starting Claude Code, set `autoUpdate: false` in the `harnesses["claude-code"]` section of `~/.hindsight/coding-agent.json` to protect the shared runtime. Set the Claude capture scope explicitly, and make sure its hooks and MCP use the existing daemon provider on cold starts. Keep the existing banks and Codex settings.
3. Start a fresh Claude Code session in an approved project. Review the installed hooks, check the Hindsight MCP connection and resolved bank, and verify that a harmless fact can be recalled in a new session. Verify Codex separately if you use both; Mirket's Codex bank routing does not apply to Claude Code.

## Other self-hosting options

| Option | Fit | Tradeoff |
| --- | --- | --- |
| **Local daemon + Codex provider** | Recommended first for one Mac and an existing Codex subscription. Local database and simple setup. | Fact extraction uses a remote model and subscription usage; provider configuration must reach the daemon. |
| **Local daemon + Ollama** | Local memory and local inference after model downloads. | Install and run Ollama and a suitable model; speed and quality depend on Mac resources and model choice. Explicitly configure the provider and model. |
| **Docker + local model** | Separate service and a portable Docker volume; can serve multiple local agents. | More infrastructure and storage. The full Apple Silicon image is roughly 3.7 GB; the LLM must run separately, for example with Ollama or llama.cpp. |
| **Docker + hosted model** | Local database with hosted inference; useful when local hardware is constrained. | Memory content sent to the model provider; API cost and credentials apply. |
| **Self-hosted server + external PostgreSQL** | Persistent shared service with separate database and backup lifecycle. | Highest operational overhead; appropriate when multiple machines or explicit database administration are needed. |

For Docker and external PostgreSQL, use Hindsight's supported [installation guide](https://hindsight.vectorize.io/developer/installation), [local-model Compose example](https://github.com/vectorize-io/hindsight/blob/main/docker/docker-compose/local-llm/README.md), and [external PostgreSQL example](https://github.com/vectorize-io/hindsight/blob/main/docker/docker-compose/external-pg/docker-compose.yaml). Connect Codex using the upstream installer with `--server self-hosted --api-url <your-server-url>`; this repository's local-daemon wrapper does not configure those alternatives.

## Project freshness and bounded recovery

The doctor now uses the pinned upstream configuration resolver rather than approximating its precedence. It reports effective MCP and hook settings separately: environment fallback, file, harness, path, and bank settings are resolved by the same runtime. Tokens are represented only by a configured/not-configured flag. The current shell plus explicit launcher settings cannot prove what a running Desktop process inherited; the fresh-host check below covers that boundary.

Rewiring preserves literal upstream hook environment assignments and MCP environment settings, including capture restrictions. It inspects the raw Codex TOML as well as the CLI's projection: upstream entries with tool restrictions, timeouts or unknown options are refused before mutation because `codex mcp add` would discard them. Already-managed entries are left intact. It also refuses disabled MCP entries, unrecognized wrappers, compound commands and conflicting routing overrides. Python 3.11+ uses its standard TOML parser; older supported Python versions use the parser already bundled in the pinned runtime through a temporary import that never runs the installer. Setup failures suppress credential-bearing command arguments and subprocess output. Existing legacy mappings for Git subdirectories and linked worktrees are canonicalized to their main project; conflicting banks fail closed. Directory-prefix mappings need explicit project mappings rather than silently selecting a new bank.

For a project already enabled by the existing capture policy, opt into a tighter freshness profile:

```sh
python3 -B memory/install.py --wire
python3 -B memory/install.py --freshness --directory /absolute/project
```

The second command changes only that project's Codex bank settings: `surveyRefreshCommits: 1`, `pageTriggerType: "auto-refresh"`, and `pageRefreshEveryTurns: 1`. It backs up the prior configuration, preserves the entire inherited bank policy, and never enables capture, session retention, Git ingestion or surveys that were disabled. It does not broaden approved paths or change another host. When source capture and surveys are already enabled, the next fresh trusted session can survey a new commit, and upstream background maintenance aligns managed page triggers to refresh after consolidation. This increases processing within the selected project; it does not promise immediate consistency or survey uncommitted work. Keep the default profile elsewhere unless the benefit warrants the cost.

Run `python3 -B memory/doctor.py --directory /absolute/project` after a fresh session. Inspect these dimensions separately:

- `effective_mcp_settings` and `effective_hook_settings`: capture, retention, automatic seeding, Git ingestion, survey cadence and page trigger configuration. `hook_mcp_differences` identifies drift; differences may be intentional but must be understood.
- `source_freshness`: current HEAD, dirty worktree, nearest **completed** survey receipt and commits behind it, plus whether that receipt carries generation timestamp evidence. Legacy receipts are reported as `legacy_receipt_only`; they are preserved, not retroactively certified. An in-progress receipt is not completion, and a clean survey cannot certify later uncommitted changes.
- `missing_primary_session_ids`: locally identified primary sessions without a retained chat document. An active chat may still be waiting for Stop; this is a coverage signal, not proof of capture failure.
- `stale_pages`, `pages_with_refresh_failure`, and `operation_health`: synthesis lag, failed refreshes, and bounded pending/processing/failed operation samples with creation ages and scheduled retry times. Attention flags distinguish pending from processing work; a zero pending count does not mean the worker is idle. A job's creation time does not establish when it failed; historical failures are not automatically current failures.

For stale or failed pages after source ingestion has drained:

```sh
python3 -B memory/doctor.py --directory /absolute/project --refresh-pages --limit 3 --wait 45
```

This explicitly submits at most three refreshes, polls for at most 45 seconds between bounded API calls, and reports operation IDs and actual statuses. Limits are capped at five pages and 55 seconds. Existing content remains protected by the server's refresh behavior; the command never deletes pages, changes source scope, changes triggers, replays transcripts or retries indefinitely. Before submitting, it checks pending and processing operations separately and refuses to add work while either is active or its state cannot be established. This is a point-in-time check, not a lock against new background work. Inspect reported operation details and rerun the doctor before another batch. A successful page refresh cannot recover a transcript or source finding that was never ingested.

A fresh page timestamp does not establish that its content reflects the latest facts. Check that relevant retained facts are retrievable under the page's filters: a general correction can lack the `knowledge:feature-work` tag used by initiative pages. For material changes to an existing initiative, use the supported `hindsight_capture_initiative` update with its existing `relates_to_page_id`, then verify the retained facts and their retrieval before accepting the refreshed page. Do not create duplicate initiatives or widen page filters to hide a coverage gap.

If full refresh still presents superseded architecture as current, review the page's synthesis query rather than repeating refreshes blindly. Test a narrowly scoped supported query update, preserving the page ID, filters, trigger and generated-history records, and inspect the resulting content. When automatic seeding runs at SessionStart, seeded queries are synchronized: a durable override must also be recorded in the effective host's project-bank configuration under `pages["Component map"].source_query` (or the relevant seeded page name). Back up configuration first, preserve existing effective page overrides, and verify resolution in both MCP and hook contexts; a harness-level bank section can shadow the same bank’s top-level settings. Prefer guidance that compares the latest verified inventory with historical evidence, without permanently pinning a version. Re-seed idempotently and confirm the query survives without adding pages or changing capture policy.

For a missing chat, first verify its session ID and project against the local transcript metadata. From that project, use `codex resume <verified-session-id>`, complete a harmless turn, and allow its real Stop hook to run. Recheck coverage and retrieve the remembered fact from a separate fresh session. Do not manufacture a Stop event or manually ingest a canary to claim host capture worked. Archived history that the host cannot resume needs a separately reviewed import; preserve originals and skip already retained IDs.

For a missing or lagging survey, inspect effective `autoSeed`, `codebaseSurvey`, `surveyRefreshCommits`, pending operations and hook wiring. With the project freshness profile and eligible committed source, start a fresh trusted host session and allow upstream's bounded survey to finish. If capture or surveys are deliberately disabled, report that policy rather than overriding it. Do not delete survey receipts, banks or legacy history to force a refresh. Use current files and transcripts for fresh decisions while background consolidation catches up.

The generation check fails closed when document metadata is unavailable, a retry changes the pending receipt, or unchanged-content retention does not advance a finding's timestamp. That condition requires direct review of source and survey output; old identical documents are not silently promoted to proof of a new survey. Generation timestamps establish refreshed source documents, not extraction completion, page correctness or host capture.

### Real host capture acceptance

Record a unique harmless decision in a normal session within an approved project. Let that turn finish through the host's real Stop event. Within five minutes, confirm that the bank contains the chat document for that session, then open a separate fresh session and retrieve the decision with its chat provenance. Repeat in a linked worktree and confirm an unrelated project cannot retrieve it. Record elapsed time, document/session identity, retrieval evidence and any pending operation or trust blocker. Manual document ingestion, a synthetic hook call, page refresh, and a healthy daemon are not substitutes for this test. If the five-minute expectation is missed, record a failure or pending condition rather than asserting readiness.

### Verification commands

```sh
python3 -B -m unittest discover -s memory
MIRKET_TEST_RUNTIME="$HOME/.hindsight/coding-agents" python3 -B -m unittest discover -s memory
```

The second command adds a real pinned-runtime configuration parity check in a disposable directory. It imports the generated adapter without starting MCP, a daemon, capture, or network activity. It verifies environment/file/harness/path/bank precedence and secret redaction. The installer packages this adapter alongside its survey adapters; a missing or incompatible adapter stops diagnostics and requests rewiring.
