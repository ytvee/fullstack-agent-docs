--------------------------------------------------------------------------------
title: "NO_INSTANCEOF_ERROR"
description: "Disallows using "
last_updated: "2026-04-03T23:47:18.334Z"
source: "https://vercel.com/docs/conformance/rules/NO_INSTANCEOF_ERROR"
--------------------------------------------------------------------------------

# NO_INSTANCEOF_ERROR

> **🔒 Permissions Required**: Conformance

A common pattern for checking if an object is an error is to use
`error instanceof Error`.

This pattern is problematic because errors can come from other [realms](https://tc39.es/ecma262/#realm).
Errors from other realms are instantiated from the realm's global `Error`
constructor, and are therefore not instances of the current realm's global
`Error` constructor and will not pass the `instanceof` check.

Some examples of where you might hit this include:

- In Node.js, errors from a workers are instances of `Error` from the worker's
  global environment.
- In browser environments, errors from `iframe` are instances of `Error` from
  the `iframe`'s global environment (i.e. `iframe.contentWindow.Error`).

By default, this rule is disabled. To enable it, refer to
[customizing Conformance](/docs/conformance/customize).

## Examples

In this example, an error is returned from a [`vm`](https://nodejs.org/api/vm.html) context. As this error was created in a different realm, `instanceof Error` returns false.

```tsx {6}
const vm = require('node:vm');

const context = vm.createContext({});
const error = vm.runInContext('new Error()', context);

if (error instanceof Error) {
  // Returns `false` because `error` is from a different realm.
}
```

## How to fix

### Node.js

You can use [`isNativeError`](https://nodejs.org/api/util.html#utiltypesisnativeerrorvalue)
in Node.js environments, which will return `true` for errors from other realms.

```tsx {7}
import { isNativeError } from 'node:util/types';
const vm = require('node:vm');

const context = vm.createContext({});
const error = vm.runInContext('new Error()', context);

if (isNativeError(error)) {
  // ...
}
```

### Browsers

Use a library like [`is-error`](https://www.npmjs.com/package/is-error) to
ensure you cover errors from other realms.

You can also use `Object.prototype.toString.call(error) === '[object Error]'`
in some cases. This method will not work for custom errors, and you'll need to
traverse the prototype chain (i.e. `Object.getPrototypeOf(error)`)to handle
those cases.

The following code is a simplified version of the code used in the `is-error`
library:

```ts
function isError(error) {
  if (typeof error !== 'object') {
    return false;
  }

  if (error instanceof Error) {
    return true;
  }

  let currentError = error;
  while (currentError) {
    if (Object.prototype.toString.call(currentError) === '[object Error]') {
      return true;
    }
    currentError = Object.getPrototypeOf(currentError);
  }

  return false;
}
```


