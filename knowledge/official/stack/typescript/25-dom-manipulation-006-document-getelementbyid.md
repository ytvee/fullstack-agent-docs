### `Document.getElementById`

The definition for this method is as follows:

```ts
getElementById(elementId: string): HTMLElement | null;
```

Pass it an element id string and it will return either `HTMLElement` or `null`. This method introduces one of the most important types, `HTMLElement`. It serves as the base interface for every other element interface. For example, the `p` variable in the code example is of type `HTMLParagraphElement`. Also, take note that this method can return `null`. This is because the method can't be certain pre-runtime if it will be able to actually find the specified element or not. In the last line of the code snippet, the new _optional chaining_ operator is used to call `appendChild`.
