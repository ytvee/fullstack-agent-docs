--------------------------------------------------------------------------------
title: "PACKAGE_JSON_DESCRIPTION_REQUIRED"
description: "Requires that every package.json file has the description field set."
last_updated: "2026-04-03T23:47:18.358Z"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE_JSON_DESCRIPTION_REQUIRED

> **🔒 Permissions Required**: Conformance

This check ensures that every `package.json` has a `description` field.
This field is used to describe the workspace's purpose within the monorepo.

See the [Node.js docs](https://nodejs.org/api/packages.html#description) for more information.

## Related Rules

- [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
- [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
- [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)
- [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## How to fix

Add the `description` field to the `package.json` file that explains
what the package does and when it should be used.


