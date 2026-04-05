##### Example

```ts
// file src/a.ts
import * as B from "./lib/b";
export function createA() {
  return B.createB();
}
```

```ts
// file src/lib/b.ts
export function createB() {
  return {};
}
```

Results in:

```js
define("lib/b", ["require", "exports"], function (require, exports) {
  "use strict";
  function createB() {
    return {};
  }
  exports.createB = createB;
});
define("a", ["require", "exports", "lib/b"], function (require, exports, B) {
  "use strict";
  function createA() {
    return B.createB();
  }
  exports.createA = createA;
});
```
