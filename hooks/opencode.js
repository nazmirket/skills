import { execFile } from "node:child_process";
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const skillsDirectory = fileURLToPath(new URL("../skills/", import.meta.url));

function loadSkills() {
  return readdirSync(skillsDirectory, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map(({ name: id }) => {
      const path = join(skillsDirectory, id, "SKILL.md");
      const source = readFileSync(path, "utf8");
      const header = /^---\r?\n([\s\S]*?)\r?\n---\r?\n/.exec(source);
      const name = header?.[1].match(/^name: ([a-z0-9-]+)\r?$/m)?.[1];
      const description = header?.[1].match(/^description: ("[^"\r\n]+")\r?$/m)?.[1];
      if (name !== id || !description) throw new Error(`Invalid Mirket skill metadata in ${path}`);
      return { id, name, description: JSON.parse(description), path, content: source.slice(header[0].length).trimStart() };
    });
}

function runHook(script, payload) {
  const path = fileURLToPath(new URL(script, import.meta.url));
  return new Promise((resolve, reject) => {
    const child = execFile("python3", ["-I", path], { timeout: 5000 }, (error, stdout) => {
      if (error) {
        reject(new Error(`Mirket could not run ${script}. Check that Python 3.8 or later is available to OpenCode.`));
        return;
      }
      try {
        resolve(JSON.parse(stdout));
      } catch {
        reject(new Error(`Mirket received invalid output from ${script}.`));
      }
    });
    // The process callback reports spawn failures, including a closed stdin.
    child.stdin.on("error", () => {});
    child.stdin.end(JSON.stringify(payload));
  });
}

export default {
  id: "mirket",
  async setup({ skill, session, tool }) {
    const catalog = loadSkills();
    const startup = await runHook("execute.py", { hook_event_name: "SessionStart" })
      .then((result) => result.hookSpecificOutput.additionalContext, (error) => error.message);

    await skill.transform((editor) => {
      for (const entry of catalog) {
        if (!editor.get(entry.id)) editor.add(entry);
      }
    });
    await session.hook("context", (event) => {
      event.system.push({ type: "text", text: startup });
    });

    await tool.transform((editor) => {
      editor.update("shell", (shell) => {
        const execute = shell.execute;
        shell.execute = async (input, context) => {
          const { hookSpecificOutput, systemMessage } = await runHook("cleanup.py", {
            hook_event_name: "PreToolUse",
            tool_name: "Bash",
            tool_input: input,
          });
          if (hookSpecificOutput?.permissionDecision === "deny") {
            throw new Error(hookSpecificOutput.permissionDecisionReason);
          }
          const result = await execute(input, context);
          if (!systemMessage) return result;

          const content = typeof result.content === "string"
            ? [{ type: "text", text: result.content }]
            : (result.content ?? []);
          return { ...result, content: [...content, { type: "text", text: systemMessage }] };
        };
      });
    });
  },
};
