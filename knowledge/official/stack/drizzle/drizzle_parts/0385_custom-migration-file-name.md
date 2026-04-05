### Custom migration file name
You can set custom migration file names by providing `--name` CLI option
```shell
npx drizzle-kit generate --name=init
```
```plaintext {4}
📦 <project root>
 ├ 📂 drizzle
 │ └ 📂 20242409125510_init
 │   ├ 📜 snapshot.json
 │   └ 📜 migration.sql
 ├ 📂 src
 └ …
```

