##### Example

```ts
type Required<T> = { [P in keyof T]-?: T[P] };
```

Note that in [`strictNullChecks`](/tsconfig#strictNullChecks) mode, when a homomorphic mapped type removes a `?` modifier from a property in the underlying type it also removes `undefined` from the type of that property:
