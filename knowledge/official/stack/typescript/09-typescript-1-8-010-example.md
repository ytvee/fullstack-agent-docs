##### Example

```ts
function f(x) {
  // Error: Not all code paths return a value.
  if (x) {
    return false;
  }

  // implicitly returns `undefined`
}
```
