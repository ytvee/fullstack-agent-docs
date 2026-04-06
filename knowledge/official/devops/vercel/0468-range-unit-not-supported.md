---
id: "vercel-0468"
title: "RANGE_UNIT_NOT_SUPPORTED"
description: "The unit identifier of the Range header in the request is not supported. This is a request error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/RANGE_UNIT_NOT_SUPPORTED"
tags: ["range", "unit", "not", "supported", "range-unit-not-supported", "troubleshoot"]
related: ["0466-range-missing-unit.md", "0464-range-end-not-valid.md", "0465-range-group-not-valid.md"]
last_updated: "2026-04-03T23:47:20.601Z"
---

# RANGE_UNIT_NOT_SUPPORTED

The `RANGE_UNIT_NOT_SUPPORTED` error occurs when the unit identifier of the `Range` header in a request is not supported by the server. The `Range` header is used to request a specific portion of a resource from the server, and the unit identifier indicates the unit in which the range is specified, such as bytes.

**Error Code:** `416`

**Name:** Requested Range Not Satisfiable

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Verify supported Range units:** Check the documentation for the server or service you are interacting with to determine the supported range units
2. **Correct Range unit:** If the `Range` header in your request specifies an unsupported unit, correct it to use a supported unit
3. **Check configuration:** If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure a supported unit identifier is being used
4. **Debugging:** If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests


