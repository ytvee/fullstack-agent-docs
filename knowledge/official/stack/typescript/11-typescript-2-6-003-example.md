##### Example

```ts
interface Comparer<T> {
  compare: (a: T, b: T) => number;
}

declare let animalComparer: Comparer<Animal>;
declare let dogComparer: Comparer<Dog>;

animalComparer = dogComparer; // Error
dogComparer = animalComparer; // Ok
```

The first assignment is now an error. Effectively, `T` is contravariant in `Comparer<T>` because it is used only in function type parameter positions.

By the way, note that whereas some languages (e.g. C# and Scala) require variance annotations (`out`/`in` or `+`/`-`), variance emerges naturally from the actual use of a type parameter within a generic type due to TypeScript's structural type system.
