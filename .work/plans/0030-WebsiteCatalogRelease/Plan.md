# Plan

1. Compare public production to the current Git source and verify the rollback target.
2. Build the clean candidate, run repository and export checks, and compare the generated pages and links to the full catalog. Smoke key navigation in a browser.
3. Transfer a checksum-verified static export and switch the existing release link atomically.
4. Compare production routes, assets, metadata and navigation with the candidate; restore the previous release if verification fails.
