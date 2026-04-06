---
id: "vercel-0475"
title: "ROUTER_TOO_MANY_HAS_SELECTIONS"
description: "The router has too many selections. This is a routing error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/ROUTER_TOO_MANY_HAS_SELECTIONS"
tags: ["router", "too", "many", "has", "selections", "troubleshoot"]
related: ["0479-too-many-filesystem-checks.md", "0463-optimized-external-image-too-many-redirects.md", "0481-too-many-ranges.md"]
last_updated: "2026-04-03T23:47:20.644Z"
---

# ROUTER_TOO_MANY_HAS_SELECTIONS

The `ROUTER_TOO_MANY_HAS_SELECTIONS` error occurs when the router encounters too many selections while processing the request. This could happen due to misconfiguration or a complex routing setup that exceeds the router's capabilities.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review routing configuration:** Check the [routing configuration](/docs/redirects#configuration-redirects) to ensure it's correctly set up and doesn't contain excessive selections
2. **Simplify routing setup:** If possible, simplify the routing setup to reduce the number of selections the router has to process
3. **Check for recursive or looping logic:** Ensure there isn't any recursive or looping logic in the routing configuration that could lead to excessive selections
4. **Review application logs:** Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to routing or selections


