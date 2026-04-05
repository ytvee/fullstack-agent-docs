#### Define a TypeScript type

Define a TypeScript type for a todo item in `src/types/todoType.ts` with three properties: **`id`** of type **`number`**, **`text`** of type **`string`**, and **`done`** of type **`boolean`**. This type, named **`todoType`**, represents the structure of a typical todo item within your application.

```ts copy filename="src/types/todoType.ts"
export type todoType = {
  id: number;
  text: string;
  done: boolean;
};
```

