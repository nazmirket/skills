# LLDB

Identify the target binary, build configuration, architecture, SDK or OS, symbols and source revision. Prefer a local reproduction or authorized crash artifact to attaching to a shared process; attaching, stepping or pausing can change service timing.

- Make frame and symbol evidence reliable first. Verify the loaded module and matching debug symbols, including the dSYM and UUID where applicable. Preserve the crashing build's symbols. A nearby source checkout or a binary rebuilt with different flags may give misleading lines and variable values.
- For a crash, inspect the stop reason, selected thread and stack. Use `thread backtrace all` when other threads may explain a wait or deadlock. Select the first relevant application frame and inspect its inputs and dependencies using `frame variable`. Evaluating an expression can call code in the target; prefer passive inspection until changing execution is intentional.
- For a repeatable failure, start with a narrow breakpoint near the first divergence. Check that it resolves against the loaded module. Use a watchpoint when a stable address and a specific unexpected write are in question; verify that it still refers to the intended object and account for hardware limits.
- Do not infer production timing from stepped execution. Use representative optimized builds and a platform profiler for performance. Use the debugger to explain a suspected path or state, then verify the original case without the debugger.

After an authorized fix, check the original input and relevant neighboring behavior. Report the exact symbolized frame, input or ownership boundary and what the rerun established. Treat crash dumps, arguments, and memory views as sensitive.
