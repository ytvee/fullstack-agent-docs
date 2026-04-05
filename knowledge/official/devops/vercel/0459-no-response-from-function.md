--------------------------------------------------------------------------------
title: "NO_RESPONSE_FROM_FUNCTION"
description: "The application did not respond correctly, this is likely due to an exception being thrown from the function handler."
last_updated: "2026-04-03T23:47:20.560Z"
source: "https://vercel.com/docs/errors/NO_RESPONSE_FROM_FUNCTION"
--------------------------------------------------------------------------------

# NO_RESPONSE_FROM_FUNCTION

The `NO_RESPONSE_FROM_FUNCTION` error occurs when a function invocation completes without returning a response. This might happen if the function encounters an error that prevents it from responding, or if it fails to generate a response within the allowed execution time.

Potential causes include:

- A global uncaught exception
- A global unhandled rejection
- A deployment that introduced incorrect syntax

**Error Code:** `502`

**Name:** Bad Gateway

#### Troubleshoot

To troubleshoot this error, follow these steps:

1. **Verify return statements:** Ensure that the function has the necessary return statements to generate a response
2. **Check the function logs**: Open the [realtime request logs](/docs/logs#function-logs) for the application in a separate tab - this tab **must be kept open** while reproducing the error
3. **Review realtime logs**: Repeat the application behavior that led to the error being thrown and review the realtime request logs where it will now show
   - Use the information contained within the error logs to understand where the function is failing
4. **Use Log Drains**: Create a [Log Drain](/docs/drains) if you do not have one yet, to persist errors from Vercel functions
5. **Check external dependencies:** If the function relies on external services or APIs, ensure they are responding in a timely manner


