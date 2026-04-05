### `@typedef`, `@callback`, and `@param`

You can define complex types with `@typedef`.
Similar syntax works with `@param`.

```js twoslash
/**
 * @typedef {Object} SpecialType - creates a new type named 'SpecialType'
 * @property {string} prop1 - a string property of SpecialType
 * @property {number} prop2 - a number property of SpecialType
 * @property {number=} prop3 - an optional number property of SpecialType
 * @prop {number} [prop4] - an optional number property of SpecialType
 * @prop {number} [prop5=42] - an optional number property of SpecialType with default
 */

/** @type {SpecialType} */
var specialTypeObject;
specialTypeObject.prop3;
```

You can use either `object` or `Object` on the first line.

```js twoslash
/**
 * @typedef {object} SpecialType1 - creates a new type named 'SpecialType1'
 * @property {string} prop1 - a string property of SpecialType1
 * @property {number} prop2 - a number property of SpecialType1
 * @property {number=} prop3 - an optional number property of SpecialType1
 */

/** @type {SpecialType1} */
var specialTypeObject1;
```

`@param` allows a similar syntax for one-off type specifications.
Note that the nested property names must be prefixed with the name of the parameter:

```js twoslash
/**
 * @param {Object} options - The shape is the same as SpecialType above
 * @param {string} options.prop1
 * @param {number} options.prop2
 * @param {number=} options.prop3
 * @param {number} [options.prop4]
 * @param {number} [options.prop5=42]
 */
function special(options) {
  return (options.prop4 || 1001) + options.prop5;
}
```

`@callback` is similar to `@typedef`, but it specifies a function type instead of an object type:

```js twoslash
/**
 * @callback Predicate
 * @param {string} data
 * @param {number} [index]
 * @returns {boolean}
 */

/** @type {Predicate} */
const ok = (s) => !(s.length % 2);
```

Of course, any of these types can be declared using TypeScript syntax in a single-line `@typedef`:

```js
/** @typedef {{ prop1: string, prop2: string, prop3?: number }} SpecialType */
/** @typedef {(data: string, index?: number) => boolean} Predicate */
```
