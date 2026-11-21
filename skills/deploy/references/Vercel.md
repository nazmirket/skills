# Vercel

Identify team, project, source SHA, deployment ID, framework preset, build settings and environment. A deployment URL and the production hostname can serve different revisions. Check automatic production-branch promotion and the project's protection and approval settings before changing them.

- Keep Preview, staging, and Production inputs distinct. Check build-time versus runtime environment variables, build region and runtime selection where supported. A Preview may prove functionality but not Production parity. If promoting a Preview triggers a new build, validate the new production candidate. When an exact previously tested artifact matters, use a staged Production deployment and the supported promotion path.
- Preserve the deployment ID and supported rollback target. A rollback or re-alias may restore an earlier build and its configuration snapshot; it does not restore databases, caches or external state. Confirm compatibility, and check whether automation or domain routing could undo the recovery.
- Separate build queue and build time from request cold start, execution, and upstream latency. Scope builds to affected workspaces when safe, reuse reproducible build caches, and profile region or cache changes through representative cold and warm traffic. Review public versus personalized cache behavior.

Verify actual production domains, deployment identity, one affected route and a relevant auth or data request. Compare errors or latency to the baseline. Do not treat “Ready” or a working Preview link as proof of production success.
