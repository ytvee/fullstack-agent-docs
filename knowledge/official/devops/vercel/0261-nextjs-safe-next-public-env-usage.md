---
id: "vercel-0261"
title: "NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE"
description: "Usage process.env.NEXT_PUBLIC_* environment variables must be allowlisted."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE"
tags: ["environment-variables", "nextjs", "safe", "next", "public", "env"]
related: ["0267-nextjs-use-next-image.md", "0268-nextjs-use-next-script.md", "0266-nextjs-use-next-font.md"]
last_updated: "2026-04-03T23:47:18.217Z"
---

# NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE

> **🔒 Permissions Required**: Conformance

The use of `process.env.NEXT_PUBLIC_*` environment variables may warrant a review from other developers to ensure there are no unintended leakage of environment variables.

When enabled, this rule requires that all usage of `NEXT_PUBLIC_*` must be included in the [allowlist](https://vercel.com/docs/conformance/allowlist).

## Examples

This rule will catch any pages or routes that are using `process.env.NEXT_PUBLIC_*` environment variables.

In the following example, we are using a local variable to initialize our analytics service. As the variable will be visible in the client, a review of the code is required, and the usage should be added to the [allowlist](https://vercel.com/docs/conformance/allowlist).

```tsx filename="app/dashboard/page.tsx" {1}
setupAnalyticsService(process.env.NEXT_PUBLIC_ANALYTICS_ID);

function HomePage() {
  return <h1>Hello World</h1>;
}

export default HomePage;
```

## How to fix

If you hit this issue, include the entry in the [Conformance allowlist file](https://vercel.com/docs/conformance/allowlist).


