import assert from 'node:assert/strict';
import test from 'node:test';
import plugin from '../hooks/opencode.js';

async function host(entries = []) {
  const skills = new Map(entries.map(entry => [entry.id, entry]));
  const calls = [];
  const shell = { execute: async (input, context) => {
    calls.push([input, context]);
    return { content: 'result' };
  } };
  let contextHook;
  await plugin.setup({
    skill: { transform: register => register({ get: id => skills.get(id), add: entry => {
      assert.ok(!skills.has(entry.id));
      skills.set(entry.id, entry);
    } }) },
    session: { hook: (event, callback) => { assert.equal(event, 'context'); contextHook = callback; } },
    tool: { transform: register => register({ update: (id, wrap) => { assert.equal(id, 'shell'); wrap(shell); } }) },
  });
  const event = { system: [] };
  contextHook(event);
  return { skills, startup: event.system[0].text, shell, calls };
}

test('default and occupied IDs resolve to the installed Execute in session context', async () => {
  const normal = await host();
  assert.equal(normal.skills.size, 20);
  assert.ok(normal.startup.includes('`execute`'));
  const prior = ['execute', 'mirket-execute'].map(id => ({ id, path: `/other/${id}/SKILL.md` }));
  const { skills, startup } = await host(prior);
  for (const entry of prior) assert.equal(skills.get(entry.id), entry);
  const id = 'mirket-mirket-execute';
  assert.ok(startup.includes(`\`${id}\``));
  assert.equal(skills.get(id).path, normal.skills.get('execute').path);
  assert.ok(startup.includes(skills.get(id).path));
});

test('denied commit does not reach the shell; warnings preserve the shell response', async () => {
  const { shell, calls } = await host();
  await assert.rejects(shell.execute({ command: 'git commit -m example' }, {}), /Before committing/);
  assert.equal(calls.length, 0);
  const result = await shell.execute({ command: "echo 'unfinished" }, {});
  assert.equal(result.content[0].text, 'result');
  assert.match(result.content[1].text, /could not parse/);
});

test('ordinary reads still work without Python; ambiguous commands and guarded commits stop', async t => {
  const path = process.env.PATH;
  t.after(() => { process.env.PATH = path; });
  process.env.PATH = '/missing-mirket-test-interpreter';
  const { shell, calls } = await host();
  const input = { command: 'pwd' };
  const ctx = { marker: 1 };
  assert.deepEqual(await shell.execute(input, ctx), { content: 'result' });
  for (const command of ['git commit -m example', 'pwd && git status', 'git status\nls']) {
    await assert.rejects(shell.execute({ command }, ctx), /could not run cleanup.py/);
  }
  assert.deepEqual(calls, [[input, ctx]]);
});
