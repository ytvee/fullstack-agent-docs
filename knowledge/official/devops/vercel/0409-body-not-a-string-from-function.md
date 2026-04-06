---
id: "vercel-0409"
title: "BODY_NOT_A_STRING_FROM_FUNCTION"
description: "The function returned a non-string body. This is a function error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/BODY_NOT_A_STRING_FROM_FUNCTION"
tags: ["body", "not", "string", "function", "troubleshoot", "setup"]
related: ["0421-edge-function-invocation-failed.md", "0413-deployment-not-found.md", "0414-deployment-not-ready-redirecting.md"]
last_updated: "2026-04-03T23:47:20.309Z"
---

# BODY_NOT_A_STRING_FROM_FUNCTION

The `BODY_NOT_A_STRING_FROM_FUNCTION` error occurs when a function returns a body that is not a string. It's essential that functions return a string body to ensure that they can be correctly processed and executed.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check function return type:** Ensure that the function is structured to return a string. If the function is returning a different data type, modify the function to return a string, using `JSON.stringify()` if necessary
2. **Review function code:** Inspect the function code for any logic that might cause a non-string value to be returned
3. **Check data types:** If the function is processing input data or retrieving data from external sources, ensure that the data is being correctly converted to a string before being returned
4. **Review function logs:** Check the [function logs](/docs/runtime-logs#type) for any errors or warnings that might indicate why a non-string value is being returned


