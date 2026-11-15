# Install Mirket in other agents

Use Mirket's Markdown skills in [Cursor](#cursor), [Pi](#pi), [Oh My Pi](#oh-my-pi), [GitHub Copilot](#github-copilot), [Google Antigravity](#google-antigravity), [OpenCode](#opencode), [Hermes Agent](#hermes-agent), or [Muse Code](#muse-code).

These installs make the catalog available inside one project. They do not install Mirket's lifecycle hooks, commit guard, or global instructions. Use the [native plugins](README.md#install-mirket) for Codex and Claude Code.

## Install the shared catalog

From your project root, run:

```sh
npx skills add nazmirket/skills --skill '*' --agent universal
```

The [skills installer](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) uses Node.js and npm. Its [Universal target](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) installs to `.agents/skills/`, which all eight agents can discover. Install the full catalog so links between skills resolve.

## Verify in your agent

Open the project in a fresh session and confirm the host can discover the `adapt` skill at `.agents/skills/adapt/SKILL.md`. Ask for a read-only orientation using it and check that the agent can follow one of its relative references. Prefer the project copy if discovery shows multiple skills with the same name.

### Cursor

Open the project and check **Customize → Skills**. The project skill should appear in **Agent Decides**. Follow the [Cursor skill discovery guide](https://cursor.com/docs/skills#skill-directories) for remote sessions.

### Pi

Start Pi from the project and invoke `/skill:adapt`. See [Pi skill discovery and invocation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md).

### Oh My Pi

From the project, run `omp skill list --json` and find the project path for `adapt`. With interactive skill commands enabled, use `/skill:adapt`. See the [Oh My Pi skill guide](https://github.com/can1357/oh-my-pi/blob/main/docs/skills.md) and its [Agents discovery provider](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/src/discovery/agents.ts).

### GitHub Copilot

In the Copilot CLI, check `copilot skill list` from the repository. For an existing CLI session, use `/skills reload`. In a remote or cloud agent, the project files must be present in the checkout it sees. See [Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) and [Copilot project skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

### Google Antigravity

Start from the workspace root. Check the app's **Customizations → Skills** or run `/skills` in the CLI. The current workspace path also works in the Antigravity IDE. See [Antigravity skill locations](https://antigravity.google/docs/skills) and [discovery troubleshooting](https://antigravity.google/docs/customization-discovery/).

### OpenCode

OpenCode searches `.agents/skills/` as a project compatibility location. Ask OpenCode to load the skill ID `adapt` with its `skill` tool and confirm it can see the project copy. See [OpenCode skill discovery and permissions](https://opencode.ai/docs/skills/).

### Hermes Agent

Use a Git checkout: Hermes resolves project skills relative to its Git root. After reviewing the workspace, run `hermes skills trust` from that checkout if you want to enable its project skills. Start a new session and run `hermes skills list` to confirm the project entry. See [Hermes project-local skills and trust](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#project-local-skills).

### Muse Code

For Meta's Muse Code, open a trusted Git project and run `muse skills list` or `muse skills inspect adapt` from its root. Confirm the listed source is the project instead of a built-in or personal skill. See [Muse Code skill discovery](https://dev.meta.ai/docs/muse-code/extending#skills).

## Update or remove the catalog

Use the installer's [update and removal commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-update). Restart your agent after changes.
