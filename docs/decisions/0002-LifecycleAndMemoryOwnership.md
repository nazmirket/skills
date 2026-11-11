# 0002: Keep lifecycle ownership and memory evidence explicit

**Status:** Accepted

The 25-skill catalog adds Secure, Release, Migrate, Deploy and Operate to cover product delivery and recovery. Each owns a distinct result: security/privacy assessment and hardening, a versioned artifact, a reconciled state transition, an environment rollout, or service health and recovery. Focus evaluates shipped outcomes. Supporting skills return evidence to the owner; they do not restart authorization or infer permission to publish from permission to prepare.

These boundaries avoid a generic shipping workflow that mixes artifact preparation, persistent state, activation and ongoing operations. The shared routing reference records the boundaries; existing skills link to an owner only when that work is relevant. Global instructions remain a short routing and evidence contract rather than duplicating each workflow.

Memory reliability uses the same principle: identity, capture, ingestion, synthesis and retrieval have separate evidence. The project registry owns canonical bank identity. Diagnostics import the pinned upstream configuration resolver through a guarded adapter instead of maintaining a second precedence implementation. An incompatible runtime must be reviewed and rewired; the adapter does not start MCP while reading configuration.

The optional project freshness profile changes only refresh cadence for an already-enabled bank. It preserves capture scope and inherited policy. Current files remain authoritative for uncommitted work, and a real host capture followed by independent retrieval verifies the integration after setup or wiring changes. Ordinary tasks reuse current verification evidence. Page refresh, manual ingestion and a healthy daemon cannot substitute for capture evidence.

This keeps the integration small and reviewable at the cost of a pinned runtime and explicit upgrade checks. A future supported upstream resolver/routing interface should replace the adapter when it preserves these contracts.
