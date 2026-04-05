---
title: generateEtags
description: Next.js will generate etags for every page by default. Learn more about how to disable etag generation here.
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags"
version: 16.2.2
router: Pages Router
---

# generateEtags

Next.js will generate [etags](https://en.wikipedia.org/wiki/HTTP_ETag) for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open `next.config.js` and disable the `generateEtags` option:

```js filename="next.config.js"
module.exports = {
  generateEtags: false,
}
```


