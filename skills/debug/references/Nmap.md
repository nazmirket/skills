# Nmap

Use for defensive reachability diagnosis when an expected listener or port is in dispute. Start with the affected client's normal request, an existing connection check, or known listener state. Use Nmap only if scoped network observation adds evidence.

- Confirm the approved source, exact destination and expected port, protocol and time window. Keep the check to that known endpoint. Use ordinary, bounded reachability checks within the network owner's authorization; avoid broad discovery or unrelated probes. A result from a laptop may differ from one inside the workload network.
- Interpret results as observations from a specific source at a specific time. An open TCP port means a listener accepted a connection or probe; it does not prove TLS, virtual-host routing, authentication or application health. A closed state is a response that no listener accepted the probe on that path. A filtered state does not identify which control or hop blocked traffic.
- Check direction before diagnosing. Compare an affected client with an approved known-working route, and reconcile the finding with listener logs, routing and intended firewall or security-group rules. Don't infer that a network control needs changing just because it blocked traffic as configured.
- Use application measurements for performance. A scan duration includes probe behavior and is not a valid service latency benchmark.

After an authorized fix, repeat the same limited probe and the actual client request. Record source, destination, expected listener, observed state and the application result. Keep host inventory or other unrelated findings out of the report.

Upstream: [Port states and their limits](https://nmap.org/book/man-port-scanning-basics.html), [Nmap reference](https://nmap.org/book/man.html).
