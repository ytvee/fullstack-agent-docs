## What Do Type Declarations Look Like?

Let's say you write some code like this:

```ts twoslash
// @errors: 2339
const k = Math.max(5, 6);
const j = Math.mix(7, 8);
```

How did TypeScript know that `max` was present but not `mix`, even though `Math`'s implementation wasn't part of your code?

The answer is that there are _declaration files_ describing these built-in objects.
A declaration file provides a way to _declare_ the existence of some types or values without actually providing implementations for those values.
