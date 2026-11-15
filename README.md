# Mirket

<img src="website/public/mirket-sprite.png" alt="Mirket, the pixel-art meerkat mascot" width="64" height="64">

Mirket is a free collection of **20 reusable skills** for **Codex** and **Claude Code**. Research markets, shape products, plan and build changes, verify results, and release and operate services.

Visit [skills.mirket.dev](https://skills.mirket.dev) for installation and workflow examples. Read the [repository documentation](docs/README.md) for the skills, philosophy, and plugin architecture.

## Install

**Codex**

```sh
codex plugin marketplace add https://github.com/nazmirket/skills.git
codex plugin add mirket@mirket
```

**Claude Code**

```sh
claude plugin marketplace add nazmirket/skills
claude plugin install mirket@mirket
```

Start a fresh session after installing. If your host asks you to trust hooks, review them first. See [hook requirements and behavior](CONTRIBUTING.md#lifecycle-hooks).

For Cursor, Pi, Oh My Pi, GitHub Copilot, Google Antigravity, OpenCode, Hermes Agent, or Muse Code, follow the [skills-only installation guide](docs/OtherAgents.md).

## Try it

Ask for the result you want, or name a skill:

- “Use Mirket Plan to outline this change and how we’ll verify it.”
- “Use Mirket Market to define our brand voice and check it against our onboarding copy.”
- “Use Mirket Ship to compare these product opportunities and propose what to test first.”
- “Use Mirket Code to review the React state model and the Next.js server boundary.”
- “Use Mirket Debug to reproduce this failure and find its cause.”
- “Use Mirket Audit to review this patch and report findings.”
- “Prepare this versioned artifact, then use Mirket Deploy to roll it out to staging.”
- “Use Mirket Deploy to check whether this service is healthy and its data is current.”

The [routing guide](skills/execute/references/Routing.md) helps you pick a workflow. You can also [browse all skills](skills/).

If you want Mirket to guide work by default, merge the [Codex instructions](instructions/AGENTS.md) into `~/.codex/AGENTS.md` or the [Claude Code instructions](instructions/CLAUDE.md) into `~/.claude/CLAUDE.md`.

## Mirket in practice

![One skill owns the result. Bring in another only when it answers a distinct question. The human decides changes in scope. The agent reports what changed and what its checks proved.](docs/diagrams/mirket-loop.svg)

![Illustrative run: Debug traces a slow CSV export to repeated queries, Code supplies SQL guidance, and Test checks that the same fixture finishes within its timeout and the output is unchanged.](docs/diagrams/debug-with-evidence.svg)

## License

[MIT](LICENSE). Anyone can use, modify, and redistribute Mirket, including commercially, as long as the license and copyright notices are retained.

[Contributing and testing](CONTRIBUTING.md)
