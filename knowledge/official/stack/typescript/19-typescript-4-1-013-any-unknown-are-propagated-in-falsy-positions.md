### `any`/`unknown` Are Propagated in Falsy Positions

Previously, for an expression like `foo && somethingElse`, the type of `foo` was `any` or `unknown`, the type of the whole that expression would be the type of `somethingElse`.

For example, previously the type for `x` here was `{ someProp: string }`.

```ts
declare let foo: unknown;
declare let somethingElse: { someProp: string };

let x = foo && somethingElse;
```

However, in TypeScript 4.1, we are more careful about how we determine this type.
Since nothing is known about the type on the left side of the `&&`, we propagate `any` and `unknown` outward instead of the type on the right side.

The most common pattern we saw of this tended to be when checking compatibility with `boolean`s, especially in predicate functions.

```ts
function isThing(x: any): boolean {
  return x && typeof x === "object" && x.blah === "foo";
}
```

Often the appropriate fix is to switch from `foo && someExpression` to `!!foo && someExpression`.
