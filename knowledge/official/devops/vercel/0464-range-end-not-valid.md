---
id: "vercel-0464"
title: "RANGE_END_NOT_VALID"
description: "The end value of the Range header in the request is invalid. This is a request error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/RANGE_END_NOT_VALID"
tags: ["range", "end", "not", "valid", "range-end-not-valid", "troubleshoot"]
related: ["0465-range-group-not-valid.md", "0467-range-start-not-valid.md", "0468-range-unit-not-supported.md"]
last_updated: "2026-04-03T23:47:20.592Z"
---

# RANGE_END_NOT_VALID

The `RANGE_END_NOT_VALID` error occurs when the end value of the `Range` header in a request is invalid. This header is used to request a specific portion of a resource from the server, which is useful for operations like resuming downloads or streaming media.

**Error Code:** `416`

**Name:** Requested Range Not Satisfiable

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Validate Range header values:** Ensure that the end value in the `Range` header is a valid integer. It should not be a letter, a decimal, or a scientific notation value
2. **Correct ordering:** Ensure the start value is less than the end value in the `Range` header
3. **Omit end value if necessary:** If you want to request all bytes from a certain start point to the end of the resource, you can omit the end value
4. **Check configuration:** If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure it's being set correctly
5. **Debugging:** If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests


