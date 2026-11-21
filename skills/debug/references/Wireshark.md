# Wireshark

Use when existing application or connection evidence cannot distinguish a transport problem. Confirm the approved interfaces, endpoints, direction and time window. Use the smallest authorized capture or an existing trace; avoid collecting unrelated traffic or payloads.

- Pick the capture point based on the question. A client-side trace cannot by itself tell where a packet disappeared downstream. If available and approved, align a short capture on either side of the suspect hop with request IDs, host logs and timestamps. Record tunnel, proxy or NAT boundaries that change what each point sees.
- Capture filters determine what is retained; display filters change only what is shown. Restrict collection at capture time where possible. Identify one conversation and follow DNS, TCP setup, TLS negotiation, and whichever application metadata is actually visible. Encrypted payload is not needed for most handshake and timing questions.
- Separate a real network symptom from capture limitations. Check capture loss, interfaces, clock offset and offload artifacts before treating apparent gaps, duplicate segments or checksum anomalies as network faults. Correlate analysis flags and timing with the affected client; Wireshark's labels are clues.
- For performance, check where idle time accumulates and compare a representative working path. An observed round trip is specific to the capture point and transport; correlate it with server processing and the user's timing.

Record the minimal timings, frame numbers, capture points and limitations needed to explain the observation. Keep raw packet files restricted; summarize or sanitize before sharing. After a change, rerun the same transaction and check both the packet-level symptom and the user-visible result.
