# Plan (draft; execution authorized)

1. Harden the staged-index hook against ambiguous target directories and keep explicitly recognized dry runs neutral. Default Stop to no continuation; retain one combined Distill/Clean pass only when enabled and the shared loop guard permits it.
2. Surface the routing guide in the session hook and key skill entry points. Clarify read-only routing, bounded root integration, and repository ADR conventions; initialize this repository's ADR location for the Git-target decision.
3. Add meaningful hook regressions, package link/discovery checks, and a fresh-session smoke matrix for both hosts. Run repository checks, the static website build, and a scoped cleanup review. Report installed-host behavior only when exercised.

## Current status

Implemented in the working tree. The regression suite reproduced the target, preview, and Stop issues before the fix. Final checks: 33 plugin tests, 30 memory tests, static site build, SEO checks, and Git whitespace check passed. Claude plugin and marketplace validation passed with unchanged metadata warnings; strict validation flags those warnings. The fresh-session smoke checklist was not run in installed hosts. No commit, install, or deployment was performed.
