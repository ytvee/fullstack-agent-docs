---
id: "vercel-0452"
title: "MALFORMED_REQUEST_HEADER"
description: "The MALFORMED_REQUEST_HEADER error occurs when a request contains an improperly formatted or invalid header. This is a request error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/MALFORMED_REQUEST_HEADER"
tags: ["malformed", "request", "header", "malformed-request-header", "troubleshoot", "setup"]
related: ["0447-internal-static-request-failed.md", "0450-invalid-image-optimize-request.md", "0451-invalid-request-method.md"]
last_updated: "2026-04-03T23:47:20.519Z"
---

# MALFORMED_REQUEST_HEADER

The `MALFORMED_REQUEST_HEADER` error signifies that a request made to the server includes a header that is incorrectly formatted or contains invalid data. This could be due to syntax errors, incorrect header field names, or incompatible header values.

**Error Code:** `400`

**Name:** Bad Request

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Inspect request headers**: Review the headers in your request. Ensure that they are correctly formatted and adhere to the [HTTP standard](https://developer.mozilla.org/en-US/docs/Glossary/Request_header)
2. **Validate UTF-8 encoding**: Confirm that all request headers, especially cookie values, are valid UTF-8 strings. Non-UTF-8 characters in headers, particularly in the cookie header, often cause this error
3. **Examine Vercel Function behavior**: Since this error is specific to Vercel functions, verify the functionality and responses of your Vercel functions. Ensure they are correctly handling request headers and not contributing to malformed responses


