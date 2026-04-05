### `verbose`
<rem025/>

Print all SQL statements during `drizzle-kit push` command.

|               |                      |
| :------------ | :-----------------   |
| type          | `boolean` |
| default       | `true`                    |
| commands      | `generate` `pull`   |

<rem025/>

```ts
export default defineConfig({
  dialect: "postgresql",
  verbose: false,
});
```

