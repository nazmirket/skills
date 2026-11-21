# C++

Confirm the language standard, compiler and library baselines, build flags, and exceptions, RTTI, allocation and ABI conventions. A modern idiom is not permission to change the toolchain.

- Make resource lifetime visible with RAII. Prefer value ownership or unique ownership where applicable; add shared ownership only when the lifetime truly is shared. Label borrowing with an appropriate view, reference, or pointer and account for invalidation after moves, reallocations or destruction.
- Use established containers and algorithms, const-correct interfaces, and types that express units and validity. Keep bounds, iterator ranges and signed conversions visible. Avoid exposing raw ownership or choosing templates solely for imagined reuse.
- Follow the project's error policy and define invariants across exceptions or returned errors. A destructor or cleanup path must not introduce another failure a caller cannot handle. Preserve an ABI surface when changing public layouts or exception behavior.
- For concurrency, identify shared state and memory ordering requirements before changing synchronization. Prefer obvious locking and resource ownership unless measurement or platform requirements warrant more complex primitives.

## Make lifetime and performance choices explicit

- Document what a returned view borrows and what invalidates it. For public or cross-library interfaces, prefer stable types and a small header surface; verify an actual caller against supported build configurations. Escape hatches such as raw pointers should keep ownership unambiguous.
- Keep algorithm and data-layout choices tied to workload. For example, dense contiguous storage may help repeated traversal, but insertion patterns and view invalidation can dominate. Profile allocation, cache behavior, and contention in a representative optimized build before designing a new container or lock-free path.
- Isolate deterministic logic from I/O and platform dependencies when that makes behavior easier to exercise. Test lifetime and cleanup on exceptional paths; sanitizers complement configuration-appropriate tests rather than proving correctness.

Verify the actual toolchain and target modes. Run focused tests and applicable sanitizers with lifetime, bounds or concurrent use cases; verify performance with comparable workloads when it drove the change.
