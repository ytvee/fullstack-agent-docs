--------------------------------------------------------------------------------
title: "NO_EVAL"
description: "Prevent unsafe usage of eval() in your application."
last_updated: "2026-04-03T23:47:18.302Z"
source: "https://vercel.com/docs/conformance/rules/NO_EVAL"
--------------------------------------------------------------------------------

# NO_EVAL

> **🔒 Permissions Required**: Conformance

JavaScript's `eval()` function is potentially dangerous, is often misused, and
might cause security issues. Using `eval()` on untrusted code can open an
application up to several different injection attacks.

This rule will also catch eval-like function usage (or *implied eval*), such as
passing a string as the first argument to `setTimeout`.

This is especially dangerous when working with data from external sources.

```ts
const dontDoThis = req.body;
setTimeout(dontDoThis, 1000);
```

For more information on why you should never use evaluation, see the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#never_use_eval!).

## Example

The lines below (and variations of those) will all be caught by this rule.

```ts
eval('() => console.log("DROP TABLE")');

setTimeout('() => console.log("DROP TABLE")', 1000);

window.setInterval('() => console.log("DROP TABLE")', 1000);

new Function('() => console.log("DROP TABLE")');
```

### References

Conformance rules are not type-aware, but will follow variable references
within the current module (or file).

```ts
import { importedVar } from 'foo';

// No error reported, as this rule doesn't have access to the value.
setTimeout(importedVar, 100);

const localVar = 'bar';

// An error will be reported, as the variable was declared in this file.
setTimeout(localVar, 100);
```

## How to fix

Avoid usage of this type of evaluation entirely in your application. Instead,
you should write the same functionality as raw code (not within a string).

```ts
setTimeout(() => {
  console.log('Safe usage');
});
```


