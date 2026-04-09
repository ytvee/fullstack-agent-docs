---
name: mdx-blog
description: Creates and configures MDX blog functionality for Next.js App Router projects. Handles gray-matter frontmatter parsing, static params generation from filesystem, remark/rehype plugin setup, post listing with sorting and tag filtering. Triggers on requests like "create a blog post", "add MDX support", "set up blog", "configure frontmatter", "list posts by tag", "generate static params for blog".
---

## File structure

Store all posts in `content/posts/` at the project root. Never put posts inside `src/`.

Naming convention: `YYYY-MM-DD-slug.mdx`. The slug is derived from the filename by stripping the date prefix.

```
content/
└── posts/
    ├── 2024-01-15-getting-started.mdx
    └── 2024-02-20-nextjs-tips.mdx
```

## Frontmatter schema

Every post must have these fields:

```yaml
---
title: string
date: YYYY-MM-DD
description: string
tags: string[]
published: boolean
---
```

`published: false` hides the post in production but renders it in development. Check `process.env.NODE_ENV === 'development'` to filter unpublished posts.

See [full frontmatter reference](docs/frontmatter.md) for optional fields (`coverImage`, `author`, `readingTime`, `canonical`).

## TypeScript types

Define in `src/lib/posts.ts`:

```typescript
export interface Post {
  slug: string
  title: string
  date: string
  description: string
  tags: string[]
  published: boolean
  content: string
}

export interface PostMeta extends Omit<Post, 'content'> {}
```

## Parsing posts with gray-matter

Install: `npm install gray-matter`

Create `src/lib/posts.ts` with `import 'server-only'` at the top — these functions must never run on the client.

```typescript
import 'server-only'
import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const postsDirectory = path.join(process.cwd(), 'content/posts')

export function getAllPosts(): PostMeta[] {
  const fileNames = fs.readdirSync(postsDirectory)

  const posts = fileNames
    .filter((name) => name.endsWith('.mdx') || name.endsWith('.md'))
    .map((fileName) => {
      const slug = fileName
        .replace(/^\d{4}-\d{2}-\d{2}-/, '')
        .replace(/\.mdx?$/, '')

      const fullPath = path.join(postsDirectory, fileName)
      const fileContents = fs.readFileSync(fullPath, 'utf8')
      const { data } = matter(fileContents)

      return {
        slug,
        title: data.title as string,
        date: data.date as string,
        description: data.description as string,
        tags: (data.tags as string[]) ?? [],
        published: data.published as boolean,
      }
    })
    .filter((post) => {
      if (process.env.NODE_ENV === 'development') return true
      return post.published
    })

  return posts.sort((a, b) => (a.date < b.date ? 1 : -1))
}

export function getPostBySlug(slug: string): Post {
  const fileNames = fs.readdirSync(postsDirectory)
  const fileName = fileNames.find((name) => name.endsWith(`-${slug}.mdx`) || name.endsWith(`-${slug}.md`))

  if (!fileName) throw new Error(`Post not found: ${slug}`)

  const fullPath = path.join(postsDirectory, fileName)
  const fileContents = fs.readFileSync(fullPath, 'utf8')
  const { data, content } = matter(fileContents)

  return {
    slug,
    title: data.title as string,
    date: data.date as string,
    description: data.description as string,
    tags: (data.tags as string[]) ?? [],
    published: data.published as boolean,
    content,
  }
}

export function getPostsByTag(tag: string): PostMeta[] {
  return getAllPosts().filter((post) => post.tags.includes(tag))
}

export function getAllTags(): string[] {
  const posts = getAllPosts()
  const tags = new Set(posts.flatMap((post) => post.tags))
  return Array.from(tags).sort()
}
```

## MDX rendering: @next/mdx vs next-mdx-remote

**`@next/mdx`** — static compilation at build time.
- Pros: faster, simpler config, no runtime overhead.
- Cons: cannot load MDX content dynamically at runtime.
- Use when: all posts exist on disk at build time (filesystem blog).

**`next-mdx-remote`** — parses and renders MDX at runtime.
- Pros: content can come from a CMS, database, or API.
- Cons: adds runtime complexity, slightly slower.
- Use when: posts are fetched from an external source or change without rebuild.

For a filesystem-based blog, use `@next/mdx`.

### Setup with @next/mdx

```bash
npm install @next/mdx @mdx-js/loader @mdx-js/react
npm install -D @types/mdx
```

See [docs/plugins.md](docs/plugins.md) for the complete `next.config.ts` configuration with remark/rehype plugins.

## App Router integration

### Route: `/blog/[slug]/page.tsx`

```typescript
import { getAllPosts, getPostBySlug } from '@/lib/posts'

export async function generateStaticParams() {
  const posts = getAllPosts()
  return posts.map((post) => ({ slug: post.slug }))
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params
  const post = getPostBySlug(slug)
  return {
    title: post.title,
    description: post.description,
  }
}

export default async function PostPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params
  const post = getPostBySlug(slug)
  // Render post.content with MDX
}
```

### Route: `/blog/page.tsx`

```typescript
import { getAllPosts } from '@/lib/posts'

export default async function BlogPage() {
  const posts = getAllPosts()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.slug}>
          <a href={`/blog/${post.slug}`}>{post.title}</a>
          <time>{post.date}</time>
        </li>
      ))}
    </ul>
  )
}
```

## remark/rehype plugins

Install:

```bash
npm install rehype-pretty-code shiki remark-gfm rehype-slug rehype-autolink-headings
```

- `rehype-pretty-code` + `shiki` — syntax highlighting with themes
- `remark-gfm` — tables, strikethrough, task lists
- `rehype-slug` — adds `id` attributes to headings
- `rehype-autolink-headings` — adds anchor links to headings

See [docs/plugins.md](docs/plugins.md) for full configuration.

## Common mistakes

**`fs` does not work in Edge Runtime.** Post-reading functions must run in Node.js runtime only. Do not use them in middleware or edge routes.

**Use `process.cwd()`, not `__dirname`.** In Next.js, `__dirname` points to the compiled output directory, not the project root. Always use `process.cwd()` to build absolute paths.

**Do not call `readFileSync` inside React components.** Keep all filesystem access inside `src/lib/` functions that are called from Server Components or `generateStaticParams`. Components should receive already-parsed data as props.

**Do not import `gray-matter` on the client.** The `import 'server-only'` guard at the top of `src/lib/posts.ts` enforces this. If you see a build error about `server-only`, a client component is importing a server module.
