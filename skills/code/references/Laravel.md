# Laravel

Read the framework and PHP versions from Composer, then identify the request or worker runtime, queue connection, database, and test configuration. Use [PHP](PHP.md) when the question belongs to the language.

- Keep validation at the HTTP boundary and authorization on the actual action and resource. Controllers, routes and jobs should make the call path readable. Keep domain invariants in the operation that owns them when they must also hold for CLI, queues, or other callers. Use the framework's conventions before adding a separate layer.
- Choose Eloquent relationships from the access pattern. Look for N+1 queries on collections or resources; eager-load what the caller needs and include the keys necessary for the relationship. Avoid fetching all columns, all relations, or all rows by default. For bulk changes, check batching, memory, and whether changing the API would bypass per-model events.
- Keep database transactions short. Dispatch after commit when a job depends on the committed records. Assume a retry can run after partial success; use the business key or database invariant that makes replay safe. Define timeouts and failure behavior for the configured worker and driver. Avoid per-request state in process-wide singletons.
- Cache only with a clear freshness and access boundary. Include account or visibility scope when needed and verify behavior after mutation. Compare actual query count and duration for representative input before adding an optimization.

Use a feature test for a real route and policy decision, or a real database and queue path for concerns their fakes cannot show. Cover rejected access, a failed or repeated job, or a query budget when it is the behavior being changed.

Upstream: [Eloquent relationships](https://laravel.com/docs/eloquent-relationships), [Queues](https://laravel.com/docs/12.x/queues), [HTTP tests](https://laravel.com/docs/12.x/http-tests); select the installed major.
