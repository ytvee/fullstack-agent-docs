---
title: authInterrupts
description: "Learn how to enable the experimental `authInterrupts` configuration option to use `forbidden` and `unauthorized`."
url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts"
version: 16.2.2
---

# authInterrupts

> This feature is currently available in the canary channel and subject to change.

The `authInterrupts` configuration option allows you to use [`forbidden`](/docs/app/api-reference/functions/forbidden) and [`unauthorized`](/docs/app/api-reference/functions/unauthorized) APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
module.exports = {
  experimental: {
    authInterrupts: true,
  },
}
```
- [forbidden](/docs/app/api-reference/functions/forbidden)
  - API Reference for the forbidden function.
- [unauthorized](/docs/app/api-reference/functions/unauthorized)
  - API Reference for the unauthorized function.
- [forbidden.js](/docs/app/api-reference/file-conventions/forbidden)
  - API reference for the forbidden.js special file.
- [unauthorized.js](/docs/app/api-reference/file-conventions/unauthorized)
  - API reference for the unauthorized.js special file.


