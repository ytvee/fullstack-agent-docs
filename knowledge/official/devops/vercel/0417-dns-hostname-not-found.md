---
id: "vercel-0417"
title: "DNS_HOSTNAME_NOT_FOUND"
description: "The domain does not exist, resulting in an NXDOMAIN error during DNS resolution. This is a DNS error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_NOT_FOUND"
tags: ["dns", "hostname", "not", "found", "dns-hostname-not-found", "troubleshoot"]
related: ["0418-dns-hostname-resolved-private.md", "0419-dns-hostname-resolve-failed.md", "0413-deployment-not-found.md"]
last_updated: "2026-04-03T23:47:20.357Z"
---

# DNS_HOSTNAME_NOT_FOUND

The `DNS_HOSTNAME_NOT_FOUND` error occurs when there's an `NXDOMAIN` error during the DNS resolution while attempting to connect to a private IP from an external rewrite. This error indicates that the domain being requested does not exist.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review DNS configuration:** Check the [DNS configuration](/docs/domains/working-with-dns) to ensure that the domain being requested is correctly set up and registered
2. **Verify domain registration:** Ensure that the domain has been [registered](/docs/domains/working-with-domains/view-and-search-domains) and is currently active
3. **Check for private IP addresses:** Ensure that the request isn't attempting to connect to a private IP address from an external source
4. **Review application logs:** Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to DNS or the attempted connections


