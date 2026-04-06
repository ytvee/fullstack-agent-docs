---
id: "vercel-0457"
title: "MIDDLEWARE_RUNTIME_DEPRECATED"
description: "A middleware is using a deprecated runtime."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/MIDDLEWARE_RUNTIME_DEPRECATED"
tags: ["middleware-runtime-deprecated", "middleware", "runtime", "deprecated", "troubleshoot", "setup"]
related: ["0453-microfrontends-middleware-error.md", "0455-middleware-invocation-failed.md", "0456-middleware-invocation-timeout.md"]
last_updated: "2026-04-03T23:47:20.535Z"
---

# MIDDLEWARE_RUNTIME_DEPRECATED

The `MIDDLEWARE_RUNTIME_DEPRECATED` error occurs when a middleware is using a deprecated runtime. This error can occur when a middleware is using a runtime that is no longer supported by the platform.

**Error Code:** `503`

**Name:** Middleware Runtime Deprecated

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Identify the affected project:** Use [Vercel Logs](/docs/observability/runtime-logs) to identify if your project is experiencing this error. Look for the `MIDDLEWARE_RUNTIME_DEPRECATED` error in your project's runtime logs.
2. **Locate the middleware:** Once you've identified the project, check if it has a `middleware.js` or `middleware.ts` file in the root directory or uses Routing Middleware in any way.
3. **Redeploy the project:** Redeploy the project to automatically upgrade to the latest supported runtime version. However, if the redeploy fails, you may need to:
   - **Update your Node.js version:** Check your project's Node.js version setting in the Vercel dashboard or `package.json` and update it to a [supported version](/docs/functions/runtimes/node-js#node.js-version)
   - **Update dependencies:** Outdated dependencies may not be compatible with newer Node.js versions. Update your `package.json` dependencies to their latest compatible versions before redeploying


