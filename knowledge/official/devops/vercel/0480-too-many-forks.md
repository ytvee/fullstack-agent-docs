---
id: "vercel-0480"
title: "TOO_MANY_FORKS"
description: "An error occurred in the application when matching too many conditional routes. You cannot have more than 5 \"
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/TOO_MANY_FORKS"
tags: ["too", "many", "forks", "too-many-forks", "setup", "how-to"]
related: ["0481-too-many-ranges.md", "0479-too-many-filesystem-checks.md", "0425-function-invocation-timeout.md"]
last_updated: "2026-04-03T23:47:20.663Z"
---

# TOO_MANY_FORKS

The `TOO_MANY_FORKS` error occurs when too many forks are generated while processing the request. This usually happens when matching too many conditional routes, which could lead to a loop or excessive resource usage.

You cannot have more than 5 `has` routes matched on a single path.

**Error Code:** `502`

**Name:** Bad Gateway

#### Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review routing configuration**: Reduce the number of [rewrites](/docs/rewrites), [redirects](/docs/redirects#configuration-redirects), or [headers](/docs/headers) with a `has` key (conditional route) that match the erroring request path
2. **Check for recursive logic**: Ensure there isn't any recursive logic in the routing configuration that could lead to excessive forking
3. **Handle unhandled exceptions**: Check the [application logs](/docs/deployments/logs) for any unhandled exceptions that may be causing the error


