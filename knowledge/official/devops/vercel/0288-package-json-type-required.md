--------------------------------------------------------------------------------
title: "PACKAGE_JSON_TYPE_REQUIRED"
description: "Requires that every package.json file has the type field set to encourage using ES Modules since commonjs is the default."
last_updated: "2026-04-03T23:47:18.381Z"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE_JSON_TYPE_REQUIRED

> **🔒 Permissions Required**: Conformance

This check ensures that every `package.json` has a `type` field. This field determines
how files within the workspace are treated by default. Files are treated as
[CommonJS](https://nodejs.org/api/modules.html) by default. However, the new recommendation
is to use [ES Modules](https://nodejs.org/api/esm.html).

This field is required so that packages explicitly choose which module format to use,
preferring ES Modules when possible.

See the [Node.js docs](https://nodejs.org/api/packages.html#type) for more information.

## Related Rules

- [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
- [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
- [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
- [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## How to fix

The `type` field should be set to `module` when possible, although there are still situations
where `commonjs` has to be used.


