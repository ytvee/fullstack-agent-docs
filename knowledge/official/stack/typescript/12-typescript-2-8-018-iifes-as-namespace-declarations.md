## IIFEs as namespace declarations

An IIFE returning a function, class or empty object literal, is also recognized as a namespace:

```js
var C = (function() {
  function C(n) {
    this.p = n;
  }
  return C;
})();
C.staticProperty = 1;
```
