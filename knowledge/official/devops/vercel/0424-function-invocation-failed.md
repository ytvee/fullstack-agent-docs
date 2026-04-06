---
id: "vercel-0424"
title: "FUNCTION_INVOCATION_FAILED"
description: "The invocation of a function failed. This is a function error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/FUNCTION_INVOCATION_FAILED"
tags: ["function", "invocation", "failed", "function-invocation-failed", "possible-causes", "troubleshoot"]
related: ["0421-edge-function-invocation-failed.md", "0435-internal-edge-function-invocation-failed.md", "0437-internal-function-invocation-failed.md"]
last_updated: "2026-04-03T23:47:20.386Z"
---

# FUNCTION_INVOCATION_FAILED

The `FUNCTION_INVOCATION_FAILED` error occurs when a function invocation fails. This could be due to an error within the function itself, or an issue with the environment in which the function is running.

**Error Code:** `500`

**Name:** Internal Server Error

## Possible causes

- The runtime process (Node.js, Bun, Python, etc.) has crashed.
- Node.js or Bun threw an unhandled rejection/uncaught exception.

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check application logs:** Review the application logs to identify any specific errors related to the function invocation. They can be found under the [Logs tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Flogs\&title=Application+Logs)
2. **Review function code:** Ensure that the code for the function is correct and does not contain any errors or infinite loops. Use a `try/catch` block to catch any errors that might be occurring within the function code
3. **Check for unhandled exceptions:** Look for any unhandled exceptions within the function code that might be causing the invocation to fail
4. **Verify function configuration:** Double-check the function configuration to ensure that it's set up correctly, including any environment variables or other settings


