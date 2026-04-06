---
id: "vercel-0450"
title: "INVALID_IMAGE_OPTIMIZE_REQUEST"
description: "The query string is using an invalid value for q, w, or url parameters. This is a request error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/INVALID_IMAGE_OPTIMIZE_REQUEST"
tags: ["invalid-image-optimize-request", "invalid", "optimize", "request", "troubleshoot", "setup"]
related: ["0451-invalid-request-method.md", "0461-optimized-external-image-request-invalid.md", "0452-malformed-request-header.md"]
last_updated: "2026-04-03T23:47:20.500Z"
---

# INVALID_IMAGE_OPTIMIZE_REQUEST

The `INVALID_IMAGE_OPTIMIZE_REQUEST` error occurs when the query string is using an invalid value for `q` (quality) or `w` (width), or `url` returns a non-image response.

**Error Code:** `400`

**Name:** Bad Request

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check for typos:** Verify that there are no typos in the parameter names or values
2. **Review request format:** Ensure that the request URL is correctly formatted and includes the required parameters
   - The `q` parameter controls the quality of the image and must follow these rules:
     - The `q` parameter must be an integer
     - The `q` integer must be greater than or equal to 1
     - The `q` integer must be less than or equal to 100
     - The `q` integer must be the same as one specified in [`qualities`](https://nextjs.org/docs/app/api-reference/components/image#qualities), if defined
   - The `w` parameter defines the width of the image and must follow these rules:
     - The `w` parameter must be an integer
     - The `w` integer must be the same as one specified in [`deviceSizes`](https://nextjs.org/docs/app/api-reference/components/image#devicesizes) or [`imageSizes`](https://nextjs.org/docs/app/api-reference/components/image#imagesizes) in your [`next.config.js`](https://nextjs.org/docs/app/api-reference/next-config-js).
   - The `url` parameter specifies the image location and must follow these rules:
     - The `url` parameter must start with `/`, `http://`, or `https://`
     - The `url` parameter must match one of the configured [`remotePatterns`](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns) or [`localPatterns`](https://nextjs.org/docs/app/api-reference/components/image#localpatterns) in your `next.config.js`
     - The `url` parameter must have a `Content-Type` header that starts with `image/`
     - The `url` parameter must have a response body **less than 300 MB** (or **less than 100 MB for hobby**), otherwise the image won't be optimized

Run `next dev` locally to reproduce the error and get additional details.


