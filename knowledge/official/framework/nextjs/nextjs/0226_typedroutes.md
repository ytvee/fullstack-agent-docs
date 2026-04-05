---
title: typedRoutes
description: Enable support for statically typed links.
url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes"
version: 16.2.2
---

# typedRoutes

> **Note**: This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](/docs/app/api-reference/config/typescript#statically-typed-links). This feature requires using TypeScript in your project.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  typedRoutes: true,
}

module.exports = nextConfig
```


