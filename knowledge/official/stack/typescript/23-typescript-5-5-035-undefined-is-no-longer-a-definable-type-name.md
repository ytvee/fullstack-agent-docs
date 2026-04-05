### `undefined` is No Longer a Definable Type Name

TypeScript has always disallowed type alias names that conflict with built-in types:

```ts
// Illegal
type null = any;
// Illegal
type number = any;
// Illegal
type object = any;
// Illegal
type any = any;
```

Due to a bug, this logic didn't also apply to the built-in type `undefined`.
In 5.5, this is now correctly identified as an error:

```ts
// Now also illegal
type undefined = any;
```

Bare references to type aliases named `undefined` never actually worked in the first place.
You could define them, but you couldn't use them as an unqualified type name.

```ts
export type undefined = string;
export const m: undefined = "";
//           ^
// Errors in 5.4 and earlier - the local definition of 'undefined' was not even consulted.
```

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/57575).
