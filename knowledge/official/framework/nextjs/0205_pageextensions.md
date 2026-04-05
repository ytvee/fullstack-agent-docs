---
title: pageExtensions
description: Extend the default page extensions used by Next.js when resolving pages in the Pages Router.
url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions"
version: 16.2.2
---

# pageExtensions

By default, Next.js accepts files with the following extensions: `.tsx`, `.ts`, `.jsx`, `.js`. This can be modified to allow other extensions like markdown (`.md`, `.mdx`).

```js filename="next.config.js"
const withMDX = require('@next/mdx')()

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}

module.exports = withMDX(nextConfig)
```


