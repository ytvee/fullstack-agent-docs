--------------------------------------------------------------------------------
title: "NEXTJS_NO_BEFORE_INTERACTIVE"
description: "Requires review of usage of the beforeInteractive strategy in Script (next/script) elements."
last_updated: "2026-04-03T23:47:18.163Z"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_BEFORE_INTERACTIVE"
--------------------------------------------------------------------------------

# NEXTJS_NO_BEFORE_INTERACTIVE

> **🔒 Permissions Required**: Conformance

The default [loading strategy](https://nextjs.org/docs/basic-features/script#strategy)
for [`next/script`](https://nextjs.org/docs/basic-features/script) is optimised
for fast page loads.

Setting the strategy to [`beforeInteractive`](https://nextjs.org/docs/api-reference/next/script#beforeinteractive)
forces the script to load before any Next.js code and before hydration occurs,
which delays the page from becoming interactive.

For further reading, see:

- [Loading strategy in Next.js](https://nextjs.org/docs/basic-features/script#strategy)
- [`next/script` docs](https://nextjs.org/docs/api-reference/next/script#beforeinteractive)
- [Chrome blog on the Next.js Script component](https://developer.chrome.com/blog/script-component/#the-nextjs-script-component)

## Examples

This rule will catch the following code.

```ts {5}
import Script from 'next/script';

export default function MyPage() {
  return (
    <Script src="https://example.com/script.js" strategy="beforeInteractive" />
  );
}
```

## How to fix

This rule flags any usage of `beforeInteractive` for review. If approved, the
exception should be added to the allowlist.


