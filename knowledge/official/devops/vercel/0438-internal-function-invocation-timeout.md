---
id: "vercel-0438"
title: "INTERNAL_FUNCTION_INVOCATION_TIMEOUT"
description: "The internal invocation of a function timed out. This is Vercel"
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/INTERNAL_FUNCTION_INVOCATION_TIMEOUT"
tags: ["internal", "function", "invocation", "timeout", "troubleshoot", "setup"]
related: ["0422-edge-function-invocation-timeout.md", "0436-internal-edge-function-invocation-timeout.md", "0437-internal-function-invocation-failed.md"]
last_updated: "2026-04-03T23:47:20.454Z"
---

# INTERNAL_FUNCTION_INVOCATION_TIMEOUT

The `INTERNAL_FUNCTION_INVOCATION_TIMEOUT` error occurs when a function invocation takes longer than the allowed execution time. This could be due to an error within the function itself, a slow network call, or an issue with the environment in which the function is running.

**Error Code:** `504`

**Name:** Gateway Timeout

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **The function is taking too long to process a request**: Ensure that any API or database requests you make in your function respond within the [Vercel Function maximum duration](/docs/functions/limitations#max-duration) limit applicable to your plan. **If you require a longer execution**, consider enabling [Fluid compute](/docs/fluid-compute), which provides significantly longer durations and optimized performance for extended workloads.
2. **The function isn't returning a response**: The function must return an HTTP response, even if that response is an error. If no response is returned, the function will time out
3. **You have an infinite loop within your function**: Check that your function is not making an infinite loop at any stage of execution
4. **Upstream errors**: Check that any external API or database that you are attempting to call doesn't have any errors
5. A common cause for this issue is when the application contains an unhandled exception. Check the application logs, which can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view), for example:

```javascript filename="logs-url"
https://my-deployment-my-username.vercel.app/_logs
```

For more information on Vercel Functions timeouts, see [What can I do about Vercel Functions timing out?](/kb/guide/what-can-i-do-about-vercel-serverless-functions-timing-out)


