## Unrelated Types for Getters and Setters

TypeScript 4.3 made it possible to say that a `get` and `set` accessor pair might specify two different types.

```ts
interface Serializer {
    set value(v: string | number | boolean);
    get value(): string;
}
declare let box: Serializer;
// Allows writing a 'boolean'
box.value = true;
// Comes out as a 'string'
console.log(box.value.toUpperCase());
```

Initially we required that the `get` type had to be a subtype of the `set` type.
This meant that writing

```ts
box.value = box.value;
```

would always be valid.

However, there are plenty of existing and proposed APIs that have completely unrelated types between their getters and setters.
For example, consider one of the most common examples - the `style` property in the DOM and [`CSSStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule) API.
Every style rule has [a `style` property](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule/style) that is a [`CSSStyleDeclaration`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration);
however, if you try to write to that property, it will only work correctly with a string!

TypeScript 5.1 now allows completely unrelated types for `get` and `set` accessor properties, provided that they have explicit type annotations.
And while this version of TypeScript does not yet change the types for these built-in interfaces, `CSSStyleRule` can now be defined in the following way:

```ts
interface CSSStyleRule {
    // ...
    /** Always reads as a `CSSStyleDeclaration` */
    get style(): CSSStyleDeclaration;
    /** Can only write a `string` here. */
    set style(newValue: string);
    // ...
}
```

This also allows other patterns like requiring `set` accessors to accept only "valid" data, but specifying that `get` accessors may return `undefined` if some underlying state hasn't been initialized yet.

```ts
class SafeBox {
    #value: string | undefined;
    // Only accepts strings!
    set value(newValue: string) {
    }
    // Must check for 'undefined'!
    get value(): string | undefined {
        return this.#value;
    }
}
```

In fact, this is similar to how optional properties are checked under `--exactOptionalProperties`.

You can read up more on [the implementing pull request](https://github.com/microsoft/TypeScript/pull/53417).
