#### Exporting from Modules

Typically, exporting from a module involves adding properties to a value like `exports` or `module.exports`.
TypeScript allows you to use top-level export statements.
For instance, if you exported a function like so:

```js
module.exports.feedPets = function (pets) {
  // ...
};
```

you could write that out as the following:

```ts
export function feedPets(pets) {
  // ...
}
```

Sometimes you'll entirely overwrite the exports object.
This is a common pattern people use to make their modules immediately callable like in this snippet:

```js
var express = require("express");
var app = express();
```

You might have previously written that like so:

```js
function foo() {
  // ...
}
module.exports = foo;
```

In TypeScript, you can model this with the `export =` construct.

```ts
function foo() {
  // ...
}
export = foo;
```
