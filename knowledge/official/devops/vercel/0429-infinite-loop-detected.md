--------------------------------------------------------------------------------
title: "INFINITE_LOOP_DETECTED"
description: "An infinite loop was detected within the application."
last_updated: "2026-04-03T23:47:20.415Z"
source: "https://vercel.com/docs/errors/INFINITE_LOOP_DETECTED"
--------------------------------------------------------------------------------

# INFINITE_LOOP_DETECTED

The `INFINITE_LOOP_DETECTED` error occurs when an infinite loop is detected within the application. This error can occur when the application is making an infinite number of requests to itself, or when the application is making an infinite number of requests to an external API or database.

**Error Code:** `508`

**Name:** Loop Detected

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check the application's source code:** Look for any code that might cause an infinite loop, such as a looping fetch or an unconditional redirect
2. **Check the application's configuration:** Review any [configuration](/docs/redirects#configuration-redirects) files, such as `next.config.js` or `vercel.json`, to ensure they are not causing the infinite loop
3. **Review external API or database calls:** Ensure that any external API or database calls your application is making do not have errors or infinite loops
4. **Handle unhandled exceptions:** Check the application logs for any unhandled exceptions that might be causing the infinite loop
5. **Use Vercel's status page:** If you have tried the steps above and are still experiencing the error, check Vercel's [status page](https://www.vercel-status.com/) for any reported outages in the CDN, which can sometimes cause this error


