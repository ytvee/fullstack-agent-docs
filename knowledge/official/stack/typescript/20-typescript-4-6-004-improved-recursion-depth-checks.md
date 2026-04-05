## Improved Recursion Depth Checks

TypeScript has some interesting challenges due to the fact that it's built on a structural type system that also provides generics.

In a structural type system, object types are compatible based on the members they have.

```ts
interface Source {
  prop: string;
}

interface Target {
  prop: number;
}

function check(source: Source, target: Target) {
  target = source;
  // error!
  // Type 'Source' is not assignable to type 'Target'.
  //   Types of property 'prop' are incompatible.
  //     Type 'string' is not assignable to type 'number'.
}
```

Notice that whether or not `Source` is compatible with `Target` has to do with whether their _properties_ are assignable.
In this case, that's just `prop`.

When you introduce generics into this, there are some harder questions to answer.
For instance, is a `Source<string>` assignable to a `Target<number>` in the following case?

```ts
interface Source<T> {
  prop: Source<Source<T>>;
}

interface Target<T> {
  prop: Target<Target<T>>;
}

function check(source: Source<string>, target: Target<number>) {
  target = source;
}
```

In order to answer that, TypeScript needs to check whether the types of `prop` are compatible.
That leads to the another question: is a `Source<Source<string>>` assignable to a `Target<Target<number>>`?
To answer that, TypeScript checks whether `prop` is compatible for _those_ types, and ends up checking whether `Source<Source<Source<string>>>` is assignable to `Target<Target<Target<number>>>`.
Keep going for a bit, and you might notice that the type infinitely expands the more you dig in.

TypeScript has a few heuristics here - if a type _appears_ to be infinitely expanding after encountering a certain depth check, then it considers that the types _could_ be compatible.
This is usually enough, but embarrassingly there were some false-negatives that this wouldn't catch.

```ts
interface Foo<T> {
  prop: T;
}

declare let x: Foo<Foo<Foo<Foo<Foo<Foo<string>>>>>>;
declare let y: Foo<Foo<Foo<Foo<Foo<string>>>>>;

x = y;
```

A human reader can see that `x` and `y` should be incompatible in the above example.
While the types are deeply nested, that's just a consequence of how they were declared.
The heuristic was meant to capture cases where deeply-nested types were generated through exploring the types, not from when a developer wrote that type out themselves.

TypeScript 4.6 is now able to distinguish these cases, and correctly errors on the last example.
Additionally, because the language is no longer concerned with false-positives from explicitly-written types, TypeScript can conclude that a type is infinitely expanding much earlier, and save a bunch of work in checking for type compatibility.
As a result, libraries on DefinitelyTyped like `redux-immutable`, `react-lazylog`, and `yup` saw a 50% reduction in check-time.

You may already have this change because it was cherry-picked into TypeScript 4.5.3, but it is a notable feature of TypeScript 4.6 which you can read up more about [here](https://github.com/microsoft/TypeScript/pull/46599).
