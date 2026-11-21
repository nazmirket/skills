# PostgreSQL

Identify the server major, relevant extensions, isolation, roles, and real query shape. Use representative statistics and concurrency rather than tuning against a tiny empty fixture.

- Put invariants that must survive concurrent writers in constraints when expressible. Decide NULL semantics and uniqueness intentionally. Keep transactions short and document retry behavior for serialization failures or deadlocks; retry the whole unit only when replay is safe.
- Use parameters for values and allowlisted or properly quoted identifiers for generated SQL. Choose types by meaning and comparison: clarify time zone interpretation, currency representation and equality before choosing a schema or index.
- Inspect `EXPLAIN` for estimates and compare with actual rows, loops and buffers in a safe environment. `EXPLAIN ANALYZE` executes the statement. Compare representative cardinalities and skew; a sequential scan can be the right plan.
- Choose index columns and predicates from frequent access patterns and data distribution. Check write cost, disk, lock behavior and existing coverage; confirm actual plan benefit. Treat a schema or index rollout as a state change and use Migrate when compatibility or recoverability matters.

Verify result semantics with NULLs or duplicates, concurrent updates where applicable, and representative plans. Report measured differences with conditions rather than claiming an index is universally faster.
