### `@extends`

When JavaScript classes extend a generic base class, there is no JavaScript syntax for passing a type argument. The `@extends` tag allows this:

```js twoslash
/**
 * @template T
 * @extends {Set<T>}
 */
class SortableSet extends Set {
  // ...
}
```

Note that `@extends` only works with classes. Currently, there is no way for a constructor function to extend a class.
