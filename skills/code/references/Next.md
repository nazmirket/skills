# Next.js

Read the installed Next.js major, App or Pages Router, route and cache configuration, and deployment runtime. Do not carry defaults or APIs across router or major-version boundaries.

- In the App Router, keep data access and secrets on the server. Add client boundaries around interactive or browser-dependent pieces; understand which modules enter the client graph. Pass supported serializable data, keeping only what the browser needs. Pages Router has different fetching and rendering conventions.
- For each data read, decide who can see it and how stale it may be. Distinguish per-request freshness, reusable public data, and personalized responses. Check the installed version's defaults and enabled cache options before adding revalidation. Verify warm navigation and fresh/direct requests after mutations.
- Treat server actions and route handlers as callable entry points. Validate input and authorize against the actual resource on the server. Never rely on hiding a client button or on a cache key to enforce access.
- Put loading and error boundaries where users can understand the delayed part and recover. Check static export or runtime limitations before adding a request-time feature. Prefer supported metadata, links and image handling when they fit the project.

## Keep route behavior intentional

- Put a client boundary around the part that needs browser state or event handlers. Moving the boundary up the tree may increase shipped JavaScript and serialize more data. Confirm bundle or route impact before replacing a working server composition.
- Start independent reads as early as their inputs allow. Keep dependent reads ordered. Stream or put a loading boundary around slow work when it improves the useful first response; measure both the first meaningful UI and the completed interaction.
- Revalidate only the data or route scopes affected by the mutation. Verify the installed caching mode and adapter; a passing local development test is weak evidence for an output or caching problem in production. Use a production build with representative navigation, auth and cache state.

Run the production-mode build and smoke the affected route directly and through navigation. Check one fresh and one previously loaded case; include anonymous or another user's state when cache isolation matters.
