##### Example

Below both `n` and `m` will be marked as unused, because their values are never _read_. Previously TypeScript would only check whether their values were _referenced_.

```ts
function f(n: number) {
  n = 0;
}

class C {
  private m: number;
  constructor() {
    this.m = 0;
  }
}
```

Also functions that are only called within their own bodies are considered unused.
