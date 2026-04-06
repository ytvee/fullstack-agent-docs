---
id: "vercel-0428"
title: "FUNCTION_THROTTLED"
description: "The function you are trying to call has exceeded the rate limit."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/FUNCTION_THROTTLED"
tags: ["function", "throttled", "function-throttled", "troubleshoot", "setup", "how-to"]
related: ["0409-body-not-a-string-from-function.md", "0411-deployment-deleted.md", "0421-edge-function-invocation-failed.md"]
last_updated: "2026-04-03T23:47:20.411Z"
---

# FUNCTION_THROTTLED

The `FUNCTION_THROTTLED` error occurs when your Vercel Functions exceed the concurrent execution limit, often due to a sudden request spike or backend API issues. For more information, see [What should I do if I receive a 503 error on Vercel?](/kb/guide/what-should-i-do-if-i-receive-a-503-error-on-vercel).

Although this is a rare scenario, this error can also occur when Vercel's infrastructure encounters an abnormal system load and tries to mitigate the impact autonomously.

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check application logs**: Review the application logs to identify any specific errors related to the Vercel Function being invoked. For example, your function might be waiting for a slow backend API without a reasonable timeout. These information can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view), as well as the [Observability](/docs/observability) section in the sidebar in the Vercel dashboard.
2. **Handle request spikes**: If you're experiencing a sudden spike in requests, consider using the [Vercel Firewall](/docs/vercel-firewall) to block unwanted traffic, or enabling [Rate Limiting](/docs/security/vercel-waf/rate-limiting) to limit the number of requests per second.
3. **Optimize your function**: Review your function code to ensure it's optimized for performance. For example, you can use [Vercel's CDN Cache](/docs/cdn-cache) to cache responses and reduce the number of invocations. You can also enable [fluid compute](/docs/fluid-compute) to handle more requests concurrently on a single function instance.


