# Mirket

<img src="website/public/mirket-sprite.png" alt="Mirket, the pixel-art meerkat mascot" width="64" height="64">

Mirket is a free collection of reusable skills for **Codex** and **Claude Code**. Use it to plan changes, debug failures, review code, design interfaces, and hand work off with enough context to resume.

Read the [documentation](docs/README.md) for the skills, philosophy, and plugin architecture.

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

### Optional: local Hindsight

Mirket works without Hindsight. The [Codex setup prompt](docs/README.md#codex-setup-prompt) and [Claude Code setup prompt](docs/README.md#claude-code-setup-prompt) ask whether you want local Hindsight or Mirket only. They wait for an explicit yes before changing Hindsight.

For manual setup, follow [Mirket's guarded Codex installer](memory/README.md#recommended-local-daemon) or [Hindsight's upstream Claude Code installer](memory/README.md#claude-code-with-the-upstream-installer). Review your provider, capture scope, and any existing Hindsight installation first.

## Try it

Ask for the result you want, or name a skill:

- “Use Mirket Plan to outline this change and how we’ll verify it.”
- “Use Mirket Debug to reproduce this failure and find its cause.”
- “Use Mirket Audit to review this patch and report findings.”

The [routing guide](plugins/mirket/references/routing.md) helps you pick a workflow. You can also [browse all skills](plugins/mirket/skills/).

If you want Mirket to guide work by default, merge the [Codex instructions](instructions/AGENTS.md) into `~/.codex/AGENTS.md` or the [Claude Code instructions](instructions/CLAUDE.md) into `~/.claude/CLAUDE.md`.

## Mirket in practice

![The Mirket loop: name the outcome, pick a skill, make and verify, and report the change.](docs/diagrams/mirket-loop.svg)

![Building a site with Mirket: Plan sets the direction, Design shapes the page, Test checks the result, and Distill shares what changed.](docs/diagrams/build-a-site.svg)

## License

[MIT](LICENSE). Anyone can use, modify, and redistribute Mirket, including commercially, as long as the license and copyright notices are retained.

[Contributing and testing](CONTRIBUTING.md)
