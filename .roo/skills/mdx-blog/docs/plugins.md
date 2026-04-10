# remark/rehype plugins configuration

## Installation

```bash
npm install rehype-pretty-code shiki remark-gfm rehype-slug rehype-autolink-headings
npm install @next/mdx @mdx-js/loader @mdx-js/react
npm install -D @types/mdx
```

## next.config.ts

```typescript
import type { NextConfig } from 'next'
import createMDX from '@next/mdx'
import remarkGfm from 'remark-gfm'
import rehypePrettyCode from 'rehype-pretty-code'
import rehypeSlug from 'rehype-slug'
import rehypeAutolinkHeadings from 'rehype-autolink-headings'

const rehypePrettyCodeOptions = {
  theme: 'github-dark',
  keepBackground: true,
  onVisitLine(node: { children: { type: string }[] }) {
    if (node.children.length === 0) {
      node.children = [{ type: 'text', value: ' ' }]
    }
  },
}

const withMDX = createMDX({
  options: {
    remarkPlugins: [remarkGfm],
    rehypePlugins: [
      [rehypePrettyCode, rehypePrettyCodeOptions],
      rehypeSlug,
      [rehypeAutolinkHeadings, { behavior: 'wrap' }],
    ],
  },
})

const nextConfig: NextConfig = {
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}

export default withMDX(nextConfig)
```

## src/mdx-components.tsx

Required by `@next/mdx` for App Router. Place at the project root (next to `src/`):

```typescript
import type { MDXComponents } from 'mdx/types'
import Image, { ImageProps } from 'next/image'
import Link from 'next/link'

export function useMDXComponents(components: MDXComponents): MDXComponents {
  return {
    h1: ({ children }) => <h1 className="text-3xl font-bold mt-8 mb-4">{children}</h1>,
    h2: ({ children }) => <h2 className="text-2xl font-semibold mt-6 mb-3">{children}</h2>,
    h3: ({ children }) => <h3 className="text-xl font-medium mt-4 mb-2">{children}</h3>,
    p: ({ children }) => <p className="leading-7 mb-4">{children}</p>,
    a: ({ href, children }) => (
      <Link href={href ?? '#'} className="text-blue-600 underline hover:text-blue-800">
        {children}
      </Link>
    ),
    img: (props) => (
      <Image
        {...(props as ImageProps)}
        className="rounded-lg my-6"
        width={800}
        height={450}
        alt={props.alt ?? ''}
      />
    ),
    code: ({ children }) => (
      <code className="bg-gray-100 text-gray-800 px-1 py-0.5 rounded text-sm font-mono">
        {children}
      </code>
    ),
    ...components,
  }
}
```

## rehype-pretty-code themes

Available Shiki themes: `github-dark`, `github-light`, `dracula`, `nord`, `one-dark-pro`, `catppuccin-mocha`.

For light/dark mode switching:

```typescript
const rehypePrettyCodeOptions = {
  theme: {
    dark: 'github-dark',
    light: 'github-light',
  },
}
```

Then in CSS:

```css
code[data-theme='light'],
pre[data-theme='light'] {
  display: block;
}

code[data-theme='dark'],
pre[data-theme='dark'] {
  display: none;
}

@media (prefers-color-scheme: dark) {
  code[data-theme='light'],
  pre[data-theme='light'] {
    display: none;
  }

  code[data-theme='dark'],
  pre[data-theme='dark'] {
    display: block;
  }
}
```

## Line highlighting in code blocks

With `rehype-pretty-code`, highlight specific lines in MDX:

````markdown
```typescript {2,4-6}
const a = 1
const b = 2  // highlighted
const c = 3
const d = 4  // highlighted
const e = 5  // highlighted
const f = 6  // highlighted
```
````

## rehype-autolink-headings behavior options

- `'prepend'` — inserts anchor before heading text
- `'append'` — inserts anchor after heading text
- `'wrap'` — wraps the entire heading in an anchor
- `'before'` — inserts anchor as a sibling before the heading
- `'after'` — inserts anchor as a sibling after the heading

`'wrap'` is the most accessible option. For a visible anchor icon, use `'prepend'` with custom content:

```typescript
[rehypeAutolinkHeadings, {
  behavior: 'prepend',
  properties: { className: ['anchor'] },
  content: { type: 'text', value: '#' },
}]
```
