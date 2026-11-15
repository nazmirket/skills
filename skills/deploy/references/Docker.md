# Docker

Identify the builder, supported platforms, registry, and runtime. Separate Dockerfile and BuildKit problems from how a running service is scheduled.

## Build once, keep the inputs explicit

- Use a multi-stage build when compilers or test tools do not belong in the runtime image. Copy dependency manifests before frequently edited source so unrelated edits do not invalidate dependency installation. Use a small build context and a deliberate `.dockerignore`.
- Pin the base by digest when reproducibility matters, and make updates to that pin reviewable. Include target platform, build arguments, and lockfiles in the artifact record. Use BuildKit secret or SSH mounts for private inputs; build arguments and environment variables are not secret storage.
- Reuse a package cache mount or a compatible external cache for slow, repeated builds. Keep trusted release caches separate from untrusted builds and verify cold-cache correctness. Compare build duration, transferred bytes, compressed image size, and startup separately; a small image is not proof of faster startup.

## Check the running image

Run the exact digest on the intended platform with the expected user, storage, and resource limits. Use a non-root process where the app supports it. Make signal delivery and graceful stop explicit; check startup, one user path, and a stop/restart against a disposable fixture. A container health check does not establish that the upstream or proxy can serve users. For a cluster rollout, use [Kubernetes](Kubernetes.md).

Upstream: [Docker build best practices](https://docs.docker.com/build/building/best-practices/), [Build cache optimization](https://docs.docker.com/build/cache/optimize/), [Build secrets](https://docs.docker.com/build/building/secrets/).
