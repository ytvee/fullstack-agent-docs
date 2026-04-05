### Migrations folder
`out` param lets you define folder for your migrations, it's optional and `drizzle` by default.  
It's very useful since you can have many separate schemas for different databases in the same project 
and have different migration folders for them.  
  
Migration folder contains folders with `.sql` migration files which is used by `drizzle-kit`

<Section>
```plaintext {3}
📦 <project root>
 ├ ...
 ├ 📂 drizzle
 │ ├ 📂 20242409125510_premium_mister_fear
 │ ├ 📜 user.ts 
 │ ├ 📜 post.ts 
 │ └ 📜 comment.ts 
 ├ 📂 src
 ├ 📜 drizzle.config.ts
 └ 📜 package.json
```
```ts {5}
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql", // "mysql" | "sqlite" | "postgresql" | "turso" | "singlestore" | "mssql"
  schema: "./src/schema/*",
  out: "./drizzle",
});
```
</Section>

