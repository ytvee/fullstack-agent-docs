--------------------------------------------------------------------------------
title: "DNS_HOSTNAME_RESOLVED_PRIVATE"
description: "The DNS hostname resolved to a private IP address or an IPv6 address during an external rewrite. This is a DNS error."
last_updated: "2026-04-03T23:47:20.361Z"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_RESOLVED_PRIVATE"
--------------------------------------------------------------------------------

# DNS_HOSTNAME_RESOLVED_PRIVATE

The `DNS_HOSTNAME_RESOLVED_PRIVATE` error occurs when attempting to connect to a private IP from an external rewrite, or when trying to connect to an IPv6 address. The error indicates that the DNS hostname resolved to a private or inaccessible IP address.

Examples of such IPs would be:

- `192.0.0.1`
- `168.0.0.1`

**Error Code:** `404`

**Name:** Not Found

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check the IP address:** Ensure that the IP address you are trying to connect to is publicly accessible and not a private or reserved IP address
2. **Inspect network connectivity:** Ensure that there are no network issues that could be affecting the DNS resolution
3. **Review application logs:** Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to DNS or the attempted connections


