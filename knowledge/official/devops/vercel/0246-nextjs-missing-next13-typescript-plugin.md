---
id: "vercel-0246"
title: "NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN"
description: "Applications using Next 13 should use the "
category: "vercel-conformance"
subcategory: "conformance"
type: "guide"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN"
tags: ["nextjs", "missing", "next13", "typescript", "plugin", "rules"]
related: ["0248-nextjs-missing-react-strict-mode.md", "0245-nextjs-missing-modularize-imports.md", "0247-nextjs-missing-optimize-package-imports.md"]
last_updated: "2026-04-03T23:47:18.117Z"
---

# NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN

> **🔒 Permissions Required**: Conformance

Next 13 introduced a TypeScript plugin to provide richer information for
Next.js applications using TypeScript. See the [Next.js docs](https://nextjs.org/docs/app/building-your-application/configuring/typescript#using-the-typescript-plugin) for more information.

## How to fix

Add the following to `plugins` in the `compilerOptions` of your `tsconfig.json`
file.

```json filename="tsconfig.json"
  "compilerOptions": {
    "plugins": [{ "name": "next" }]
  }
```


