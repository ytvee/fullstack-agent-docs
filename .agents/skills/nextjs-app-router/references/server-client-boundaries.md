# Server/Client Boundaries

- Prefer Server Components by default.
- Add `'use client'` only for hooks, browser APIs, event handlers, or required
  client-side interactivity.
- Do not import server-only modules into client code.
- Do not fetch your own route handlers from server-side code when direct module
  access is available.
- Keep async and data-loading concerns outside leaf presentation components.
