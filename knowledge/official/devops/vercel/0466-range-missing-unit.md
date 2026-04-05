--------------------------------------------------------------------------------
title: "RANGE_MISSING_UNIT"
description: "The unit identifier of the Range header in the request is missing. This is a request error."
last_updated: "2026-04-03T23:47:20.588Z"
source: "https://vercel.com/docs/errors/RANGE_MISSING_UNIT"
--------------------------------------------------------------------------------

# RANGE_MISSING_UNIT

The `RANGE_MISSING_UNIT` error occurs when the unit identifier of the `Range` header in a request is missing. The `Range` header is used to request a specific portion of a resource from the server, and the unit identifier indicates the unit in which the range is specified, such as bytes.

**Error Code:** `416`

**Name:** Requested Range Not Satisfiable

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Specify unit identifier:** Ensure that the `Range` header in your request specifies a unit identifier like `bytes`
2. **Check configuration:** If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure the unit identifier is being included
3. **Verify syntax:** Verify that the syntax of the `Range` header is correct and follows the format `unit=range-start-range-end`, for example, `bytes=0-999`
4. **Debugging:** If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests


