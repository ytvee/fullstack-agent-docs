# Drizzle \<\> Expo SQLite
According to the **[official website](https://expo.dev/)**, Expo is an ecosystem of tools to develop, build and ship applications on React Native. 
It's powered by Hermes JavaScript runtime and Metro bundler, Drizzle Expo driver is built to natively support both.  
  
Drizzle ORM has the best in class toolkit for Expo SQLite:
- Native ORM driver for Expo SQLite ✅
- [Drizzle Kit](/docs/kit-overview) support for migration generation and bundling in application ✅
- [Drizzle Studio](https://github.com/drizzle-team/drizzle-studio-expo) dev tools plugin to browse on device database ✅
- Live Queries ✅
  
<Npm>
drizzle-orm expo-sqlite@next
-D drizzle-kit 
</Npm>

```ts
import { drizzle } from "drizzle-orm/expo-sqlite";
import { openDatabaseSync } from "expo-sqlite";

const expo = openDatabaseSync("db.db");
const db = drizzle(expo);

await db.select().from(users);
```
