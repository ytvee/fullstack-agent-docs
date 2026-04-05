### Basic file structure

This is the basic file structure of the project. In the `src/db` directory, we have database-related files including connection in `db.ts`, schema definitions in `schema.ts`, and a migration script in `migrate.ts` file which is responsible for applying migrations that stored in the `migrations` directory.

```plaintext
📦 <project root>
 ├ 📂 src
 │  ├ 📜 db.ts
 │  └ 📜 schema.ts
 ├ 📂 migrations
 │  ├ 📂 meta
 │  │  ├ 📜 _journal.json
 │  │  └ 📜 0000_snapshot.json
 │  └ 📜 0000_dry_richard_fisk.sql
 ├ 📜 .env
 ├ 📜 drizzle.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

