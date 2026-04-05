### Why are errors desirable?

Because it means that TypeScript can

1. Tell us up-front whether other tools will have issues with generating declaration files
2. Provide a quick fix to help add these missing annotations.

This mode doesn't require annotations *everywhere* though.
For locals, these can be ignored, since they don't affect the public API.
For example, the following code would **not** produce an error:

```ts
import { add } from "./add";

const x = add("1", "2"); // no error on 'x', it's not exported.

export function foo(): string {
    return x;
}
```

There are also certain expressions where the type is "trivial" to calculate.

```ts
// No error on 'x'.
// It's trivial to calculate the type is 'number'
export let x = 10;

// No error on 'y'.
// We can get the type from the return expression.
export function y() {
    return 20;
}

// No error on 'z'.
// The type assertion makes it clear what the type is.
export function z() {
    return Math.max(x, y()) as number;
}
```
