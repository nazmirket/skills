# Storybook

Use an existing Storybook to inspect or exercise a component and its states in isolation. Start with the project's story convention, installed version, and preview configuration. Use the project's existing start or test command when needed.

1. Open the affected story and confirm the component, args, decorators or providers, theme, viewport and mocked data that produce the state. Keep these conditions matched for before and after comparisons.
2. Reuse stories that already cover the decision. When creating a story is in scope, expose the smallest missing case through normal component inputs or the existing mock boundary. If interaction matters, use the story's existing checks or exercise it directly; a play function can replay actions after rendering when the project supports it.
3. Record the story link or ID, revision, state and observed result. For an interaction, distinguish the action from its assertion. For visual evidence, inspect the actual canvas instead of inferring appearance from story source.

A story proves the component in its configured preview. Verify the actual app for claims about routing, live data, integration, or layout outside the story. If Storybook is unavailable, reuse an equivalent local preview or the app itself and name any gap. Installing or introducing Storybook is a separate decision.
