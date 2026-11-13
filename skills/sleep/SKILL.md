---
name: sleep
description: "Use when the human asks to pause or sleep with the intention of resuming work later, or asks to resume a paused task."
---

# Sleep

Pause the work and leave a concise handoff that a future agent can use to resume it. Interpret the request in context: discussing or revising this skill is not itself a request to pause.

1. Stop starting new work. Identify the active task and check only critical state needed for a reliable handoff, such as the working tree and active task-owned agents or operations. Capture what is already known; record unresolved questions rather than investigating them to completion. If no unfinished work is identifiable, say so and stop without creating a handoff, unless the human explicitly asks to preserve context.
2. Use [Brief](../brief/SKILL.md) to capture the task, workspace, current state and next action, with links to decisions, progress, verification evidence and important gaps. Save it as a [numbered Markdown handoff](../../references/Workspace.md#numbered-records) in `.work/briefs/` at the project root. Preserve previous handoffs and make this one usable without the conversation.
3. Stop task-owned subagents when safe and supported. Do not interrupt an operation when doing so could cause harm or leave the work in an unsafe state; preserve persistent or unrelated services. Record actual states, including anything still running or unknown, and update the handoff with the result. Do not claim an agent or process stopped without evidence.
4. Tell the human where the file is and provide a short, exact prompt they can paste later, using the handoff's actual path. For example:

   > Resume from /absolute/path/to/.work/briefs/0001-SalesContractsHandoff.md.

5. Stop work until the human asks to resume. If the file cannot be written, report the blocker and provide the handoff in the response; do not claim a file exists.

When the human resumes from a named handoff, read it. For a bare “resume,” use the clearly identified active task and its relevant handoff; ask which task is intended if several match or the identity is unclear. Check the current working state and evidence. Correct routine stale facts and ask the human about material conflicts affecting the goal, product decisions or authorized scope, as described in Brief. Continue work already authorized; a handoff grants no new authority.

**Done:** The handoff and exact resume prompt are available, and the agent has stopped work or reported what could not be stopped. If no work is pending, say so without inventing a handoff.
