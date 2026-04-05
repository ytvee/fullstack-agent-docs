##### Example

```ts
type ElementType<T> = T extends any[] ? ElementType<T[number]> : T; // Error
```
