# 0002: Keep lifecycle ownership explicit

**Status:** Accepted

The 25-skill catalog adds Secure, Release, Migrate, Deploy and Operate to cover product delivery and recovery. Each owns a distinct result: security/privacy assessment and hardening, a versioned artifact, a reconciled state transition, an environment rollout, or service health and recovery. Focus evaluates shipped outcomes. Supporting skills return evidence to the owner; they do not restart authorization or infer permission to publish from permission to prepare.

These boundaries avoid a generic shipping workflow that mixes artifact preparation, persistent state, activation and ongoing operations. The shared routing reference records the boundaries; existing skills link to an owner only when that work is relevant. Global instructions remain a short routing and evidence contract rather than duplicating each workflow.
