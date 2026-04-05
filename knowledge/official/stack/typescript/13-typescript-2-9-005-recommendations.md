#### Recommendations

- If your functions are only able to handle string named property keys, use `Extract<keyof T, string>` in the declaration:

  ```ts
  function useKey<T, K extends Extract<keyof T, string>>(o: T, k: K) {
    var name: string = k; // OK
  }
  ```

- If your functions are open to handling all property keys, then the changes should be done down-stream:

  ```ts
  function useKey<T, K extends keyof T>(o: T, k: K) {
    var name: string | number | symbol = k;
  }
  ```

- Otherwise use [`keyofStringsOnly`](/tsconfig#keyofStringsOnly) compiler option to disable the new behavior.
