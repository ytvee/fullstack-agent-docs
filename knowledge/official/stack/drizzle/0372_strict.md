### `strict`
<rem025/>

Prompts confirmation to run printed SQL statements when running `drizzle-kit push` command.

|               |                      |
| :------------ | :-----------------   |
| type          | `boolean` |
| default       | `false`                    |
| commands      | `push`   |

<rem025/>

```ts
export default defineConfig({
  dialect: "postgresql",
  strict: false,
});
```

