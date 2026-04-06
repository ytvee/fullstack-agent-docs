---
id: "vercel-0297"
title: "REQUIRE_ONE_VERSION_POLICY"
description: "Requires all dependencies in a monorepo to have the same version policy."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY"
tags: ["monorepos", "require", "one", "version", "policy", "rules"]
related: ["0296-require-node-version-file.md", "0295-require-docs-on-exported-functions.md", "0240-bfcache-integrity-require-noopener-attribute.md"]
last_updated: "2026-04-03T23:47:18.433Z"
---

# REQUIRE_ONE_VERSION_POLICY

> **🔒 Permissions Required**: Conformance

Dependency mismatch is a common and easily preventable problem. When there
are multiple versions of a single dependency, not only is there additional complexity
in maintaining different versions of that dependency, there are also code size complications
with bundling. Having multiple versions of a given dependency will likely result in bloated
code size as each dependency version will need to be bundled independently. Having multiple
versions might also leave developers confused and lead to possible security implications.

Additionally – keeping versions consistent reduces the possibility of type mismatches across
the monorepo.

By default, this rule is disabled. Enable it by [customizing Conformance](/docs/conformance/customize).

## How to fix

Ensure all `package.json` files in your monorepo that have a `dependency` are
aligned to all have the same version. Version ranges are not always reliable, so it's recommended that
you pin all versions to the same given version to ensure consistency.

## Exceptions

Sometimes it is useful to temporarily have two or more versions of a dependency whilst incrementally
migrating a monorepo to having the same version policy. In which case, it's acceptable to allowlist
this rule on specific parts of the codebase using by [customizing Conformance](/docs/conformance/customize)
until all packages have been successfully migrated.


