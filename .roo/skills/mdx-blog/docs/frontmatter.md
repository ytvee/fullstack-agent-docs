# Frontmatter fields reference

All frontmatter is parsed by `gray-matter`. Fields are typed via the `Post` interface in `src/lib/posts.ts`.

## Required fields

| Field | Type | Description |
|---|---|---|
| `title` | `string` | Post title, used in `<title>` and `<h1>` |
| `date` | `YYYY-MM-DD` | Publication date, used for sorting |
| `description` | `string` | Short summary, used in meta description and post cards |
| `tags` | `string[]` | Topic tags, used for filtering |
| `published` | `boolean` | `false` hides in production, shows in development |

Example:

```yaml
---
title: Building a Blog with Next.js and MDX
date: 2024-03-10
description: Step-by-step guide to setting up a filesystem-based MDX blog with Next.js App Router.
tags: [nextjs, mdx, blog]
published: true
---
```

## Optional fields

### coverImage

```yaml
coverImage: /images/posts/nextjs-blog-cover.jpg
```

Path relative to `public/`. Used in Open Graph and post header. Add to `Post` interface:

```typescript
coverImage?: string
```

In `getAllPosts`, read as:

```typescript
coverImage: data.coverImage as string | undefined,
```

### author

```yaml
author: Jane Doe
```

For multi-author blogs. Alternatively store as an object:

```yaml
author:
  name: Jane Doe
  avatar: /images/authors/jane.jpg
```

Then type as:

```typescript
author?: { name: string; avatar?: string }
```

### readingTime

Do not store as frontmatter — compute from content length:

```typescript
export function computeReadingTime(content: string): number {
  const wordsPerMinute = 200
  const words = content.trim().split(/\s+/).length
  return Math.ceil(words / wordsPerMinute)
}
```

Call in `getPostBySlug` and add `readingTime: number` to the `Post` interface.

### canonical

```yaml
canonical: https://original-source.com/article
```

For syndicated content. Use in `generateMetadata`:

```typescript
export async function generateMetadata({ params }) {
  const post = getPostBySlug((await params).slug)
  return {
    alternates: {
      canonical: post.canonical ?? `https://yourdomain.com/blog/${post.slug}`,
    },
  }
}
```

## Type-safe frontmatter parsing

Validate frontmatter with Zod to catch malformed posts early:

```typescript
import { z } from 'zod'

const FrontmatterSchema = z.object({
  title: z.string(),
  date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
  description: z.string(),
  tags: z.array(z.string()).default([]),
  published: z.boolean(),
  coverImage: z.string().optional(),
  author: z.string().optional(),
  canonical: z.string().url().optional(),
})
```

Replace manual casts in `getAllPosts` and `getPostBySlug` with `FrontmatterSchema.parse(data)`. This will throw at build time if a post has invalid frontmatter.
