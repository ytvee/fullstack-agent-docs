## Basic file structure

This is the basic file structure of the project. In the `src` directory, we have database-related files including connection in `db.ts` and schema definitions in `schema.ts`.

```plaintext
📦 <project root>
 ├ 📂 src
 │  ├ 📜 db.ts
 │  ├ 📜 schema.ts
 │  └ 📜 index.ts
 ├ 📂 migrations
 │  ├ 📂 meta
 │  │  ├ 📜 _journal.json
 │  │  └ 📜 0000_snapshot.json
 │  └ 📜 0000_whole_nomad.sql
 ├ 📜 .env
 ├ 📜 drizzle.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

