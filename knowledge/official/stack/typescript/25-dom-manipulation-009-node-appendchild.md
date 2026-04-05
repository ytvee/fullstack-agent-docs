### `Node.appendChild`

The last line of the code snippet is `app?.appendChild(p)`. The previous, `document.getElementById`, section detailed that the _optional chaining_ operator is used here because `app` can potentially be null at runtime. The `appendChild` method is defined by:

```ts
appendChild<T extends Node>(newChild: T): T;
```

This method works similarly to the `createElement` method as the generic parameter `T` is inferred from the `newChild` argument. `T` is _constrained_ to another base interface `Node`.
