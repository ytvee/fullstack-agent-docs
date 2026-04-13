# Review Checklist

## Code quality

- Does the change follow the current repo patterns and styling system?
- Is the data flow explicit and understandable?
- Are there unnecessary abstractions, wrappers, or hooks?
- Did the change introduce framework misuse or hidden coupling?
- Are types, boundary validation, and error states handled clearly?

## Next.js 16 specifics

- Are `params`, `searchParams`, `cookies()`, `headers()` awaited before use?
- Is caching expressed via `'use cache'` rather than the legacy `cache: 'force-cache'`
  on individual `fetch()` calls?
- Is `notFound()` called outside any `<Suspense>` boundary?
- Does the root layout have `metadataBase` set if relative OG image paths are used?

## Performance

- Does the change add a large new client bundle entry when a Server Component
  would serve the same purpose?
- Are there `useEffect` calls that duplicate logic that could run during render
  or in an event handler?

## Accessibility

- Do interactive elements have accessible labels (`aria-label`, `aria-labelledby`,
  or visible text)?
- Are images given descriptive `alt` attributes?
- Does keyboard navigation work for any new interactive elements?

## Security

- Are any environment variables that should be server-only accidentally prefixed
  with `NEXT_PUBLIC_`?
- Is user-supplied content rendered safely (no `dangerouslySetInnerHTML` on
  untrusted input)?
