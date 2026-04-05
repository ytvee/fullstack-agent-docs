--------------------------------------------------------------------------------
title: "RANGE_GROUP_NOT_VALID"
description: "The group value of the Range header in the request is invalid. This is a request error."
last_updated: "2026-04-03T23:47:20.583Z"
source: "https://vercel.com/docs/errors/RANGE_GROUP_NOT_VALID"
--------------------------------------------------------------------------------

# RANGE_GROUP_NOT_VALID

The `RANGE_GROUP_NOT_VALID` error occurs when the group value of the `Range` header in a request is invalid. This header is used to request a specific portion of a resource from the server, and the group value can be used to specify multiple ranges or a set of subranges.

**Error Code:** `416`

**Name:** Requested Range Not Satisfiable

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Validate Range header values:** Ensure that the group value in the `Range` header is a valid format. It should correctly specify the range or subranges you wish to retrieve
2. **Correct grouping:** Ensure that the group value is correctly formatted and contains valid range specifications
3. **Check configuration:** If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure it's being set correctly
4. **Debugging:** If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests


