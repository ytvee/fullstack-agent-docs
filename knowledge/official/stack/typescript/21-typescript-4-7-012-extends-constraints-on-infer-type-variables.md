## `extends` Constraints on `infer` Type Variables

Conditional types are a bit of a power-user feature.
They allow us to match and infer against the shape of types, and make decisions based on them.
For example, we can write a conditional type that returns the first element of a tuple type if it's a `string`-like type.

```ts
type FirstIfString<T> =
    T extends [infer S, ...unknown[]]
        ? S extends string ? S : never
        : never;

 // string
type A = FirstIfString<[string, number, number]>;

// "hello"
type B = FirstIfString<["hello", number, number]>;

// "hello" | "world"
type C = FirstIfString<["hello" | "world", boolean]>;

// never
type D = FirstIfString<[boolean, number, string]>;
```

`FirstIfString` matches against any tuple with at least one element and grabs the type of the first element as `S`.
Then it checks if `S` is compatible with `string` and returns that type if it is.

Note that we had to use two conditional types to write this.
We could have written `FirstIfString` as follows:

```ts
type FirstIfString<T> =
    T extends [string, ...unknown[]]
        // Grab the first type out of `T`
        ? T[0]
        : never;
```

This works, but it's slightly more "manual" and less declarative.
Instead of just pattern-matching on the type and giving the first element a name, we have to fetch out the `0`th element of `T` with `T[0]`.
If we were dealing with types more complex than tuples, this could get a lot trickier, so `infer` can simplify things.

Using nested conditionals to infer a type and then match against that inferred type is pretty common.
To avoid that second level of nesting, TypeScript 4.7 now allows you to place a constraint on any `infer` type.

```ts
type FirstIfString<T> =
    T extends [infer S extends string, ...unknown[]]
        ? S
        : never;
```

This way, when TypeScript matches against `S`, it also ensures that `S` has to be a `string`.
If `S` isn't a `string`, it takes the false path, which in these cases is `never`.

For more details, you can [read up on the change on GitHub](https://github.com/microsoft/TypeScript/pull/48112).
