---
id: "vercel-0287"
title: "PACKAGE_JSON_PRIVATE_REQUIREDPACKAGE_JSON_SIDE_EFFECTS_REQUIRED"
description: "Requires that every package.json file has the sideEffects field set to ensure tree-shaking works optimally."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED"
tags: ["package", "json", "private", "requiredpackage", "side", "effects"]
related: ["0286-package-json-private-required.md", "0285-package-json-name-required.md", "0283-package-json-description-required.md"]
last_updated: "2026-04-03T23:47:18.376Z"
---

# PACKAGE_JSON_PRIVATE_REQUIREDPACKAGE_JSON_SIDE_EFFECTS_REQUIRED

> **🔒 Permissions Required**: Conformance

This check ensures that every `package.json` has a `sideEffects` field.
The `sideEffects` field is required for shared packages. This field helps bundlers
make assumptions about packages that improve tree shaking, or pruning
files that aren't used and don't have any global side effects.

See https://webpack.js.org/guides/tree-shaking/ for more information.

## Related Rules

- [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
- [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
- [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
- [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)

## How to fix

The `sideEffects` field should be set to `false` unless the code in that workspace has
global side effects, in which case it should be set to `true` or an array of glob
patterns for files that do have side effects.


