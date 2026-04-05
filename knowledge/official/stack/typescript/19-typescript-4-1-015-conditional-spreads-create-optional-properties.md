### Conditional Spreads Create Optional Properties

In JavaScript, object spreads (like `{ ...foo }`) don't operate over falsy values.
So in code like `{ ...foo }`, `foo` will be skipped over if it's `null` or `undefined`.

Many users take advantage of this to spread properties "conditionally".

```ts
interface Person {
  name: string;
  age: number;
  location: string;
}

interface Animal {
  name: string;
  owner: Person;
}

function copyOwner(pet?: Animal) {
  return {
    ...(pet && pet.owner),
    otherStuff: 123,
  };
}

// We could also use optional chaining here:

function copyOwner(pet?: Animal) {
  return {
    ...pet?.owner,
    otherStuff: 123,
  };
}
```

Here, if `pet` is defined, the properties of `pet.owner` will be spread in - otherwise, no properties will be spread into the returned object.

The return type of `copyOwner` was previously a union type based on each spread:

```
{ x: number } | { x: number, name: string, age: number, location: string }
```

This modeled exactly how the operation would occur: if `pet` was defined, all the properties from `Person` would be present; otherwise, none of them would be defined on the result.
It was an all-or-nothing operation.

However, we've seen this pattern taken to the extreme, with hundreds of spreads in a single object, each spread potentially adding in hundreds or thousands of properties.
It turns out that for various reasons, this ends up being extremely expensive, and usually for not much benefit.

In TypeScript 4.1, the returned type sometimes uses all-optional properties.

```
{
    x: number;
    name?: string;
    age?: number;
    location?: string;
}
```

This ends up performing better and generally displaying better too.

For more details, [see the original change](https://github.com/microsoft/TypeScript/pull/40778).
While this behavior is not entirely consistent right now, we expect a future release will produce cleaner and more predictable results.
