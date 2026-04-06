---
id: "vercel-0275"
title: "NO_FETCH_FROM_MIDDLEWARE"
description: "Requires that any fetch call that is depended on transitively by Next.js middleware be reviewed and approved before use."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE"
tags: ["nextjs", "no", "fetch", "middleware", "rules", "no-fetch-from-middleware"]
related: ["0256-nextjs-no-get-initial-props.md", "0253-nextjs-no-client-deps-in-middleware.md", "0255-nextjs-no-fetch-in-server-props.md"]
last_updated: "2026-04-03T23:47:18.310Z"
---

# NO_FETCH_FROM_MIDDLEWARE

> **🔒 Permissions Required**: Conformance

[Next.js middleware](https://nextjs.org/docs/advanced-features/middleware) runs
code at the Edge. This means that the code is globally distributed. When
middleware makes a `fetch` call, it may be to a backend that is not globally
distributed, in which case the latency of the middleware function will be
really slow. To prevent this, `fetch` calls that can be made from middleware are
flagged and reviewed to make sure that it looks like an appropriate use.

## Example

This check will fail when a `fetch` call is detected from Next.js middleware or
transitive dependencies used by the middleware file.

In this example, there are two files. An experiments file asynchronously
fetches experiments using `fetch`. The middleware file uses the experiments
library to fetch the experiments and then decide to rewrite the URL.

```ts filename="experiments.ts"
export async function getExperiments() {
  const res = await fetch('/experiments');
  return res.json();
}
```

```ts filename="middleware.ts"
export async function middleware(
  request: NextRequest,
  event: NextFetchEvent,
): Promise<Response> {
  const experiments = await getExperiments();

  if (experiments.includes('new-marketing-page)) {
    return NextResponse.rewrite(MARKETING_PAGE_URL);
  }
  return NextResponse.next();
}
```

## How to fix

The correct fix will depend on the specific situation. If the server that is
being called is globally distributed, then this asynchronous call may be okay.
If not, then the code should try to remove the `fetch` statement to avoid
making a request that would add latency to middleware.


