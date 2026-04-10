# 40 - Skills (On-demand Knowledge)

> **Scope:** All tasks
>
> **Purpose:** Instructs the agent to load specialized knowledge before writing code for a known domain.

## How skills work

Skills in `.roo/skills/` contain focused, battle-tested knowledge for recurring tasks.
Before writing code for any domain listed below, **read the corresponding `SKILL.md` file first**.

| Task | Read before starting |
|---|---|
| Pages, routes, layouts, features, Server Actions, DAL, Suspense | `.roo/skills/nextjs-app-router/SKILL.md` |
| Blog posts, MDX, frontmatter, gray-matter, remark/rehype | `.roo/skills/mdx-blog/SKILL.md` |
| shadcn/ui components, `cn()`, `cva`, variants, wrappers | `.roo/skills/shadcn-component/SKILL.md` |
| Zod schemas, validation, Server Actions, search params | `.roo/skills/zod-schema/SKILL.md` |

## When to apply a skill

Match the user's request against these triggers:

**`nextjs-app-router`** — triggered by: "create a page", "add a route", "set up layout", "implement Server Action", "configure DAL", "add loading state", "set up Suspense", "create a feature", "structure a new feature", "generateStaticParams", "dynamic segment".

**`mdx-blog`** — triggered by: "create a blog post", "add MDX support", "set up blog", "configure frontmatter", "list posts by tag", "generate static params for blog", "gray-matter", "remark plugin", "rehype plugin".

**`shadcn-component`** — triggered by: "add a button", "install shadcn", "customize theme", "create a variant", "add dialog", "use cn()", "make a card", "shadcn add", "asChild".

**`zod-schema`** — triggered by: "validate form data", "parse search params", "add Zod schema", "validate Server Action input", "type-safe env vars", "safeParse", "schema for form".

## Protocol

1. Identify which skill applies to the request.
2. Read the `SKILL.md` file — do not skip this step even if the task seems straightforward.
3. If the skill references `docs/` files for a specific sub-topic, read those too.
4. Follow the patterns and conventions in the skill exactly — they encode project-specific decisions.
5. If no skill matches, proceed with the rules from `00-context.md` through `30-security.md`.
