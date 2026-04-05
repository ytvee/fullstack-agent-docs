##### Example

```ts
type Foo = { a?: string }; // Same as { a?: string | undefined }
type Bar = Required<Foo>; // Same as { a: string }
```
