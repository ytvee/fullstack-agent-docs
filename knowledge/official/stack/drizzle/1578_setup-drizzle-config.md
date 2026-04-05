#### Setup Drizzle config

Create a `drizzle.config.ts` file:

```typescript copy filename="drizzle.config.ts"
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  out: "migrations",
  schema: "schema.ts",
  dialect: "postgresql",
});
```

