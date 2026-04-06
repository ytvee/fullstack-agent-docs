---
id: "vercel-0471"
title: "ROUTER_CANNOT_MATCH"
description: "The router cannot match the route to any of the known patterns. This is a routing error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/ROUTER_CANNOT_MATCH"
tags: ["router", "cannot", "match", "router-cannot-match", "troubleshoot", "setup"]
related: ["0455-middleware-invocation-failed.md", "0456-middleware-invocation-timeout.md", "0472-router-external-target-connection-error.md"]
last_updated: "2026-04-03T23:47:20.628Z"
---

# ROUTER_CANNOT_MATCH

The `ROUTER_CANNOT_MATCH` error occurs when the router is unable to match the requested route to any of the known patterns. This could happen due to a misconfiguration in the routing setup or an erroneous request path.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review routing configuration:** Check the [routing configuration](/docs/redirects#configuration-redirects) to ensure that it is correctly set up to handle the requested route
2. **Verify request path:** Ensure that the request path is correct and adheres to the expected patterns defined in the routing configuration
3. **Check for typos:** Look for any typos or misconfigurations in the routing setup that might be causing the mismatch
4. **Review application logs:** Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to routing


