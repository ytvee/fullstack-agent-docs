### `@link`

`@link` is like `@see`, except that it can be used inside other tags:

```ts twoslash
type Box<T> = { t: T }
/** @returns A {@link Box} containing the parameter. */
function box<U>(u: U): Box<U> {
  return { t: u };
}
```

You can also link a property:

```ts twoslash 
type Pet = {
  name: string
  hello: () => string
}

/**
 * Note: you should implement the {@link Pet.hello} method of Pet.
 */
function hello(p: Pet) {
  p.hello()
}
```

Or with an optional name:

```ts twoslash
type Pet = {
  name: string
  hello: () => string
}

/**
 * Note: you should implement the {@link Pet.hello | hello} method of Pet.
 */
function hello(p: Pet) {
  p.hello()
}
```
