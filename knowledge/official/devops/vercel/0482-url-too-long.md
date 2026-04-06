---
id: "vercel-0482"
title: "URL_TOO_LONG"
description: "The URL of the request is too long. This is a request error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/URL_TOO_LONG"
tags: ["url", "too", "long", "url-too-long", "troubleshoot", "setup"]
related: ["0481-too-many-ranges.md", "0431-internal-cache-key-too-long.md", "0450-invalid-image-optimize-request.md"]
last_updated: "2026-04-03T23:47:20.671Z"
---

# URL_TOO_LONG

The `URL_TOO_LONG` error occurs when the URL of the request exceeds the maximum length allowed by the CDN (**14 KB**). Long URLs can be a result of long query strings, lengthy path segments, or an excessive number of path segments.

**Error Code:** `414`

**Name:** Request-URI Too Long

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Shorten the URL:** Simplify the URL by reducing the length of the path segments and the query string
2. **Reduce query parameters:** If the URL has many query parameters, consider reducing the number of parameters or use `POST` method instead where the parameters can be sent in the body of the request
3. **Use POST method:** If the long URL is a result of a form submission, consider changing the form method from `GET` to `POST`
4. **Check for unintended redirection:** Ensure there isn't a redirection loop or logic that is appending to the URL causing it to grow in length with each redirect


