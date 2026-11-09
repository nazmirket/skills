# Task Plan: Make the Mirket catalog a maintained project

## Goal
Convert the Desktop catalog from a placeholder starter into a coherent, lean project for authoring and distributing the six Mirket skills in Codex and Claude Code, without changing the reference repository or running behavioral skill tests.

## Next Step
Deliver the result with the verification evidence and outstanding host testing.

## Current Phase
Phase 5

## Phases

### Phase 1: Requirements & Discovery
- [x] Inspect the catalog, manifests, documentation and references.
- [x] Preserve the reference repository and existing research/evaluation history.
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Review this plan independently and address findings.
- [x] Set the target layout and documentation scope.
- **Status:** complete

### Phase 3: Implementation
- [x] Rename the placeholder plugin directory and update both marketplace descriptors and plugin manifests.
- [x] Replace starter README with concise current catalog, layout, authoring and local marketplace instructions. Preserve earlier outline, source review and evaluation as clearly historical material, with usable links.
- [x] Fix stale current references and wording throughout; preserve all six skills, metadata and user decisions. Retain authoring templates if useful.
- **Status:** complete

### Phase 4: Testing & Verification
- [x] Inspect JSON, paths, skill names, display metadata and local Markdown links with read-only structural checks; do not run skill behavioral tests or install plugins.
- [x] Confirm original reference repository is unchanged. Disclose host validation or functionality not verified.
- **Status:** complete

### Phase 5: Delivery
- [x] Record evidence and present the resulting project and limits.
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Keep the shared portable plugin and separate host marketplace files | Matches both supported distribution formats. |
| Use the human-selected plugin namespace | Keep identity consistent across both marketplace descriptors and plugin manifests. |
| Preserve previous plan/research/evaluation records as history | They document prior decisions and limitations; current instructions should not misrepresent them as the present state. |
| Initialize a local Git repository, without committing, registering, installing or publishing | The user requested a real repository; Git initialization is local and reversible. Skill behavior testing remains deferred. |

## Errors Encountered
| Error | Resolution |
|-------|------------|
