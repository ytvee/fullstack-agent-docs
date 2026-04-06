---
id: "vercel-0479"
title: "TOO_MANY_FILESYSTEM_CHECKS"
description: "Too many filesystem checks occurred while processing the request. This is a routing error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/TOO_MANY_FILESYSTEM_CHECKS"
tags: ["too", "many", "filesystem", "checks", "too-many-filesystem-checks", "troubleshoot"]
related: ["0463-optimized-external-image-too-many-redirects.md", "0475-router-too-many-has-selections.md", "0481-too-many-ranges.md"]
last_updated: "2026-04-03T23:47:20.658Z"
---

# TOO_MANY_FILESYSTEM_CHECKS

The `TOO_MANY_FILESYSTEM_CHECKS` error occurs when there are excessive filesystem checks while processing a request. This could happen during the routing process, especially when using rewrites, redirects, or any other configuration that requires checking the filesystem repeatedly.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review routing configuration**: Check the routing configuration to ensure that it is not causing excessive filesystem checks, especially in the case of [rewrites](/docs/rewrites) or [redirects](/docs/redirects#configuration-redirects).
2. **Optimize routing configuration**: Reduce the number of has routes matched on a single path. You cannot have more than 5 has routes matched on a single path
3. **Check for Loops**: Ensure there isn't any looping logic in the routing or filesystem access code that could lead to excessive filesystem checks
4. **Review application logs**: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to filesystem access or routing


