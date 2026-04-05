#### `roles`

<rem025/>

If you are using Drizzle Kit to manage your schema and especially the defined roles, there may be situations where you have some roles that are not defined in the Drizzle schema. 
In such cases, you may want Drizzle Kit to skip those `roles` without the need to write each role in your Drizzle schema and mark it with `.existing()`.

The `roles` option lets you:

- Enable or disable role management with Drizzle Kit.
- Exclude specific roles from management by Drizzle Kit.
- Include specific roles for management by Drizzle Kit.
- Enable modes for providers like `Neon` and `Supabase`, which do not manage their specific roles.
- Combine all the options above

|               |                       |
| :------------ | :-----------------    |
| type          | `boolean \| { provider: "neon" \| "supabase", include: string[], exclude: string[]}`|
| default       | `false`                  |
| commands      | `push` `pull` `generate` |

<rem025/>

By default, `drizzle-kit` won't manage roles for you, so you will need to enable that. in `drizzle.config.ts`
```ts
export default defineConfig({
  dialect: "postgresql",
  entities: {
    roles: true
  }
});
```

**You have a role `admin` and want to exclude it from the list of manageable roles**

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      exclude: ['admin']
    }
  }
});
```

**You have a role `admin` and want to include to the list of manageable roles**

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      include: ['admin']
    }
  }
});
```

**If you are using `Neon` and want to exclude roles defined by `Neon`, you can use the provider option**

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      provider: 'neon'
    }
  }
});
```

**If you are using `Supabase` and want to exclude roles defined by `Supabase`, you can use the provider option**

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      provider: 'supabase'
    }
  }
});
```

<Callout title='important'>
You may encounter situations where Drizzle is slightly outdated compared to new roles specified by database providers, 
so you may need to use both the `provider` option and `exclude` additional roles. You can easily do this with Drizzle:

```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  ...
  entities: {
    roles: {
      provider: 'supabase',
      exclude: ['new_supabase_role']
    }
  }
});
```
</Callout>

