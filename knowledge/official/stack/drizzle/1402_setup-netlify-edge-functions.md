#### Setup Netlify Edge Functions

Create `netlify/edge-functions` directory in the root of your project. This is where you'll store your Edge Functions.

Create a function `user.ts` in the `netlify/edge-functions` directory.

```typescript copy filename="netlify/edge-functions/user.ts"
import type { Context } from "@netlify/edge-functions";

export default async (request: Request, context: Context) => {
  return new Response("User data");
};
```

<Callout type="warning">
The types for the `Request` and `Response` objects are in the global scope.
</Callout>

