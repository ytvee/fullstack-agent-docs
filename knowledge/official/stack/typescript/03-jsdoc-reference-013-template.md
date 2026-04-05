### `@template`

You can declare type parameters with the `@template` tag.
This lets you make functions, classes, or types that are generic:

```js twoslash
/**
 * @template T
 * @param {T} x - A generic parameter that flows through to the return type
 * @returns {T}
 */
function id(x) {
  return x;
}

const a = id("string");
const b = id(123);
const c = id({});
```

Use comma or multiple tags to declare multiple type parameters:

```js
/**
 * @template T,U,V
 * @template W,X
 */
```

You can also specify a type constraint before the type parameter name.
Only the first type parameter in a list is constrained:

```js twoslash
/**
 * @template {string} K - K must be a string or string literal
 * @template {{ serious(): string }} Seriousalizable - must have a serious method
 * @param {K} key
 * @param {Seriousalizable} object
 */
function seriousalize(key, object) {
  // ????
}
```

Finally, you can specify a default for a type parameter:

```js twoslash
/** @template [T=object] */
class Cache {
    /** @param {T} initial */
    constructor(initial) {
    }
}
let c = new Cache()
```
