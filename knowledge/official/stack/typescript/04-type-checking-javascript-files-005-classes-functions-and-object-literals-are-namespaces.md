## Classes, functions, and object literals are namespaces

Classes are namespaces in `.js` files.
This can be used to nest classes, for example:

```js twoslash
class C {}
C.D = class {};
```

And, for pre-ES2015 code, it can be used to simulate static methods:

```js twoslash
function Outer() {
  this.y = 2;
}

Outer.Inner = function () {
  this.yy = 2;
};

Outer.Inner();
```

It can also be used to create simple namespaces:

```js twoslash
var ns = {};
ns.C = class {};
ns.func = function () {};

ns;
```

Other variants are allowed as well:

```js twoslash
// IIFE
var ns = (function (n) {
  return n || {};
})();
ns.CONST = 1;

// defaulting to global
var assign =
  assign ||
  function () {
    // code goes here
  };
assign.extra = 1;
```
