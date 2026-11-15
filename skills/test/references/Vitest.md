# Vitest

Confirm the configured project, module aliases, Vite/Vitest version, environment, setup files and CI command. Choose Node for pure logic, the configured DOM environment for suitable component tests, and Browser Mode or a browser runner when real browser behavior is the claim.

- Test through a public function, rendered interaction, or supported boundary. Keep fixture values close to the behavior they establish. Mock I/O or an expensive boundary only when appropriate; a mock of the implementation cannot establish that the real adapter works.
- Check how the installed runner transforms ESM and hoists `vi.mock`. Imports evaluated in shared setup can already be cached. Make the mocked dependencies and their lifetime explicit; reset or restore only the state your tests own. Use fake timers only for time-based behavior, and await resulting promises rather than assuming the timer advanced all async work.
- Isolate tests that share globals, modules or backend data. Avoid disabling worker isolation or switching the pool before identifying a bottleneck. Measure configuration, transforms, setup and test time under the actual command; scope unnecessary setup before raising parallelism. Compare single-run and watch timing separately.
- Use the intended project and environment to run a focused test. For a regression, record the intended assertion failure on the old code and the pass on the fix. Run the broader configured check if there are shared setup or cross-project effects.

Report the project, environment, relevant fixture or mock and expected versus actual behavior. A DOM simulation or mock that makes a focused check faster does not prove the full browser or integration path.

Upstream: [Improving performance](https://vitest.dev/guide/improving-performance), [Mocking modules](https://vitest.dev/guide/mocking/modules), [Browser Mode](https://vitest.dev/guide/browser/).
