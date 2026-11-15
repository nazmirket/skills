# Next.js

Read the installed Next.js major, App or Pages Router, route and cache configuration, and deployment runtime. Do not carry defaults or APIs across router or major-version boundaries.

- In the App Router, keep data access and secrets on the server. Add client boundaries around interactive or browser-dependent pieces; understand which modules enter the client graph. Pass supported serializable data, keeping only what the browser needs. Pages Router has different fetching and rendering conventions.
- For each data read, decide who can see it and how stale it may be. Distinguish per-request freshness, reusable public data, and personalized responses. Check the installed version's defaults and enabled cache options before adding revalidation. Verify warm navigation and fresh/direct requests after mutations.
- Treat server actions and route handlers as callable entry points. Validate input and authorize against the actual resource on the server. Never rely on hiding a client button or on a cache key to enforce access.
- Put loading and error boundaries where users can understand the delayed part and recover. Check static export or runtime limitations before adding a request-time feature. Prefer supported metadata, links and image handling when they fit the project.

Run the production-mode build and smoke the affected route directly and through navigation. Check one fresh and one previously loaded case; include anonymous or another user's state when cache isolation matters.

Official: [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Caching](https://nextjs.org/docs/app/getting-started/caching).
