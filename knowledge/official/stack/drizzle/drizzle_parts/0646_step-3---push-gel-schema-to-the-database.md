#### Step 3 - Push Gel schema to the database

Generate Gel migration file:
```bash
gel migration create
```

Apply Gel migrations to the database
```bash
gel migration apply
```

<Callout>
Now you should have this file structure

```plaintext
📦 <project root>
 ├ 📂 dbschema
 │ ├ 📂 migrations
 │ ├ 📜 default.esdl
 │ └ 📜 scoping.esdl
 ├ 📂 src
 │ └ 📜 index.ts
 ├ 📜 drizzle.config.ts
 ├ 📜 edgedb.toml
 ├ 📜 package.json
 └ 📜 tsconfig.json
```
</Callout>

