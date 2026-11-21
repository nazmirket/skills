# 0002: Keep lifecycle ownership explicit

**Status:** Accepted

**Catalog update:** Focus, Secure, Release, and Operate were later retired as standalone skills. The human still owns product decisions, with Ship supporting product judgment. Audit handles security and privacy findings, Architect handles design-time threat modeling, and the implementer handles authorized hardening. The task owner prepares or publishes a versioned artifact, and Deploy handles rollout and operations. See the [current routing guide](../../references/Routing.md).

The 25-skill catalog adds Secure, Release, Migrate, Deploy and Operate to cover product delivery and recovery. Each owns a distinct result: security/privacy assessment and hardening, a versioned artifact, a reconciled state transition, an environment rollout, or service health and recovery. Focus evaluates shipped outcomes. Supporting skills return evidence to the owner; they do not restart authorization or infer permission to publish from permission to prepare.

These boundaries avoid a generic shipping workflow that mixes artifact preparation, persistent state, activation and ongoing operations. The shared routing reference records the boundaries; existing skills link to an owner only when that work is relevant. Global instructions remain a short routing and evidence contract rather than duplicating each workflow.
