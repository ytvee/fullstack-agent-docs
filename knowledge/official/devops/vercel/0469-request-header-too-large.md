---
id: "vercel-0469"
title: "REQUEST_HEADER_TOO_LARGE"
description: "Request header size exceeds the permissible limit."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/REQUEST_HEADER_TOO_LARGE"
tags: ["request", "header", "too", "large", "request-header-too-large", "troubleshoot"]
related: ["0423-fallback-body-too-large.md", "0426-function-payload-too-large.md", "0427-function-response-payload-too-large.md"]
last_updated: "2026-04-03T23:47:20.604Z"
---

# REQUEST_HEADER_TOO_LARGE

The `REQUEST_HEADER_TOO_LARGE` error occurs when the size of the request headers in your function and [Routing Middleware](/docs/routing-middleware) exceeds the allowed limits. Specifically, individual request headers must not exceed 16 KB, and the combined size of all headers, including the header names, must not exceed 32 KB.

This issue often arises from excessively large headers in a request. On Vercel, applications may have custom headers, which, if overly large, can trigger this error during server request processing.

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Limit header size:** Ensure that the size of each request header does not exceed 16 KB
2. **Manage total header size:** Monitor and control the combined size of all headers, keeping it under 32 KB
3. **Review cookies:** Since cookies are included in the header, it's crucial to limit their size as part of the overall header size


