# `drizzle-kit studio`
<Prerequisites>
- Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file)
- Drizzle Studio, our database browser - [read here](/drizzle-studio/overview)
</Prerequisites>

`drizzle-kit studio` command spins up a server for [Drizzle Studio](/drizzle-studio/overview) hosted on [local.drizzle.studio](https://local.drizzle.studio). 
It requires you to specify database connection credentials via [drizzle.config.ts](/docs/drizzle-config-file) config file.

By default it will start a Drizzle Studio server on `127.0.0.1:4983`
<Section>
```ts {6}
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname"
  },
});
```
```shell
npx drizzle-kit migrate
```
</Section>

