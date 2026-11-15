# Git and GitHub code review

Pin the base and head commits, or the staged snapshot for a local review. Use the project’s intended comparison: a pull request usually shows the change since the branches diverged, while comparing two endpoint trees answers a different question. Review the actual revision tested in CI.

- Start with the changed paths and then read the relevant callers, data contracts and tests. Follow renamed or generated files back to their maintained source. Compare the behavior before and after; do not report an unchanged issue as a new regression unless the change exposes it or makes it worse.
- Separate an issue that blocks approval from a meaningful suggestion. Point to the line or smallest relevant range and explain the condition, consequence and next step. Tie test evidence to the same revision and distinguish a check that ran from one merely present in code.
- Recheck the head before relying on a review, approval or stale comment. Reuse evidence for unchanged paths when the integration conditions hold; revisit changed boundaries and the relevant checks. Treat formatted, whitespace-ignored or collapsed diffs as aids, not complete coverage when syntax or generated output carries meaning.
- Review untrusted changes without running their scripts by default. Draft comments locally unless posting was authorized. GitHub review submission, approval and requesting changes are separate actions from reading a pull request.

Return the revision, material findings with evidence, and any coverage limits. Preserve the review gate required by Audit.

Upstream: [Git diff](https://git-scm.com/docs/git-diff), [GitHub pull request reviews](https://docs.github.com/en/pull-requests/reference/pull-request-reviews).
