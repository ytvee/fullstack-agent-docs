---
id: "vercel-0294"
title: "REQUIRE_CARET_DEPENDENCIES"
description: "Prevent the use of dependencies without a caret ("
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES"
tags: ["require", "caret", "dependencies", "rules", "require-caret-dependencies", "examples"]
related: ["0260-nextjs-require-explicit-dynamic.md", "0295-require-docs-on-exported-functions.md", "0297-require-one-version-policy.md"]
last_updated: "2026-04-03T23:47:18.420Z"
---

# REQUIRE_CARET_DEPENDENCIES

> **🔒 Permissions Required**: Conformance

Using a caret ("^") as a prefix in the version of your dependencies is recommended. [Caret Ranges](https://github.com/npm/node-semver?tab=readme-ov-file#caret-ranges-123-025-004) allows patch and minor updates for versions 1.0.0 and above, patch updates for versions 0.X >=0.1.0, and no updates for versions 0.0.X. This rule is applicable to `"dependencies"` and `"devDependencies"`, and it helps maintain the security and health of your codebase.

By default, this rule is disabled. To enable it, refer to
[customizing Conformance](/docs/conformance/customize).

## Examples

This rule will catch any `package.json` files:

- Using `~` or `*` as a prefix of the version, like `~1.0.0`.
- Version without a prefix, such as `1.0.0`.

```JSX filename="package.json" {3-4} {7}
{
  "dependencies": {
    "chalk": "~5.3.0",
    "ms": "*2.1.3",
  },
  "devDependencies": {
    "semver": "7.6.0"
  },
}
```

## How to fix

If you hit this issue, you can resolve it by adding a `"^"` to the version of your dependency. If you want to keep using a pinned version, or another prefix, you can include the dependency in the [Allowlist](https://vercel.com/docs/conformance/allowlist).

```JSX filename="package.json" {3}
{
  "dependencies": {
    "semver": "^7.6.0"
  },
}
```


