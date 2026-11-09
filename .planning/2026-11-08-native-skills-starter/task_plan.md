# Task Plan: Native skills starter

## Goal
Prepare a review of the 18 Mirket parent skills, an actionable outline, and a separate fresh starter for authoring skills across Codex and Claude Code.

## Next Step
Deliver the starter and note that host installation and skill behavior require later testing.

## Current Phase
Phase 5

## Phases

### Phase 1: Requirements & Discovery
- [x] Inspect parent catalog and provenance; consult host documentation.
- [x] Confirm the Desktop destination is new and original repo must remain unchanged.
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Freeze the proposal in OUTLINE.md and obtain independent critique.
- [x] Address material findings and document the review.
- **Status:** complete

### Phase 3: Implementation
- [x] Write guides, one blank skill template and two marketplace descriptors for a single shared skills folder.
- [x] Avoid importing skill content, hooks, or upstream assets.
- **Status:** complete

### Phase 4: Testing & Verification
- [x] Parse metadata and check marketplace paths; Claude validator is unavailable.
- [x] Confirm no repository changes; disclose untested host behavior.
- **Status:** complete

### Phase 5: Delivery
- [x] Link the review, plan, and starter; identify choices still open.
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| One shared plugin skills directory, separate native marketplace and plugin metadata | Portable content with explicit host-specific packaging. |
| Blank template outside discoverable skills directory | User wants to author their own skills, not ship a fake example. |
| No hooks or automatic routing | These need host-specific testing and a deliberate future decision. |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| Initial plan creation used a nonexistent working directory | Created the requested Desktop directory and reran the initializer. |
