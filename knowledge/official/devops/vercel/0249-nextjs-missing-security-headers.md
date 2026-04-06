---
id: "vercel-0249"
title: "NEXTJS_MISSING_SECURITY_HEADERS"
description: "Requires that security headers are set correctly for Next.js apps and contain valid directives."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_SECURITY_HEADERS"
tags: ["nextjs", "missing", "security", "headers", "rules", "example"]
related: ["0242-eslint-next-rules-required.md", "0275-no-fetch-from-middleware.md", "0245-nextjs-missing-modularize-imports.md"]
last_updated: "2026-04-03T23:47:18.131Z"
---

# NEXTJS_MISSING_SECURITY_HEADERS

> **🔒 Permissions Required**: Conformance

Security headers are important to set to improve the security of your application.
Security headers can be set for all routes in \[`next.config.js` files]
(https://nextjs.org/docs/advanced-features/security-headers). This
conformance check requires that the security headers are set and use a valid
value.

Required headers:

- Content-Security-Policy
- Strict-Transport-Security
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy

## Example

```sh
Conformance errors found!

A Conformance error occurred in test "NEXTJS_MISSING_SECURITY_HEADERS".

The security header "Strict-Transport-Security" is not set correctly. The "includeSubDomains" directive should be used in conjunction with the "preload" directive.

To find out more information and how to fix this error, visit
/docs/conformance/rules/NEXTJS_MISSING_SECURITY_HEADERS.

If this violation should be ignored, add the following entry to
/apps/docs/.allowlists/NEXTJS_MISSING_SECURITY_HEADERS.allowlist.json
and get approval from the appropriate person.

{
  "testName": "NEXTJS_MISSING_SECURITY_HEADERS",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "docs"
  },
  "details": {
    "header": "Strict-Transport-Security"
  }
}
```

## How to fix

Follow the [Next.js security headers documentation](https://nextjs.org/docs/advanced-features/security-headers)
to fix this Conformance test. That document will walk through each of the
headers and also links to further documentation to understand what the headers
do and how to set the best values for your application.


