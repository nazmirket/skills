# 0005: Separate Design formats from tools

**Status:** Accepted

The maintainer approved keeping one Design skill with a lean router and adding formats and tools alongside flows, concepts, and styles. A flow owns the requested job and its stopping point. A format owns the deliverable-specific acceptance and handoff. A concept explains shared craft, a style describes a visual treatment, and a tool guide explains how to perform an operation and what its evidence can support.

A deliverable can use several technologies. A browser-based design may be inspected directly, checked with automation, or captured as an image. Those operations must remain optional and must not change who owns the result or what a review is authorized to do. We considered putting all guidance under concepts and registering separate domain skills. The former hides the contract for each deliverable; the latter repeats workflows and creates competing owners.

Start with [Web Design](../../skills/design/references/formats/WebDesign.md) and the [browser evidence tools](../../skills/design/references/tools/README.md). Route by job first; open a format when it changes the checks or handoff, and open a tool guide only for an operation needed now. Reuse the project's stack and verification. Keep original Mirket guidance in the package; upstream material stays a reference rather than a runtime dependency.
