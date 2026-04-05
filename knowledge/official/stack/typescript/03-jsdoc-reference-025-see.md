### `@see`

`@see` lets you link to other names in your program:

```ts twoslash
type Box<T> = { t: T }
/** @see Box for implementation details */
type Boxify<T> = { [K in keyof T]: Box<T> };
```

Some editors will turn `Box` into a link to make it easy to jump there and back.
