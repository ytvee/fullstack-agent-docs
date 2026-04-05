--------------------------------------------------------------------------------
title: "RANGE_START_NOT_VALID"
description: "The start value of the Range header in the request is invalid. This is a request error."
last_updated: "2026-04-03T23:47:20.595Z"
source: "https://vercel.com/docs/errors/RANGE_START_NOT_VALID"
--------------------------------------------------------------------------------

# RANGE_START_NOT_VALID

The `RANGE_START_NOT_VALID` error occurs when the start value of the `Range` header in a request is invalid. The `Range` header is used to request a specific portion of a resource from the server, and the start value should be a valid integer indicating the beginning of the requested range.

**Error Code:** `416`

**Name:** Requested Range Not Satisfiable

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Validate Range header values:** Ensure that the start value in the `Range` header is a valid integer. It should not be a letter, a decimal, or a scientific notation value
2. **Correct ordering:** Ensure the start value is less than the end value in the `Range` header, if an end value is specified
3. **Check configuration:** If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure it's being set correctly
4. **Debugging:** If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests


