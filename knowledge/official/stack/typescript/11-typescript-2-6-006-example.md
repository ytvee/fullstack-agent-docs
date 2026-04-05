##### Example

```ts
export function id(x: TemplateStringsArray) {
  return x;
}

export function templateObjectFactory() {
  return id`hello world`;
}

let result = templateObjectFactory() === templateObjectFactory(); // true in TS 2.6
```

Results in the following generated code:

```js
"use strict";
var __makeTemplateObject =
  (this && this.__makeTemplateObject) ||
  function(cooked, raw) {
    if (Object.defineProperty) {
      Object.defineProperty(cooked, "raw", { value: raw });
    } else {
      cooked.raw = raw;
    }
    return cooked;
  };

function id(x) {
  return x;
}

var _a;
function templateObjectFactory() {
  return id(
    _a || (_a = __makeTemplateObject(["hello world"], ["hello world"]))
  );
}

var result = templateObjectFactory() === templateObjectFactory();
```

> Note: This change brings a new emit helper, `__makeTemplateObject`;
> if you are using [`importHelpers`](/tsconfig#importHelpers) with [`tslib`](https://github.com/Microsoft/tslib), an updated to version 1.8 or later.
