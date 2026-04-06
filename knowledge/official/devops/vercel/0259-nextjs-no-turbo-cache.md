---
id: "vercel-0259"
title: "NEXTJS_NO_TURBO_CACHE"
description: "Prevent Turborepo from caching the Next.js .next/cache folder to prevent an oversized cache."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_TURBO_CACHE"
tags: ["turborepo", "nextjs", "no", "turbo", "cache", "rules"]
related: ["0250-nextjs-no-async-layout.md", "0251-nextjs-no-async-page.md", "0252-nextjs-no-before-interactive.md"]
last_updated: "2026-04-03T23:47:18.205Z"
---

# NEXTJS_NO_TURBO_CACHE

> **🔒 Permissions Required**: Conformance

This rule prevents the `.next/cache` folder from being added to the Turborepo cache.
This is important because including the `.next/cache` folder in the Turborepo cache can cause
the cache to grow to an excessive size. Vercel also already includes this cache in the build
container cache.

## Examples

The following `turbo.json` config will be caught by this rule for Next.js apps:

```json filename="turbo.json" {5}
{
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**"]
    }
  }
}
```

## How to fix

To fix, add `"!.next/cache/**"` to the list of outputs for the task.

```json filename="turbo.json" {5}
{
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**", "!.next/cache/**"]
    }
  }
}
```


