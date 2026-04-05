---
title: mdxRs
description: Use the new Rust compiler to compile MDX files in the App Router.
url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs"
version: 16.2.2
---

# mdxRs

> This feature is currently experimental and subject to change, it is not recommended for production.

For experimental use with `@next/mdx`. Compiles MDX files using the new Rust compiler.

```js filename="next.config.js"
const withMDX = require('@next/mdx')()

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['ts', 'tsx', 'mdx'],
  experimental: {
    mdxRs: true,
  },
}

module.exports = withMDX(nextConfig)
```


