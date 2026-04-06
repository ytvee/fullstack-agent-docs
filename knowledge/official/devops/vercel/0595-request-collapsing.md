---
id: "vercel-0595"
title: "Request Collapsing"
description: "Learn how Vercel"
category: "vercel-frameworks"
subcategory: "incremental-static-regeneration"
type: "guide"
source: "https://vercel.com/docs/incremental-static-regeneration/request-collapsing"
tags: ["request", "collapsing", "request-collapsing", "how-request-collapsing-works", "example", "supported-features"]
related: ["0594-getting-started-with-isr.md", "0593-incremental-static-regeneration-isr.md", "0592-isr-usage-and-pricing.md"]
last_updated: "2026-04-03T23:47:23.147Z"
---

# Request Collapsing

Vercel uses **request collapsing** to protect uncached routes during high traffic. It reduces duplicate work by combining concurrent requests into a single function invocation within the same region. This feature is especially valuable for high-scale applications.

## How request collapsing works

When a request for an uncached path arrives, Vercel invokes the origin [function](/docs/functions) and stores the response in the [cache](/docs/cdn-cache). In most cases, any following requests are served from this cached response.

However, if multiple requests arrive while the initial function is still processing, the cache is still empty. Instead of triggering additional invocations, Vercel's CDN collapses these concurrent requests into the original one. They wait for the first response to complete, then all receive the same result.

This prevents overwhelming the origin with duplicate work during traffic spikes and helps ensure faster, more stable performance.

Vercel also applies request collapsing when serving [STALE](/docs/headers/response-headers#stale) responses (with [stale-while-revalidate](/docs/headers/cache-control-headers#stale-while-revalidate) semantics), ensuring that concurrent background revalidation of multiple requests is collapsed into a single invocation.

### Example

Suppose a new blog post is published and receives 1,000 requests at once. Without request collapsing, each request would trigger a separate function invocation, which could overload the backend and slow down responses, causing a [**cache stampede**](https://en.wikipedia.org/wiki/Cache_stampede).

With request collapsing, Vercel handles the first request, then holds the remaining 999 requests until the initial response is ready. Once cached, the response is sent to all users who requested the post.

## Supported features

Request collapsing is supported for:

- [Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration)
- [Image Optimization](/docs/image-optimization)


