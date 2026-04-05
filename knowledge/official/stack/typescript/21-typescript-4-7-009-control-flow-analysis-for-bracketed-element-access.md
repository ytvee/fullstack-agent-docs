## Control-Flow Analysis for Bracketed Element Access

TypeScript 4.7 now narrows the types of element accesses when the indexed keys are literal types and unique symbols.
For example, take the following code:

```ts
const key = Symbol();

const numberOrString = Math.random() < 0.5 ? 42 : "hello";

const obj = {
    [key]: numberOrString,
};

if (typeof obj[key] === "string") {
    let str = obj[key].toUpperCase();
}
```

Previously, TypeScript would not consider any type guards on `obj[key]`, and would have no idea that `obj[key]` was really a `string`.
Instead, it would think that `obj[key]` was still a `string | number` and accessing `toUpperCase()` would trigger an error.

TypeScript 4.7 now knows that `obj[key]` is a string.

This also means that under `--strictPropertyInitialization`, TypeScript can correctly check that computed properties are initialized by the end of a constructor body.

```ts
// 'key' has type 'unique symbol'
const key = Symbol();

class C {
    [key]: string;

    constructor(str: string) {
        // oops, forgot to set 'this[key]'
    }

    screamString() {
        return this[key].toUpperCase();
    }
}
```

Under TypeScript 4.7, `--strictPropertyInitialization` reports an error telling us that the `[key]` property wasn't definitely assigned by the end of the constructor.

We'd like to extend our gratitude to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) who provided [this change](https://github.com/microsoft/TypeScript/pull/45974)!
