### Node Reuse in Declaration Emit

As part of the work to enable `isolatedDeclarations`, we've substantially improved how often TypeScript can directly copy your input source code when producing declaration files.

For example, let's say you wrote

```ts
export const strBool: string | boolean = "hello";
export const boolStr: boolean | string = "world";
```

Note that the union types are equivalent, but the order of the union is different.
When emitting the declaration file, TypeScript has two equivalent output possibilities.

The first is to use a consistent canonical representation for each type:

```ts
export const strBool: string | boolean;
export const boolStr: string | boolean;
```

The second is to re-use the type annotations exactly as written:

```ts
export const strBool: string | boolean;
export const boolStr: boolean | string;
```

The second approach is generally preferable for a few reasons:

* Many equivalent representations still encode some level of intent that is better to preserve in the declaration file
* Producing a fresh representation of a type can be somewhat expensive, so avoiding is better
* User-written types are usually shorter than generated type representations

In 5.5, we've greatly improved the number of places where TypeScript can correctly identify places where it's safe and correct to print back types exactly as they were written in the input file.
Many of these cases are invisible performance improvements - TypeScript would generate fresh sets of syntax nodes and serialize them into a string.
Instead, TypeScript can now operate over the original syntax nodes directly, which is much cheaper and faster.
