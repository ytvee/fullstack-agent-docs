---
id: "vercel-0472"
title: "ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR"
description: "Connection error occurred while routing to an external target. This is a routing error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR"
tags: ["router", "external", "target", "connection", "error", "troubleshoot"]
related: ["0473-router-external-target-error.md", "0474-router-external-target-handshake-error.md", "0471-router-cannot-match.md"]
last_updated: "2026-04-03T23:47:20.632Z"
---

# ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR

The `ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR` error occurs when there is a connection error while routing to an external target. This could happen due to network issues, incorrect routing configuration, or the external target being unreachable.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check network connectivity:** Ensure that the network connectivity between your deployment and the external target is stable
2. **Verify external target availability:** Make sure the external target is online and reachable
3. **Review routing configuration:** Check the [routing configuration](/docs/redirects#configuration-redirects) to ensure that it is correctly set up to route to the external target
4. **Inspect firewall settings:** Verify that there are no firewall settings blocking the connection to the external target
5. **Review application logs:** Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to routing or network connectivity


