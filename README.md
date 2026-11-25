# Mirket Skills

<img src="website/public/mirket-sprite.png" alt="Mirket, the pixel-art meerkat mascot" width="64" height="64">

Mirket is an open-source collection of reusable workflows for **Codex**, **Claude Code**, and **OpenCode**. Each skill tells your agent what to inspect, when to ask you for a decision, and how to verify the result. Use it to research a market, plan a change, diagnose a bug, or ship and operate a service.

[Browse the skills](https://skills.mirket.dev/#skills) · [Documentation](docs/README.md) · [Routing guide](skills/execute/references/Routing.md)

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

**OpenCode 2.4.1+**

```sh
opencode plugin add github:nazmirket/skills
```

Start a fresh session after installing. If your agent asks you to trust hooks, [review what they do](CONTRIBUTING.md#lifecycle-hooks) first. For Cursor, GitHub Copilot, and other hosts, see the [skills-only installation guide](docs/OtherAgents.md).

## Try it

Ask for the result you want, or name a skill directly:

- “This test is failing. Find the cause and verify the fix.”
- “Use Mirket Plan to outline this change and how we’ll verify it.”

To use Mirket by default, merge the [Codex instructions](instructions/AGENTS.md) into `~/.codex/AGENTS.md` or the [Claude Code instructions](instructions/CLAUDE.md) into `~/.claude/CLAUDE.md`.

![One skill owns the result. Another helps when it answers a distinct question. The human decides changes in scope, and the agent reports what its checks proved.](docs/diagrams/mirket-loop.svg)

See an [example debugging workflow](docs/diagrams/debug-with-evidence.svg) from first report to verified fix.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) to improve a skill or run the package checks. Mirket is available under the [MIT license](LICENSE).
