---
id: "vercel-0416"
title: "DNS_HOSTNAME_EMPTY"
description: "An empty DNS record was received as part of the DNS response. This is a DNS error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_EMPTY"
tags: ["dns", "hostname", "empty", "dns-hostname-empty", "troubleshoot", "setup"]
related: ["0418-dns-hostname-resolved-private.md", "0419-dns-hostname-resolve-failed.md", "0420-dns-hostname-server-error.md"]
last_updated: "2026-04-03T23:47:20.353Z"
---

# DNS_HOSTNAME_EMPTY

The `DNS_HOSTNAME_EMPTY` error occurs when an empty DNS record is received as part of the DNS response while attempting to connect to a private IP from an external rewrite.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review DNS configuration:** Check the [DNS configuration](/docs/domains/working-with-dns) to ensure that it's correctly set up and doesn't have any empty or incorrect entries
2. **Check for private IP addresses:** Ensure that the request isn't attempting to connect to a private IP address from an external source
3. **Review application logs:** Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to DNS or the attempted connections


