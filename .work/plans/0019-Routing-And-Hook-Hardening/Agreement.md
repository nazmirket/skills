# Agreement

The human authorized implementing all findings from the preceding review and explicitly chose docs/decisions as the fallback ADR location. The two independent Astra High reviews are evidence for the findings, not approval of this written execution plan.

Keep the shared hook portable by requiring a first absolute, literal Git -C target on both hosts. The alternative of trusting session cwd is unsafe for Codex; inferring the host from incidental environment variables would add uncertainty. Use opt-in final continuation rather than parsing transcripts. Preserve Git guard scope, exact exceptions, and authorization boundaries. No release, installation, deployment, or remote change is part of this request.

Independent draft review: the original Astra High hook reviewer found no blocker. The implementation parses dry-run options and their negation without treating option values as flags, keeps compound commands from borrowing a preview exemption, and treats unset or invalid opt-in as neutral. The host smoke checklist and contributor guidance distinguish synthetic tests from live behavior.
