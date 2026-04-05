##### Example

```ts
// Ensure this is treated as a module.
export {};

declare global {
  interface Array<T> {
    mapToNumbers(): number[];
  }
}

Array.prototype.mapToNumbers = function () {
  /* ... */
};
```
