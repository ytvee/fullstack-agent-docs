## Control Flow Analysis for Destructured Discriminated Unions

TypeScript is able to narrow types based on what's called a discriminant property.
For example, in the following code snippet, TypeScript is able to narrow the type of `action` based on every time we check against the value of `kind`.

```ts
type Action =
  | { kind: "NumberContents"; payload: number }
  | { kind: "StringContents"; payload: string };

function processAction(action: Action) {
  if (action.kind === "NumberContents") {
    // `action.payload` is a number here.
    let num = action.payload * 2;
    // ...
  } else if (action.kind === "StringContents") {
    // `action.payload` is a string here.
    const str = action.payload.trim();
    // ...
  }
}
```

This lets us work with objects that can hold different data, but a common field tells us _which_ data those objects have.

This is very common in TypeScript; however, depending on your preferences, you might have wanted to destructure `kind` and `payload` in the example above.
Perhaps something like the following:

```ts
type Action =
  | { kind: "NumberContents"; payload: number }
  | { kind: "StringContents"; payload: string };

function processAction(action: Action) {
  const { kind, payload } = action;
  if (kind === "NumberContents") {
    let num = payload * 2;
    // ...
  } else if (kind === "StringContents") {
    const str = payload.trim();
    // ...
  }
}
```

Previously TypeScript would error on these - once `kind` and `payload` were extracted from the same object into variables, they were considered totally independent.

In TypeScript 4.6, this just works!

When destructuring individual properties into a `const` declaration, or when destructuring a parameter into variables that are never assigned to, TypeScript will check for if the destructured type is a discriminated union.
If it is, TypeScript can now narrow the types of variables depending on checks of other variables
So in our example, a check on `kind` narrows the type of `payload`.

For more information, [see the pull request that implemented this analysis](https://github.com/microsoft/TypeScript/pull/46266).
