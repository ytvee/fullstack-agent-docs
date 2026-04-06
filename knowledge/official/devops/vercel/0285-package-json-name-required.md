---
id: "vercel-0285"
title: "PACKAGE_JSON_NAME_REQUIRED"
description: "Requires that every package.json file has the name field set to ensure each workspace has a unique identifier."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED"
tags: ["package", "json", "name", "required", "rules", "package-json-name-required"]
related: ["0283-package-json-description-required.md", "0286-package-json-private-required.md", "0288-package-json-type-required.md"]
last_updated: "2026-04-03T23:47:18.366Z"
---

# PACKAGE_JSON_NAME_REQUIRED

> **🔒 Permissions Required**: Conformance

This check ensures that every `package.json` has a `name` field. This field is important because
it used to identify the workspace in the monorepo.

See the [Node.js docs](https://nodejs.org/api/packages.html#name) for more information.

## Related Rules

- [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
- [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
- [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)
- [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## How to fix

Add the `name` field to the `package.json` file that contains a unique name for
this package. The name should be understandable by someone viewing or using the
package as to what it does.


