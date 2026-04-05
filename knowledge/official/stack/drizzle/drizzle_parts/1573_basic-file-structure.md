## Basic file structure

This guide uses the following file structure:

```text
📦 <project root>
 ├ 📂 migrations
 │  ├ 📂 meta
 │  └ 📜 0000_heavy_doctor_doom.sql
 ├ 📂 public
 ├ 📂 src
 │  ├ 📂 actions
 │  │  └ 📜 todoActions.ts
 │  ├ 📂 app
 │  │  ├ 📜 favicon.ico
 │  │  ├ 📜 globals.css
 │  │  ├ 📜 layout.tsx
 │  │  └ 📜 page.tsx
 │  ├ 📂 components
 │  │  ├ 📜 addTodo.tsx
 │  │  ├ 📜 todo.tsx
 │  │  └ 📜 todos.tsx
 │  └ 📂 db
 │  │  ├ 📜 drizzle.ts
 │  │  └ 📜 schema.ts
 │  └ 📂 types
 │     └ 📜 todoType.ts
 ├ 📜 .env
 ├ 📜 .eslintrc.json
 ├ 📜 .gitignore
 ├ 📜 drizzle.config.ts
 ├ 📜 next-env.d.ts
 ├ 📜 next.config.mjs
 ├ 📜 package-lock.json
 ├ 📜 package.json
 ├ 📜 postcss.config.mjs
 ├ 📜 README.md
 ├ 📜 tailwind.config.ts
 └ 📜 tsconfig.json
```


Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-encore


import Steps from "@mdx/Steps.astro";
import Npm from "@mdx/Npm.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import CodeTab from "@mdx/CodeTab.astro";
import Section from "@mdx/Section.astro";
import Callout from "@mdx/Callout.astro";
import Prerequisites from "@mdx/Prerequisites.astro";

This tutorial demonstrates how to use **Drizzle ORM** with **Encore**, an open source backend framework with built-in infrastructure automation and observability.

<Prerequisites>
  - You should have the Encore CLI installed. You can install it with:
  ```bash
  # macOS
  brew install encoredev/tap/encore

  # Linux
  curl -L https://encore.dev/install.sh | bash

  # Windows
  iwr https://encore.dev/install.ps1 | iex
  ```

  - You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
  <Npm>
    drizzle-orm
    -D drizzle-kit
  </Npm>
</Prerequisites>

