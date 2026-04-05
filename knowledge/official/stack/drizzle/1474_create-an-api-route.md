#### Create an API route

Create `route.ts` in `src/app/api/hello` directory. To learn more about how to write a function, see the [Functions API Reference](https://vercel.com/docs/functions/functions-api-reference) and [Vercel Functions Quickstart](https://vercel.com/docs/functions/quickstart).

```ts copy filename="src/app/api/hello/route.ts"
import { db } from "@/app/db/db";
import { usersTable } from "@/app/db/schema";
import { NextResponse } from "next/server";

export const dynamic = 'force-dynamic'; // static by default, unless reading the request
export const runtime = 'edge' // specify the runtime to be edge

export async function GET(request: Request) {
  const users = await db.select().from(usersTable)

  return NextResponse.json({ users, message: 'success' });
}
```

