## The `Omit` helper type

TypeScript 3.5 introduces the new `Omit` helper type, which creates a new type with some properties dropped from the original.

```ts
type Person = {
  name: string;
  age: number;
  location: string;
};

type QuantumPerson = Omit<Person, "location">;

// equivalent to
type QuantumPerson = {
  name: string;
  age: number;
};
```

Here we were able to copy over all the properties of `Person` except for `location` using the `Omit` helper.

For more details, [see the pull request on GitHub to add `Omit`](https://github.com/Microsoft/TypeScript/pull/30552), as well as [the change to use `Omit` for object rest](https://github.com/microsoft/TypeScript/pull/31134).
