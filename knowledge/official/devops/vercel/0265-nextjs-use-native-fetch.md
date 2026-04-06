---
id: "vercel-0265"
title: "NEXTJS_USE_NATIVE_FETCH"
description: "Requires using native "
category: "vercel-conformance"
subcategory: "conformance"
type: "guide"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_USE_NATIVE_FETCH"
tags: ["nextjs", "native", "fetch", "rules", "nextjs-use-native-fetch", "examples"]
related: ["0266-nextjs-use-next-font.md", "0260-nextjs-require-explicit-dynamic.md", "0267-nextjs-use-next-image.md"]
last_updated: "2026-04-03T23:47:18.251Z"
---

# NEXTJS_USE_NATIVE_FETCH

> **🔒 Permissions Required**: Conformance

Next.js extends the native [Web `fetch` API](https://nextjs.org/docs/app/api-reference/functions/fetch)
with additional caching capabilities which means third-party fetch libraries are not needed.
Including these libraries in your app can increase bundle size and negatively impact performance.

This rule will detect any usage of the following third-party fetch libraries:

- `isomorphic-fetch`
- `whatwg-fetch`
- `node-fetch`
- `cross-fetch`
- `axios`

If there are more libraries you would like to restrict,
consider using a [custom rule](https://vercel.com/docs/conformance/custom-rules).

By default, this rule is disabled. You can enable it by
[customizing Conformance](/docs/conformance/customize).

For further reading, see:

- https://nextjs.org/docs/app/api-reference/functions/fetch
- https://developer.mozilla.org/en-US/docs/Web/API/Fetch\_API

## Examples

This rule will catch the following code.

```tsx {1}
import fetch from 'isomorphic-fetch';

export async function getAuth() {
  const auth = await fetch('/api/auth');
  return auth.json();
}
```

## How to fix

Replace the third-party fetch library with the native `fetch` API Next.js provides.


