---
id: "vercel-0276"
title: "NO_INLINE_SVG"
description: "Prevent the use of "
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_INLINE_SVG"
tags: ["no", "inline", "svg", "rules", "no-inline-svg", "how-to-fix"]
related: ["0271-no-dangerous-html.md", "0272-no-document-write.md", "0279-no-postinstall-script.md"]
last_updated: "2026-04-03T23:47:18.314Z"
---

# NO_INLINE_SVG

> **🔒 Permissions Required**: Conformance

Preventing the use of `<svg></svg>` inline improves the health of your codebase at the page level.
Using inlined `svg` tags in excess can cause hydration issues, negatively impact the performance of both
the browser and the server rendering.

By default, this rule is disabled. To enable it, refer to
[customizing Conformance](/docs/conformance/customize).

## How to fix

If you hit this issue, you can resolve it by using SVGs as an [`<Image>`](https://nextjs.org/docs/pages/api-reference/components/image)
component. Don't forget to enable [`dangerouslyAllowSVG`](https://nextjs.org/docs/pages/api-reference/components/image#dangerouslyallowsvg)
in your application's `next.config.js` file, and use the `unoptimized` component prop.

```JSX filename=".app/page.js"
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/logo.svg"
      width={100}
      height={100}
      alt="Logo of ACME"
      unoptimized
    />
  )
}
```


