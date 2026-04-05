---
title: onDemandEntries
description: Configure how Next.js will dispose and keep in memory pages created in development.
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries"
version: 16.2.2
router: Pages Router
---

# onDemandEntries

Next.js exposes some options that give you some control over how the server will dispose or keep in memory built pages in development.

To change the defaults, open `next.config.js` and add the `onDemandEntries` config:

```js filename="next.config.js"
module.exports = {
  onDemandEntries: {
    // period (in ms) where the server will keep pages in the buffer
    maxInactiveAge: 25 * 1000,
    // number of pages that should be kept simultaneously without being disposed
    pagesBufferLength: 2,
  },
}
```


