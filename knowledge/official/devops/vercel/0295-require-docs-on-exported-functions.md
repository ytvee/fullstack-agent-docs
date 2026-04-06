---
id: "vercel-0295"
title: "REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS"
description: "Requires that all exported functions have JSDoc comments."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS"
tags: ["require", "exported", "functions", "rules", "examples", "how-to-fix"]
related: ["0260-nextjs-require-explicit-dynamic.md", "0296-require-node-version-file.md", "0294-require-caret-dependencies.md"]
last_updated: "2026-04-03T23:47:18.425Z"
---

# REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS

> **🔒 Permissions Required**: Conformance

Adding JSDoc to exported functions helps engineers to quickly understand the
purpose and application of those functions when reviewing or using them.

This is particularly important in packages where the source code may be
minified and/or obfuscated, and can save users time by avoiding the need to
find usage information in external documentation.

For more information on JSDoc, see [Getting started with JSDoc](https://jsdoc.app/about-getting-started).

Additionally, for non-TypeScript projects, JSDoc can be used to declare type
information for function parameters and return values. For packages, these
declarations can provide type information for both JavaScript and TypeScript
consumers.

## Examples

The below function is a minimal example of a function that would be caught by
this rule.

```ts
export function appendWorld(str: string): string {
  return str + ' world';
}
```

This rule will also catch references within the same file, and different ways
of declaring functions. For example:

```ts
const appendWorld = function (str: string): string {
  return str + ' world';
};

export default appendWorld;
```

This rule non-function exports and re-exports of functions.

## How to fix

To resolve this issue, add a JSDoc comment to the exported function.

```ts
/**
 * Modifies a string by appending `' world'` to it.
 */
export function appendWorld(str: string): string {
  return str + ' world';
}
```

You can add additional information to the JSDoc comment, such as descriptions
of the function's parameters and return value.

```ts
/**
 * Modifies a string by appending `' world'` to it.
 *
 * @param str - The string to modify.
 * @returns The modified string.
 */
export function appendWorld(str: string): string {
  return str + ' world';
}
```

The example above doesn't provide type information in the JSDoc comment, as
this information is already provided by the function signature. When working
without TypeScript, you can also provide this information using JSDoc.

```js
/**
 * Modifies a string by appending `' world'` to it.
 *
 * @param {string} str - The string to modify.
 * @returns {string} The modified string.
 */
export function appendWorld(str) {
  return str + ' world';
}
```


