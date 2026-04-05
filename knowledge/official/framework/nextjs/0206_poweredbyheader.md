---
title: poweredByHeader
description: "Next.js will add the `x-powered-by` header by default. Learn to opt-out of it here."
url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader"
version: 16.2.2
---

# poweredByHeader

By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

```js filename="next.config.js"
module.exports = {
  poweredByHeader: false,
}
```


