---
id: "vercel-0292"
title: "REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS"
description: "Prevent static imports that are referenced only in React event handlers from being eagerly loaded in React components."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS"
tags: ["react", "no", "static", "imports", "event", "handlers"]
related: ["0290-package-management-no-unresolved-imports.md", "0274-no-external-css-at-imports.md", "0289-package-management-no-circular-imports.md"]
last_updated: "2026-04-03T23:47:18.413Z"
---

# REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS

> **🔒 Permissions Required**: Conformance

React event handlers are async, and as such, this means we can defer loading the
associated code until we interact with the UI, triggering that event handler. Specifically, this
means we can improve initial code size and the overhead of loading the code until it is actually needed.

## How to fix

Instead of using static imports at the top of your module, you can use dynamic imports as needed in your React event handlers.

Before:

```js
import foo from 'foo';

const onClick = () => {
  foo.doSomething();
};
```

After:

```js
const onClick = () => {
  import('foo').then((foo) => {
    foo.doSomething();
  });
};
```

Additionally, you can [configure](/docs/conformance/customize) the rule for only specific React event handlers:

```json
"REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS": {
  eventAllowList: ['onClick'],
}
```


