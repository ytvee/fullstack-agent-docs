## Instantiation Expressions

Occasionally functions can be a bit more general than we want.
For example, let's say we had a `makeBox` function.

```ts
interface Box<T> {
    value: T;
}

function makeBox<T>(value: T) {
    return { value };
}
```

Maybe we want to create a more specialized set of functions for making `Box`es of `Wrench`es and `Hammer`s.
To do that today, we'd have to wrap `makeBox` in other functions, or use an explicit type for an alias of `makeBox`.

```ts
function makeHammerBox(hammer: Hammer) {
    return makeBox(hammer);
}

// or...

const makeWrenchBox: (wrench: Wrench) => Box<Wrench> = makeBox;
```

These work, but wrapping a call to `makeBox` is a bit wasteful, and writing the full signature of `makeWrenchBox` could get unwieldy.
Ideally, we would be able to say that we just want to alias `makeBox` while replacing all of the generics in its signature.

TypeScript 4.7 allows exactly that!
We can now take functions and constructors and feed them type arguments directly.

```ts
const makeHammerBox = makeBox<Hammer>;
const makeWrenchBox = makeBox<Wrench>;
```

So with this, we can specialize `makeBox` to accept more specific types and reject anything else.

```ts
const makeStringBox = makeBox<string>;

// TypeScript correctly rejects this.
makeStringBox(42);
```

This logic also works for constructor functions such as `Array`, `Map`, and `Set`.

```ts
// Has type `new () => Map<string, Error>`
const ErrorMap = Map<string, Error>;

// Has type `// Map<string, Error>`
const errorMap = new ErrorMap();
```

When a function or constructor is given type arguments, it will produce a new type that keeps all signatures with compatible type parameter lists, and replaces the corresponding type parameters with the given type arguments.
Any other signatures are dropped, as TypeScript will assume that they aren't meant to be used.

For more information on this feature, [check out the pull request](https://github.com/microsoft/TypeScript/pull/47607).
