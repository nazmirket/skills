# C

Confirm the dialect, architecture, compiler flags, allocator and ABI. Check target sizes and integer promotion rules rather than assuming values match the development machine.

- Make pointer ownership, valid length, mutability and result status explicit at API boundaries. Check sizes before pointer arithmetic or allocation; verify the multiplication fits the allocation size type. NUL-terminated strings and counted buffers are different contracts.
- Initialize data before use and centralize cleanup when a function acquires several resources. Handle partial initialization and allocation failures. Preserve the original allocation while checking whether a reallocation succeeded.
- Avoid undefined behavior rather than assuming it will fail visibly. Check signed arithmetic and sentinel conversions before narrowing. Do not serialize or equate structs by assuming padding, native byte order, or compatible alignment.
- Validate at boundaries and return errors that can be acted on. Pass buffers and capacity together where the caller owns storage. Keep foreign ownership, thread safety, and compiler extensions explicit.

Build with existing warnings on supported compilers and run targeted tests under available sanitizers. Cover zero, maximum and one-past limits, failed allocation where possible, truncated input, and repeated cleanup.

Sources: [SEI CERT C Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard) for integer, buffer and resource rules, and the [GNU C Library memory allocation manual](https://www.gnu.org/software/libc/manual/html_node/Memory-Allocation.html) for glibc behavior.
