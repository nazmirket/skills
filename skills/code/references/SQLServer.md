# SQL Server and T-SQL

Confirm engine edition, database compatibility level, row-versioning settings, and workload. SQL Server, Azure SQL variants and other SQL engines do not share every behavior.

- Use typed query parameters and keep predicates compatible with intended seeks where it matters. Watch for implicit conversions, nonselective filters, and applying functions to indexed columns. Use stable ordering when paging.
- Choose keys and constraints that match domain invariants. Keep transactions focused, handle failures cleanly, and reproduce competing writes with separate sessions if the behavior depends on isolation. Do not use `NOLOCK` as a default fix for contention; it can read inconsistent data.
- Examine actual versus estimated rows and plans with representative parameter values. Separate version and compatibility effects from skew or stale statistics. Consider Query Store where available to compare real workloads. Do not execute a mutating statement merely to obtain an actual plan in production.
- Balance indexes for seek, sort and coverage against writes, space and phased rollout cost. Avoid copying every missing-index recommendation. Choose clustered and nonclustered keys with workload evidence and use Migrate for durable schema changes.

Check stable results, affected locking or deadlock behavior, and duration or logical reads across comparable inputs before recommending a tuning change.
