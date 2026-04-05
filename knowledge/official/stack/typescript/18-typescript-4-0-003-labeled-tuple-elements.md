## Labeled Tuple Elements

Improving the experience around tuple types and parameter lists is important because it allows us to get strongly typed validation around common JavaScript idioms - really just slicing and dicing argument lists and passing them to other functions.
The idea that we can use tuple types for rest parameters is one place where this is crucial.

For example, the following function that uses a tuple type as a rest parameter...

```ts
function foo(...args: [string, number]): void {
  // ...
}
```

...should appear no different from the following function...

```ts
function foo(arg0: string, arg1: number): void {
  // ...
}
```

...for any caller of `foo`.

```ts twoslash
// @errors: 2554
function foo(arg0: string, arg1: number): void {
  // ...
}
// ---cut---
foo("hello", 42);

foo("hello", 42, true);
foo("hello");
```

There is one place where the differences begin to become observable though: readability.
In the first example, we have no parameter names for the first and second elements.
While these have no impact on type-checking, the lack of labels on tuple positions can make them harder to use - harder to communicate our intent.

That's why in TypeScript 4.0, tuples types can now provide labels.

```ts
type Range = [start: number, end: number];
```

To deepen the connection between parameter lists and tuple types, the syntax for rest elements and optional elements mirrors the syntax for parameter lists.

```ts
type Foo = [first: number, second?: string, ...rest: any[]];
```

There are a few rules when using labeled tuples.
For one, when labeling a tuple element, all other elements in the tuple must also be labeled.

```ts twoslash
// @errors: 5084
type Bar = [first: string, number];
```

It's worth noting - labels don't require us to name our variables differently when destructuring.
They're purely there for documentation and tooling.

```ts twoslash
function foo(x: [first: string, second: number]) {
    // ...

    // note: we didn't need to name these 'first' and 'second'
    const [a, b] = x;
    a
//  ^?
    b
//  ^?
}
```

Overall, labeled tuples are handy when taking advantage of patterns around tuples and argument lists, along with implementing overloads in a type-safe way.
In fact, TypeScript's editor support will try to display them as overloads when possible.

![Signature help displaying a union of labeled tuples as in a parameter list as two signatures](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/08/signatureHelpLabeledTuples.gif)

To learn more, check out [the pull request](https://github.com/microsoft/TypeScript/pull/38234) for labeled tuple elements.
