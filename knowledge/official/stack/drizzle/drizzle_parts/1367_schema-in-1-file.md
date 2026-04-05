#### Schema in 1 file
The most common way to declare your schema with Drizzle is to put all your tables into one `schema.ts` file.

> Note: You can name your schema file whatever you like. For example, it could be `models.ts`, or something else.

This approach works well if you don't have too many table models defined, or if you're okay with keeping them all in one file

Example:
```plaintext
📦 <project root>
 └ 📂 src
    └ 📂 db
       └ 📜 schema.ts
```

In the `drizzle.config.ts` file, you need to specify the path to your schema file. With this configuration, Drizzle will 
read from the `schema.ts` file and use this information during the migration generation process. For more information 
about the `drizzle.config.ts` file and migrations with Drizzle, please check: [link](/docs/drizzle-config-file)
```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: 'postgresql', // 'mysql' | 'sqlite' | 'turso'
  schema: './src/db/schema.ts'
})
```

