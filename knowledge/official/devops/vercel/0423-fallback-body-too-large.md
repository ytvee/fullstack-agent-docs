---
id: "vercel-0423"
title: "FALLBACK_BODY_TOO_LARGE"
description: "The fallback body is too large for the cache. This is a cache error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/FALLBACK_BODY_TOO_LARGE"
tags: ["fallback", "body", "too", "large", "fallback-body-too-large", "troubleshoot"]
related: ["0426-function-payload-too-large.md", "0427-function-response-payload-too-large.md", "0469-request-header-too-large.md"]
last_updated: "2026-04-03T23:47:20.382Z"
---

# FALLBACK_BODY_TOO_LARGE

The `FALLBACK_BODY_TOO_LARGE` error indicates that the size of the fallback body exceeds the maximum cache limit. This error typically occurs in prerendered pages when the response body of a fallback page is larger than the cache can accommodate. Notably, if the fallback exceeds 10MB, it cannot be cached.

**Error Code:** `502`

**Name:** Prerender fallback file is too big for cache

## Troubleshoot

To resolve this error, consider the following steps:

1. **Review response size:** Examine the size of the response body for the affected page. If it's too large, try to reduce the content size
2. **Optimize content:** Minimize HTML, CSS, and JavaScript on the fallback page Remove unnecessary assets or data to reduce the page size
3. **Implement pagination:** If the large response body is due to extensive datasets, consider using pagination. This divides the data into smaller, manageable sections
4. **Dynamic data loading:** Where possible, load data dynamically on the client-side instead of sending all data in the initial server response

To prevent this error, ensure that the size of the fallback page is less than 10 MB.


