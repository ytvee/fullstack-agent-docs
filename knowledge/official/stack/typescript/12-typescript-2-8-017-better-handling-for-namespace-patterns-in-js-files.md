## Better handling for namespace patterns in `.js` files

TypeScript 2.8 adds support for understanding more namespace patterns in `.js` files.
Empty object literals declarations on top level, just like functions and classes, are now recognized as namespace declarations in JavaScript.

```js
var ns = {}; // recognized as a declaration for a namespace `ns`
ns.constant = 1; // recognized as a declaration for var `constant`
```

Assignments at the top-level should behave the same way; in other words, a `var` or `const` declaration is not required.

```js
app = {}; // does NOT need to be `var app = {}`
app.C = class {};
app.f = function() {};
app.prop = 1;
```
