### `@enum`

The `@enum` tag allows you to create an object literal whose members are all of a specified type. Unlike most object literals in JavaScript, it does not allow other members.
`@enum` is intended for compatibility with Google Closure's `@enum` tag.

```js twoslash
/** @enum {number} */
const JSDocState = {
  BeginningOfLine: 0,
  SawAsterisk: 1,
  SavingComments: 2,
};

JSDocState.SawAsterisk;
```

Note that `@enum` is quite different from, and much simpler than, TypeScript's `enum`. However, unlike TypeScript's enums, `@enum` can have any type:

```js twoslash
/** @enum {function(number): number} */
const MathFuncs = {
  add1: (n) => n + 1,
  id: (n) => -n,
  sub1: (n) => n - 1,
};

MathFuncs.add1;
```
