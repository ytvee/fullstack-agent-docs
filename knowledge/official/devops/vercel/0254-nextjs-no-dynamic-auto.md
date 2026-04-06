---
id: "vercel-0254"
title: "NEXTJS_NO_DYNAMIC_AUTO"
description: "Prevent usage of force-dynamic as a dynamic page rendering strategy."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_DYNAMIC_AUTO"
tags: ["nextjs", "no", "dynamic", "auto", "rules", "nextjs-no-dynamic-auto"]
related: ["0251-nextjs-no-async-page.md", "0252-nextjs-no-before-interactive.md", "0255-nextjs-no-fetch-in-server-props.md"]
last_updated: "2026-04-03T23:47:18.170Z"
---

# NEXTJS_NO_DYNAMIC_AUTO

> **🔒 Permissions Required**: Conformance

Changing the dynamic behavior of a layout or page using "force-dynamic" is
not recommended in App Router. This is because this will force only dynamic rendering
of those pages and opt-out "fetch" request from the fetch cache. Furthermore, opting
out will also prevent future optimizations such as partially static subtrees and
hybrid server-side rendering, which can significantly improve performance.

See [Next.js Segment Config docs](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)
for more information on the different migration strategies that can be used and how
they work.

## How to fix

Usage of `force-dynamic` can be avoided and instead `no-store` or `fetch` calls
can be used instead. Alternatively, usage of `cookies()` can also avoid the need
to use `force-dynamic`.

```js
// Example of how to use `no-store` on `fetch` calls.
const data = fetch(someURL, { cache: 'no-store' });
```


