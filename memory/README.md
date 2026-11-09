# Hindsight for Codex

This directory contains setup guidance and a guarded installer. Hindsight installs its own runtime, configuration and memory data in its normal user-level locations; this repository is not the memory store. No installation happens until you run the installer.

## Recommended: local daemon

This setup uses Hindsight's coding-agents integration and a local daemon. The upstream installer configures Codex hooks and MCP. Default routing uses the project name, so unrelated repositories with the same name can share a bank unless explicitly mapped. The daemon starts on demand and keeps running until stopped. The first start downloads its package and models and may not be ready for the first turn or two.

You need Python 3, Node.js and npm/npx, Codex, `uvx` (from `uv`), and a current Rust toolchain on macOS. Install missing tools using their official guidance: [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Rust](https://www.rust-lang.org/tools/install). This installer does not install prerequisites or change model providers for you.

Choose the LLM deliberately. Hindsight supports your Codex subscription (`openai-codex`), local models such as Ollama, and other providers. Local memory storage does not make a remote provider local. A local model must already be running and configured; Codex provider requests use your subscription and send context to OpenAI. See [Hindsight model configuration](https://hindsight.vectorize.io/developer/models).

For example, after signing in to the Codex CLI, select the Codex provider in the shell that runs setup:

```sh
export HINDSIGHT_API_LLM_PROVIDER=openai-codex
python3 memory/install.py --check
python3 memory/install.py
```

Run these commands from the repository root. `--check` is read-only; actual installation downloads the pinned coding-agents package and updates user-level Codex hooks, MCP configuration and Hindsight settings. The wrapper stops if dependencies are missing, no provider is selected, Hindsight already has relevant configuration or a Codex MCP registration, an alternate Hindsight or Codex configuration path is set, an existing Codex hooks file has an invalid structure, or a service is already listening on the daemon's default port. Review existing installations using the [upstream instructions](https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/coding-agents/README.md) rather than deleting or replacing them.

The provider selected for installation must also be available to the environment that starts future hooks. An export in your terminal does **not** automatically configure a separately launched Codex Desktop app, and Hindsight may otherwise detect a different configured provider. For the CLI, launch Codex from the same configured shell. For Desktop, arrange for the app's hook environment to receive your selected provider and prerequisites, or start a separately configured Hindsight server and use the upstream self-hosted setup. Verify this in the actual host before relying on memory. This repository does not modify your shell, desktop environment, existing secrets, or login settings.

After installation:

1. Restart Codex, review and trust the hooks as required by your host, and check `codex features list` for the `hooks` feature. If needed, use `codex features enable hooks` deliberately; see [Codex hooks](https://learn.chatgpt.com/docs/hooks).
2. Use a test project to record a harmless decision, start a fresh session, and check that it is recalled. Inspect Hindsight's logs and the daemon if it is not. This is a host integration check, separate from testing Mirket's skills.
3. Inspect Hindsight's configuration and data locations before backing up or deleting anything. Follow [coding-agents documentation](https://github.com/vectorize-io/hindsight/blob/main/hindsight-integrations/coding-agents/README.md) and [embedded daemon documentation](https://github.com/vectorize-io/hindsight/blob/main/hindsight-embed/README.md).

Hindsight automatically checks for runtime updates by default, and model downloads may occur later; the installer's package version does not pin those downloads. Set `autoUpdate` to `false` in Hindsight's configuration if you prefer to manage updates. Hindsight retains session conversations and ingests repository commit messages by default. Model processing may use subscription limits or API credits, and captured content can be sent to whichever model provider you select. Inherited `HINDSIGHT_API_*` settings can also redirect storage or other processing: review them before starting the daemon if data locality matters.

## Directory-based memory registry

The installer above does not configure directory-based isolation. The registry below is an optional integration component; its behavior applies only after it has been wired into the matching Codex hooks and MCP configuration and verified in a fresh session.

The Codex-specific [project registry](project_registry.py) can route each Hindsight hook and MCP session to the bank assigned to its canonical project root. It records local paths and bank identifiers in `~/.hindsight/mirket/projects.json`, without conversation text. Existing explicitly mapped project banks are preserved. Separate Git repositories with the same name receive different banks; subdirectories and linked worktrees use the same bank as their Git project. For a Git repository with a separate Git directory, the shared Git metadata directory is its stable identity. Non-Git sessions use their starting directory.

Hindsight's MCP server resolves its bank at session startup. Start a new Codex session when switching projects; if a hook detects a change to another project in the same session it skips memory rather than mixing banks. The registry applies to Codex only. Other agent integrations need equivalent routing before their cross-agent bank sharing is reliable.

The wrapper requires Hindsight coding-agents 0.8.6 and disables automatic updates for Codex. A runtime upgrade or reinstall needs review and may overwrite the wrapper's hook and MCP registrations; changed hooks also need trust review. Existing banks and global path mappings remain intact. `project_registry.py` is an integration component, not a standalone installer; installing it without the matching Codex hook, MCP, and Hindsight configuration would not enable isolation.

## Other self-hosting options

| Option | Fit | Tradeoff |
| --- | --- | --- |
| **Local daemon + Codex provider** | Recommended first for one Mac and an existing Codex subscription. Local database and simple setup. | Fact extraction uses a remote model and subscription usage; provider configuration must reach the daemon. |
| **Local daemon + Ollama** | Local memory and local inference after model downloads. | Install and run Ollama and a suitable model; speed and quality depend on Mac resources and model choice. Explicitly configure the provider and model. |
| **Docker + local model** | Separate service and a portable Docker volume; can serve multiple local agents. | More infrastructure and storage. The full Apple Silicon image is roughly 3.7 GB; the LLM must run separately, for example with Ollama or llama.cpp. |
| **Docker + hosted model** | Local database with hosted inference; useful when local hardware is constrained. | Memory content sent to the model provider; API cost and credentials apply. |
| **Self-hosted server + external PostgreSQL** | Persistent shared service with separate database and backup lifecycle. | Highest operational overhead; appropriate when multiple machines or explicit database administration are needed. |

For Docker and external PostgreSQL, use Hindsight's supported [installation guide](https://hindsight.vectorize.io/developer/installation), [local-model Compose example](https://github.com/vectorize-io/hindsight/blob/main/docker/docker-compose/local-llm/README.md), and [external PostgreSQL example](https://github.com/vectorize-io/hindsight/blob/main/docker/docker-compose/external-pg/docker-compose.yaml). Connect Codex using the upstream installer with `--server self-hosted --api-url <your-server-url>`; this repository's local-daemon wrapper does not configure those alternatives.
