--------------------------------------------------------------------------------
title: "NO_EXTERNAL_CSS_AT_IMPORTS"
description: "Disallows @import at-rules that import from URLs."
last_updated: "2026-04-03T23:47:18.306Z"
source: "https://vercel.com/docs/conformance/rules/NO_EXTERNAL_CSS_AT_IMPORTS"
--------------------------------------------------------------------------------

# NO_EXTERNAL_CSS_AT_IMPORTS

> **🔒 Permissions Required**: Conformance

Importing CSS through ([`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/@import))
is render blocking, causing browsers to sequentially download and parse the
imported CSS (a [critical request chain](https://developer.chrome.com/en/docs/lighthouse/performance/critical-request-chains/)).

```css filename="app.module.css"
@import url('https://fonts.googleapis.com/css2?family=Inter');
```

This can result in a [flash of unstyled content (FOUC)](https://en.wikipedia.org/wiki/Flash_of_unstyled_content),
where page content is briefly shown without complete styles until all required
CSS has been downloaded and parsed, along with slower page load times.

Imports to relative paths are processed by frameworks like Next.js, and will
not be affected by this issue.

```css filename="app.module.css"
/* This import is safe. */
@import './globals.css';
```

> **💡 Note:** Note that this rule currently only parses CSS and not CSS written in Less,
> Sass, or other CSS preprocessor syntaxes.

## How to fix

If you're importing a font, you can use [`next/font`](https://nextjs.org/docs/basic-features/font-optimization)
which will automatically optimize your fonts (including custom fonts) and
remove external network requests.

If you're importing CSS, such as Bootstrap, avoid loading it from external
sources, such as a CDN or the [Next.js public folder](https://nextjs.org/docs/basic-features/static-file-serving).
Instead, you can import that CSS relatively, or from a package.

```ts filename="layout.tsx"
// CSS imported relatively from a local file.
import './globals.css';
// CSS from a package in `node_modules`.
import 'bootstrap/dist/css/bootstrap.css';

interface RootLayoutProps {
  children: React.ReactNode;
}

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <head />
      <body>{children}</body>
    </html>
  );
}
```


