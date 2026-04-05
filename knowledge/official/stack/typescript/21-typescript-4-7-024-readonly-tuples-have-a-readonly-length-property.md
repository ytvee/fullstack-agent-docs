### `readonly` Tuples Have a `readonly` `length` Property

A `readonly` tuple will now treat its `length` property as `readonly`.
This was almost never witnessable for fixed-length tuples, but was an oversight which could be observed for tuples with trailing optional and rest element types.

As a result, the following code will now fail:

```ts
function overwriteLength(tuple: readonly [string, string, string]) {
    // Now errors.
    tuple.length = 7;
}
```

You can [read more on this change here](https://github.com/microsoft/TypeScript/pull/47717).
