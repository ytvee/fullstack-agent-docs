### Stricter Checks with Template String Expressions

When a `symbol` value is used in a template string, it will trigger a runtime error in JavaScript.

```js
let str = `hello ${Symbol()}`;
// TypeError: Cannot convert a Symbol value to a string
```

As a result, TypeScript will issue an error as well;
however, TypeScript now also checks if a generic value that is constrained to a symbol in some way is used in a template string.

```ts
function logKey<S extends string | symbol>(key: S): S {
    // Now an error.
    console.log(`${key} is the key`);
    return key;
}

function get<T, K extends keyof T>(obj: T, key: K) {
    // Now an error.
    console.log(`Grabbing property '${key}'.`);
    return obj[key];
}
```

TypeScript will now issue the following error:

```
Implicit conversion of a 'symbol' to a 'string' will fail at runtime. Consider wrapping this expression in 'String(...)'.
```

In some cases, you can get around this by wrapping the expression in a call to `String`, just like the error message suggests.

```ts
function logKey<S extends string | symbol>(key: S): S {
    // No longer an error.
    console.log(`${String(key)} is the key`);
    return key;
}
```

In others, this error is too pedantic, and you might not ever care to even allow `symbol` keys when using `keyof`.
In such cases, you can switch to `string & keyof ...`:

```ts
function get<T, K extends string & keyof T>(obj: T, key: K) {
    // No longer an error.
    console.log(`Grabbing property '${key}'.`);
    return obj[key];
}
```

For more information, you can [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/44578).
