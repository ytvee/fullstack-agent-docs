## Control Flow Analysis for Dependent Parameters

A signature can be declared with a rest parameter whose type is a discriminated union of tuples.

```ts
function func(...args: ["str", string] | ["num", number]) {
  // ...
}
```

What this says is that the arguments to `func` depends entirely on the first argument.
When the first argument is the string `"str"`, then its second argument has to be a `string`.
When its first argument is the string `"num"`, its second argument has to be a `number`.

In cases where TypeScript infers the type of a function from a signature like this, TypeScript can now narrow parameters that depend on each other.

```ts
type Func = (...args: ["a", number] | ["b", string]) => void;

const f1: Func = (kind, payload) => {
  if (kind === "a") {
    payload.toFixed(); // 'payload' narrowed to 'number'
  }
  if (kind === "b") {
    payload.toUpperCase(); // 'payload' narrowed to 'string'
  }
};

f1("a", 42);
f1("b", "hello");
```

For more information, [see the change on GitHub](https://github.com/microsoft/TypeScript/pull/47190).
