# SQL

Identify the engine and version, the isolation and collation in use, and the expected result grain: what does one row represent? Start here for query semantics. Use [PostgreSQL](PostgreSQL.md) or [SQL Server](SQLServer.md) for engine behavior, or the installed engine's documentation when it differs.

## Make result shape predictable

- Name join keys and check their cardinality. A one-to-many join changes the row grain; joining two detail tables can multiply totals. Aggregate each detail to the intended grain before joining, or use `EXISTS` when only existence matters. Use `DISTINCT` when deduplication is part of the contract.
- Keep predicates on an optional joined table in the join condition when unmatched rows must survive. State how NULLs compare and aggregate: `COUNT(*)` and `COUNT(column)` answer different questions. A nullable subquery makes `NOT IN` easy to misuse; use `NOT EXISTS` when its comparison matches the desired semantics.
- Order explicitly, including a tie-breaker when paging. Use window functions when you need per-row rank or a running total; use grouping when the result should collapse rows. Make the partition and frame explicit when defaults could change the answer.
- Bind data values through the driver. For dynamic identifiers, choose from supported names and quote using the engine's API. Let storage enforce uniqueness or referential integrity when the rule must hold across concurrent writers. Define the transaction and what makes retries safe.

## Tune against real cardinality

Use the engine's plan tooling and compare estimates with actual work in a safe environment. Check for row multiplication, expensive sorts, unnecessary round trips, and predicates that prevent a useful index match. Choose indexes for the actual predicates and ordering; count writes and storage too. Bulk operations reduce round trips but can lengthen locks or increase memory. CTE materialization, NULL sort order, collation, upsert, and pagination syntax vary across engines.

Check duplicates, NULLs, missing matches, ties, and a realistic high-cardinality case. Test concurrency on the target engine for writes. Compare results as well as timing before replacing a query.
