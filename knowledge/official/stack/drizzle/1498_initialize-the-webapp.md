#### Initialize the webapp

Now that we have set up Drizzle to connect to Nile and we have our schema in place, we can use them in a multi-tenant web application. 
We are using Express as the web framework in this example, although Nile and Drizzle can be used from any web framework.

To keep the example simple, we'll implement the webapp in a single file - `src/app.ts`. We'll start by initializing the webapp:

```typescript copy filename="src/app.ts"
import express from "express";
import { tenantDB, tenantContext, db } from "./db/db";
import {
  tenants as tenantSchema,
  todos as todoSchema,
} from "./db/schema";
import { eq } from "drizzle-orm";

const PORT = process.env.PORT || 3001;

const app = express();
app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
app.use(express.json());
```

