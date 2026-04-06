---
id: "vercel-0420"
title: "DNS_HOSTNAME_SERVER_ERROR"
description: "The DNS server was unable to fulfill the DNS request due to an internal issue or misconfiguration. This is a DNS error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_SERVER_ERROR"
tags: ["dns", "hostname", "server", "error", "dns-hostname-server-error", "troubleshoot"]
related: ["0416-dns-hostname-empty.md", "0419-dns-hostname-resolve-failed.md", "0417-dns-hostname-not-found.md"]
last_updated: "2026-04-03T23:47:20.368Z"
---

# DNS_HOSTNAME_SERVER_ERROR

The `DNS_HOSTNAME_SERVER_ERROR` error occurs when attempting to connect to a private IP from an external rewrite. This error typically means that the DNS server was unable to fulfill the DNS request due to an internal issue or misconfiguration.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review DNS configuration:** Check the [DNS configuration](/docs/domains/working-with-dns) to ensure it's correctly set up and doesn't contain any errors or misconfigurations
2. **Inspect network connectivity:** Ensure that there are no network issues that could be affecting the DNS resolution
3. **Check DNS server logs:** Review the logs of the DNS server for any warnings or errors that might indicate what's causing the issue
4. **Verify domain registration:** Ensure that the domain has been [registered](/docs/domains/working-with-domains/view-and-search-domains) and is currently active


