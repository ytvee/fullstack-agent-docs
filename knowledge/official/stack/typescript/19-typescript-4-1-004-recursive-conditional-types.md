## Recursive Conditional Types

In JavaScript it's fairly common to see functions that can flatten and build up container types at arbitrary levels.
For example, consider the `.then()` method on instances of `Promise`.
`.then(...)` unwraps each promise until it finds a value that's not "promise-like", and passes that value to a callback.
There's also a relatively new `flat` method on `Array`s that can take a depth of how deep to flatten.

Expressing this in TypeScript's type system was, for all practical intents and purposes, not possible.
While there were hacks to achieve this, the types ended up looking very unreasonable.

That's why TypeScript 4.1 eases some restrictions on conditional types - so that they can model these patterns.
In TypeScript 4.1, conditional types can now immediately reference themselves within their branches, making it easier to write recursive type aliases.

For example, if we wanted to write a type to get the element types of nested arrays, we could write the following `deepFlatten` type.

```ts
type ElementType<T> = T extends ReadonlyArray<infer U> ? ElementType<U> : T;

function deepFlatten<T extends readonly unknown[]>(x: T): ElementType<T>[] {
  throw "not implemented";
}

// All of these return the type 'number[]':
deepFlatten([1, 2, 3]);
deepFlatten([[1], [2, 3]]);
deepFlatten([[1], [[2]], [[[3]]]]);
```

Similarly, in TypeScript 4.1 we can write an `Awaited` type to deeply unwrap `Promise`s.

```ts
type Awaited<T> = T extends PromiseLike<infer U> ? Awaited<U> : T;

/// Like `promise.then(...)`, but more accurate in types.
declare function customThen<T, U>(
  p: Promise<T>,
  onFulfilled: (value: Awaited<T>) => U
): Promise<Awaited<U>>;
```

Keep in mind that while these recursive types are powerful, they should be used responsibly and sparingly.

First off, these types can do a lot of work which means that they can increase type-checking time.
Trying to model numbers in the Collatz conjecture or Fibonacci sequence might be fun, but don't ship that in `.d.ts` files on npm.

But apart from being computationally intensive, these types can hit an internal recursion depth limit on sufficiently-complex inputs.
When that recursion limit is hit, that results in a compile-time error.
In general, it's better not to use these types at all than to write something that fails on more realistic examples.

See more [at the implementation](https://github.com/microsoft/TypeScript/pull/40002).
