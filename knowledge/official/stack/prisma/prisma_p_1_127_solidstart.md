# SolidStart (/docs/guides/frameworks/solid-start)



Introduction [#introduction]

Prisma ORM streamlines database access with type-safe queries and a smooth developer experience. SolidStart, a modern framework for building reactive web apps with SolidJS, pairs well with Prisma and Postgres to create a clean and scalable full-stack architecture.

In this guide, you'll learn how to integrate Prisma ORM with a Prisma Postgres database in a SolidStart project from scratch. You can find a complete example of this guide on [GitHub](https://github.com/prisma/prisma-examples/tree/latest/orm/solid-start).

Prerequisites [#prerequisites]

* [Node.js 20+](https://nodejs.org)

1. Set up your project [#1-set-up-your-project]

Begin by creating a new SolidStart app. In your terminal, run:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm init solid@latest
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm create solid
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn create solid
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx create-solid
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Use the following options when prompted:

<CalloutContainer type="info">
  <CalloutDescription>
    * *Project name:* `my-solid-prisma-app`
    * *Is this a SolidStart project:* `Yes`
    * *Template:* `bare`
    * *Use TypeScript:* `Yes`
  </CalloutDescription>
</CalloutContainer>

Next, navigate into your new project, install dependencies, and start the development server:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    cd my-solid-prisma-app
    npm install
    npm run dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    cd my-solid-prisma-app
    pnpm install
    pnpm run dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    cd my-solid-prisma-app
    yarn install
    yarn dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    cd my-solid-prisma-app
    bun install
    bun run dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Once the dev server is running, open `http://localhost:3000` in your browser. You should see the SolidStart welcome screen.

Clean up the default UI by editing the `app.tsx` file and replacing its content with the following code:

```typescript title="src/app.tsx"
import "./app.css";

export default function App() {
  return (
    <main>
      <h1>SolidStart + Prisma</h1>
    </main>
  );
}
```

2. Install and Configure Prisma [#2-install-and-configure-prisma]

2.1. Install dependencies [#21-install-dependencies]

To get started with Prisma, you'll need to install a few dependencies:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm install prisma tsx @types/pg --save-dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add prisma tsx @types/pg --save-dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add prisma tsx @types/pg --dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add prisma tsx @types/pg --dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm install @prisma/client @prisma/adapter-pg dotenv pg
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add @prisma/client @prisma/adapter-pg dotenv pg
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add @prisma/client @prisma/adapter-pg dotenv pg
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add @prisma/client @prisma/adapter-pg dotenv pg
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CalloutContainer type="info">
  <CalloutDescription>
    If you are using a different database provider (MySQL, SQL Server, SQLite), install the corresponding driver adapter package instead of `@prisma/adapter-pg`. For more information, see [Database drivers](/orm/core-concepts/supported-databases/database-drivers).
  </CalloutDescription>
</CalloutContainer>

Once installed, initialize Prisma in your project:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma init --output ../src/generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma init --output ../src/generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma init --output ../src/generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma init --output ../src/generated/prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CalloutContainer type="info">
  <CalloutDescription>
    `prisma init` creates the Prisma scaffolding and a local `DATABASE_URL`. In the next step, you will create a Prisma Postgres database and replace that value with a direct `postgres://...` connection string.
  </CalloutDescription>
</CalloutContainer>

This will create:

* A `prisma` directory with a `schema.prisma` file.
* A `prisma.config.ts` file for configuring Prisma
* A `.env` file containing a local `DATABASE_URL` at the project root.
* An `output` directory for the generated Prisma Client as `src/generated/prisma`.

Create a Prisma Postgres database and replace the generated `DATABASE_URL` in your `.env` file with the `postgres://...` connection string from the CLI output:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx create-db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx create-db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx create-db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun create-db
    ```
  </CodeBlockTab>
</CodeBlockTabs>

2.2. Define your Prisma Schema [#22-define-your-prisma-schema]

In the `prisma/schema.prisma` file, add the following models and change the generator to use the `prisma-client` provider:

```prisma title="prisma/schema.prisma"
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}

datasource db {
  provider = "postgresql"
}

model User { // [!code ++]
  id    Int     @id @default(autoincrement()) // [!code ++]
  email String  @unique // [!code ++]
  name  String? // [!code ++]
  posts Post[] // [!code ++]
} // [!code ++]
 // [!code ++]
model Post { // [!code ++]
  id        Int     @id @default(autoincrement()) // [!code ++]
  title     String // [!code ++]
  content   String? // [!code ++]
  published Boolean @default(false) // [!code ++]
  authorId  Int // [!code ++]
  author    User    @relation(fields: [authorId], references: [id]) // [!code ++]
} // [!code ++]
```

This creates two models: `User` and `Post`, with a one-to-many relationship between them.

2.3 Add dotenv to prisma.config.ts [#23-add-dotenv-to-prismaconfigts]

To get access to the variables in the `.env` file, they can either be loaded by your runtime, or by using `dotenv`.
Include an import for `dotenv` at the top of the `prisma.config.ts`

```ts
import "dotenv/config"; // [!code ++]
import { defineConfig, env } from "prisma/config";
export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

2.4. Configure the Prisma Client generator [#24-configure-the-prisma-client-generator]

Now, run the following command to create the database tables and generate the Prisma Client:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma migrate dev --name init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev --name init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev --name init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev --name init
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma generate
    ```
  </CodeBlockTab>
</CodeBlockTabs>

2.5. Seed the database [#25-seed-the-database]

Let's add some seed data to populate the database with sample users and posts.

Create a new file called `seed.ts` in the `prisma/` directory:

```typescript title="prisma/seed.ts"
import { PrismaClient, Prisma } from "../src/generated/prisma/client.js";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

const prisma = new PrismaClient({
  adapter,
});

const userData: Prisma.UserCreateInput[] = [
  {
    name: "Alice",
    email: "alice@prisma.io",
    posts: {
      create: [
        {
          title: "Join the Prisma Discord",
          content: "https://pris.ly/discord",
          published: true,
        },
        {
          title: "Prisma on YouTube",
          content: "https://pris.ly/youtube",
        },
      ],
    },
  },
  {
    name: "Bob",
    email: "bob@prisma.io",
    posts: {
      create: [
        {
          title: "Follow Prisma on Twitter",
          content: "https://www.twitter.com/prisma",
          published: true,
        },
      ],
    },
  },
];

export async function main() {
  for (const u of userData) {
    await prisma.user.create({ data: u });
  }
}

main();
```

Now, tell Prisma how to run this script by updating your `prisma.config.ts`:

```ts title="prisma.config.ts"
import "dotenv/config";
import { defineConfig, env } from "prisma/config";
export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    seed: `tsx prisma/seed.ts`, // [!code ++]
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

Run the seed script:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma db seed
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db seed
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db seed
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db seed
    ```
  </CodeBlockTab>
</CodeBlockTabs>

And open Prisma Studio to inspect your data:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma studio
    ```
  </CodeBlockTab>
</CodeBlockTabs>

3. Integrate Prisma into SolidStart [#3-integrate-prisma-into-solidstart]

3.1. Create a Prisma Client [#31-create-a-prisma-client]

At the root of your project, create a new `lib` folder and a `prisma.ts` file inside it:

```bash
mkdir -p lib && touch lib/prisma.ts
```

Add the following code to create a Prisma Client instance:

```typescript title="lib/prisma.ts"
import { PrismaClient } from "../src/generated/prisma/client.js";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

const prisma = new PrismaClient({
  adapter,
});

export default prisma;
```

<CalloutContainer type="warning">
  <CalloutDescription>
    We recommend using a connection pooler (like [Prisma Accelerate](https://www.prisma.io/accelerate)) to manage database connections efficiently.

    If you choose not to use one, **avoid** instantiating `PrismaClient` globally in long-lived environments. Instead, create and dispose of the client per request to prevent exhausting your database connections.
  </CalloutDescription>
</CalloutContainer>

3.2. Create an API Route [#32-create-an-api-route]

Now, let's fetch data from the database using an API route.

Create a new file at `src/routes/api/users.ts`:

```typescript title="src/routes/api/users.ts"
import prisma from "../../../lib/prisma";

export async function GET() {
  const users = await prisma.user.findMany({
    include: {
      posts: true,
    },
  });
  return new Response(JSON.stringify(users), {
    headers: { "Content-Type": "application/json" },
  });
}
```

3.3. Fetch Data in Your Component [#33-fetch-data-in-your-component]

In your `app.tsx` file, use `createResource` to fetch data from your new API route:

```typescript title="src/app.tsx"
import "./app.css";
import { createResource } from "solid-js"; // [!code ++]
import { User, Post } from "./generated/prisma/client"; // [!code ++]
 // [!code ++]
type UserWithPosts = User & { // [!code ++]
  posts: Post[]; // [!code ++]
}; // [!code ++]
 // [!code ++]
const fetchUsers = async () => { // [!code ++]
  const res = await fetch("http://localhost:3000/api/users"); // [!code ++]
  return res.json(); // [!code ++]
}; // [!code ++]

export default function App() {
  const [users, { mutate, refetch }] = createResource<UserWithPosts[]>(fetchUsers); // [!code ++]

  return (
    <main>
      <h1>SolidStart + Prisma</h1>
    </main>
  );
}
```

<CalloutContainer type="info">
  <CalloutDescription>
    `createResource` is a SolidJS hook for managing async data. It tracks loading and error states automatically. [Learn more](https://docs.solidjs.com/reference/basic-reactivity/create-resource#createresource).
  </CalloutDescription>
</CalloutContainer>

3.4. Display the Data [#34-display-the-data]

To show the users and their posts, use SolidJS's `<For>` component:

```typescript title="src/app.tsx"
import "./app.css";
import { createResource, For } from "solid-js"; // [!code highlight]
import { User, Post } from "./generated/prisma/client";

type UserWithPosts = User & {
  posts: Post[];
};

const fetchUsers = async () => {
  const res = await fetch("http://localhost:3000/api/users");
  return res.json();
};

export default function App() {
  const [users, { mutate, refetch }] =
    createResource<UserWithPosts[]>(fetchUsers);

  return (
    <main>
      <h1>SolidJS + Prisma</h1>
      <For each={users() ?? []}> // [!code ++]
        {(user) => ( // [!code ++]
          <div> // [!code ++]
            <h3>{user.name}</h3> // [!code ++]
            <For each={user.posts}>{(post) => <p>{post.title}</p>}</For> // [!code ++]
          </div> // [!code ++]
        )} // [!code ++]
      </For> // [!code ++]
    </main>
  );
}
```

<CalloutContainer type="info">
  <CalloutDescription>
    `<For>` loops through an array reactively. Think of it like `.map()` in React. [Learn more](https://docs.solidjs.com/reference/components/for)
  </CalloutDescription>
</CalloutContainer>

3.5. Add Loading and Error States [#35-add-loading-and-error-states]

Use SolidJS's `<Show>` component to handle loading and error conditions:

```typescript title="src/app.tsx"
import "./app.css";
import { createResource, For, Show } from "solid-js"; // [!code highlight]
import { User, Post } from "./generated/prisma/client";

type UserWithPosts = User & {
  posts: Post[];
};

const fetchUsers = async () => {
  const res = await fetch("http://localhost:3000/api/users");
  return res.json();
};

export default function App() {
  const [users, { mutate, refetch }] =
    createResource<UserWithPosts[]>(fetchUsers);

  return (
    <main>
      <h1>SolidJS + Prisma</h1>
      <Show when={!users.loading} fallback={<p>Loading...</p>}> // [!code ++]
        <Show when={!users.error} fallback={<p>Error loading data</p>}> // [!code ++]
          <For each={users()}>
            {(user) => (
              <div>
                <h3>{user.name}</h3>
                <For each={user.posts}>{(post) => <p>{post.title}</p>}</For>
              </div>
            )}
          </For>
        </Show> // [!code ++]
      </Show> // [!code ++]
    </main>
  );
}
```

<CalloutContainer type="info">
  <CalloutDescription>
    `<Show>` conditionally renders content. It's similar to an `if` statement. [Learn more](https://docs.solidjs.com/reference/components/show)
  </CalloutDescription>
</CalloutContainer>

You're done! You've just created a SolidStart app connected to a Prisma Postgres database.

Next Steps [#next-steps]

Now that you have a working SolidStart app connected to a Prisma Postgres database, you can:

* Extend your Prisma schema with more models and relationships
* Add create/update/delete routes and forms
* Explore authentication, validation, and optimistic updates

More Info [#more-info]

* [Prisma ORM Docs](/orm)
* [SolidStart Documentation](https://start.solidjs.com/)


