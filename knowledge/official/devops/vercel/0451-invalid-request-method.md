---
id: "vercel-0451"
title: "INVALID_REQUEST_METHOD"
description: "The request method used is invalid or not supported. This is a request error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/INVALID_REQUEST_METHOD"
tags: ["invalid", "request", "method", "invalid-request-method", "troubleshoot", "setup"]
related: ["0450-invalid-image-optimize-request.md", "0461-optimized-external-image-request-invalid.md", "0452-malformed-request-header.md"]
last_updated: "2026-04-03T23:47:20.506Z"
---

# INVALID_REQUEST_METHOD

The `INVALID_REQUEST_METHOD` error occurs when a request is made with a method that is either invalid or not supported by the server. This error typically happens when trying to use an HTTP method that the endpoint does not accept or recognize.

**Error Code:** `405`

**Name:** Method Not Allowed

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Verify request method:** Ensure that the HTTP request method used is correct and supported by the endpoint. Common HTTP methods include `GET`, `POST`, `PUT`, `DELETE` etc
2. **Review code:** Check the code where the request is being made to ensure the correct method is being used
3. **Test with different methods:** If possible, test the endpoint with different HTTP methods to determine if the issue is with the method or another part of the request


