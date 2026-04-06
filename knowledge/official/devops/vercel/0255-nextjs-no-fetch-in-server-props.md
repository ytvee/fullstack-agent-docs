---
id: "vercel-0255"
title: "NEXTJS_NO_FETCH_IN_SERVER_PROPS"
description: "Prevent relative fetch calls in getServerSideProps from being added to Next.js applications."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_FETCH_IN_SERVER_PROPS"
tags: ["nextjs", "no", "fetch", "server", "props", "rules"]
related: ["0256-nextjs-no-get-initial-props.md", "0258-nextjs-no-self-hosted-videos.md", "0275-no-fetch-from-middleware.md"]
last_updated: "2026-04-03T23:47:18.174Z"
---

# NEXTJS_NO_FETCH_IN_SERVER_PROPS

> **🔒 Permissions Required**: Conformance

Since both `getServerSideProps` and API routes run on the server, calling `fetch` on a non-relative
URL will trigger an additional network request.

## How to fix

Instead of using `fetch` to make a call to the API route, you can instead share the code in a shared
library or module to avoid another network request. You can then import this hared logic and call directly
within your `getServerSideProps` function, avoiding additional network requests entirely.


