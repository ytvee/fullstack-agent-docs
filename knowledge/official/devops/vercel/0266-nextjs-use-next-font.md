---
id: "vercel-0266"
title: "NEXTJS_USE_NEXT_FONT"
description: "Requires using next/font to load local fonts and fonts from supported CDNs."
category: "vercel-conformance"
subcategory: "conformance"
type: "guide"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_FONT"
tags: ["nextjs", "next", "font", "rules", "nextjs-use-next-font", "examples"]
related: ["0267-nextjs-use-next-image.md", "0268-nextjs-use-next-script.md", "0265-nextjs-use-native-fetch.md"]
last_updated: "2026-04-03T23:47:18.262Z"
---

# NEXTJS_USE_NEXT_FONT

> **🔒 Permissions Required**: Conformance

[`next/font`](https://nextjs.org/docs/pages/api-reference/components/font)
automatically optimizes fonts and removes external network requests for
improved privacy and performance.

By default, this rule is disabled. Enable it by
[customizing Conformance](/docs/conformance/customize).

This means you can optimally load web fonts with zero layout shift, thanks to
the underlying CSS size-adjust property used.

For further reading, see:

- https://nextjs.org/docs/basic-features/font-optimization
- https://nextjs.org/docs/pages/api-reference/components/font
- https://www.lydiahallie.io/blog/optimizing-webfonts-in-nextjs-13

## Examples

This rule will catch the following code.

```css {3-4}
@font-face {
  font-family: Foo;
  src:
    url(https://fonts.gstatic.com/s/roboto/v30/KFOiCnqEu92Fr1Mu51QrEz0dL-vwnYh2eg.woff2)
      format('woff2'),
    url(/custom-font.ttf) format('truetype');
  font-display: block;
  font-style: normal;
  font-weight: 400;
}
```

```ts {3-6}
function App() {
  return (
    <link
      href="https://fonts.googleapis.com/css2?family=Krona+One&display=optional"
      rel="stylesheet"
    />
  );
}
```

## How to fix

Replace any `@font-face` at-rules and `link` elements that are caught by this
rule with [`next/font`](https://nextjs.org/docs/api-reference/next/font).


