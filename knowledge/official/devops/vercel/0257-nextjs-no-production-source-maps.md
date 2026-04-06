---
id: "vercel-0257"
title: "NEXTJS_NO_PRODUCTION_SOURCE_MAPS"
description: "Applications using Next.js should not enable production source maps so that they don"
category: "vercel-conformance"
subcategory: "conformance"
type: "guide"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_PRODUCTION_SOURCE_MAPS"
tags: ["nextjs", "no", "production", "source", "maps", "rules"]
related: ["0251-nextjs-no-async-page.md", "0250-nextjs-no-async-layout.md", "0248-nextjs-missing-react-strict-mode.md"]
last_updated: "2026-04-03T23:47:18.184Z"
---

# NEXTJS_NO_PRODUCTION_SOURCE_MAPS

> **🔒 Permissions Required**: Conformance

Enabling production source maps in your Next.js application will publicly share your
application's source code and should be done with caution. This rule flags any
usage of `productionBrowserSourceMaps` for review. If intentional, the exception
should be added to an allowlist.

For further reading, see:

- [`productionBrowserSourceMaps` documentation](https://nextjs.org/docs/app/api-reference/next-config-js/productionBrowserSourceMaps)

## Examples

This rule will catch the following code.

```next.config.js {2}
module.exports = {
  productionBrowserSourceMaps: true,
};
```

## How to fix

To fix this issue, either set the value of `productionBrowserSourceMaps` configuration to false,
or if intentional add an exception to an allowlist.

## Considerations

### Tradeoffs of Disabling Source Maps

Disabling source maps in production has the benefit of not exposing your source code publicly, but it also means that errors in production will lack helpful stack traces, complicating the debugging process.

### Protected Deployments

For [protected deployments](/docs/security/deployment-protection/methods-to-protect-deployments), it is generally safe to enable source maps, as these deployments are only accessible by authorized users who would already have access to your source code. Preview deployments are protected by default, making them a safe environment for enabling source maps.

### Third-Party Error Tracking Services

If you use a third-party error tracking service like [Sentry](https://sentry.io/), you can safely enable source maps by:

1. Uploading the source maps to your error tracking service
2. Emptying or deleting the source maps before deploying to production

Many third-party providers like Sentry offer built-in configuration options to automatically delete sourcemaps after uploading them. Check your provider's documentation for these features before implementing a manual solution.

If you need to implement this manually, you can use an approach like this:

```ts
// Empty the source maps after uploading them to your error tracking service
const sourcemapFiles = await findFiles('.next', /\.js\.map$/);
await Promise.all(
  sourcemapFiles.map(async (file) => {
    await writeFile(file, '', 'utf8');
  }),
);
```


