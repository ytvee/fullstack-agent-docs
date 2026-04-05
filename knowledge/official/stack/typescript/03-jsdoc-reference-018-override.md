### `@override`

`@override` works the same way as in TypeScript; use it on methods that override a method from a base class:

```js twoslash
export class C {
  m() { }
}
class D extends C {
  /** @override */
  m() { }
}
```

Set `noImplicitOverride: true` in tsconfig to check overrides.
