---
id: "vercel-0440"
title: "INTERNAL_FUNCTION_NOT_READY"
description: "The internal function is not ready to be invoked. This is a Vercel error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/INTERNAL_FUNCTION_NOT_READY"
tags: ["internal", "function", "not", "ready", "internal-function-not-ready", "troubleshoot"]
related: ["0439-internal-function-not-found.md", "0409-body-not-a-string-from-function.md", "0414-deployment-not-ready-redirecting.md"]
last_updated: "2026-04-03T23:47:20.461Z"
---

# INTERNAL_FUNCTION_NOT_READY

The `INTERNAL_FUNCTION_NOT_READY` error occurs when an attempt is made to invoke a function before it is ready to accept requests. This might happen if the function is still being deployed, initialized, or if there is a misconfiguration preventing the function from becoming ready.

**Error Code:** `500`

**Name:** Internal Server Error

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Verify deployment status:** Ensure that the function has been successfully deployed and the deployment process has completed
2. **Check initialization logs:** Review the function's initialization logs to identify any errors or warnings that might indicate why the function is not ready
3. **Review configuration:** Ensure that the function and environment configurations are correct and that there are no misconfigurations preventing the function from becoming ready
4. **Check dependencies:** Verify that all dependencies required by the function are available and correctly configured


