# Route Patterns

- Use `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`,
  and `route.ts` only for their intended Next.js roles.
- Keep page files thin and centered on composition.
- For dynamic resources, prefer `notFound()` over silent null rendering.
- Add `generateStaticParams()` when static generation is intended and the app has
  a finite build-time list.
- Keep route-level fetching close to the route shell unless a reusable helper
  already owns that concern.
