---
title: transpilePackages
description: "Automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`)."
url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages"
version: 16.2.2
---

# transpilePackages

Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`). This replaces the `next-transpile-modules` package.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ['package-name'],
}

module.exports = nextConfig
```

## Version History

| Version   | Changes                    |
| --------- | -------------------------- |
| `v13.0.0` | `transpilePackages` added. |


