--------------------------------------------------------------------------------
title: "TOO_MANY_RANGES"
description: "Too many ranges have been specified in the Range header of the request. This is a request error."
last_updated: "2026-04-03T23:47:20.668Z"
source: "https://vercel.com/docs/errors/TOO_MANY_RANGES"
--------------------------------------------------------------------------------

# TOO_MANY_RANGES

The `TOO_MANY_RANGES` error occurs when too many ranges have been specified in the `Range` header of a request. The `Range` header is used to request specific portions of a resource from the server, and specifying too many ranges can lead to an excessive load on the server.

**Error Code:** `416`

**Name:** Requested Range Not Satisfiable

## Troubleshoot

To troubleshoot this error, follow these steps:

To troubleshoot this error, follow these steps:

1. **Reduce number of Ranges:** Reduce the number of ranges specified in the `Range` header to a reasonable amount
2. **Check configuration:** If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure a reasonable number of ranges are being specified
3. **Verify server capabilities:** Check the documentation for the server or service you are interacting with to determine the maximum number of supported ranges
4. **Debugging:** If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests


