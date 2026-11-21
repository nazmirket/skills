# Google Cloud Storage (GCS)

Identify the project, bucket, location and IAM principal. Check lifecycle rules, versioning or soft-delete policy, the audience, and any CDN, load balancer or cache between the bucket and client. These are object-storage practices; compute deployment needs its own service docs.

- Use immutable object names for release assets where practical. Publish assets before updating the manifest or entry page that refers to them. Use generation preconditions for conditional writes and deletes so a retry cannot overwrite a newer revision. Verify checksums and set intended content type and cache metadata.
- Keep resolvers and object permissions consistent with the audience; use the established IAM model and prefer narrower access for private data. Do not enable blanket public bucket access to fix a private origin or CDN issue. Verify HTTPS and authorization through the intended client path as well as direct origin access where appropriate.
- Measure transfer size, request rates and latency with realistic object sizes and key patterns. Use resumable uploads for large transfers where appropriate, bound parallelism and retries, and ramp high request rates per the service guidance. Treat cache hit rates and origin response as separate signals.
- Keep prior entry documents and assets available until old cached references expire and rollback is no longer needed. Restoring an object generation alone does not invalidate a cache or restore a coherent multi-object release.

Verify the consumer URL, expected object generation or digest, response metadata, and a warm and cold path. Explicitly check recovery and cache behavior when deleting or replacing shared objects.
