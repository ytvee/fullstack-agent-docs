--------------------------------------------------------------------------------
title: "NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN"
description: "Applications using Next 13 should use the "
last_updated: "2026-04-03T23:47:18.117Z"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN"
--------------------------------------------------------------------------------

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


