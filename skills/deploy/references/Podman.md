# Podman

Identify Podman version, rootful versus rootless operation, registry policy, storage driver, network backend, SELinux policy where relevant, and the systemd manager if one runs the workload. OCI image compatibility alone does not make runtime behavior identical to Docker.

- For a persistent host service managed by systemd, use Quadlet where available. Keep the desired unit and image reference reviewable; make network and mount dependencies explicit. Use the correct system or user manager, and review what starts at boot or after logout before changing persistence. Leave ad hoc test containers ad hoc.
- Keep rootless user mappings and mount ownership visible. Check the mounted files as the service user. Use the applicable SELinux label convention; do not disable labels or broaden privileges to conceal a mount failure. Treat the Podman API socket as privileged access to everything the owning user can run.
- Measure pull, storage growth, network throughput and application readiness separately. Cached layers can help pull time; user-mode networking, storage, and application startup have different costs. Check the workload under its intended cgroup limits and realistic I/O before tuning.

Validate the generated unit for the installed version; inspect service status and logs using the matching manager. Check the candidate digest, the served path, reboot or restart behavior if in scope, and compatibility of volume data before restoring the prior unit and digest.

Upstream: [Quadlet systemd units](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html), [Podman run](https://docs.podman.io/en/latest/markdown/podman-run.1.html).
