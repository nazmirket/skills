# Root skills catalog

## Outcome

Canonical skill definitions live at repository root `skills/`. Codex, Claude Code and the website use that catalog. Existing install IDs, skill workflows, hooks and public URLs stay intact. No additional targets or rollout in this task.

## Agreement

The user authorized implementing the refactor directly. The candidate is to make the repository itself the shared package root while keeping separate host manifests and portable sibling references. Probe this before moving files: a nested package pointing to `../` cannot count on host validation or cache copying; generated duplicate trees would add a sync step. This is an execution record, not a separately approved written plan.

## Plan

1. Probe marketplace installation and discovery using an isolated copy, preserving the compatibility manifest layout.
2. Move the catalog and runtime resources needed for relative references. Update marketplace wiring, tests, documentation and the website source reader/link mapping.
3. Check the installed catalog and hooks, local test suite, generated diagrams and site export. Check rendered links and confirm no stale paths or unrelated edits.

## Current status

Implemented in the working tree. Isolated installs on Codex CLI 0.167.0 and Claude Code 2.1.323 reported 25 skills and four hooks each. Codex hooks were untrusted; no live host behavior was exercised. Claude validation passed with advisory metadata warnings. All 41 unit tests, site build, diagram generation, discovery checks, exported skill link checks and representative desktop/mobile docs checks passed. The package wiring tests were rerun after adding the ADR. No release or deployment was performed.
