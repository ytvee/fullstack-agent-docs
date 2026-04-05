#### Establish server-side functions
In this step, we establish server-side functions in the **src/actions/todoAction.ts** file to handle crucial operations on todo items:

1. **`getData`:**
    - Fetches all existing todo items from the database.
2. **`addTodo`:**
    - Adds a new todo item to the database with the provided text.
    - Initiates revalidation of the home page using **`revalidatePath("/")`**.
3. **`deleteTodo`:**
    - Removes a todo item from the database based on its unique ID.
    - Triggers a revalidation of the home page.
4. **`toggleTodo`:**
    - Toggles the completion status of a todo item, updating the database accordingly.
    - Revalidates the home page after the operation.
5. **`editTodo`:**
    - Modifies the text of a todo item identified by its ID in the database.
    - Initiates a revalidation of the home page.

```tsx collapsable copy filename="src/actions/todoAction.ts"
"use server";
import { eq, not } from "drizzle-orm";
import { revalidatePath } from "next/cache";
import { db } from "@/db/drizzle";
import { todo } from "@/db/schema";

export const getData = async () => {
  const data = await db.select().from(todo);
  return data;
};

export const addTodo = async (id: number, text: string) => {
  await db.insert(todo).values({
    id: id,
    text: text,
  });
};

export const deleteTodo = async (id: number) => {
  await db.delete(todo).where(eq(todo.id, id));

  revalidatePath("/");
};

export const toggleTodo = async (id: number) => {
  await db
    .update(todo)
    .set({
      done: not(todo.done),
    })
    .where(eq(todo.id, id));

  revalidatePath("/");
};

export const editTodo = async (id: number, text: string) => {
  await db
    .update(todo)
    .set({
      text: text,
    })
    .where(eq(todo.id, id));

  revalidatePath("/");
};
```

