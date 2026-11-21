# Prometheus

Identify the scrape and evaluation topology, storage and retention, label conventions, and expected target coverage. Confirm the time range, scraper freshness and metric type before interpreting a result.

- Use counters for events and calculate rates before aggregation so counter resets can be handled per series. Choose latency buckets from meaningful thresholds and use the correct aggregation for the histogram representation. Keep labels bounded; use logs or traces for per-request details. Each unique label combination creates another series.
- Alert on user-facing symptoms that call for action. Separate missing or stale data from a real zero. Choose thresholds, evaluation duration and alert labels deliberately; ensure the alert identifies the affected service and a useful action. Check that scrape, rule evaluation, and notification failure each have a visible signal.
- Measure scrape volume, active series, query latency, storage and rule evaluation cost. Reduce unbounded labels or repeated expensive queries before increasing capacity. Use recording rules for frequently repeated expressions where the storage and freshness tradeoff fits; avoid hiding raw evidence behind a single aggregate.

Use the installed `promtool` to check and test rule files before a reload. Test healthy, failing, absent and recovery windows with representative series. Verify target freshness and that the alert reaches the intended route in a safe test. For panel and contact behavior use [Grafana](Grafana.md).
