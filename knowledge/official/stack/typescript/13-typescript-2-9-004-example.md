##### Example

```ts
function useKey<T, K extends keyof T>(o: T, k: K) {
  var name: string = k; // Error: keyof T is not assignable to string
}
```
