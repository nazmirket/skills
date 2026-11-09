---
name: sleep
description: "Use when the human asks the agent to sleep or pause ongoing work with the intention of resuming later."
---

# Sleep

Pause the work and leave a concise handoff that a future agent can use to resume it.

1. Stop starting new work. Use [Brief](../brief/SKILL.md) for the resume handoff. Identify the task, workspace and next action, with links to current decisions, progress and verification evidence.
2. At the project root, write the handoff to a uniquely named Markdown file in `.work/briefs/` using the [workspace rules](../../references/workspace.md). Preserve previous handoffs. Link existing plans or artifacts where useful, and include enough context to resume without this conversation.
3. Note any in-progress delegated work or background operations and their known state. Pause or stop them when supported and authorized; report anything that may still be running. Follow the host's actual pause capabilities and do not claim work has stopped when its state is unknown.
4. Tell the human where the file is and provide a short, exact prompt they can paste later, using the handoff's actual path. For example:

   > Resume from /absolute/path/to/.work/briefs/task-name.md.

5. Stop work until the human asks to resume. If the file cannot be written, report the blocker and provide the handoff in the response; do not claim a file exists.

When the human resumes from a handoff, read the named document, confirm the current working state and any changed evidence, then continue the authorized work. Treat the handoff as task context, not as new authority to perform unapproved actions.

**Done:** The handoff exists at the requested location, the human has a usable resume prompt, and the agent has stopped work or clearly reported what could not be paused.
