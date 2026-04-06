---
id: "vercel-0540"
title: "Advanced Configuration"
description: "Learn how to add utility files to the /api directory, and bundle Vercel Functions."
category: "vercel-functions"
subcategory: "functions"
type: "guide"
source: "https://vercel.com/docs/functions/configuring-functions/advanced-configuration"
tags: ["configuration", "configuring-functions", "advanced-configuration", "bundling-vercel-functions", "setup", "how-to"]
related: ["0541-configuring-in-function-concurrency.md", "0544-configuring-functions.md", "0542-configuring-maximum-duration-for-vercel-functions.md"]
last_updated: "2026-04-03T23:47:21.735Z"
---

# Advanced Configuration

For an advanced configuration, you can create a `vercel.json` file to use [Runtimes](/docs/functions/runtimes) and other customizations. To view more about the properties you can customize, see the [Configuring Functions](/docs/functions/configuring-functions) and [Project config with vercel.json](/docs/project-configuration).

If your use case requires that you work asynchronously with the results of a function invocation, you may need to consider a queuing, pooling, or [streaming](/docs/functions/streaming-functions) approach because of how functions are created on Vercel.

## Adding utility files to the `/api` directory

Sometimes, you need to place extra code files, such as `utils.js` or `my-types.d.ts`, inside the `/api` folder. To avoid turning these files into functions, Vercel ignores files with the following characters:

- Files that start with an underscore, `_`
- Files that start with `.`
- Files that end with `.d.ts`

If your file uses any of the above, it will **not** be turned into a function.

## Bundling Vercel Functions

In order to optimize resources, Vercel uses a process to bundle as many routes as possible into a single Vercel Function.

To provide more control over the bundling process, you can use the [`functions` property](/docs/project-configuration#functions) in your `vercel.json` file to define the configuration for a route. If a configuration is present, Vercel will bundle functions based on the configuration first. Vercel will then bundle together the remaining routes, optimizing for how many functions are created.

This bundling process is currently only enabled for Next.js, but it will be enabled in other scenarios in the future.

> For \['other']:

In the following example,  will be bundled separately from  since each has a different configuration:

> For \['nextjs']:

In the following example,  will be bundled separately from  since each has a different configuration:

> For \['nextjs-app']:

In the following example,  will be bundled separately from  since each has a different configuration:

```js filename="vercel.json" framework=nextjs
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "pages/api/hello.js": {
      "memory": 3009,
      "maxDuration": 60
    },
    "pages/api/another.js": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```

```ts filename="vercel.json" framework=nextjs
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "pages/api/hello.ts": {
      "memory": 3009,
      "maxDuration": 60
    },
    "pages/api/another.ts": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```

```js filename="vercel.json" framework=other
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/hello.js": {
      "memory": 3009,
      "maxDuration": 60
    },
    "api/another.js": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```

```ts filename="vercel.json" framework=other
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/hello.ts": {
      "memory": 3009,
      "maxDuration": 60
    },
    "api/another.ts": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```

```js filename="vercel.json" framework=nextjs-app
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "app/api/hello/route.js": {
      "memory": 3009,
      "maxDuration": 60
    },
    "app/api/another/route.js": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```

```ts filename="vercel.json" framework=nextjs-app
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "app/api/hello/route.ts": {
      "memory": 3009,
      "maxDuration": 60
    },
    "app/api/another/route.ts": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```


