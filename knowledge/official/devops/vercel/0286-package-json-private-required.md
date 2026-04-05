--------------------------------------------------------------------------------
title: "PACKAGE_JSON_PRIVATE_REQUIRED"
description: "Requires that every package.json file has the private field set to prevent accidental publishing to npm."
last_updated: "2026-04-03T23:47:18.372Z"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE_JSON_PRIVATE_REQUIRED

> **🔒 Permissions Required**: Conformance

This check ensures that every `package.json` has the `private` field set to true or false.
This field ensures that the workspace is not accidentally published to npm. In a monorepo,
this should be the default to prevent packages from being accidentally published and can be explicitly set to
`false` to indicate that the package can be published.

## Related Rules

- [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
- [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
- [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)
- [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## How to fix

Packages should set `private` to `true` unless the package is
intended to be published in which case it can be explicitly set to `false`.


