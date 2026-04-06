---
id: "vercel-0253"
title: "NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE"
description: "Disallows dependency on client libraries inside of middleware to improve performance of middleware."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE"
tags: ["nextjs", "no", "client", "deps", "middleware", "rules"]
related: ["0275-no-fetch-from-middleware.md", "0256-nextjs-no-get-initial-props.md", "0250-nextjs-no-async-layout.md"]
last_updated: "2026-04-03T23:47:18.167Z"
---

# NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE

> **🔒 Permissions Required**: Conformance

This check disallows dependencies on client libraries, such as `react` and
`next/router` in Next.js middleware. Since middleware runs on the server and
runs on every request, this code is not able to run any client side code and it
should have a small bundle size to improve loading and execution times.

## Example

An example of when this check could manifest is when middleware transitively
depends on a file that also uses `react` within the same file.

For example:

```ts filename="experiments.ts"
import { createContext, type Context } from 'react';

export function createExperimentContext(): Context<ExperimentContext> {
  return createContext<ExperimentContext>({
    experiments: () => {
      return EXPERIMENT_DEFAULTS;
    },
  });
}

export async function getExperiments() {
  return activeExperiments;
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

In this example, the `experiments.ts` file both fetches the active experiments
as well as provides helper functions to use experiments on the client in React.

## How to fix

Client dependencies used or transitively depended on by middleware files should
be refactored to avoid depending on the client libraries. In the example above,
the code that is used by middleware to fetch experiments should be moved to a
separate file from the code that provides the React functionality.


