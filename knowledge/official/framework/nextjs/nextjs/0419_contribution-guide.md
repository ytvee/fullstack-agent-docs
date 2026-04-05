---
title: Contribution Guide
description: Learn how to contribute to Next.js Documentation
url: "https://nextjs.org/docs/community/contribution-guide"
version: 16.2.2
---

# Contribution Guide

Welcome to the Next.js Docs Contribution Guide! We're excited to have you here.

This page provides instructions on how to edit the Next.js documentation. Our goal is to ensure that everyone in the community feels empowered to contribute and improve our docs.

## Why Contribute?

Open-source work is never done, and neither is documentation. Contributing to docs is a good way for beginners to get involved in open-source and for experienced developers to clarify more complex topics while sharing their knowledge with the community.

By contributing to the Next.js docs, you're helping us build a more robust learning resource for all developers. Whether you've found a typo, a confusing section, or you've realized that a particular topic is missing, your contributions are welcomed and appreciated.

## How to Contribute

The docs content can be found on the [Next.js repo](https://github.com/vercel/next.js/tree/canary/docs). To contribute, you can edit the files directly on GitHub or clone the repo and edit the files locally.

### GitHub Workflow

If you're new to GitHub, we recommend reading the [GitHub Open Source Guide](https://opensource.guide/how-to-contribute/#opening-a-pull-request) to learn how to fork a repository, create a branch, and submit a pull request.

> **Good to know**: The underlying docs code lives in a private codebase that is synced to the Next.js public repo. This means that you can't preview the docs locally. However, you'll see your changes on [nextjs.org](https://nextjs.org/docs) after merging a pull request.

### Writing MDX

The docs are written in [MDX](https://mdxjs.com/), a markdown format that supports JSX syntax. This allows us to embed React components in the docs. See the [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) for a quick overview of markdown syntax.

### VSCode

#### Previewing Changes Locally

VSCode has a built-in markdown previewer that you can use to see your edits locally. To enable the previewer for MDX files, you'll need to add a configuration option to your user settings.

Open the command palette (`⌘ + ⇧ + P` on Mac or `Ctrl + Shift + P` on Windows) and search from `Preferences: Open User Settings (JSON)`.

Then, add the following line to your `settings.json` file:

```json filename="settings.json"
{
  "files.associations": {
    "*.mdx": "markdown"
  }
}
```

Next, open the command palette again, and search for `Markdown: Preview File` or `Markdown: Open Preview to the Side`. This will open a preview window where you can see your formatted changes.

#### Extensions

We also recommend the following extensions for VSCode users:

* [MDX](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx): Intellisense and syntax highlighting for MDX.
* [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Format MDX files on save.

### Review Process

Once you've submitted your contribution, the Next.js or Developer Experience teams will review your changes, provide feedback, and merge the pull request when it's ready.

Please let us know if you have any questions or need further assistance in your PR's comments. Thank you for contributing to the Next.js docs and being a part of our community!

> **Tip:** Run `pnpm prettier-fix` to run Prettier before submitting your PR.

## File Structure

The docs use **file-system routing**. Each folder and files inside [`/docs`](https://github.com/vercel/next.js/tree/canary/docs) represent a route segment. These segments are used to generate the URL paths, navigation, and breadcrumbs.

The file structure reflects the navigation that you see on the site, and by default, navigation items are sorted alphabetically. However, we can change the order of the items by prepending a two-digit number (`00-`) to the folder or file name.

For example, in the [functions API Reference](/docs/app/api-reference/functions), the pages are sorted alphabetically because it makes it easier for developers to find a specific function:

```txt
04-functions
├── after.mdx
├── cacheLife.mdx
├── cacheTag.mdx
└── ...
```

But, in the [app router section](/docs/app), the files are prefixed with a two-digit number, sorted in the order developers should learn these concepts:

```txt
01-getting-started
├── 01-installation.mdx
├── 02-project-structure.mdx
├── 03-layouts-and-pages.mdx
└── ...
```

To quickly find a page, you can use `⌘ + P` (Mac) or `Ctrl + P` (Windows) to open the search bar on VSCode. Then, type the slug of the page you're looking for. E.g. `installation`

> **Why not use a manifest?**
>
> We considered using a manifest file (another popular way to generate the docs navigation), but we found that a manifest would quickly get out of sync with the files. File-system routing forces us to think about the structure of the docs and feels more native to Next.js.

## Metadata

Each page has a metadata block at the top of the file separated by three dashes.

### Required Fields

The following fields are **required**:

| Field         | Description                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| `title`       | The page's `<h1>` title, used for SEO and OG Images.                         |
| `description` | The page's description, used in the `<meta name="description">` tag for SEO. |

```yaml filename="required-fields.mdx"
