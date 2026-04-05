### Upstash integration

Drizzle provides an `upstashCache()` helper out of the box. By default, this uses Upstash Redis with automatic configuration if environment variables are set.

```ts
import { upstashCache } from "drizzle-orm/cache/upstash";
import { drizzle } from "drizzle-orm/...";

const db = drizzle(process.env.DB_URL!, {
  cache: upstashCache(),
});
```

You can also explicitly define your Upstash credentials, enable global caching for all queries by default or pass custom caching options:

```ts
import { upstashCache } from "drizzle-orm/cache/upstash";
import { drizzle } from "drizzle-orm/...";

const db = drizzle(process.env.DB_URL!, {
  cache: upstashCache({
    // 👇 Redis credentials (optional — can also be pulled from env vars)
    url: '<UPSTASH_URL>',
    token: '<UPSTASH_TOKEN>',

    // 👇 Enable caching for all queries by default (optional)
    global: true,

    // 👇 Default cache behavior (optional)
    config: { ex: 60 }
  })
});
```

