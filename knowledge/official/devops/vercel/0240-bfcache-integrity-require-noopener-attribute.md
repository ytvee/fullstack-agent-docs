---
id: "vercel-0240"
title: "BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE"
description: "Requires that links opened with window.open use the noopener attribute to eliminate a source of eviction from the browser"
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE"
tags: ["bfcache", "integrity", "require", "noopener", "attribute", "rules"]
related: ["0239-bfcache-integrity-no-unload-listeners.md", "0295-require-docs-on-exported-functions.md", "0296-require-node-version-file.md"]
last_updated: "2026-04-03T23:47:18.074Z"
---

# BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE

> **🔒 Permissions Required**: Conformance

The Back-Forward Cache (bfcache) is a browser feature that allows pages to be cached in memory when the user navigates
away from them. When the user navigates back to the page, it can be loaded almost instantly from the cache instead of
having to be reloaded from the network. Breaking the bfcache's integrity can cause a page to be reloaded from the network
when the user navigates back to it, which can be slow and jarring.

Pages opened with `window.open` that do not use the `noopener` attribute can both be a security risk and also will
prevent browsers from caching the page in the bfcache. This is because the new window can access the `window.opener` property
of the original window, so putting the original page into the bfcache could break the new window when attempting to access it.

Using the `noreferrer` attribute will also set the `noopener` attribute to true, so it can also be used to ensure
the page is placed into the bfcache.

To learn more about the bfcache, see the [web.dev docs](https://web.dev/bfcache).

## Related Rules

- [BFCACHE\_INTEGRITY\_NO\_UNLOAD\_LISTENERS](/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS)

## Example

Examples of when this check would fail:

```ts
window.open('https://example.com', '_blank');
window.open('https://example.com');
```

## How to fix

Instead, use the `noopener` or `noreferrer` attributes:

```ts
window.open('https://example.com', '_blank', 'noopener');
window.open('https://example.com', '_top', 'noreferrer');
```


