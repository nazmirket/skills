# Grafana

Identify the instance or stack, organization, data source, dashboard ownership, and alerting mode. A panel can show the wrong environment or lagging data while Grafana itself is healthy.

- Confirm data source, environment filter, units, time range and freshness before comparing a signal across releases. Keep a small overview around user symptoms, with drill-down views for causes. Label missing data explicitly and leave deployment annotations keyed to the actual release.
- Treat dashboards, rules, routing and contact points as managed config if this instance is provisioned. Update the authoritative source rather than making edits it will overwrite. Change labels and routing together where needed; do not test by paging production responders without authorization.
- Bound expensive variables, refresh rates and dashboard fan-out. Compare dashboard load and query spans at representative ranges; separate frontend rendering from slow data-source queries. Time series aggregations and recording rules belong with the data source owner.
- Choose evaluation windows and handling for no data and errors. Review grouping, deduplication and mute timing so related symptoms don't cause noisy pages or silence actionable ones.

Check a normal and an adverse window with the intended data source. Use preview and approved test notifications to verify route, labels and recovery. Verify the actual user path as well if the dashboard supports a rollout decision.

Upstream: [Alerting best practices](https://grafana.com/docs/grafana/latest/alerting/guides/best-practices/), [Provision Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/), [Dashboard troubleshooting](https://grafana.com/docs/grafana/latest/dashboards/troubleshoot-dashboards/).
