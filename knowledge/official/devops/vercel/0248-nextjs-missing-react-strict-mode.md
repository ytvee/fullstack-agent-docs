--------------------------------------------------------------------------------
title: "NEXTJS_MISSING_REACT_STRICT_MODE"
description: "Applications using Next.js should enable React Strict Mode"
last_updated: "2026-04-03T23:47:18.127Z"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_REACT_STRICT_MODE"
--------------------------------------------------------------------------------

# NEXTJS_MISSING_REACT_STRICT_MODE

> **🔒 Permissions Required**: Conformance

We strongly suggest you enable Strict Mode in your Next.js application
to better prepare your application for the future of React. See the [Next.js doc on React Strict Mode](https://nextjs.org/docs/api-reference/next.config.js/react-strict-mode)
for more information.

## How to fix

Add the following to your `next.config.js` file.

```json filename="next.config.js"
module.exports = {
  reactStrictMode: true,
}
```


