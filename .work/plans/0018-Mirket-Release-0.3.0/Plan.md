# Plan — draft; execution authorized

1. Review the staged scope and package version parity; run package checks and the 56 existing tests. Commit and build the exact revision from a clean archive.
2. Push main, refresh the configured marketplaces, and verify both installed package trees, versions, and Hindsight preservation.
3. Transfer the checked static export, activate the versioned release atomically, and verify live skill pages, reference link, cards and release version; retain the preceding release for rollback.

## Result

Released bf3703d to origin/main with matching 0.3.0 manifests. All 56 tests, both Claude validators (existing advisories only), and the clean-archive static build and export checks passed. Both installed plugins report 0.3.0 enabled; all 66 package files match the commit and installed hook payload checks passed. Hindsight config and hook wiring hashes are unchanged. No host hook trust was bypassed.

Activated the exact built release on skills.mirket.dev, keeping e465ef9 for rollback. Live homepage, docs, Equip and Distill skill pages, both cards, and sitemap match the export byte for byte. The homepage structured data lists 0.3.0, and the Equip reference link returns the updated GitHub content. Nginx is healthy; Git worktree is clean.
