## Smarter union type checking

In TypeScript 3.4 and prior, the following example would fail:

```ts
type S = { done: boolean; value: number };
type T = { done: false; value: number } | { done: true; value: number };

declare let source: S;
declare let target: T;

target = source;
```

That's because `S` isn't assignable to `{ done: false, value: number }` nor `{ done: true, value: number }`.
Why?
Because the `done` property in `S` isn't specific enough - it's `boolean` whereas each constituent of `T` has a `done` property that's specifically `true` or `false`.
That's what we meant by each constituent type being checked in isolation: TypeScript doesn't just union each property together and see if `S` is assignable to that.
If it did, some bad code could get through like the following:

```ts
interface Foo {
  kind: "foo";
  value: string;
}

interface Bar {
  kind: "bar";
  value: number;
}

function doSomething(x: Foo | Bar) {
  if (x.kind === "foo") {
    x.value.toLowerCase();
  }
}

// uh-oh - luckily TypeScript errors here!
doSomething({
  kind: "foo",
  value: 123
});
```

However, this was a bit overly strict for the original example.
If you figure out the precise type of any possible value of `S`, you can actually see that it matches the types in `T` exactly.

In TypeScript 3.5, when assigning to types with discriminant properties like in `T`, the language actually _will_ go further and decompose types like `S` into a union of every possible inhabitant type.
In this case, since `boolean` is a union of `true` and `false`, `S` will be viewed as a union of `{ done: false, value: number }` and `{ done: true, value: number }`.

For more details, you can [see the original pull request on GitHub](https://github.com/microsoft/TypeScript/pull/30779).
