# PHP

Check the supported PHP version and extensions, Composer constraints and autoloading, and whether the runtime is a short-lived request or a persistent process. Use [Laravel](Laravel.md) for Laravel lifecycle, Eloquent, containers, and queues.

- Keep domain functions and types separate from superglobals, HTTP responses, and persistence details. Validate external arrays or JSON once. Distinguish a missing key from an explicit null when it matters; `isset` conflates them. Choose simple typed inputs and return values; `strict_types` does not validate fields in an array.
- Prefer a narrow exception boundary where an error can be handled or translated. Preserve exception context, and use `finally` for cleanup on both success and failure. Avoid hidden request state in globals or static properties, especially in long-lived workers.
- Use the project's Composer autoloading and namespace conventions. Open interfaces when there is a real second implementation or an effectful boundary to exercise. Avoid mixing autoloaded definitions with work that runs on import.
- In PDO, bind values and use allowlisted identifiers where query parts are genuinely dynamic. Stream large result sets or files where the driver/runtime permits it; a generator does not undo an upstream buffered query. Profile request and worker work separately, checking database trips, peak memory, and repeat processing before tuning.

Run the project's Composer scripts, test runner, and configured static analysis at the supported runtime. Include malformed input and the production-style entry point. Test long-lived state across two jobs or requests if affected.

Upstream: [PHP type declarations](https://www.php.net/manual/en/language.types.declarations.php), [PDO prepared statements](https://www.php.net/manual/en/pdo.prepare.php), [Composer autoloading](https://getcomposer.org/doc/01-basic-usage.md#autoloading).
