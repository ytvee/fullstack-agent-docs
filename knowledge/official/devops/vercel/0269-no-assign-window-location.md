---
id: "vercel-0269"
title: "NO_ASSIGN_WINDOW_LOCATION"
description: "Prevent unsafe assignment to window.location.href in your application."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_ASSIGN_WINDOW_LOCATION"
tags: ["no", "assign", "window", "location", "rules", "no-assign-window-location"]
related: ["0271-no-dangerous-html.md", "0272-no-document-write.md", "0273-no-eval.md"]
last_updated: "2026-04-03T23:47:18.277Z"
---

# NO_ASSIGN_WINDOW_LOCATION

> **🔒 Permissions Required**: Conformance

Direct assignments to "window.location.href" or "window.location" should be avoided due to possible XSS attacks that can occur from lack
of sanitization of input to the "href".

## How to fix

The recommended approach for Next.js applications is to use a custom `redirectTo` function. This provides a clear way to use `router.push()`
or `window.location.href` to provide an experience that is best for the user (client-side navigation only, or a full page refresh).
Here's an example of how you might do this using Next.js:

Before:

```js filename="my-site.js"
windows.location.href = '/login';
```

After:

```js filename="my-site.js"
router.push('/login');
```


