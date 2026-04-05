--------------------------------------------------------------------------------
title: "SET_COOKIE_VALIDATION"
description: "Prevents usage of cookies that do not conform to the allowed cookie policy."
last_updated: "2026-04-03T23:47:18.435Z"
source: "https://vercel.com/docs/conformance/rules/SET_COOKIE_VALIDATION"
--------------------------------------------------------------------------------

# SET_COOKIE_VALIDATION

> **🔒 Permissions Required**: Conformance

It's a good practice to enforce a cookie policy across a workspace to ensure only
certain cookies are allowed to be set.

## How to fix

Engineers should reach out to the appropriate engineer(s) or team(s) for a
review of the defined cookie and request the cookie name be added to the
allowed cookie policy list. This can be set in the `conformance.config.jsonc` configuration
file as follows:

```json filename="conformance.config.jsonc"
"SET_COOKIE_VALIDATION": {
  "cookieAllowList": ["some-cookie-name"]
}
```


