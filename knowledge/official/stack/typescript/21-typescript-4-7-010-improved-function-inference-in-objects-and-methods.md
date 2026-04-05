## Improved Function Inference in Objects and Methods

TypeScript 4.7 can now perform more granular inferences from functions within objects and arrays.
This allows the types of these functions to consistently flow in a left-to-right manner just like for plain arguments.

```ts
declare function f<T>(arg: {
    produce: (n: string) => T,
    consume: (x: T) => void }
): void;

// Works
f({
    produce: () => "hello",
    consume: x => x.toLowerCase()
});

// Works
f({
    produce: (n: string) => n,
    consume: x => x.toLowerCase(),
});

// Was an error, now works.
f({
    produce: n => n,
    consume: x => x.toLowerCase(),
});

// Was an error, now works.
f({
    produce: function () { return "hello"; },
    consume: x => x.toLowerCase(),
});

// Was an error, now works.
f({
    produce() { return "hello" },
    consume: x => x.toLowerCase(),
});
```

Inference failed in some of these examples because knowing the type of their `produce` functions would indirectly request the type of `arg` before finding a good type for `T`.
TypeScript now gathers functions that could contribute to the inferred type of `T` and infers from them lazily.

For more information, you can [take a look at the specific modifications to our inference process](https://github.com/microsoft/TypeScript/pull/48538).
