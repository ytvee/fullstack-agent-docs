### Mock Driver
This API is a successor to an undefined `drizzle({} as any)` API which we've used internally in Drizzle tests and rarely recommended to external developers. 

We decided to build and expose a proper API, every `drizzle` driver now has `drizzle.mock()`:
```ts
import { drizzle } from "drizzle-orm/...";

const db = drizzle.mock();
```

you can provide schema if necessary for types
```ts
import { drizzle } from "drizzle-orm/...";
import * as schema from "./schema"

const db = drizzle.mock({ schema });
```

Source: https://orm.drizzle.team/docs/gotchas

import CodeTab from "@mdx/CodeTab.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from "@mdx/Section.astro";
import Tab from "@mdx/Tab.astro";
import Tabs from "@mdx/Tabs.astro";
import Callout from "@mdx/Callout.astro";

