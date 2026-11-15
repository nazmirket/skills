# GDB

Confirm the runnable target or core dump, architecture, executable, dependent libraries, debug packages and source revision. Prefer a local reproduction or an approved dump to attaching to a shared process.

- Check that the binary and symbols came from the same build, and that debug files for relevant libraries are loaded. Establish which values and frames are trustworthy in an optimized build. An optimized-out variable can be unavailable even when symbols are correct; a debug build can change scheduling and memory behavior.
- Start with `bt` and inspect the first relevant application frame. For hangs or worker failures, compare all thread stacks with `thread apply all bt`; locate the blocked dependency, owning thread or condition before changing locks. Avoid printing bulk locals or core memory into shared logs.
- Use a breakpoint near the first divergence. Bound conditional checks on hot paths and use watchpoints for a specific write when supported. Keep debugger auto-loading limited to trusted project scripts. Prefer direct inspection of variables and memory over evaluating functions that can mutate the target.
- Distinguish debugger-induced pauses from application latency. Compare runs without the debugger using the same inputs and build mode. Use a profiler to rank hot paths before selecting a narrow state question for GDB.

Repeat the failing case with the authorized fix, and validate the relevant optimized build when the failure depended on its behavior. Record signal, thread, relevant frame and exact build; omit sensitive core contents.

Upstream: [GDB manual](https://sourceware.org/gdb/current/onlinedocs/gdb.html/), [Threads](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Threads.html), [Separate debug files](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Separate-Debug-Files.html).
