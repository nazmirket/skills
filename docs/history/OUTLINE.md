> Historical record from the initial catalog design. It describes the project at that time; see the [current README](../../README.md) for the maintained catalog.

# Draft outline: your native skill collection

Status: independently reviewed proposal. This roadmap is a proposal, not a commitment to recreate Mirket.

## Objective and constraints

Author original, reusable workflows inspired by the parent responsibilities in Mirket. Maintain a single shared set of skill files with separate Codex and Claude Code marketplace metadata. The existing Mirket repository remains unchanged. Begin with a fresh starter, not copied skill text, executable hooks, or a full production catalog.

## Proposed steps

1. Decide the collection name, intended users and primary jobs. Review the mapping in PARENT-REVIEW.md; choose your first useful workflow and intended boundaries.
2. Capture three real prompts, expected outcomes and a counterexample. Run a baseline without the new skill, recording relevant gaps.
3. Author one original SKILL.md from templates/skill-template.md. Use concrete triggers, steps and observable completion criteria; add references only when necessary. Keep a source and license record for any actual adaptations.
4. Evaluate that skill in clean Codex and Claude Code sessions: explicit and natural invocation, negative triggers, useful task behavior, and missing capabilities. Record failures and revise; do not claim behavioral reliability from metadata validation.
5. Repeat one skill at a time. Introduce a router, shared policy, independent review, plan persistence, hooks, or additional plugins only after a demonstrated need; make host-specific behavior explicit.
6. Choose names, ownership, a license and distribution repository; validate both descriptors, test local installation in each host, then configure or publish the marketplace when desired. This starter does not register or publish anything.

## Candidate starter

One plugin folder owns `skills/` and an OpenAI portable root `plugin.json`, plus a Claude `.claude-plugin/plugin.json`; the marketplace root contains `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`. Both entries point to the same plugin directory. A blank template stays outside `skills/` until a skill has a real name and behavior. An empty `.gitkeep` preserves the skills directory in Git. The starter contains no active skill and has not been installed or behavior-tested. README explains host-specific validation, discovery, installation, new sessions, refresh/cache behavior, limits, and what still needs testing. Keep planning records outside the distributable plugin.

## Acceptance checks

- All 18 parents are individually mapped with recommended action and relationship to other parents.
- Source-inspired ideas are distinct from copied content; retain license/provenance requirements if copying later.
- Both marketplace files parse and their sources resolve inside the root; plugin identities match; Claude validation runs if available.
- Local install and invocation in both hosts remain explicitly unverified until actually tested.
- Original repository is not changed.
