### `@implements`

In the same way, there is no JavaScript syntax for implementing a TypeScript interface. The `@implements` tag works just like in TypeScript:

```js twoslash
/** @implements {Print} */
class TextBook {
  print() {
    // TODO
  }
}
```
