---
id: "vercel-0427"
title: "FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE"
description: "The function returned a response that is too large. This is a function error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE"
tags: ["function", "response", "payload", "too", "large", "troubleshoot"]
related: ["0426-function-payload-too-large.md", "0423-fallback-body-too-large.md", "0409-body-not-a-string-from-function.md"]
last_updated: "2026-04-03T23:47:20.407Z"
---

# FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE

The `FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE` error occurs when the function returned a response that exceeds the maximum allowed size of 4.5 MB.

**Error Code:** `500`

**Name:** Response Payload Too Large

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Review response payload size:** Check the size of the response payload being returned by the function to ensure it's within the allowed limits, and does not exceed the [limit of 4.5 MB](/docs/functions/runtimes#size-limits)
2. **Reduce response payload size:** If possible, reduce the size of the response payload being returned by the function


