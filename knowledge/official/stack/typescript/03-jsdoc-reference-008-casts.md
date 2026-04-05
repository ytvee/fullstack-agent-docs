#### Casts

TypeScript borrows cast syntax from Google Closure.
This lets you cast types to other types by adding a `@type` tag before any parenthesized expression.

```js twoslash
/**
 * @type {number | string}
 */
var numberOrString = Math.random() < 0.5 ? "hello" : 100;
var typeAssertedNumber = /** @type {number} */ (numberOrString);
```

You can even cast to `const` just like TypeScript:

```js twoslash
let one = /** @type {const} */(1);
```
