--------------------------------------------------------------------------------
title: "NEXTJS_NO_FETCH_IN_SERVER_PROPS"
description: "Prevent relative fetch calls in getServerSideProps from being added to Next.js applications."
last_updated: "2026-04-03T23:47:18.174Z"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_FETCH_IN_SERVER_PROPS"
--------------------------------------------------------------------------------

# NEXTJS_NO_FETCH_IN_SERVER_PROPS

> **🔒 Permissions Required**: Conformance

Since both `getServerSideProps` and API routes run on the server, calling `fetch` on a non-relative
URL will trigger an additional network request.

## How to fix

Instead of using `fetch` to make a call to the API route, you can instead share the code in a shared
library or module to avoid another network request. You can then import this hared logic and call directly
within your `getServerSideProps` function, avoiding additional network requests entirely.


