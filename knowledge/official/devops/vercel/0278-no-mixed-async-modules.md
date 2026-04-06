---
id: "vercel-0278"
title: "NO_MIXED_ASYNC_MODULES"
description: "Prevent imports to modules that contain top-level awaits in your applications."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_MIXED_ASYNC_MODULES"
tags: ["no", "mixed", "async", "modules", "rules", "no-mixed-async-modules"]
related: ["0280-no-serial-async-calls.md", "0250-nextjs-no-async-layout.md", "0251-nextjs-no-async-page.md"]
last_updated: "2026-04-03T23:47:18.338Z"
---

# NO_MIXED_ASYNC_MODULES

> **🔒 Permissions Required**: Conformance

Top-level await expressions in modules that are imported by other modules in sync
prevent possible lazy module optimizations from being deployed on the module containing
the top-level await.

One such optimization this prevents is inline lazy imports. Inline lazy imports allow
for modules to be lazily evaluated and executed when they're used, rather than at
initialization time of the module that uses them, improving initialization performance.

This is particularly impactful for modules that might only be used conditionally or
given a user's interaction which might happen much latter in an application. Without this optimization, the module initialization times, such as for cold boots on Vercel Functions, could be slowed down for every request.

## How to fix

Consider refactoring the import to a dynamic import instead, or removing the top-level await
in favor of standard import.

If a top-level await is important, then it's important that any other modules importing the
module with the top-level await do so dynamically, as to avoid affecting initialization performance.

For example, this can be refactored:

```js
// Contains a top-level await
import { asyncConfig } from 'someModule';

function doSomething(data) {
  processData(data, asyncConfig);
}
```

To this:

```js
function doSomething(data) {
  import('someModule').then(({ asyncConfig }) => {
    processData(data, asyncConfig);
  });
}
```

Or this:

```js
import { asyncConfig } from 'someModule';

// Note the async keyword on the function
async function doSomething(data) {
  processData(data, asyncConfig);
}
```


