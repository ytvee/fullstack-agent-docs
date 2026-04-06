---
id: "vercel-0262"
title: "NEXTJS_SAFE_SVG_IMAGES"
description: "Prevent dangerouslyAllowSVG without Content Security Policy in Next.js applications."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_SVG_IMAGES"
tags: ["nextjs", "safe", "svg", "images", "rules", "nextjs-safe-svg-images"]
related: ["0263-nextjs-safe-url-imports.md", "0255-nextjs-no-fetch-in-server-props.md", "0258-nextjs-no-self-hosted-videos.md"]
last_updated: "2026-04-03T23:47:18.221Z"
---

# NEXTJS_SAFE_SVG_IMAGES

> **🔒 Permissions Required**: Conformance

SVG can do many of the same things that HTML/JS/CSS can, meaning that it can be dangerous to execute SVG
as this can lead to vulnerabilities without proper [Content Security Policy](https://nextjs.org/docs/advanced-features/security-headers) (CSP) headers.

## How to fix

If you need to serve SVG images with the default Image Optimization API, you
can set `dangerouslyAllowSVG` inside your `next.config.js`:

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
};
```

In addition, it is strongly recommended to also set `contentDispositionType` to
force the browser to download the image, as well as `contentSecurityPolicy` to
prevent scripts embedded in the image from executing.


