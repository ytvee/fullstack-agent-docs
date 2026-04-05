# shadcn/ui React Documentation (aggregated)

> Source: `apps/v4/content/docs` (excluding `changelog`).



---

<!-- SOURCE: apps/v4/content/docs/(root)/_blocks.mdx -->

## apps/v4/content/docs/(root)/_blocks.mdx

---
title: Blocks
description: Contribute components to the blocks library.
---

We are inviting the community to contribute to the [blocks library](/blocks). Share your components and blocks with other developers and help build a library of high-quality, reusable components.

We'd love to see all types of blocks: applications, marketing, products, and more.

## Setup your workspace

<Steps>

### Fork the repository

```bash
git clone https://github.com/shadcn-ui/ui.git
```

### Create a new branch

```bash
git checkout -b username/my-new-block
```

### Install dependencies

```bash
pnpm install
```

### Start the dev server

```bash
pnpm www:dev
```

</Steps>

## Add a block

A block can be a single component (eg. a variation of a ui component) or a complex component (eg. a dashboard) with multiple components, hooks, and utils.

<Steps>

### Create a new block

Create a new folder in the `apps/www/registry/new-york/blocks` directory. Make sure the folder is named in kebab-case and under `new-york`.

```txt
apps
└── www
    └── registry
        └── new-york
            └── blocks
                └── dashboard-01
```

<Callout className="mt-6">

**Note:** The build script will take care of building the block for the `default` style.

</Callout>

### Add your block files

Add your files to the block folder. Here is an example of a block with a page, components, hooks, and utils.

```txt
dashboard-01
└── page.tsx
└── components
    └── hello-world.tsx
    └── example-card.tsx
└── hooks
    └── use-hello-world.ts
└── lib
    └── format-date.ts
```

<Callout className="mt-6">

**Note:** You can start with one file and add more files later.

</Callout>

</Steps>

## Add your block to the registry

<Steps>

### Add your block definition to `registry-blocks.tsx`

To add your block to the registry, you need to add your block definition to `registry-blocks.ts`.

This follows the registry schema at [https://ui.shadcn.com/schema/registry-item.json](https://ui.shadcn.com/schema/registry-item.json).

```tsx title="apps/www/registry/registry-blocks.tsx" showLineNumbers
export const blocks = [
  // ...
  {
    name: "dashboard-01",
    author: "shadcn (https://ui.shadcn.com)",
    title: "Dashboard",
    description: "A simple dashboard with a hello world component.",
    type: "registry:block",
    registryDependencies: ["input", "button", "card"],
    dependencies: ["zod"],
    files: [
      {
        path: "blocks/dashboard-01/page.tsx",
        type: "registry:page",
        target: "app/dashboard/page.tsx",
      },
      {
        path: "blocks/dashboard-01/components/hello-world.tsx",
        type: "registry:component",
      },
      {
        path: "blocks/dashboard-01/components/example-card.tsx",
        type: "registry:component",
      },
      {
        path: "blocks/dashboard-01/hooks/use-hello-world.ts",
        type: "registry:hook",
      },
      {
        path: "blocks/dashboard-01/lib/format-date.ts",
        type: "registry:lib",
      },
    ],
    categories: ["dashboard"],
  },
]
```

Make sure you add a name, description, type, registryDependencies, dependencies, files, and categories. We'll go over each of these in more detail in the schema docs (coming soon).

### Run the build script

```bash
pnpm registry:build
```

<Callout className="mt-6">

**Note:** you do not need to run this script for every change. You only need to run it when you update the block definition.

</Callout>

### View your block

Once the build script is finished, you can view your block at `http://localhost:3333/blocks/[CATEGORY]` or a full screen preview at `http://localhost:3333/view/styles/new-york/dashboard-01`.

<Image
  src="/images/block-preview-light.png"
  width="1432"
  height="960"
  alt="Block preview"
  className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
/>
<Image
  src="/images/block-preview-dark.png"
  width="1432"
  height="960"
  alt="Block preview"
  className="mt-6 hidden w-full overflow-hidden rounded-lg border shadow-sm dark:block"
/>

### Build your block

You can now build your block by editing the files in the block folder and viewing the changes in the browser.

If you add more files, make sure to add them to the `files` array in the block definition.

</Steps>

## Publish your block

Once you're ready to publish your block, you can submit a pull request to the main repository.

<Steps>

### Run the build script

```bash
pnpm registry:build
```

### Capture a screenshot

```bash
pnpm registry:capture
```

<Callout className="mt-6">

**Note:** If you've run the capture script before, you might need to delete the existing screenshots (both light and dark) at `apps/www/public/r/styles/new-york` and run the script again.

</Callout>

### Submit a pull request

Commit your changes and submit a pull request to the main repository.

Your block will be reviewed and merged. Once merged it will be published to the website and available to be installed via the CLI.

</Steps>

## Categories

The `categories` property is used to organize your block in the registry.

### Add a category

If you need to add a new category, you can do so by adding it to the `registryCategories` array in `apps/www/registry/registry-categories.ts`.

```tsx title="apps/www/registry/registry-categories.ts" showLineNumbers
export const registryCategories = [
  // ...
  {
    name: "Input",
    slug: "input",
    hidden: false,
  },
]
```

## Guidelines

Here are some guidelines to follow when contributing to the blocks library.

- The following properties are required for the block definition: `name`, `description`, `type`, `files`, and `categories`.
- Make sure to list all registry dependencies in `registryDependencies`. A registry dependency is the name of the component in the registry eg. `input`, `button`, `card`, etc.
- Make sure to list all dependencies in `dependencies`. A dependency is the name of the package in the registry eg. `zod`, `sonner`, etc.
- If your block has a page (optional), it should be the first entry in the `files` array and it should have a `target` property. This helps the CLI place the page in the correct location for file-based routing.
- **Imports should always use the `@/registry` path.** eg. `import { Input } from "@/registry/new-york/input"`


---

<!-- SOURCE: apps/v4/content/docs/(root)/cli.mdx -->

## apps/v4/content/docs/(root)/cli.mdx

---
title: shadcn
description: Use the shadcn CLI to add components to your project.
---

## init

Use the `init` command to initialize configuration and dependencies for a new project.

The `init` command installs dependencies, adds the `cn` util and configures CSS variables for the project.

```bash
npx shadcn@latest init
```

**Options**

```bash
Usage: shadcn init [options] [components...]

initialize your project and install dependencies

Arguments:
  components              name, url or local path to component

Options:
  -t, --template <template>  the template to use. (next, vite, start, react-router, laravel, astro)
  -b, --base <base>          the component library to use. (radix, base)
  -p, --preset [name]        use a preset configuration. (name, URL, or preset code)
  -n, --name <name>          the name for the new project.
  -d, --defaults             use default configuration. (default: false)
  -y, --yes                  skip confirmation prompt. (default: true)
  -f, --force                force overwrite of existing configuration. (default: false)
  -c, --cwd <cwd>            the working directory. defaults to the current directory.
  -s, --silent               mute output. (default: false)
  --monorepo                 scaffold a monorepo project.
  --no-monorepo              skip the monorepo prompt.
  --reinstall                re-install existing UI components.
  --no-reinstall             do not re-install existing UI components.
  --rtl                      enable RTL support.
  --no-rtl                   disable RTL support.
  --css-variables            use css variables for theming. (default: true)
  --no-css-variables         do not use css variables for theming.
  -h, --help                 display help for command
```

The `create` command is an alias for `init`:

```bash
npx shadcn@latest create
```

---

## add

Use the `add` command to add components and dependencies to your project.

```bash
npx shadcn@latest add [component]
```

**Options**

```bash
Usage: shadcn add [options] [components...]

add a component to your project

Arguments:
  components           name, url or local path to component

Options:
  -y, --yes            skip confirmation prompt. (default: false)
  -o, --overwrite      overwrite existing files. (default: false)
  -c, --cwd <cwd>      the working directory. defaults to the current directory.
  -a, --all            add all available components (default: false)
  -p, --path <path>    the path to add the component to.
  -s, --silent         mute output. (default: false)
  --dry-run            preview changes without writing files. (default: false)
  --diff [path]        show diff for a file.
  --view [path]        show file contents.
  -h, --help           display help for command
```

---

## view

Use the `view` command to view items from the registry before installing them.

```bash
npx shadcn@latest view [item]
```

You can view multiple items at once:

```bash
npx shadcn@latest view button card dialog
```

Or view items from namespaced registries:

```bash
npx shadcn@latest view @acme/auth @v0/dashboard
```

**Options**

```bash
Usage: shadcn view [options] <items...>

view items from the registry

Arguments:
  items            the item names or URLs to view

Options:
  -c, --cwd <cwd>  the working directory. defaults to the current directory.
  -h, --help       display help for command
```

---

## search

Use the `search` command to search for items from registries.

```bash
npx shadcn@latest search [registry]
```

You can search with a query:

```bash
npx shadcn@latest search @shadcn -q "button"
```

Or search multiple registries at once:

```bash
npx shadcn@latest search @shadcn @v0 @acme
```

The `list` command is an alias for `search`:

```bash
npx shadcn@latest list @acme
```

**Options**

```bash
Usage: shadcn search|list [options] <registries...>

search items from registries

Arguments:
  registries             the registry names or urls to search items from. Names
                         must be prefixed with @.

Options:
  -c, --cwd <cwd>        the working directory. defaults to the current directory.
  -q, --query <query>    query string
  -l, --limit <number>   maximum number of items to display per registry (default: "100")
  -o, --offset <number>  number of items to skip (default: "0")
  -h, --help             display help for command
```

---

## build

Use the `build` command to generate the registry JSON files.

```bash
npx shadcn@latest build
```

This command reads the `registry.json` file and generates the registry JSON files in the `public/r` directory.

**Options**

```bash
Usage: shadcn build [options] [registry]

build components for a shadcn registry

Arguments:
  registry             path to registry.json file (default: "./registry.json")

Options:
  -o, --output <path>  destination directory for json files (default: "./public/r")
  -c, --cwd <cwd>      the working directory. defaults to the current directory.
  -h, --help           display help for command
```

To customize the output directory, use the `--output` option.

```bash
npx shadcn@latest build --output ./public/registry
```

---

## docs

Use the `docs` command to fetch documentation and API references for components.

```bash
npx shadcn@latest docs [component]
```

**Options**

```bash
Usage: shadcn docs [options] [component]

fetch documentation and API references for components

Arguments:
  component          the component to get docs for

Options:
  -c, --cwd <cwd>    the working directory. defaults to the current directory.
  -b, --base <base>  the base to use either 'base' or 'radix'. defaults to project base.
  --json             output as JSON. (default: false)
  -h, --help         display help for command
```

---

## info

Use the `info` command to get information about your project.

```bash
npx shadcn@latest info
```

**Options**

```bash
Usage: shadcn info [options]

get information about your project

Options:
  -c, --cwd <cwd>  the working directory. defaults to the current directory.
  --json            output as JSON. (default: false)
  -h, --help        display help for command
```

---

## migrate

Use the `migrate` command to run migrations on your project.

```bash
npx shadcn@latest migrate [migration]
```

**Available Migrations**

| Migration | Description                                             |
| --------- | ------------------------------------------------------- |
| `icons`   | Migrate your UI components to a different icon library. |
| `radix`   | Migrate to radix-ui.                                    |
| `rtl`     | Migrate your components to support RTL (right-to-left). |

**Options**

```bash
Usage: shadcn migrate [options] [migration] [path]

run a migration.

Arguments:
  migration        the migration to run.
  path             optional path or glob pattern to migrate.

Options:
  -c, --cwd <cwd>  the working directory. defaults to the current directory.
  -l, --list       list all migrations. (default: false)
  -y, --yes        skip confirmation prompt. (default: false)
  -h, --help       display help for command
```

---

### migrate rtl

The `rtl` migration transforms your components to support RTL (right-to-left) languages.

```bash
npx shadcn@latest migrate rtl
```

This will:

1. Update `components.json` to set `rtl: true`
2. Transform physical CSS properties to logical equivalents (e.g., `ml-4` → `ms-4`, `text-left` → `text-start`)
3. Add `rtl:` variants where needed (e.g., `space-x-4` → `space-x-4 rtl:space-x-reverse`)

**Migrate specific files**

You can migrate specific files or use glob patterns:

```bash
# Migrate a specific file
npx shadcn@latest migrate rtl src/components/ui/button.tsx

# Migrate files matching a glob pattern
npx shadcn@latest migrate rtl "src/components/ui/**"
```

If no path is provided, the migration will transform all files in your `ui` directory (from `components.json`).

---

### migrate radix

The `radix` migration updates your imports from individual `@radix-ui/react-*` packages to the unified `radix-ui` package.

```bash
npx shadcn@latest migrate radix
```

This will:

1. Transform imports from `@radix-ui/react-*` to `radix-ui`
2. Add the `radix-ui` package to your `package.json`

**Before**

```tsx
import * as DialogPrimitive from "@radix-ui/react-dialog"
import * as SelectPrimitive from "@radix-ui/react-select"
```

**After**

```tsx
import { Dialog as DialogPrimitive, Select as SelectPrimitive } from "radix-ui"
```

**Migrate specific files**

You can migrate specific files or use glob patterns:

```bash
# Migrate a specific file.
npx shadcn@latest migrate radix src/components/ui/dialog.tsx

# Migrate files matching a glob pattern.
npx shadcn@latest migrate radix "src/components/ui/**"
```

If no path is provided, the migration will transform all files in your `ui` directory (from `components.json`).

Once complete, you can remove any unused `@radix-ui/react-*` packages from your `package.json`.


---

<!-- SOURCE: apps/v4/content/docs/(root)/components-json.mdx -->

## apps/v4/content/docs/(root)/components-json.mdx

---
title: components.json
description: Configuration for your project.
---

The `components.json` file holds configuration for your project.

We use it to understand how your project is set up and how to generate components customized for your project.

<Callout className="mt-6" title="Note: The `components.json` file is optional">
  It is **only required if you're using the CLI** to add components to your
  project. If you're using the copy and paste method, you don't need this file.
</Callout>

You can create a `components.json` file in your project by running the following command:

```bash
npx shadcn@latest init
```

See the <Link href="/docs/cli">CLI section</Link> for more information.

## $schema

You can see the JSON Schema for `components.json` [here](https://ui.shadcn.com/schema.json).

```json title="components.json"
{
  "$schema": "https://ui.shadcn.com/schema.json"
}
```

## style

The style for your components. **This cannot be changed after initialization.**

```json title="components.json"
{
  "style": "new-york"
}
```

The `default` style has been deprecated. Use the `new-york` style instead.

## tailwind

Configuration to help the CLI understand how Tailwind CSS is set up in your project.

See the <Link href="/docs/installation">installation section</Link> for how to set up Tailwind CSS.

### tailwind.config

Path to where your `tailwind.config.js` file is located. **For Tailwind CSS v4, leave this blank.**

```json title="components.json"
{
  "tailwind": {
    "config": "tailwind.config.js" | "tailwind.config.ts"
  }
}
```

### tailwind.css

Path to the CSS file that imports Tailwind CSS into your project.

```json title="components.json"
{
  "tailwind": {
    "css": "styles/global.css"
  }
}
```

### tailwind.baseColor

This is used to generate the default theme tokens for your components. **This cannot be changed after initialization.**

```json title="components.json"
{
  "tailwind": {
    "baseColor": "neutral" | "stone" | "zinc" | "mauve" | "olive" | "mist" | "taupe"
  }
}
```

### tailwind.cssVariables

We use and recommend CSS variables for theming.

Set `tailwind.cssVariables` to `true` to generate semantic theme tokens like `background`, `foreground`, and `primary`. Set it to `false` to generate inline Tailwind color utilities instead.

```json title="components.json"
{
  "tailwind": {
    "cssVariables": `true` | `false`
  }
}
```

For more information, see the <Link href="/docs/theming">theming docs</Link>.

**This cannot be changed after initialization.** To switch between CSS variables and utility classes, you'll have to delete and re-install your components.

### tailwind.prefix

The prefix to use for your Tailwind CSS utility classes. Components will be added with this prefix.

```json title="components.json"
{
  "tailwind": {
    "prefix": "tw-"
  }
}
```

## rsc

Whether or not to enable support for React Server Components.

The CLI automatically adds a `use client` directive to client components when set to `true`.

```json title="components.json"
{
  "rsc": `true` | `false`
}
```

## tsx

Choose between TypeScript or JavaScript components.

Setting this option to `false` allows components to be added as JavaScript with the `.jsx` file extension.

```json title="components.json"
{
  "tsx": `true` | `false`
}
```

## aliases

The CLI uses these values and the `paths` config from your `tsconfig.json` or `jsconfig.json` file to place generated components in the correct location.

Path aliases have to be set up in your `tsconfig.json` or `jsconfig.json` file.

<Callout className="mt-6">
  **Important:** If you're using the `src` directory, make sure it is included
  under `paths` in your `tsconfig.json` or `jsconfig.json` file.
</Callout>

### aliases.utils

Import alias for your utility functions.

```json title="components.json"
{
  "aliases": {
    "utils": "@/lib/utils"
  }
}
```

### aliases.components

Import alias for your components.

```json title="components.json"
{
  "aliases": {
    "components": "@/components"
  }
}
```

### aliases.ui

Import alias for `ui` components.

The CLI will use the `aliases.ui` value to determine where to place your `ui` components. Use this config if you want to customize the installation directory for your `ui` components.

```json title="components.json"
{
  "aliases": {
    "ui": "@/app/ui"
  }
}
```

### aliases.lib

Import alias for `lib` functions such as `format-date` or `generate-id`.

```json title="components.json"
{
  "aliases": {
    "lib": "@/lib"
  }
}
```

### aliases.hooks

Import alias for `hooks` such as `use-media-query` or `use-toast`.

```json title="components.json"
{
  "aliases": {
    "hooks": "@/hooks"
  }
}
```

## registries

Configure multiple resource registries for your project. This allows you to install components, libraries, utilities, and other resources from various sources including private registries.

See the <Link href="/docs/registry/namespace">Namespaced Registries</Link> documentation for detailed information.

### Basic Configuration

Configure registries with URL templates:

```json title="components.json"
{
  "registries": {
    "@v0": "https://v0.dev/chat/b/{name}",
    "@acme": "https://registry.acme.com/{name}.json",
    "@internal": "https://internal.company.com/{name}.json"
  }
}
```

The `{name}` placeholder is replaced with the resource name when installing.

### Advanced Configuration with Authentication

For private registries that require authentication:

```json title="components.json"
{
  "registries": {
    "@private": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}",
        "X-API-Key": "${API_KEY}"
      },
      "params": {
        "version": "latest"
      }
    }
  }
}
```

Environment variables in the format `${VAR_NAME}` are automatically expanded from your environment.

### Using Namespaced Registries

Once configured, install resources using the namespace syntax:

```bash
# Install from a configured registry
npx shadcn@latest add @v0/dashboard

# Install from private registry
npx shadcn@latest add @private/button

# Install multiple resources
npx shadcn@latest add @acme/header @internal/auth-utils
```

### Example: Multiple Registry Setup

```json title="components.json"
{
  "registries": {
    "@shadcn": "https://ui.shadcn.com/r/{name}.json",
    "@company-ui": {
      "url": "https://registry.company.com/ui/{name}.json",
      "headers": {
        "Authorization": "Bearer ${COMPANY_TOKEN}"
      }
    },
    "@team": {
      "url": "https://team.company.com/{name}.json",
      "params": {
        "team": "frontend",
        "version": "${REGISTRY_VERSION}"
      }
    }
  }
}
```

This configuration allows you to:

- Install public components from shadcn/ui
- Access private company UI components with authentication
- Use team-specific resources with versioning

For more information about authentication, see the <Link href="/docs/registry/authentication">Authentication</Link> documentation.


---

<!-- SOURCE: apps/v4/content/docs/(root)/directory.mdx -->

## apps/v4/content/docs/(root)/directory.mdx

---
title: Registry Directory
description: Discover community registries for shadcn/ui components and blocks.
---

import { TriangleAlertIcon } from "lucide-react"

These registries are built into the CLI with no additional configuration required. To add a component, run: `npx shadcn add @<registry>/<component>`.

<Callout
  type="warning"
  className="border-amber-200 bg-amber-50 font-semibold dark:border-amber-900 dark:bg-amber-950"
>
  Community registries are maintained by third-party developers. Always review
  code on installation to ensure it meets your security and quality standards.
</Callout>

Don't see a registry? Learn how to [add it here](/docs/registry/registry-index).

<DirectoryList />

## Documentation

You can use the `shadcn` CLI to run your own code registry. Running your own registry allows you to distribute your custom components, hooks, pages, config, rules and other files to any project.

<div className="mt-6 grid gap-4 sm:grid-cols-2">
  <LinkedCard href="/docs/registry/getting-started" className="items-start text-sm md:p-6">
    <div className="font-medium">Getting Started</div>
    <div className="text-muted-foreground">
      Set up and build your own registry
    </div>
  </LinkedCard>

<LinkedCard
  href="/docs/registry/authentication"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Authentication</div>
  <div className="text-muted-foreground">
    Secure your registry with authentication
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/namespace"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Namespaces</div>
  <div className="text-muted-foreground">
    Configure registries with namespaces
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/registry-index"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Add a Registry</div>
  <div className="text-muted-foreground">
    Learn how to add a registry to the directory
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/examples"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Examples</div>
  <div className="text-muted-foreground">
    Registry item examples and configurations
  </div>
</LinkedCard>
  <LinkedCard
    href="/docs/registry/registry-json"
    className="items-start text-sm md:p-6"
  >
    <div className="font-medium">Schema</div>
    <div className="text-muted-foreground">
      Schema specification for registry.json
    </div>
  </LinkedCard>
</div>


---

<!-- SOURCE: apps/v4/content/docs/(root)/figma.mdx -->

## apps/v4/content/docs/(root)/figma.mdx

---
title: Figma
description: Every component recreated in Figma. With customizable props, typography and icons.
---

<Callout>
  **Note:** The Figma files are contributed by the community. If you have any
  questions or feedback, please reach out to the Figma file maintainers.
</Callout>

## Free

- [Obra shadcn/ui](https://www.figma.com/community/file/1514746685758799870/obra-shadcn-ui) by [Obra Studio](https://obra.studio/) - Carefully crafted shadcn/ui kit, MIT licensed, maintained by team of designers, with free design to code plugin
- [shadcn/ui components](https://www.figma.com/community/file/1342715840824755935) by [Sitsiilia Bergmann](https://x.com/sitsiilia) - A well-structured component library aligned with the shadcn component system, regularly maintained.
- [shadcn/ui design system](https://www.figma.com/community/file/1203061493325953101) by [Pietro Schirano](https://twitter.com/skirano) - A design companion for shadcn/ui. Each component was painstakingly crafted to perfectly match the code implementation.

## Paid

- [shadcn/ui kit](https://shadcndesign.com) by [Matt Wierzbicki](https://x.com/matsugfx) - A premium, always up-to-date UI kit for Figma - shadcn/ui compatible and optimized for smooth design-to-dev handoff.
- [shadcncraft Design System](https://shadcncraft.com) - Production-ready shadcn/ui kit with Pro React blocks and 1:1 Figma alignment. Design and ship faster with tweakcn theming, AI-assisted workflows, and Figma to React export, built for real product UIs.
- [shadcn/studio UI Kit](https://shadcnstudio.com/figma) - Accelerate design & development with a shadcn/ui compatible Figma kit with updated components, 550+ blocks, 10+ templates, 20+ themes, and an AI tool that converts designs into shadcn/ui code.
- [Shadcnblocks.com](https://www.shadcnblocks.com) - A Premium Shadcn Figma UI Kit with components, 500+ pro blocks, shadcn theme variables, light/dark mode and Figma MCP ready.


---

<!-- SOURCE: apps/v4/content/docs/(root)/index.mdx -->

## apps/v4/content/docs/(root)/index.mdx

---
title: Introduction
description: shadcn/ui is a set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks and AI models. Open Source. Open Code.
---

**This is not a component library. It is how you build your component library.**

You know how most traditional component libraries work: you install a package from NPM, import the components, and use them in your app.

This approach works well until you need to customize a component to fit your design system or require one that isn’t included in the library. **Often, you end up wrapping library components, writing workarounds to override styles, or mixing components from different libraries with incompatible APIs.**

This is what shadcn/ui aims to solve. It is built around the following principles:

- **Open Code:** The top layer of your component code is open for modification.
- **Composition:** Every component uses a common, composable interface, making them predictable.
- **Distribution:** A flat-file schema and command-line tool make it easy to distribute components.
- **Beautiful Defaults:** Carefully chosen default styles, so you get great design out-of-the-box.
- **AI-Ready:** Open code for LLMs to read, understand, and improve.

## Open Code

shadcn/ui hands you the actual component code. You have full control to customize and extend the components to your needs. This means:

- **Full Transparency:** You see exactly how each component is built.
- **Easy Customization:** Modify any part of a component to fit your design and functionality requirements.
- **AI Integration:** Access to the code makes it straightforward for LLMs to read, understand, and even improve your components.

_In a typical library, if you need to change a button’s behavior, you have to override styles or wrap the component. With shadcn/ui, you simply edit the button code directly._

<Accordion type="single" collapsible>
  <AccordionItem value="faq-1" className="border-none">
    <AccordionTrigger>
      How do I pull upstream updates in an Open Code approach?
    </AccordionTrigger>
    <AccordionContent>
      <p>
        shadcn/ui follows a headless component architecture. This means the core
        of your app can receive fixes by updating your dependencies, for
        instance, radix-ui or input-otp.
      </p>
      <p className="mt-4">
        The topmost layer, i.e., the one closest to your design system, is not
        coupled with the implementation of the library. It stays open for
        modification.
      </p>
    </AccordionContent>
  </AccordionItem>
</Accordion>

## Composition

Every component in shadcn/ui shares a common, composable interface. **If a component does not exist, we bring it in, make it composable, and adjust its style to match and work with the rest of the design system.**

_A shared, composable interface means it's predictable for both your team and LLMs. You are not learning different APIs for every new component. Even for third-party ones._

## Distribution

shadcn/ui is also a code distribution system. It defines a schema for components and a CLI to distribute them.

- **Schema:** A flat-file structure that defines the components, their dependencies, and properties.
- **CLI:** A command-line tool to distribute and install components across projects with cross-framework support.

_You can use the schema to distribute your components to other projects or have AI generate completely new components based on existing schema._

## Beautiful Defaults

shadcn/ui comes with a large collection of components that have carefully chosen default styles. They are designed to look good on their own and to work well together as a consistent system:

- **Good Out-of-the-Box:** Your UI has a clean and minimal look without extra work.
- **Unified Design:** Components naturally fit with one another. Each component is built to match the others, keeping your UI consistent.
- **Easily Customizable:** If you want to change something, it's simple to override and extend the defaults.

## AI-Ready

The design of shadcn/ui makes it easy for AI tools to work with your code. Its open code and consistent API allow AI models to read, understand, and even generate new components.

_An AI model can learn how your components work and suggest improvements or even create new components that integrate with your existing design._


---

<!-- SOURCE: apps/v4/content/docs/(root)/javascript.mdx -->

## apps/v4/content/docs/(root)/javascript.mdx

---
title: JavaScript
description: How to use shadcn/ui with JavaScript
---

This project and the components are written in TypeScript. We recommend using TypeScript for your project as well.

However we provide a JavaScript version of the components as well. The JavaScript version is available via the [cli](/docs/cli).

To opt-out of TypeScript, you can use the `tsx` flag in your `components.json` file.

```json {4} title="components.json" showLineNumbers
{
  "style": "new-york",
  "rsc": false,
  "tsx": false,
  "tailwind": {
    "config": "",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
```

To configure import aliases, you can use the following `jsconfig.json`:

```json {4} title="jsconfig.json" showLineNumbers
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```


---

<!-- SOURCE: apps/v4/content/docs/(root)/legacy.mdx -->

## apps/v4/content/docs/(root)/legacy.mdx

---
title: Legacy Docs
description: View the legacy docs for shadcn/ui and Tailwind v3.
---

You're looking at the docs for shadcn/ui + Tailwind v4. If you're looking for the docs for shadcn/ui + Tailwind v3, you can find them [here](https://v3.shadcn.com).

<Button asChild className="mt-6 no-underline" size="sm">
  <Link href="https://v3.shadcn.com" target="_blank">
    View the legacy docs
  </Link>
</Button>


---

<!-- SOURCE: apps/v4/content/docs/(root)/mcp.mdx -->

## apps/v4/content/docs/(root)/mcp.mdx

---
title: MCP Server
description: Use the shadcn MCP server to browse, search, and install components from registries.
---

The shadcn MCP Server allows AI assistants to interact with items from registries. You can browse available components, search for specific ones, and install them directly into your project using natural language.

For example, you can ask an AI assistant to "Build a landing page using components from the acme registry" or "Find me a login form from the shadcn registry".

Registries are configured in your project's `components.json` file.

```json title="components.json" showLineNumbers
{
  "registries": {
    "@acme": "https://acme.com/r/{name}.json"
  }
}
```

---

## Quick Start

Select your MCP client and follow the instructions to configure the shadcn MCP server. If you'd like to do it manually, see the [Configuration](#configuration) section.

<Tabs defaultValue="claude">
  <TabsList>
    <TabsTrigger value="claude">Claude Code</TabsTrigger>
    <TabsTrigger value="cursor">Cursor</TabsTrigger>
    <TabsTrigger value="vscode">VS Code</TabsTrigger>
    <TabsTrigger value="codex">Codex</TabsTrigger>
    <TabsTrigger value="opencode">OpenCode</TabsTrigger>
  </TabsList>
  <TabsContent value="claude" className="mt-4">
    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client claude
       ```

    **Restart Claude Code** and try the following prompts:
       - Show me all available components in the shadcn registry
       - Add the button, dialog and card components to my project
       - Create a contact form using components from the shadcn registry

    **Note:** You can use `/mcp` command in Claude Code to debug the MCP server.

  </TabsContent>

  <TabsContent value="cursor" className="mt-4">
    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client cursor
       ```

    Open **Cursor Settings** and **Enable the MCP server** for shadcn. Then try the following prompts:
       - Show me all available components in the shadcn registry
       - Add the button, dialog and card components to my project
       - Create a contact form using components from the shadcn registry

  </TabsContent>

  <TabsContent value="vscode" className="mt-4">
    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client vscode
       ```

    Open `.vscode/mcp.json` and click **Start** next to the shadcn server. Then try the following prompts with GitHub Copilot:
       - Show me all available components in the shadcn registry
       - Add the button, dialog and card components to my project
       - Create a contact form using components from the shadcn registry

  </TabsContent>

  <TabsContent value="codex" className="mt-4">
    <Callout className="mt-0">
      **Note:** The `shadcn` CLI cannot automatically update `~/.codex/config.toml`.
      You'll need to add the configuration manually for Codex.
    </Callout>

    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client codex
       ```

    **Then, add the following configuration** to `~/.codex/config.toml`:
       ```toml
       [mcp_servers.shadcn]
       command = "npx"
       args = ["shadcn@latest", "mcp"]
       ```

    **Restart Codex** and try the following prompts:
       - Show me all available components in the shadcn registry
       - Add the button, dialog and card components to my project
       - Create a contact form using components from the shadcn registry

  </TabsContent>

  <TabsContent value="opencode" className="mt-4">
    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client opencode
       ```

    **Restart OpenCode** and try the following prompts:
       - Show me all available components in the shadcn registry
       - Add the button, dialog and card components to my project
       - Create a contact form using components from the shadcn registry

  </TabsContent>
</Tabs>

---

## What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io) is an open protocol that enables AI assistants to securely connect to external data sources and tools. With the shadcn MCP server, your AI assistant gains direct access to:

- **Browse Components** - List all available components, blocks, and templates from any configured registry
- **Search Across Registries** - Find specific components by name or functionality across multiple sources
- **Install with Natural Language** - Add components using simple conversational prompts like "add a login form"
- **Support for Multiple Registries** - Access public registries, private company libraries, and third-party sources

---

## How It Works

The MCP server acts as a bridge between your AI assistant, component registries and the shadcn CLI.

1. **Registry Connection** - MCP connects to configured registries (shadcn/ui, private registries, third-party sources)
2. **Natural Language** - You describe what you need in plain English
3. **AI Processing** - The assistant translates your request into registry commands
4. **Component Delivery** - Resources are fetched and installed in your project

---

## Supported Registries

The shadcn MCP server works out of the box with any shadcn-compatible registry.

- **shadcn/ui Registry** - The default registry with all shadcn/ui components
- **Third-Party Registries** - Any registry following the shadcn registry specification
- **Private Registries** - Your company's internal component libraries
- **Namespaced Registries** - Multiple registries configured with `@namespace` syntax

---

## Configuration

You can use any MCP client to interact with the shadcn MCP server. Here are the instructions for the most popular ones.

### Claude Code

To use the shadcn MCP server with Claude Code, add the following configuration to your project's `.mcp.json` file:

```json title=".mcp.json" showLineNumbers
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

After adding the configuration, restart Claude Code and run `/mcp` to see the shadcn MCP server in the list. If you see `Connected`, you're good to go.

See the [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp) for more details.

### Cursor

To configure MCP in Cursor, add the shadcn server to your project's `.cursor/mcp.json` configuration file:

```json title=".cursor/mcp.json" showLineNumbers
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

After adding the configuration, enable the shadcn MCP server in Cursor Settings.

Once enabled, you should see a green dot next to the shadcn server in the MCP server list and a list of available tools.

See the [Cursor MCP documentation](https://docs.cursor.com/en/context/mcp#using-mcp-json) for more details.

### VS Code

To configure MCP in VS Code with GitHub Copilot, add the shadcn server to your project's `.vscode/mcp.json` configuration file:

```json title=".vscode/mcp.json" showLineNumbers
{
  "servers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

After adding the configuration, open `.vscode/mcp.json` and click **Start** next to the shadcn server.

See the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more details.

### Codex

<Callout>
  **Note:** The `shadcn` CLI cannot automatically update `~/.codex/config.toml`.
  You'll need to add the configuration manually.
</Callout>

To configure MCP in Codex, add the shadcn server to `~/.codex/config.toml`:

```toml title="~/.codex/config.toml" showLineNumbers
[mcp_servers.shadcn]
command = "npx"
args = ["shadcn@latest", "mcp"]
```

After adding the configuration, restart Codex to load the MCP server.

---

## Configuring Registries

The MCP server supports multiple registries through your project's `components.json` configuration. This allows you to access components from various sources including private registries and third-party providers.

Configure additional registries in your `components.json`:

```json title="components.json" showLineNumbers
{
  "registries": {
    "@acme": "https://registry.acme.com/{name}.json",
    "@internal": {
      "url": "https://internal.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

<Callout>
  **Note:** No configuration is needed to access the standard shadcn/ui
  registry.
</Callout>

---

## Authentication

For private registries requiring authentication, set environment variables in your `.env.local`:

```bash title=".env.local"
REGISTRY_TOKEN=your_token_here
API_KEY=your_api_key_here
```

For more details on registry authentication, see the [Authentication documentation](/docs/registry/authentication).

---

## Example Prompts

Once the MCP server is configured, you can use natural language to interact with registries. Try one of the following prompts:

### Browse & Search

- Show me all available components in the shadcn registry
- Find me a login form from the shadcn registry

### Install Items

- Add the button component to my project
- Create a login form using shadcn components
- Install the Cursor rules from the acme registry

### Work with Namespaces

- Show me components from acme registry
- Install @internal/auth-form
- Build me a landing page using hero, features and testimonials sections from the acme registry

---

## Troubleshooting

### MCP Not Responding

If the MCP server isn't responding to prompts:

1. **Check Configuration** - Verify the MCP server is properly configured and enabled in your MCP client
2. **Restart MCP Client** - Restart your MCP client after configuration changes
3. **Verify Installation** - Ensure `shadcn` is installed in your project
4. **Check Network** - Confirm you can access the configured registries

### Registry Access Issues

If components aren't loading from registries:

1. **Check components.json** - Verify registry URLs are correct
2. **Test Authentication** - Ensure environment variables are set for private registries
3. **Verify Registry** - Confirm the registry is online and accessible
4. **Check Namespace** - Ensure namespace syntax is correct (`@namespace/component`)

### Installation Failures

If components fail to install:

1. **Check Project Setup** - Ensure you have a valid `components.json` file
2. **Verify Paths** - Confirm the target directories exist
3. **Check Permissions** - Ensure write permissions for component directories
4. **Review Dependencies** - Check that required dependencies are installed

### No Tools or Prompts

If you see the `No tools or prompts` message, try the following:

1. **Clear the npx cache** - Run `npx clear-npx-cache`
2. **Re-enable the MCP server** - Try to re-enable the MCP server in your MCP client
3. **Check Logs** - In Cursor, you can see the logs under View -> Output and select `MCP: project-*` in the dropdown.

---

## Learn More

- [Registry Documentation](/docs/registry) - Complete guide to shadcn registries
- [Namespaces](/docs/registry/namespace) - Configure multiple registry sources
- [Authentication](/docs/registry/authentication) - Secure your private registries
- [MCP Specification](https://modelcontextprotocol.io) - Learn about Model Context Protocol


---

<!-- SOURCE: apps/v4/content/docs/(root)/monorepo.mdx -->

## apps/v4/content/docs/(root)/monorepo.mdx

---
title: Monorepo
description: Using shadcn/ui components and CLI in a monorepo.
---

Until now, using shadcn/ui in a monorepo was a bit of a pain. You could add
components using the CLI, but you had to manage where the components
were installed and manually fix import paths.

With the new monorepo support in the CLI, we've made it a lot easier to use
shadcn/ui in a monorepo.

The CLI now understands the monorepo structure and will install the components,
dependencies and registry dependencies to the correct paths and handle imports
for you.

## Getting started

<Steps>

### Create a new monorepo project

To create a new monorepo project, run the `init` command with the `--monorepo` flag.

```bash
npx shadcn@latest init --monorepo
```

Then select the template you want to use.

```bash
? Select a template ›
❯   Next.js
    Vite
    TanStack Start
    React Router
    Astro
```

This will create a new monorepo project with two workspaces: `web` and `ui`,
and [Turborepo](https://turbo.build/repo/docs) as the build system.

Everything is set up for you, so you can start adding components to your project.

### Add components to your project

To add components to your project, run the `add` command **in the path of your app**.

```bash
cd apps/web
```

```bash
npx shadcn@latest add [COMPONENT]
```

The CLI will figure out what type of component you are adding and install the
correct files to the correct path.

For example, if you run `npx shadcn@latest add button`, the CLI will install the button component under `packages/ui` and update the import path for components in `apps/web`.

If you run `npx shadcn@latest add login-01`, the CLI will install the `button`, `label`, `input` and `card` components under `packages/ui` and the `login-form` component under `apps/web/components`.

### Importing components

You can import components from the `@workspace/ui` package as follows:

```tsx
import { Button } from "@workspace/ui/components/button"
```

You can also import hooks and utilities from the `@workspace/ui` package.

```tsx
import { useTheme } from "@workspace/ui/hooks/use-theme"
import { cn } from "@workspace/ui/lib/utils"
```

</Steps>

## File Structure

When you create a new monorepo project, the CLI will create the following file structure:

```txt
apps
└── web         # Your app goes here.
    ├── app
    │   └── page.tsx
    ├── components
    │   └── login-form.tsx
    ├── components.json
    └── package.json
packages
└── ui          # Your components and dependencies are installed here.
    ├── src
    │   ├── components
    │   │   └── button.tsx
    │   ├── hooks
    │   ├── lib
    │   │   └── utils.ts
    │   └── styles
    │       └── globals.css
    ├── components.json
    └── package.json
package.json
turbo.json
```

## Requirements

1. Every workspace must have a `components.json` file. A `package.json` file tells npm how to install the dependencies. A `components.json` file tells the CLI how and where to install components.

2. The `components.json` file must properly define aliases for the workspace. This tells the CLI how to import components, hooks, utilities, etc.

```json showLineNumbers title="apps/web/components.json"
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "radix-nova",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "../../packages/ui/src/styles/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "hooks": "@/hooks",
    "lib": "@/lib",
    "utils": "@workspace/ui/lib/utils",
    "ui": "@workspace/ui/components"
  }
}
```

```json showLineNumbers title="packages/ui/components.json"
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "radix-nova",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/styles/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@workspace/ui/components",
    "utils": "@workspace/ui/lib/utils",
    "hooks": "@workspace/ui/hooks",
    "lib": "@workspace/ui/lib",
    "ui": "@workspace/ui/components"
  }
}
```

3. Ensure you have the same `style`, `iconLibrary` and `baseColor` in both `components.json` files.

4. **For Tailwind CSS v4, leave the `tailwind` config empty in the `components.json` file.**

By following these requirements, the CLI will be able to install ui components, blocks, libs and hooks to the correct paths and handle imports for you.


---

<!-- SOURCE: apps/v4/content/docs/(root)/new.mdx -->

## apps/v4/content/docs/(root)/new.mdx

---
title: Your project is ready!
description: You've created a new project with shadcn/ui.
---

Here are a few things you can do to get started building with shadcn/ui.

## Add Components

Use the CLI to add components to your project.

```bash
npx shadcn@latest add button
```

Then import and use it in your code.

```tsx title="app/page.tsx"
import { Button } from "@/components/ui/button"

export default function Home() {
  return <Button>Click me</Button>
}
```

Unlike traditional component libraries, shadcn/ui adds the component source code directly to your project under `components/ui/`. You own the code and can customize it however you want.

You can add multiple components at once or add all available components.

```bash
npx shadcn@latest add button card input label
```

```bash
npx shadcn@latest add --all
```

Browse all components on the [Components](/docs/components) page.

## Customize Your Theme

You can edit your theme directly in your CSS file. Learn more about [Theming](/docs/theming) and how to use CSS variables or utility classes.

If you want to try a new preset, you can create a custom theme visually on [ui.shadcn.com](https://ui.shadcn.com) and apply it to your project using a preset code.

```bash
npx shadcn@latest init --preset [CODE]
```

## Add a block

You can add a block to your project using the CLI.

```bash
npx shadcn@latest add login-03
```

This will add the `login-03` block to your project. Import and use it in your code.

```tsx title="app/page.tsx"
import { Login03 } from "@/components/login-03"

export default function Home() {
  return <Login03 />
}
```

## Install from Registries

shadcn/ui has a growing ecosystem of community registries. You can install components from any registry URL using the CLI.

```bash
npx shadcn@latest add @[registry]/[name]
```

Browse the [Registry Directory](/docs/directory) for a list of available registries.

## Use AI to Build

shadcn/ui is designed to work with AI. Your AI assistant can read the component source code in your project, understand the APIs, and compose them together to build pages and features.

Here are some example prompts to try:

- _"Create a signup page with a form for entering name, email and password."_
- _"Create a settings page with a form for updating profile information."_
- _"Build a dashboard with a header, stats cards, and a data table."_

## Install the shadcn Skills

Install the shadcn skill in your AI assistant. This will give your AI assistant access to the full component registry, documentation, and search.

```bash
npx skills add shadcn/ui
```

Learn more about [skills](/docs/skills).

## Connect the MCP Server

The shadcn MCP server gives your AI assistant access to the full component registry, documentation, and search. Connect it in your editor for the best experience.

```bash
npx shadcn@latest mcp init
```

Learn more on the [MCP Server](/docs/mcp) page.


---

<!-- SOURCE: apps/v4/content/docs/(root)/react-19.mdx -->

## apps/v4/content/docs/(root)/react-19.mdx

---
title: Next.js 15 + React 19
description: Using shadcn/ui with Next.js 15 and React 19.
---

<Callout className="">
  **Update:** We have added full support for React 19 and Tailwind v4 in the
  `latest` release. **This guide might be outdated. Proceed with caution.**
</Callout>

## TL;DR

If you're using `npm`, you can install shadcn/ui dependencies with a flag. The `shadcn` CLI will prompt you to select a flag when you run it. No flags required for pnpm, bun, or yarn.

See [Upgrade Status](#upgrade-status) for the status of React 19 support for each package.

## What's happening?

React 19 is now [rc](https://www.npmjs.com/package/react?activeTab=versions) and is [tested and supported in the latest Next.js 15 release](https://nextjs.org/blog/next-15#react-19).

To support React 19, package maintainers will need to test and update their packages to include React 19 as a peer dependency. This is [already](https://github.com/radix-ui/primitives/pull/2952) [in](https://github.com/pacocoursey/cmdk/pull/318) [progress](https://github.com/emilkowalski/vaul/pull/498).

```diff /^19.0/
"peerDependencies": {
-  "react": "^16.8 || ^17.0 || ^18.0",
+  "react": "^16.8 || ^17.0 || ^18.0 || ^19.0",
-  "react-dom": "^16.8 || ^17.0 || ^18.0"
+  "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0"
},
```

<Callout>
  You can check if a package lists React 19 as a peer dependency by running
  `npm info <package> peerDependencies`.
</Callout>

In the meantime, if you are installing a package that **does not** list React 19 as a peer dependency, you will see an error message like this:

```bash
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: my-app@0.1.0
npm error Found: react@19.0.0-rc-69d4b800-20241021
npm error node_modules/react
npm error   react@"19.0.0-rc-69d4b800-20241021" from the root project
```

<Callout>
  **Note:** This is npm only. PNPM and Bun will only show a silent warning.
</Callout>

## How to fix this

### Solution 1: `--force` or `--legacy-peer-deps`

You can force install a package with the `--force` or the `--legacy-peer-deps` flag.

```bash
npm i <package> --force

npm i <package> --legacy-peer-deps
```

This will install the package and ignore the peer dependency warnings.

<Accordion type="multiple">
  <AccordionItem value="flags">
    <AccordionTrigger className="font-medium">
      What do the `--force` and `--legacy-peer-deps` flag do?
    </AccordionTrigger>
    <AccordionContent className="[&_ul]:mt-0">

      - `--force`: Ignores and overrides any dependency conflicts, forcing the
        installation of packages.
      - `--legacy-peer-deps`: Skips strict peer dependency checks, allowing
        installation of packages with unmet peer dependencies to avoid errors.

    </AccordionContent>

  </AccordionItem>
</Accordion>

### Solution 2: Use React 18

You can downgrade `react` and `react-dom` to version 18, which is compatible with the package you are installing and upgrade when the dependency is updated.

```bash
npm i react@18 react-dom@18
```

Whichever solution you choose, make sure you test your app thoroughly to ensure
there are no regressions.

## Using shadcn/ui on Next.js 15

### Using pnpm, bun, or yarn

Follow the instructions in the [installation guide](/docs/installation/next) to install shadcn/ui. No flags are needed.

### Using npm

When you run `npx shadcn@latest init -d`, you will be prompted to select an option to resolve the peer dependency issues.

```bash
It looks like you are using React 19.
Some packages may fail to install due to peer dependency issues (see https://ui.shadcn.com/react-19).

? How would you like to proceed? › - Use arrow-keys. Return to submit.
❯   Use --force
    Use --legacy-peer-deps
```

You can then run the command with the flag you choose.

## Adding components

The process for adding components is the same as above. Select a flag to resolve the peer dependency issues.

**Remember to always test your app after installing new dependencies.**

## Upgrade Status

To make it easy for you to track the progress of the upgrade, here is a table with the React 19 support status for the shadcn/ui dependencies.

- ✅ - Works with React 19 using npm, pnpm, and bun.
- 🚧 - Works with React 19 using pnpm and bun. Requires flag for npm. PR is in progress.

| Package                                                                            | Status | Note                                                        |
| ---------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------- |
| [radix-ui](https://www.npmjs.com/package/@radix-ui/react-icons)                    | ✅     |                                                             |
| [lucide-react](https://www.npmjs.com/package/lucide-react)                         | ✅     |                                                             |
| [class-variance-authority](https://www.npmjs.com/package/class-variance-authority) | ✅     | Does not list React 19 as a peer dependency.                |
| [tailwindcss-animate](https://www.npmjs.com/package/tailwindcss-animate)           | ✅     | Does not list React 19 as a peer dependency.                |
| [embla-carousel-react](https://www.npmjs.com/package/embla-carousel-react)         | ✅     |                                                             |
| [recharts](https://www.npmjs.com/package/recharts)                                 | ✅     | See note [below](#recharts)                                 |
| [react-hook-form](https://www.npmjs.com/package/react-hook-form)                   | ✅     |                                                             |
| [react-resizable-panels](https://www.npmjs.com/package/react-resizable-panels)     | ✅     |                                                             |
| [sonner](https://www.npmjs.com/package/sonner)                                     | ✅     |                                                             |
| [react-day-picker](https://www.npmjs.com/package/react-day-picker)                 | ✅     | Works with flag for npm. Work to upgrade to v9 in progress. |
| [input-otp](https://www.npmjs.com/package/input-otp)                               | ✅     |                                                             |
| [vaul](https://www.npmjs.com/package/vaul)                                         | ✅     |                                                             |
| [@radix-ui/react-icons](https://www.npmjs.com/package/@radix-ui/react-icons)       | ✅     | See [PR #194](https://github.com/radix-ui/icons/pull/194)   |
| [cmdk](https://www.npmjs.com/package/cmdk)                                         | ✅     |                                                             |

If you have any questions, please [open an issue](https://github.com/shadcn/ui/issues) on GitHub.

## Recharts

To use recharts with React 19, you will need to override the `react-is` dependency.

<Steps>

<Step>Add the following to your `package.json`</Step>

```json title="package.json"
"overrides": {
  "react-is": "^19.0.0-rc-69d4b800-20241021"
}
```

Note: the `react-is` version needs to match the version of React 19 you are using. The above is an example.

<Step>Run `npm install --legacy-peer-deps`</Step>

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/(root)/skills.mdx -->

## apps/v4/content/docs/(root)/skills.mdx

---
title: Skills
description: Give your AI assistant deep knowledge of shadcn/ui components, patterns, and best practices.
---

Skills give AI assistants like Claude Code project-aware context about shadcn/ui. When installed, your AI assistant knows how to find, install, compose, and customize components using the correct APIs and patterns for your project.

For example, you can ask your AI assistant to:

- _"Add a login form with email and password fields."_
- _"Create a settings page with a form for updating profile information."_
- _"Build a dashboard with a sidebar, stats cards, and a data table."_
- _"Switch to --preset [CODE]"_
- _"Can you add a hero from @tailark?"_

The skill reads your project's `components.json` and provides the assistant with your framework, aliases, installed components, icon library, and base library so it can generate correct code on the first try.

---

## Install

```bash
npx skills add shadcn/ui
```

This installs the shadcn skill into your project. Once installed, your AI assistant automatically loads it when working with shadcn/ui components.

Learn more about skills at [skills.sh](https://skills.sh).

---

## What's Included

The skill provides your AI assistant with the following knowledge:

### Project Context

On every interaction, the skill runs `shadcn info --json` to get your project's configuration: framework, Tailwind version, aliases, base library (`radix` or `base`), icon library, installed components, and resolved file paths.

### CLI Commands

Full reference for all CLI commands: `init`, `add`, `search`, `view`, `docs`, `diff`, `info`, and `build`. Includes flags, dry-run mode, smart merge workflows, presets, and templates.

### Theming and Customization

How CSS variables, OKLCH colors, dark mode, custom colors, border radius, and component variants work. Includes guidance for both Tailwind v3 and v4.

### Registry Authoring

How to build and publish custom component registries: `registry.json` format, item types, file objects, dependencies, CSS variables, building, hosting, and user configuration.

### MCP Server

Setup and tools for the shadcn MCP server, which lets AI assistants search, browse, and install components from registries.

---

## How It Works

1. **Project detection** — The skill activates when it finds a `components.json` file in your project.
2. **Context injection** — It runs `shadcn info --json` to read your project configuration and injects the result into the assistant's context.
3. **Pattern enforcement** — The assistant follows shadcn/ui composition rules: using `FieldGroup` for forms, `ToggleGroup` for option sets, semantic colors, and correct base-specific APIs.
4. **Component discovery** — The assistant uses `shadcn docs`, `shadcn search`, or MCP tools to find components and their documentation before generating code.

## Learn More

- [CLI](/docs/cli) — Full CLI command reference
- [MCP Server](/docs/mcp) — Connect the MCP server for registry access
- [Theming](/docs/theming) — CSS variables and customization
- [Registry](/docs/registry) — Building and publishing custom registries
- [skills.sh](https://skills.sh) — Learn more about AI skills


---

<!-- SOURCE: apps/v4/content/docs/(root)/tailwind-v4.mdx -->

## apps/v4/content/docs/(root)/tailwind-v4.mdx

---
title: Tailwind v4
description: How to use shadcn/ui with Tailwind v4 and React 19.
---

It’s here! Tailwind v4 and React 19. Ready for you to try out. You can start using it today.

## What's New

- The CLI can now initialize projects with Tailwind v4.
- Full support for the new `@theme` directive and `@theme inline` option.
- All components are updated for Tailwind v4 and React 19.
- We’ve removed the forwardRefs and adjusted the types.
- Every primitive now has a `data-slot` attribute for styling.
- We've fixed and cleaned up the style of the components.
- We're deprecating the `toast` component in favor of `sonner`.
- Buttons now use the default cursor.
- We're deprecating the `default` style. New projects will use `new-york`.
- HSL colors are now converted to OKLCH.

**Note: this is non-breaking. Your existing apps with Tailwind v3 and React 18 will still work. When you add new components, they'll still be in v3 and React 18 until you upgrade. Only new projects start with Tailwind v4 and React 19.**

## Try It Out

You can start using Tailwind v4 + React 19 today. See the framework specific guides below for how to get started.

<div className="mt-8 grid gap-4 sm:grid-cols-2 sm:gap-6">
  <LinkedCard href="/docs/installation/next">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Next.js</title>
      <path d="M11.5725 0c-.1763 0-.3098.0013-.3584.0067-.0516.0053-.2159.021-.3636.0328-3.4088.3073-6.6017 2.1463-8.624 4.9728C1.1004 6.584.3802 8.3666.1082 10.255c-.0962.659-.108.8537-.108 1.7474s.012 1.0884.108 1.7476c.652 4.506 3.8591 8.2919 8.2087 9.6945.7789.2511 1.6.4223 2.5337.5255.3636.04 1.9354.04 2.299 0 1.6117-.1783 2.9772-.577 4.3237-1.2643.2065-.1056.2464-.1337.2183-.1573-.0188-.0139-.8987-1.1938-1.9543-2.62l-1.919-2.592-2.4047-3.5583c-1.3231-1.9564-2.4117-3.556-2.4211-3.556-.0094-.0026-.0187 1.5787-.0235 3.509-.0067 3.3802-.0093 3.5162-.0516 3.596-.061.115-.108.1618-.2064.2134-.075.0374-.1408.0445-.495.0445h-.406l-.1078-.068a.4383.4383 0 01-.1572-.1712l-.0493-.1056.0053-4.703.0067-4.7054.0726-.0915c.0376-.0493.1174-.1125.1736-.143.0962-.047.1338-.0517.5396-.0517.4787 0 .5584.0187.6827.1547.0353.0377 1.3373 1.9987 2.895 4.3608a10760.433 10760.433 0 004.7344 7.1706l1.9002 2.8782.096-.0633c.8518-.5536 1.7525-1.3418 2.4657-2.1627 1.5179-1.7429 2.4963-3.868 2.8247-6.134.0961-.6591.1078-.854.1078-1.7475 0-.8937-.012-1.0884-.1078-1.7476-.6522-4.506-3.8592-8.2919-8.2087-9.6945-.7672-.2487-1.5836-.42-2.4985-.5232-.169-.0176-1.0835-.0366-1.6123-.037zm4.0685 7.217c.3473 0 .4082.0053.4857.047.1127.0562.204.1642.237.2767.0186.061.0234 1.3653.0186 4.3044l-.0067 4.2175-.7436-1.14-.7461-1.14v-3.066c0-1.982.0093-3.0963.0234-3.1502.0375-.1313.1196-.2346.2323-.2955.0961-.0494.1313-.054.4997-.054z" />
    </svg>
    <p className="mt-2 font-medium">Next.js</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/vite">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Vite</title>
      <path d="m8.286 10.578.512-8.657a.306.306 0 0 1 .247-.282L17.377.006a.306.306 0 0 1 .353.385l-1.558 5.403a.306.306 0 0 0 .352.385l2.388-.46a.306.306 0 0 1 .332.438l-6.79 13.55-.123.19a.294.294 0 0 1-.252.14c-.177 0-.35-.152-.305-.369l1.095-5.301a.306.306 0 0 0-.388-.355l-1.433.435a.306.306 0 0 1-.389-.354l.69-3.375a.306.306 0 0 0-.37-.36l-2.32.536a.306.306 0 0 1-.374-.316zm14.976-7.926L17.284 3.74l-.544 1.887 2.077-.4a.8.8 0 0 1 .84.369.8.8 0 0 1 .034.783L12.9 19.93l-.013.025-.015.023-.122.19a.801.801 0 0 1-.672.37.826.826 0 0 1-.634-.302.8.8 0 0 1-.16-.67l1.029-4.981-1.12.34a.81.81 0 0 1-.86-.262.802.802 0 0 1-.165-.67l.63-3.08-2.027.468a.808.808 0 0 1-.768-.233.81.81 0 0 1-.217-.6l.389-6.57-7.44-1.33a.612.612 0 0 0-.64.906L11.58 23.691a.612.612 0 0 0 1.066-.004l11.26-20.135a.612.612 0 0 0-.644-.9z" />
    </svg>
    <p className="mt-2 font-medium">Vite</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/laravel">
    <svg
      role="img"
      viewBox="0 0 62 65"
      fill="currentColor"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
    >
      <path d="M61.8548 14.6253C61.8778 14.7102 61.8895 14.7978 61.8897 14.8858V28.5615C61.8898 28.737 61.8434 28.9095 61.7554 29.0614C61.6675 29.2132 61.5409 29.3392 61.3887 29.4265L49.9104 36.0351V49.1337C49.9104 49.4902 49.7209 49.8192 49.4118 49.9987L25.4519 63.7916C25.3971 63.8227 25.3372 63.8427 25.2774 63.8639C25.255 63.8714 25.2338 63.8851 25.2101 63.8913C25.0426 63.9354 24.8666 63.9354 24.6991 63.8913C24.6716 63.8838 24.6467 63.8689 24.6205 63.8589C24.5657 63.8389 24.5084 63.8215 24.456 63.7916L0.501061 49.9987C0.348882 49.9113 0.222437 49.7853 0.134469 49.6334C0.0465019 49.4816 0.000120578 49.3092 0 49.1337L0 8.10652C0 8.01678 0.0124642 7.92953 0.0348998 7.84477C0.0423783 7.8161 0.0598282 7.78993 0.0697995 7.76126C0.0884958 7.70891 0.105946 7.65531 0.133367 7.6067C0.152063 7.5743 0.179485 7.54812 0.20192 7.51821C0.230588 7.47832 0.256763 7.43719 0.290416 7.40229C0.319084 7.37362 0.356476 7.35243 0.388883 7.32751C0.425029 7.29759 0.457436 7.26518 0.498568 7.2415L12.4779 0.345059C12.6296 0.257786 12.8015 0.211853 12.9765 0.211853C13.1515 0.211853 13.3234 0.257786 13.475 0.345059L25.4531 7.2415H25.4556C25.4955 7.26643 25.5292 7.29759 25.5653 7.32626C25.5977 7.35119 25.6339 7.37362 25.6625 7.40104C25.6974 7.43719 25.7224 7.47832 25.7523 7.51821C25.7735 7.54812 25.8021 7.5743 25.8196 7.6067C25.8483 7.65656 25.8645 7.70891 25.8844 7.76126C25.8944 7.78993 25.9118 7.8161 25.9193 7.84602C25.9423 7.93096 25.954 8.01853 25.9542 8.10652V33.7317L35.9355 27.9844V14.8846C35.9355 14.7973 35.948 14.7088 35.9704 14.6253C35.9792 14.5954 35.9954 14.5692 36.0053 14.5405C36.0253 14.4882 36.0427 14.4346 36.0702 14.386C36.0888 14.3536 36.1163 14.3274 36.1375 14.2975C36.1674 14.2576 36.1923 14.2165 36.2272 14.1816C36.2559 14.1529 36.292 14.1317 36.3244 14.1068C36.3618 14.0769 36.3942 14.0445 36.4341 14.0208L48.4147 7.12434C48.5663 7.03694 48.7383 6.99094 48.9133 6.99094C49.0883 6.99094 49.2602 7.03694 49.4118 7.12434L61.3899 14.0208C61.4323 14.0457 61.4647 14.0769 61.5021 14.1055C61.5333 14.1305 61.5694 14.1529 61.5981 14.1803C61.633 14.2165 61.6579 14.2576 61.6878 14.2975C61.7103 14.3274 61.7377 14.3536 61.7551 14.386C61.7838 14.4346 61.8 14.4882 61.8199 14.5405C61.8312 14.5692 61.8474 14.5954 61.8548 14.6253ZM59.893 27.9844V16.6121L55.7013 19.0252L49.9104 22.3593V33.7317L59.8942 27.9844H59.893ZM47.9149 48.5566V37.1768L42.2187 40.4299L25.953 49.7133V61.2003L47.9149 48.5566ZM1.99677 9.83281V48.5566L23.9562 61.199V49.7145L12.4841 43.2219L12.4804 43.2194L12.4754 43.2169C12.4368 43.1945 12.4044 43.1621 12.3682 43.1347C12.3371 43.1097 12.3009 43.0898 12.2735 43.0624L12.271 43.0586C12.2386 43.0275 12.2162 42.9888 12.1887 42.9539C12.1638 42.9203 12.1339 42.8916 12.114 42.8567L12.1127 42.853C12.0903 42.8156 12.0766 42.7707 12.0604 42.7283C12.0442 42.6909 12.023 42.656 12.013 42.6161C12.0005 42.5688 11.998 42.5177 11.9931 42.4691C11.9881 42.4317 11.9781 42.3943 11.9781 42.3569V15.5801L6.18848 12.2446L1.99677 9.83281ZM12.9777 2.36177L2.99764 8.10652L12.9752 13.8513L22.9541 8.10527L12.9752 2.36177H12.9777ZM18.1678 38.2138L23.9574 34.8809V9.83281L19.7657 12.2459L13.9749 15.5801V40.6281L18.1678 38.2138ZM48.9133 9.14105L38.9344 14.8858L48.9133 20.6305L58.8909 14.8846L48.9133 9.14105ZM47.9149 22.3593L42.124 19.0252L37.9323 16.6121V27.9844L43.7219 31.3174L47.9149 33.7317V22.3593ZM24.9533 47.987L39.59 39.631L46.9065 35.4555L36.9352 29.7145L25.4544 36.3242L14.9907 42.3482L24.9533 47.987Z" />
    </svg>
    <p className="mt-2 font-medium">Laravel</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/react-router">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      className="h-10 w-10"
      fill="currentColor"
    >
      <path d="M12.118 5.466a2.306 2.306 0 0 0-.623.08c-.278.067-.702.332-.953.583-.41.423-.49.609-.662 1.469-.08.423.41 1.43.847 1.734.45.317 1.085.502 2.065.608 1.429.16 1.84.636 1.84 2.197 0 1.377-.385 1.747-1.96 1.906-1.707.172-2.58.834-2.765 2.117-.106.781.41 1.76 1.125 2.091 1.627.768 3.15-.198 3.467-2.196.211-1.284.622-1.642 1.998-1.747 1.588-.133 2.409-.675 2.713-1.787.278-1.02-.304-2.157-1.297-2.554-.264-.106-.873-.238-1.35-.291-1.495-.16-1.879-.424-2.038-1.39-.225-1.337-.317-1.562-.794-2.09a2.174 2.174 0 0 0-1.613-.73zm-4.785 4.36a2.145 2.145 0 0 0-.497.048c-1.469.318-2.17 2.051-1.35 3.295 1.178 1.774 3.944.953 3.97-1.177.012-1.193-.98-2.143-2.123-2.166zM2.089 14.19a2.22 2.22 0 0 0-.427.052c-2.158.476-2.237 3.626-.106 4.182.53.145.582.145 1.111.013 1.191-.318 1.866-1.456 1.549-2.607-.278-1.02-1.144-1.664-2.127-1.64zm19.824.008c-.233.002-.477.058-.784.162-1.39.477-1.866 2.092-.98 3.336.557.794 1.96 1.058 2.82.516 1.416-.874 1.363-3.057-.093-3.746-.38-.186-.663-.271-.963-.268z" />
    </svg>
    <p className="mt-2 font-medium">React Router</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/astro">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Astro</title>
      <path
        d="M16.074 16.86C15.354 17.476 13.917 17.895 12.262 17.895C10.23 17.895 8.527 17.263 8.075 16.412C7.914 16.9 7.877 17.458 7.877 17.814C7.877 17.814 7.771 19.564 8.988 20.782C8.988 20.15 9.501 19.637 10.133 19.637C11.216 19.637 11.215 20.582 11.214 21.349V21.418C11.214 22.582 11.925 23.579 12.937 24C12.7812 23.6794 12.7005 23.3275 12.701 22.971C12.701 21.861 13.353 21.448 14.111 20.968C14.713 20.585 15.383 20.161 15.844 19.308C16.0926 18.8493 16.2225 18.3357 16.222 17.814C16.2221 17.4903 16.1722 17.1685 16.074 16.86ZM15.551 0.6C15.747 0.844 15.847 1.172 16.047 1.829L20.415 16.176C18.7743 15.3246 17.0134 14.7284 15.193 14.408L12.35 4.8C12.3273 4.72337 12.2803 4.65616 12.2162 4.60844C12.152 4.56072 12.0742 4.53505 11.9943 4.53528C11.9143 4.5355 11.8366 4.56161 11.7727 4.60969C11.7089 4.65777 11.6623 4.72524 11.64 4.802L8.83 14.405C7.00149 14.724 5.23264 15.3213 3.585 16.176L7.974 1.827C8.174 1.171 8.274 0.843 8.471 0.6C8.64406 0.385433 8.86922 0.218799 9.125 0.116C9.415 0 9.757 0 10.443 0H13.578C14.264 0 14.608 0 14.898 0.117C15.1529 0.219851 15.3783 0.386105 15.551 0.6Z"
        fill="currentColor"
      />
    </svg>
    <p className="mt-2 font-medium">Astro</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/tanstack">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      className="h-10 w-10"
      fill="currentColor"
    >
      <path d="M6.93 13.688a.343.343 0 0 1 .468.132l.063.106c.48.851.98 1.66 1.5 2.426a35.65 35.65 0 0 0 2.074 2.742.345.345 0 0 1-.039.484l-.074.066c-2.543 2.223-4.191 2.665-4.953 1.333-.746-1.305-.477-3.672.808-7.11a.344.344 0 0 1 .153-.18ZM17.75 16.3a.34.34 0 0 1 .395.27l.02.1c.628 3.286.187 4.93-1.325 4.93-1.48 0-3.36-1.402-5.649-4.203a.327.327 0 0 1-.074-.222c0-.188.156-.34.344-.34h.121a32.984 32.984 0 0 0 2.809-.098c1.07-.086 2.191-.23 3.359-.437zm.871-6.977a.353.353 0 0 1 .445-.21l.102.034c3.262 1.11 4.504 2.332 3.719 3.664-.766 1.305-2.993 2.254-6.684 2.848a.362.362 0 0 1-.238-.047.343.343 0 0 1-.125-.476l.062-.106a34.07 34.07 0 0 0 1.367-2.523c.477-.989.93-2.051 1.352-3.184zM7.797 8.34a.362.362 0 0 1 .238.047.343.343 0 0 1 .125.476l-.062.106a34.088 34.088 0 0 0-1.367 2.523c-.477.988-.93 2.051-1.352 3.184a.353.353 0 0 1-.445.21l-.102-.034C1.57 13.742.328 12.52 1.113 11.188 1.88 9.883 4.106 8.934 7.797 8.34Zm5.281-3.984c2.543-2.223 4.192-2.664 4.953-1.332.746 1.304.477 3.671-.808 7.109a.344.344 0 0 1-.153.18.343.343 0 0 1-.468-.133l-.063-.106a34.64 34.64 0 0 0-1.5-2.426 35.65 35.65 0 0 0-2.074-2.742.345.345 0 0 1 .039-.484ZM7.285 2.274c1.48 0 3.364 1.402 5.649 4.203a.349.349 0 0 1 .078.218.348.348 0 0 1-.348.344l-.117-.004a34.584 34.584 0 0 0-2.809.102 35.54 35.54 0 0 0-3.363.437.343.343 0 0 1-.394-.273l-.02-.098c-.629-3.285-.188-4.93 1.324-4.93Zm2.871 5.812h3.688a.638.638 0 0 1 .55.316l1.848 3.22a.644.644 0 0 1 0 .628l-1.847 3.223a.638.638 0 0 1-.551.316h-3.688a.627.627 0 0 1-.547-.316L7.758 12.25a.644.644 0 0 1 0-.629L9.61 8.402a.627.627 0 0 1 .546-.316Zm3.23.793a.638.638 0 0 1 .552.316l1.39 2.426a.644.644 0 0 1 0 .629l-1.39 2.43a.638.638 0 0 1-.551.316h-2.774a.627.627 0 0 1-.546-.316l-1.395-2.43a.644.644 0 0 1 0-.629l1.395-2.426a.627.627 0 0 1 .546-.316Zm-.491.867h-1.79a.624.624 0 0 0-.546.316l-.899 1.56a.644.644 0 0 0 0 .628l.899 1.563a.632.632 0 0 0 .547.316h1.789a.632.632 0 0 0 .547-.316l.898-1.563a.644.644 0 0 0 0-.629l-.898-1.558a.624.624 0 0 0-.547-.317Zm-.477.828c.227 0 .438.121.547.317l.422.73a.625.625 0 0 1 0 .629l-.422.734a.627.627 0 0 1-.547.317h-.836a.632.632 0 0 1-.547-.317l-.422-.734a.625.625 0 0 1 0-.629l.422-.73a.632.632 0 0 1 .547-.317zm-.418.817a.548.548 0 0 0-.473.273.547.547 0 0 0 0 .547.544.544 0 0 0 .473.27.544.544 0 0 0 .473-.27.547.547 0 0 0 0-.547.548.548 0 0 0-.473-.273Zm-4.422.546h.98M18.98 7.75c.391-1.895.477-3.344.223-4.398-.148-.63-.422-1.137-.84-1.508-.441-.39-1-.582-1.625-.582-1.035 0-2.12.472-3.281 1.367a14.9 14.9 0 0 0-1.473 1.316 1.206 1.206 0 0 0-.136-.144c-1.446-1.285-2.66-2.082-3.7-2.39-.617-.184-1.195-.2-1.722-.024-.559.187-1.004.574-1.317 1.117-.515.894-.652 2.074-.46 3.527.078.59.214 1.235.402 1.934a1.119 1.119 0 0 0-.215.047C3.008 8.62 1.71 9.269.926 10.015c-.465.442-.77.938-.883 1.481-.113.578 0 1.156.312 1.7.516.894 1.465 1.597 2.817 2.155.543.223 1.156.426 1.844.61a1.023 1.023 0 0 0-.07.226c-.391 1.891-.477 3.344-.223 4.395.148.629.425 1.14.84 1.508.44.39 1 .582 1.625.582 1.035 0 2.12-.473 3.28-1.364.477-.37.973-.816 1.489-1.336a1.2 1.2 0 0 0 .195.227c1.446 1.285 2.66 2.082 3.7 2.39.617.184 1.195.2 1.722.024.559-.187 1.004-.574 1.317-1.117.515-.894.652-2.074.46-3.527a14.941 14.941 0 0 0-.425-2.012 1.225 1.225 0 0 0 .238-.047c1.828-.61 3.125-1.258 3.91-2.004.465-.441.77-.937.883-1.48.113-.578 0-1.157-.313-1.7-.515-.894-1.464-1.597-2.816-2.156a14.576 14.576 0 0 0-1.906-.625.865.865 0 0 0 .059-.195z" />
    </svg>
    <p className="mt-2 font-medium">TanStack Start</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/gatsby">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Gatsby</title>
      <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.6 0 12 0zm0 2.571c3.171 0 5.915 1.543 7.629 3.858l-1.286 1.115C16.886 5.572 14.571 4.286 12 4.286c-3.343 0-6.171 2.143-7.286 5.143l9.857 9.857c2.486-.857 4.373-3 4.973-5.572h-4.115V12h6c0 4.457-3.172 8.228-7.372 9.17L2.83 9.944C3.772 5.743 7.543 2.57 12 2.57zm-9.429 9.6l9.344 9.258c-2.4-.086-4.801-.943-6.601-2.743-1.8-1.8-2.743-4.201-2.743-6.515z" />
    </svg>
    <p className="mt-2 font-medium">Gatsby</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/manual">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>React</title>
      <path d="M14.23 12.004a2.236 2.236 0 0 1-2.235 2.236 2.236 2.236 0 0 1-2.236-2.236 2.236 2.236 0 0 1 2.235-2.236 2.236 2.236 0 0 1 2.236 2.236zm2.648-10.69c-1.346 0-3.107.96-4.888 2.622-1.78-1.653-3.542-2.602-4.887-2.602-.41 0-.783.093-1.106.278-1.375.793-1.683 3.264-.973 6.365C1.98 8.917 0 10.42 0 12.004c0 1.59 1.99 3.097 5.043 4.03-.704 3.113-.39 5.588.988 6.38.32.187.69.275 1.102.275 1.345 0 3.107-.96 4.888-2.624 1.78 1.654 3.542 2.603 4.887 2.603.41 0 .783-.09 1.106-.275 1.374-.792 1.683-3.263.973-6.365C22.02 15.096 24 13.59 24 12.004c0-1.59-1.99-3.097-5.043-4.032.704-3.11.39-5.587-.988-6.38-.318-.184-.688-.277-1.092-.278zm-.005 1.09v.006c.225 0 .406.044.558.127.666.382.955 1.835.73 3.704-.054.46-.142.945-.25 1.44-.96-.236-2.006-.417-3.107-.534-.66-.905-1.345-1.727-2.035-2.447 1.592-1.48 3.087-2.292 4.105-2.295zm-9.77.02c1.012 0 2.514.808 4.11 2.28-.686.72-1.37 1.537-2.02 2.442-1.107.117-2.154.298-3.113.538-.112-.49-.195-.964-.254-1.42-.23-1.868.054-3.32.714-3.707.19-.09.4-.127.563-.132zm4.882 3.05c.455.468.91.992 1.36 1.564-.44-.02-.89-.034-1.345-.034-.46 0-.915.01-1.36.034.44-.572.895-1.096 1.345-1.565zM12 8.1c.74 0 1.477.034 2.202.093.406.582.802 1.203 1.183 1.86.372.64.71 1.29 1.018 1.946-.308.655-.646 1.31-1.013 1.95-.38.66-.773 1.288-1.18 1.87-.728.063-1.466.098-2.21.098-.74 0-1.477-.035-2.202-.093-.406-.582-.802-1.204-1.183-1.86-.372-.64-.71-1.29-1.018-1.946.303-.657.646-1.313 1.013-1.954.38-.66.773-1.286 1.18-1.868.728-.064 1.466-.098 2.21-.098zm-3.635.254c-.24.377-.48.763-.704 1.16-.225.39-.435.782-.635 1.174-.265-.656-.49-1.31-.676-1.947.64-.15 1.315-.283 2.015-.386zm7.26 0c.695.103 1.365.23 2.006.387-.18.632-.405 1.282-.66 1.933-.2-.39-.41-.783-.64-1.174-.225-.392-.465-.774-.705-1.146zm3.063.675c.484.15.944.317 1.375.498 1.732.74 2.852 1.708 2.852 2.476-.005.768-1.125 1.74-2.857 2.475-.42.18-.88.342-1.355.493-.28-.958-.646-1.956-1.1-2.98.45-1.017.81-2.01 1.085-2.964zm-13.395.004c.278.96.645 1.957 1.1 2.98-.45 1.017-.812 2.01-1.086 2.964-.484-.15-.944-.318-1.37-.5-1.732-.737-2.852-1.706-2.852-2.474 0-.768 1.12-1.742 2.852-2.476.42-.18.88-.342 1.356-.494zm11.678 4.28c.265.657.49 1.312.676 1.948-.64.157-1.316.29-2.016.39.24-.375.48-.762.705-1.158.225-.39.435-.788.636-1.18zm-9.945.02c.2.392.41.783.64 1.175.23.39.465.772.705 1.143-.695-.102-1.365-.23-2.006-.386.18-.63.406-1.282.66-1.933zM17.92 16.32c.112.493.2.968.254 1.423.23 1.868-.054 3.32-.714 3.708-.147.09-.338.128-.563.128-1.012 0-2.514-.807-4.11-2.28.686-.72 1.37-1.536 2.02-2.44 1.107-.118 2.154-.3 3.113-.54zm-11.83.01c.96.234 2.006.415 3.107.532.66.905 1.345 1.727 2.035 2.446-1.595 1.483-3.092 2.295-4.11 2.295-.22-.005-.406-.05-.553-.132-.666-.38-.955-1.834-.73-3.703.054-.46.142-.944.25-1.438zm4.56.64c.44.02.89.034 1.345.034.46 0 .915-.01 1.36-.034-.44.572-.895 1.095-1.345 1.565-.455-.47-.91-.993-1.36-1.565z" />
    </svg>
    <p className="mt-2 font-medium">Manual</p>
  </LinkedCard>
</div>

## Upgrade Your Project

<Callout className="mt-6 mb-6 border-blue-600 bg-blue-50 dark:border-blue-900 dark:bg-blue-950 [&_code]:bg-blue-100 dark:[&_code]:bg-blue-900">
  **Important:** Before upgrading, please read the [Tailwind v4 Compatibility
  Docs](https://tailwindcss.com/docs/compatibility) and make sure your project
  is ready for the upgrade. Tailwind v4 uses bleeding-edge browser features and
  is designed for modern browsers.
</Callout>

One of the major advantages of using `shadcn/ui` is that the code you end up with is exactly what you'd write yourself. There are no hidden abstractions.

This means when a dependency has a new release, you can just follow the official upgrade paths.

Here's how to upgrade your existing projects (full docs are on the way):

### 1. Follow the Tailwind v4 Upgrade Guide

- Upgrade to Tailwind v4 by following the official upgrade guide: https://tailwindcss.com/docs/upgrade-guide
- Use the `@tailwindcss/upgrade@next` codemod to remove deprecated utility classes and update tailwind config.

### 2. Update your CSS variables

The codemod will migrate your CSS variables as references under the `@theme` directive.

```css showLineNumbers
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
  }
}

@theme {
  --color-background: hsl(var(--background));
  --color-foreground: hsl(var(--foreground));
}
```

This works. But to make it easier to work with colors and other variables, we'll need to move the `hsl` wrappers and use `@theme inline`.

Here's how you do it:

1. Move `:root` and `.dark` out of the `@layer` base.
2. Wrap the color values in `hsl()`
3. Add the `inline` option to `@theme` i.e `@theme inline`
4. Remove the `hsl()` wrappers from `@theme`

```css showLineNumbers
:root {
  --background: hsl(0 0% 100%); // <-- Wrap in hsl
  --foreground: hsl(0 0% 3.9%);
}

.dark {
  --background: hsl(0 0% 3.9%); // <-- Wrap in hsl
  --foreground: hsl(0 0% 98%);
}

@theme inline {
  --color-background: var(--background); // <-- Remove hsl
  --color-foreground: var(--foreground);
}
```

This change makes it much simpler to access your theme variables in both utility classes and outside of CSS, e.g. using color values in JavaScript.

### 3. Update colors for charts

Now that the theme colors come with `hsl()`, you can remove the wrapper in your `chartConfig`:

```diff
const chartConfig = {
  desktop: {
    label: "Desktop",
-    color: "hsl(var(--chart-1))",
+    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
-   color: "hsl(var(--chart-2))",
+   color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

### 4. Use new `size-*` utility

The new `size-*` utility (added in Tailwind v3.4), is now fully supported by `tailwind-merge`. You can replace `w-* h-*` with the new `size-*` utility:

```diff
- w-4 h-4
+ size-4
```

### 5. Update your dependencies

```bash
pnpm up "@radix-ui/*" cmdk lucide-react recharts tailwind-merge clsx --latest
```

### 6. Remove forwardRef

You can use the `remove-forward-ref` codemod to migrate your `forwardRef` to props or manually update the primitives.

For the codemod, see https://github.com/reactjs/react-codemod#remove-forward-ref.

If you want to do it manually, here's how to do it step by step:

1. Replace `React.forwardRef<...>` with `React.ComponentProps<...>`
2. Remove `ref={ref}` from the component.
3. Add a `data-slot` attribute. This will come in handy for styling with Tailwind.
4. You can optionally convert to a named function and remove the `displayName`.

#### Before

```tsx showLineNumbers
const AccordionItem = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>
>(({ className, ...props }, ref) => (
  <AccordionPrimitive.Item
    ref={ref}
    className={cn("border-b last:border-b-0", className)}
    {...props}
  />
))
AccordionItem.displayName = "AccordionItem"
```

#### After

```tsx showLineNumbers
function AccordionItem({
  className,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Item>) {
  return (
    <AccordionPrimitive.Item
      data-slot="accordion-item"
      className={cn("border-b last:border-b-0", className)}
      {...props}
    />
  )
}
```

## Changelog

### March 19, 2025 - Deprecate `tailwindcss-animate`

We've deprecated `tailwindcss-animate` in favor of `tw-animate-css`.

New projects will have `tw-animate-css` installed by default.

For existing projects, follow the steps below to migrate.

1. Remove `tailwindcss-animate` from your dependencies.
2. Remove the `@plugin 'tailwindcss-animate'` from your globals.css file.
3. Install `tw-animate-css` as a dev dependency.
4. Add the `@import "tw-animate-css"` to your globals.css file.

```diff showLineNumbers
- @plugin 'tailwindcss-animate';
+ @import "tw-animate-css";
```

### March 12, 2025 - New Dark Mode Colors

We've revisited the dark mode colors and updated them to be more accessible.

If you're running an existing Tailwind v4 project (**not an upgraded one**[^1]), you can update your components to use the new dark mode colors by re-adding your components using the CLI[^2].

<Steps>

<Step>Commit any changes</Step>

**The CLI will overwrite your existing components.** We recommend committing any changes you've made to your components before running the CLI.

```bash
git add .
git commit -m "..."
```

<Step>Update components</Step>

```bash
npx shadcn@latest add --all --overwrite
```

<Step>Update colors</Step>

Update the dark mode colors in your `globals.css` file to new OKLCH colors. See the [Base Colors](/docs/theming#base-colors) reference for a list of colors.

<Step>Review changes</Step>

Review and re-apply any changes you made to your components.

</Steps>

[^1]: Upgraded projects are not affected by this change. You can continue using the old dark mode colors.

[^2]: Updating your components will overwrite your existing components.


---

<!-- SOURCE: apps/v4/content/docs/(root)/theming.mdx -->

## apps/v4/content/docs/(root)/theming.mdx

---
title: Theming
description: Using CSS variables and theme tokens.
---

<Callout>

Want to build your theme visually? Use [shadcn/create](/create) to preview colors, radius, fonts, and icons, then generate a preset for your project.

</Callout>

We use and recommend CSS variables for theming.

This gives you semantic theme tokens like `background`, `foreground`, and `primary` that components use by default. Override those tokens in your CSS to change the look of your app without rewriting component classes.

```tsx /bg-background/ /text-foreground/
<div className="bg-background text-foreground" />
```

To use CSS variables for theming, set `tailwind.cssVariables` to `true` in your `components.json` file. This is the default.

```json {8} title="components.json" showLineNumbers
{
  "style": "base-nova",
  "rsc": true,
  "tailwind": {
    "config": "",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  }
}
```

Tailwind maps these tokens into utilities like `bg-background`, `text-foreground`, `border-border`, and `ring-ring`.

Dark mode works by overriding the same tokens inside a `.dark` selector. See the [dark mode docs](/docs/dark-mode/next) for adding a theme provider and toggling the `.dark` class.

## Token Convention

We use semantic background and foreground pairs. The base token controls the surface color and the `-foreground` token controls the text and icon color that sits on that surface.

<Callout className="mt-4">

The background suffix is omitted for the surface token. For example, `primary` pairs with `primary-foreground`.

</Callout>

Given the following CSS variables:

```css
--primary: oklch(0.205 0 0);
--primary-foreground: oklch(0.985 0 0);
```

The `background` color of the following component will be `var(--primary)` and the `foreground` color will be `var(--primary-foreground)`.

```tsx
<div className="bg-primary text-primary-foreground">Hello</div>
```

## Theme Tokens

These tokens live in your CSS file under `:root` and `.dark`.

| Token                                            | What it controls                                       | Used by                                                                      |
| ------------------------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `background` / `foreground`                      | The default app background and text color.             | The page shell, page sections, and default text.                             |
| `card` / `card-foreground`                       | Elevated surfaces and the content inside them.         | `Card`, dashboard panels, settings panels.                                   |
| `popover` / `popover-foreground`                 | Floating surfaces and the content inside them.         | `Popover`, `DropdownMenu`, `ContextMenu`, and other overlays.                |
| `primary` / `primary-foreground`                 | High-emphasis actions and brand surfaces.              | Default `Button`, selected states, badges, and active accents.               |
| `secondary` / `secondary-foreground`             | Lower-emphasis filled actions and supporting surfaces. | Secondary buttons, secondary badges, and supporting UI.                      |
| `muted` / `muted-foreground`                     | Subtle surfaces and lower-emphasis content.            | Descriptions, placeholders, empty states, helper text, and subdued surfaces. |
| `accent` / `accent-foreground`                   | Interactive hover, focus, and active surfaces.         | Ghost buttons, menu highlight states, hovered rows, and selected items.      |
| `destructive`                                    | Destructive actions and error emphasis.                | Destructive buttons, invalid states, and destructive menu items.             |
| `border`                                         | Default borders and separators.                        | Cards, menus, tables, separators, and layout dividers.                       |
| `input`                                          | Form control borders and input surface treatment.      | `Input`, `Textarea`, `Select`, and outline-style controls.                   |
| `ring`                                           | Focus rings and outlines.                              | Buttons, inputs, checkboxes, menus, and other focusable controls.            |
| `chart-1` ... `chart-5`                          | The default chart palette.                             | Charts and chart-driven dashboard blocks.                                    |
| `sidebar` / `sidebar-foreground`                 | The base sidebar surface and default sidebar text.     | The `Sidebar` container and its default content.                             |
| `sidebar-primary` / `sidebar-primary-foreground` | High-emphasis actions inside the sidebar.              | Active items, icon tiles, badges, and sidebar CTAs.                          |
| `sidebar-accent` / `sidebar-accent-foreground`   | Hover and selected states inside the sidebar.          | Sidebar menu hover states, open items, and interactive rows.                 |
| `sidebar-border`                                 | Sidebar-specific borders and separators.               | Sidebar headers, groups, and internal dividers.                              |
| `sidebar-ring`                                   | Sidebar-specific focus rings.                          | Focused controls inside the sidebar.                                         |
| `radius`                                         | The base corner radius scale.                          | Cards, inputs, buttons, popovers, and the derived `radius-*` tokens.         |

<Callout className="mt-4">

The chart tokens are covered in more detail in the [Chart theming docs](/docs/components/chart#theming).

</Callout>

## Radius Scale

`--radius` is the base radius token for your theme.

We derive a small radius scale from it so components can use consistent corner sizes while still sharing a single source of truth.

```css title="app/globals.css" showLineNumbers
@theme inline {
  --radius-sm: calc(var(--radius) * 0.6);
  --radius-md: calc(var(--radius) * 0.8);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) * 1.4);
  --radius-2xl: calc(var(--radius) * 1.8);
  --radius-3xl: calc(var(--radius) * 2.2);
  --radius-4xl: calc(var(--radius) * 2.6);
}
```

This means:

- `radius-lg` is the base value.
- Smaller radii scale down from `--radius`.
- Larger radii scale up from `--radius`.
- Changing `--radius` updates the entire radius scale.

## Adding New Tokens

To add a new token, define it under `:root` and `.dark`, then expose it to Tailwind with `@theme inline`.

```css title="app/globals.css" showLineNumbers
:root {
  --warning: oklch(0.84 0.16 84);
  --warning-foreground: oklch(0.28 0.07 46);
}

.dark {
  --warning: oklch(0.41 0.11 46);
  --warning-foreground: oklch(0.99 0.02 95);
}

@theme inline {
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
}
```

You can now use `bg-warning` and `text-warning-foreground` in your components.

```tsx /bg-warning/ /text-warning-foreground/
<div className="bg-warning text-warning-foreground" />
```

## Base Colors

`tailwind.baseColor` controls the default token values generated for your project when you run `init` or use a preset.

The available base colors are: **Neutral**, **Stone**, **Zinc**, **Mauve**, **Olive**, **Mist**, and **Taupe**.

## Default Theme CSS

The following is the full default `neutral` theme scaffold. Copy it into your global CSS file and adjust the tokens as needed.

<CodeCollapsibleWrapper>

```css showLineNumbers title="app/globals.css"
@import "tailwindcss";
@import "shadcn/tailwind.css";

@custom-variant dark (&:is(.dark *));

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
  --radius-sm: calc(var(--radius) * 0.6);
  --radius-md: calc(var(--radius) * 0.8);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) * 1.4);
  --radius-2xl: calc(var(--radius) * 1.8);
  --radius-3xl: calc(var(--radius) * 2.2);
  --radius-4xl: calc(var(--radius) * 2.6);
}

:root {
  --radius: 0.625rem;
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.145 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.145 0 0);
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
  --secondary: oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --accent: oklch(0.97 0 0);
  --accent-foreground: oklch(0.205 0 0);
  --destructive: oklch(0.577 0.245 27.325);
  --border: oklch(0.922 0 0);
  --input: oklch(0.922 0 0);
  --ring: oklch(0.708 0 0);
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-accent-foreground: oklch(0.205 0 0);
  --sidebar-border: oklch(0.922 0 0);
  --sidebar-ring: oklch(0.708 0 0);
}

.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  --card: oklch(0.205 0 0);
  --card-foreground: oklch(0.985 0 0);
  --popover: oklch(0.205 0 0);
  --popover-foreground: oklch(0.985 0 0);
  --primary: oklch(0.922 0 0);
  --primary-foreground: oklch(0.205 0 0);
  --secondary: oklch(0.269 0 0);
  --secondary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --accent: oklch(0.269 0 0);
  --accent-foreground: oklch(0.985 0 0);
  --destructive: oklch(0.704 0.191 22.216);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.556 0 0);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.556 0 0);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }

  body {
    @apply bg-background text-foreground;
  }
}
```

</CodeCollapsibleWrapper>

## Without CSS Variables

If you do not want to use CSS variables, the CLI can generate components with inline Tailwind color utilities instead.

```bash
npx shadcn@latest init --no-css-variables
```

This sets `tailwind.cssVariables` to `false` in your `components.json` file.

```tsx /bg-zinc-950/ /text-zinc-50/ /dark:bg-white/ /dark:text-zinc-950/
<div className="bg-zinc-950 text-zinc-50 dark:bg-white dark:text-zinc-950" />
```

<Callout className="mt-4">

This is an installation-time choice. To switch an existing project, delete and re-install your components.

</Callout>


---

<!-- SOURCE: apps/v4/content/docs/(root)/v0.mdx -->

## apps/v4/content/docs/(root)/v0.mdx

---
title: Open in v0
description: Open components in v0 for customization.
---

Every component on ui.shadcn.com is editable on [v0 by Vercel](https://v0.dev). This allows you to easily customize the components in natural language and paste into your app.

<a href="https://vercel.com/signup?utm_source=shad&utm_medium=web&utm_campaign=docs_cta_signup">
  <Image
    src="/images/open-in-v0.png"
    width="716"
    height="420"
    alt="Open in v0"
    className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
  />
  <Image
    src="/images/open-in-v0-dark.png"
    width="716"
    height="420"
    alt="Open in v0"
    className="mt-6 hidden w-full overflow-hidden rounded-lg border shadow-sm dark:block"
  />
  <span className="sr-only">Open in v0</span>
</a>

To use v0, sign-up for a free [Vercel account here](https://vercel.com/signup?utm_source=shad&utm_medium=web&utm_campaign=docs_cta_signup). In addition to v0, this gives you free access to Vercel's frontend cloud platform by the creators of Next.js, where you can deploy and host your project for free.

Learn more about getting started with [Vercel here](https://vercel.com/docs/getting-started-with-vercel?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_about_vercel).

Learn more about getting started with [v0 here](https://v0.dev/faq).


---

<!-- SOURCE: apps/v4/content/docs/components/base/accordion.mdx -->

## apps/v4/content/docs/components/base/accordion.mdx

---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/accordion
  api: https://base-ui.com/react/components/accordion#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="accordion-demo"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add accordion
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="accordion"
  title="components/ui/accordion.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"
```

```tsx showLineNumbers
<Accordion defaultValue={["item-1"]}>
  <AccordionItem value="item-1">
    <AccordionTrigger>Is it accessible?</AccordionTrigger>
    <AccordionContent>
      Yes. It adheres to the WAI-ARIA design pattern.
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

## Examples

### Basic

A basic accordion that shows one item at a time. The first item is open by default.

<ComponentPreview
  styleName="base-nova"
  name="accordion-basic"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Multiple

Use the `multiple` prop to allow multiple items to be open at the same time.

<ComponentPreview
  styleName="base-nova"
  name="accordion-multiple"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[450px]"
/>

### Disabled

Use the `disabled` prop on `AccordionItem` to disable individual items.

<ComponentPreview
  styleName="base-nova"
  name="accordion-disabled"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Borders

Add `border` to the `Accordion` and `border-b last:border-b-0` to the `AccordionItem` to add borders to the items.

<ComponentPreview
  styleName="base-nova"
  name="accordion-borders"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Card

Wrap the `Accordion` in a `Card` component.

<ComponentPreview
  styleName="base-nova"
  name="accordion-card"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[435px]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="accordion-rtl"
  align="start"
  direction="rtl"
/>

## API Reference

See the [Base UI](https://base-ui.com/react/components/accordion#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/alert-dialog.mdx -->

## apps/v4/content/docs/components/base/alert-dialog.mdx

---
title: Alert Dialog
description: A modal dialog that interrupts the user with important content and expects a response.
featured: true
base: base
component: true
links:
  doc: https://base-ui.com/react/components/alert-dialog
  api: https://base-ui.com/react/components/alert-dialog#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="alert-dialog-demo"
  previewClassName="h-56"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add alert-dialog
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="alert-dialog"
  title="components/ui/alert-dialog.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
```

```tsx showLineNumbers
<AlertDialog>
  <AlertDialogTrigger render={<Button variant="outline" />}>
    Show Dialog
  </AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
      <AlertDialogDescription>
        This action cannot be undone. This will permanently delete your account
        from our servers.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction>Continue</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

## Examples

### Basic

A basic alert dialog with a title, description, and cancel and continue buttons.

<ComponentPreview
  styleName="base-nova"
  name="alert-dialog-basic"
  previewClassName="h-56"
/>

### Small

Use the `size="sm"` prop to make the alert dialog smaller.

<ComponentPreview
  styleName="base-nova"
  name="alert-dialog-small"
  previewClassName="h-56"
/>

### Media

Use the `AlertDialogMedia` component to add a media element such as an icon or image to the alert dialog.

<ComponentPreview
  styleName="base-nova"
  name="alert-dialog-media"
  previewClassName="h-56"
/>

### Small with Media

Use the `size="sm"` prop to make the alert dialog smaller and the `AlertDialogMedia` component to add a media element such as an icon or image to the alert dialog.

<ComponentPreview
  styleName="base-nova"
  name="alert-dialog-small-media"
  previewClassName="h-56"
/>

### Destructive

Use the `AlertDialogAction` component to add a destructive action button to the alert dialog.

<ComponentPreview
  styleName="base-nova"
  name="alert-dialog-destructive"
  previewClassName="h-56"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="alert-dialog-rtl"
  direction="rtl"
  previewClassName="h-56"
/>

## API Reference

### size

Use the `size` prop on the `AlertDialogContent` component to control the size of the alert dialog. It accepts the following values:

| Prop   | Type                | Default     |
| ------ | ------------------- | ----------- |
| `size` | `"default" \| "sm"` | `"default"` |

For more information about the other components and their props, see the [Base UI documentation](https://base-ui.com/react/components/alert-dialog#api-reference).


---

<!-- SOURCE: apps/v4/content/docs/components/base/alert.mdx -->

## apps/v4/content/docs/components/base/alert.mdx

---
title: Alert
description: Displays a callout for user attention.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="alert-demo"
  previewClassName="h-auto sm:h-72 p-6"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add alert
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="alert" title="components/ui/alert.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Alert,
  AlertAction,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert"
```

```tsx showLineNumbers
<Alert>
  <InfoIcon />
  <AlertTitle>Heads up!</AlertTitle>
  <AlertDescription>
    You can add components and dependencies to your app using the cli.
  </AlertDescription>
  <AlertAction>
    <Button variant="outline">Enable</Button>
  </AlertAction>
</Alert>
```

## Examples

### Basic

A basic alert with an icon, title and description.

<ComponentPreview
  styleName="base-nova"
  name="alert-basic"
  previewClassName="h-auto sm:h-72 p-6"
/>

### Destructive

Use `variant="destructive"` to create a destructive alert.

<ComponentPreview
  styleName="base-nova"
  name="alert-destructive"
  previewClassName="h-auto sm:h-72 p-6"
/>

### Action

Use `AlertAction` to add a button or other action element to the alert.

<ComponentPreview
  styleName="base-nova"
  name="alert-action"
  previewClassName="h-auto sm:h-72 p-6"
/>

### Custom Colors

You can customize the alert colors by adding custom classes such as `bg-amber-50 dark:bg-amber-950` to the `Alert` component.

<ComponentPreview
  styleName="base-nova"
  name="alert-colors"
  previewClassName="h-auto sm:h-72 p-6"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="alert-rtl"
  direction="rtl"
  previewClassName="h-auto sm:h-72 p-6"
/>

## API Reference

### Alert

The `Alert` component displays a callout for user attention.

| Prop      | Type                         | Default     |
| --------- | ---------------------------- | ----------- |
| `variant` | `"default" \| "destructive"` | `"default"` |

### AlertTitle

The `AlertTitle` component displays the title of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AlertDescription

The `AlertDescription` component displays the description or content of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AlertAction

The `AlertAction` component displays an action element (like a button) positioned absolutely in the top-right corner of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |


---

<!-- SOURCE: apps/v4/content/docs/components/base/aspect-ratio.mdx -->

## apps/v4/content/docs/components/base/aspect-ratio.mdx

---
title: Aspect Ratio
description: Displays content within a desired ratio.
base: base
component: true
---

<ComponentPreview name="aspect-ratio-demo" styleName="base-nova" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add aspect-ratio
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="aspect-ratio"
  title="components/ui/aspect-ratio.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { AspectRatio } from "@/components/ui/aspect-ratio"
```

```tsx showLineNumbers
<AspectRatio ratio={16 / 9}>
  <Image src="..." alt="Image" className="rounded-md object-cover" />
</AspectRatio>
```

## Examples

### Square

A square aspect ratio component using the `ratio={1 / 1}` prop. This is useful for displaying images in a square format.

<ComponentPreview name="aspect-ratio-square" styleName="base-nova" />

### Portrait

A portrait aspect ratio component using the `ratio={9 / 16}` prop. This is useful for displaying images in a portrait format.

<ComponentPreview
  styleName="base-nova"
  name="aspect-ratio-portrait"
  previewClassName="h-96"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="aspect-ratio-rtl"
  direction="rtl"
  previewClassName="h-96"
/>

## API Reference

### AspectRatio

The `AspectRatio` component displays content within a desired ratio.

| Prop        | Type     | Default | Required |
| ----------- | -------- | ------- | -------- |
| `ratio`     | `number` | -       | Yes      |
| `className` | `string` | -       | No       |

For more information, see the [Base UI documentation](https://base-ui.com/react/components/aspect-ratio#api-reference).


---

<!-- SOURCE: apps/v4/content/docs/components/base/avatar.mdx -->

## apps/v4/content/docs/components/base/avatar.mdx

---
title: Avatar
description: An image element with a fallback for representing the user.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/avatar
  api: https://base-ui.com/react/components/avatar#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="avatar-demo"
  previewClassName="h-72"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add avatar
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="avatar"
  title="components/ui/avatar.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
```

```tsx showLineNumbers
<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" />
  <AvatarFallback>CN</AvatarFallback>
</Avatar>
```

## Examples

### Basic

A basic avatar component with an image and a fallback.

<ComponentPreview styleName="base-nova" name="avatar-basic" />

### Badge

Use the `AvatarBadge` component to add a badge to the avatar. The badge is positioned at the bottom right of the avatar.

<ComponentPreview styleName="base-nova" name="avatar-badge" />

Use the `className` prop to add custom styles to the badge such as custom colors, sizes, etc.

```tsx showLineNumbers
<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
  <AvatarFallback>CN</AvatarFallback>
  <AvatarBadge className="bg-green-600 dark:bg-green-800" />
</Avatar>
```

### Badge with Icon

You can also use an icon inside `<AvatarBadge>`.

<ComponentPreview styleName="base-nova" name="avatar-badge-icon" />

### Avatar Group

Use the `AvatarGroup` component to add a group of avatars.

<ComponentPreview styleName="base-nova" name="avatar-group" />

### Avatar Group Count

Use `<AvatarGroupCount>` to add a count to the group.

<ComponentPreview styleName="base-nova" name="avatar-group-count" />

### Avatar Group with Icon

You can also use an icon inside `<AvatarGroupCount>`.

<ComponentPreview styleName="base-nova" name="avatar-group-count-icon" />

### Sizes

Use the `size` prop to change the size of the avatar.

<ComponentPreview styleName="base-nova" name="avatar-size" />

### Dropdown

You can use the `Avatar` component as a trigger for a dropdown menu.

<ComponentPreview styleName="base-nova" name="avatar-dropdown" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="avatar-rtl"
  direction="rtl"
  previewClassName="h-72"
/>

## API Reference

### Avatar

The `Avatar` component is the root component that wraps the avatar image and fallback.

| Prop        | Type                        | Default     |
| ----------- | --------------------------- | ----------- |
| `size`      | `"default" \| "sm" \| "lg"` | `"default"` |
| `className` | `string`                    | -           |

### AvatarImage

The `AvatarImage` component displays the avatar image. It accepts all Base UI Avatar Image props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `src`       | `string` | -       |
| `alt`       | `string` | -       |
| `className` | `string` | -       |

### AvatarFallback

The `AvatarFallback` component displays a fallback when the image fails to load. It accepts all Base UI Avatar Fallback props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarBadge

The `AvatarBadge` component displays a badge indicator on the avatar, typically positioned at the bottom right.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarGroup

The `AvatarGroup` component displays a group of avatars with overlapping styling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarGroupCount

The `AvatarGroupCount` component displays a count indicator in an avatar group, typically showing the number of additional avatars.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

For more information about Base UI Avatar props, see the [Base UI documentation](https://base-ui.com/react/components/avatar#api-reference).


---

<!-- SOURCE: apps/v4/content/docs/components/base/badge.mdx -->

## apps/v4/content/docs/components/base/badge.mdx

---
title: Badge
description: Displays a badge or a component that looks like a badge.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="badge-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add badge
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="badge"
  title="components/ui/badge.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Badge } from "@/components/ui/badge"
```

```tsx
<Badge variant="default | outline | secondary | destructive">Badge</Badge>
```

## Examples

### Variants

Use the `variant` prop to change the variant of the badge.

<ComponentPreview styleName="base-nova" name="badge-variants" />

### With Icon

You can render an icon inside the badge. Use `data-icon="inline-start"` to render the icon on the left and `data-icon="inline-end"` to render the icon on the right.

<ComponentPreview styleName="base-nova" name="badge-icon" />

### With Spinner

You can render a spinner inside the badge. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` prop to the spinner.

<ComponentPreview styleName="base-nova" name="badge-spinner" />

### Link

Use the `render` prop to render a link as a badge.

<ComponentPreview styleName="base-nova" name="badge-link" />

### Custom Colors

You can customize the colors of a badge by adding custom classes such as `bg-green-50 dark:bg-green-800` to the `Badge` component.

<ComponentPreview styleName="base-nova" name="badge-colors" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="badge-rtl" direction="rtl" />

## API Reference

### Badge

The `Badge` component displays a badge or a component that looks like a badge.

| Prop        | Type                                                                          | Default     |
| ----------- | ----------------------------------------------------------------------------- | ----------- |
| `variant`   | `"default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link"` | `"default"` |
| `className` | `string`                                                                      | -           |


---

<!-- SOURCE: apps/v4/content/docs/components/base/breadcrumb.mdx -->

## apps/v4/content/docs/components/base/breadcrumb.mdx

---
title: Breadcrumb
description: Displays the path to the current resource using a hierarchy of links.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="breadcrumb-demo"
  previewClassName="p-2"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add breadcrumb
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="breadcrumb"
  title="components/ui/breadcrumb.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
```

```tsx showLineNumbers
<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink render={<a href="/" />}>Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbLink render={<a href="/components" />}>
        Components
      </BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

## Examples

### Basic

A basic breadcrumb with a home link and a components link.

<ComponentPreview styleName="base-nova" name="breadcrumb-basic" />

### Custom separator

Use a custom component as `children` for `<BreadcrumbSeparator />` to create a custom separator.

<ComponentPreview styleName="base-nova" name="breadcrumb-separator" />

### Dropdown

You can compose `<BreadcrumbItem />` with a `<DropdownMenu />` to create a dropdown in the breadcrumb.

<ComponentPreview styleName="base-nova" name="breadcrumb-dropdown" />

### Collapsed

We provide a `<BreadcrumbEllipsis />` component to show a collapsed state when the breadcrumb is too long.

<ComponentPreview
  styleName="base-nova"
  name="breadcrumb-ellipsis"
  previewClassName="p-2"
/>

### Link component

To use a custom link component from your routing library, you can use the `render` prop on `<BreadcrumbLink />`.

<ComponentPreview styleName="base-nova" name="breadcrumb-link" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="breadcrumb-rtl"
  direction="rtl"
  previewClassName="p-2"
/>

## API Reference

### Breadcrumb

The `Breadcrumb` component is the root navigation element that wraps all breadcrumb components.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbList

The `BreadcrumbList` component displays the ordered list of breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbItem

The `BreadcrumbItem` component wraps individual breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbLink

The `BreadcrumbLink` component displays a clickable link in the breadcrumb.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbPage

The `BreadcrumbPage` component displays the current page in the breadcrumb (non-clickable).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbSeparator

The `BreadcrumbSeparator` component displays a separator between breadcrumb items. You can pass custom children to override the default separator icon.

| Prop        | Type              | Default |
| ----------- | ----------------- | ------- |
| `children`  | `React.ReactNode` | -       |
| `className` | `string`          | -       |

### BreadcrumbEllipsis

The `BreadcrumbEllipsis` component displays an ellipsis indicator for collapsed breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |


---

<!-- SOURCE: apps/v4/content/docs/components/base/button-group.mdx -->

## apps/v4/content/docs/components/base/button-group.mdx

---
title: Button Group
description: A container that groups related buttons together with consistent styling.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="button-group-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add button-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="button-group"
  title="components/ui/button-group.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import {
  ButtonGroup,
  ButtonGroupSeparator,
  ButtonGroupText,
} from "@/components/ui/button-group"
```

```tsx
<ButtonGroup>
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

## Accessibility

- The `ButtonGroup` component has the `role` attribute set to `group`.
- Use <Kbd>Tab</Kbd> to navigate between the buttons in the group.
- Use `aria-label` or `aria-labelledby` to label the button group.

```tsx showLineNumbers
<ButtonGroup aria-label="Button group">
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

## ButtonGroup vs ToggleGroup

- Use the `ButtonGroup` component when you want to group buttons that perform an action.
- Use the `ToggleGroup` component when you want to group buttons that toggle a state.

## Examples

### Orientation

Set the `orientation` prop to change the button group layout.

<ComponentPreview styleName="base-nova" name="button-group-orientation" />

### Size

Control the size of buttons using the `size` prop on individual buttons.

<ComponentPreview styleName="base-nova" name="button-group-size" />

### Nested

Nest `<ButtonGroup>` components to create button groups with spacing.

<ComponentPreview styleName="base-nova" name="button-group-nested" />

### Separator

The `ButtonGroupSeparator` component visually divides buttons within a group.

Buttons with variant `outline` do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.

<ComponentPreview styleName="base-nova" name="button-group-separator" />

### Split

Create a split button group by adding two buttons separated by a `ButtonGroupSeparator`.

<ComponentPreview styleName="base-nova" name="button-group-split" />

### Input

Wrap an `Input` component with buttons.

<ComponentPreview styleName="base-nova" name="button-group-input" />

### Input Group

Wrap an `InputGroup` component to create complex input layouts.

<ComponentPreview styleName="base-nova" name="button-group-input-group" />

### Dropdown Menu

Create a split button group with a `DropdownMenu` component.

<ComponentPreview styleName="base-nova" name="button-group-dropdown" />

### Select

Pair with a `Select` component.

<ComponentPreview styleName="base-nova" name="button-group-select" />

### Popover

Use with a `Popover` component.

<ComponentPreview styleName="base-nova" name="button-group-popover" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="button-group-rtl"
  direction="rtl"
/>

## API Reference

### ButtonGroup

The `ButtonGroup` component is a container that groups related buttons together with consistent styling.

| Prop          | Type                         | Default        |
| ------------- | ---------------------------- | -------------- |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` |

```tsx
<ButtonGroup>
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

Nest multiple button groups to create complex layouts with spacing. See the [nested](#nested) example for more details.

```tsx
<ButtonGroup>
  <ButtonGroup />
  <ButtonGroup />
</ButtonGroup>
```

### ButtonGroupSeparator

The `ButtonGroupSeparator` component visually divides buttons within a group.

| Prop          | Type                         | Default      |
| ------------- | ---------------------------- | ------------ |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` |

```tsx
<ButtonGroup>
  <Button>Button 1</Button>
  <ButtonGroupSeparator />
  <Button>Button 2</Button>
</ButtonGroup>
```

### ButtonGroupText

Use this component to display text within a button group.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

```tsx
<ButtonGroup>
  <ButtonGroupText>Text</ButtonGroupText>
  <Button>Button</Button>
</ButtonGroup>
```

Use the `asChild` prop to render a custom component as the text, for example a label.

```tsx showLineNumbers
import { ButtonGroupText } from "@/components/ui/button-group"
import { Label } from "@/components/ui/label"

export function ButtonGroupTextDemo() {
  return (
    <ButtonGroup>
      <ButtonGroupText asChild>
        <Label htmlFor="name">Text</Label>
      </ButtonGroupText>
      <Input placeholder="Type something here..." id="name" />
    </ButtonGroup>
  )
}
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/button.mdx -->

## apps/v4/content/docs/components/base/button.mdx

---
title: Button
description: Displays a button or a component that looks like a button.
featured: true
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="button-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add button
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="button"
  title="components/ui/button.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Button } from "@/components/ui/button"
```

```tsx
<Button variant="outline">Button</Button>
```

## Cursor

Tailwind v4 [switched](https://tailwindcss.com/docs/upgrade-guide#buttons-use-the-default-cursor) from `cursor: pointer` to `cursor: default` for the button component.

If you want to keep the `cursor: pointer` behavior, add the following code to your CSS file:

```css showLineNumbers title="globals.css"
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

## Examples

### Size

Use the `size` prop to change the size of the button.

<ComponentPreview styleName="base-nova" name="button-size" />

### Default

<ComponentPreview styleName="base-nova" name="button-default" />

### Outline

<ComponentPreview styleName="base-nova" name="button-outline" />

### Secondary

<ComponentPreview styleName="base-nova" name="button-secondary" />

### Ghost

<ComponentPreview styleName="base-nova" name="button-ghost" />

### Destructive

<ComponentPreview styleName="base-nova" name="button-destructive" />

### Link

<ComponentPreview styleName="base-nova" name="button-link" />

### Icon

<ComponentPreview styleName="base-nova" name="button-icon" />

### With Icon

Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the icon for the correct spacing.

<ComponentPreview styleName="base-nova" name="button-with-icon" />

### Rounded

Use the `rounded-full` class to make the button rounded.

<ComponentPreview styleName="base-nova" name="button-rounded" />

### Spinner

Render a `<Spinner />` component inside the button to show a loading state. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the spinner for the correct spacing.

<ComponentPreview styleName="base-nova" name="button-spinner" />

### Button Group

To create a button group, use the `ButtonGroup` component. See the [Button Group](/docs/components/base/button-group) documentation for more details.

<ComponentPreview styleName="base-nova" name="button-group-demo" />

### As Link

You can use the `buttonVariants` helper to make a link look like a button.

**Do not use `<Button render={<a />} nativeButton={false} />` for links.** The Base UI `Button` component always applies `role="button"`, which overrides the semantic link role on `<a>` elements. Use `buttonVariants` with a plain `<a>` tag instead.

<ComponentPreview styleName="base-nova" name="button-render" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="button-rtl" direction="rtl" />

## API Reference

### Button

The `Button` component is a wrapper around the `button` element that adds a variety of styles and functionality.

| Prop      | Type                                                                                 | Default     |
| --------- | ------------------------------------------------------------------------------------ | ----------- |
| `variant` | `"default" \| "outline" \| "ghost" \| "destructive" \| "secondary" \| "link"`        | `"default"` |
| `size`    | `"default" \| "xs" \| "sm" \| "lg" \| "icon" \| "icon-xs" \| "icon-sm" \| "icon-lg"` | `"default"` |


---

<!-- SOURCE: apps/v4/content/docs/components/base/calendar.mdx -->

## apps/v4/content/docs/components/base/calendar.mdx

---
title: Calendar
description: A calendar component that allows users to select a date or a range of dates.
base: base
component: true
links:
  doc: https://react-day-picker.js.org
---

<ComponentPreview
  styleName="base-nova"
  name="calendar-demo"
  previewClassName="h-96"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add calendar
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install react-day-picker date-fns
```

<Step>Add the `Button` component to your project.</Step>

The `Calendar` component uses the `Button` component. Make sure you have it installed in your project.

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="calendar"
  title="components/ui/calendar.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Calendar } from "@/components/ui/calendar"
```

```tsx showLineNumbers
const [date, setDate] = React.useState<Date | undefined>(new Date())

return (
  <Calendar
    mode="single"
    selected={date}
    onSelect={setDate}
    className="rounded-lg border"
  />
)
```

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information.

## About

The `Calendar` component is built on top of [React DayPicker](https://react-day-picker.js.org).

## Date Picker

You can use the `<Calendar>` component to build a date picker. See the [Date Picker](/docs/components/base/date-picker) page for more information.

## Persian / Hijri / Jalali Calendar

To use the Persian calendar, edit `components/ui/calendar.tsx` and replace `react-day-picker` with `react-day-picker/persian`.

```diff
- import { DayPicker } from "react-day-picker"
+ import { DayPicker } from "react-day-picker/persian"
```

<ComponentPreview
  styleName="base-nova"
  name="calendar-hijri"
  title="Persian / Hijri / Jalali Calendar"
  description="A Persian calendar."
  previewClassName="h-[400px]"
/>

## Selected Date (With TimeZone)

The Calendar component accepts a `timeZone` prop to ensure dates are displayed and selected in the user's local timezone.

```tsx showLineNumbers
export function CalendarWithTimezone() {
  const [date, setDate] = React.useState<Date | undefined>(undefined)
  const [timeZone, setTimeZone] = React.useState<string | undefined>(undefined)

  React.useEffect(() => {
    setTimeZone(Intl.DateTimeFormat().resolvedOptions().timeZone)
  }, [])

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
      timeZone={timeZone}
    />
  )
}
```

**Note:** If you notice a selected date offset (for example, selecting the 20th highlights the 19th), make sure the `timeZone` prop is set to the user's local timezone.

**Why client-side?** The timezone is detected using `Intl.DateTimeFormat().resolvedOptions().timeZone` inside a `useEffect` to ensure compatibility with server-side rendering. Detecting the timezone during render would cause hydration mismatches, as the server and client may be in different timezones.

## Examples

### Basic

A basic calendar component. We used `className="rounded-lg border"` to style the calendar.

<ComponentPreview
  styleName="base-nova"
  name="calendar-basic"
  previewClassName="h-96"
/>

### Range Calendar

Use the `mode="range"` prop to enable range selection.

<ComponentPreview
  styleName="base-nova"
  name="calendar-range"
  previewClassName="h-[36rem] md:h-96"
/>

### Month and Year Selector

Use `captionLayout="dropdown"` to show month and year dropdowns.

<ComponentPreview
  styleName="base-nova"
  name="calendar-caption"
  previewClassName="h-96"
/>

### Presets

<ComponentPreview
  styleName="base-nova"
  name="calendar-presets"
  previewClassName="h-[650px]"
/>

### Date and Time Picker

<ComponentPreview
  styleName="base-nova"
  name="calendar-time"
  previewClassName="h-[600px]"
/>

### Booked dates

<ComponentPreview
  styleName="base-nova"
  name="calendar-booked-dates"
  previewClassName="h-96"
/>

### Custom Cell Size

<ComponentPreview
  styleName="base-nova"
  name="calendar-custom-days"
  title="Custom Cell Size"
  description="A calendar with custom cell size that's responsive."
  className="**:[.preview]:h-[560px]"
/>

You can customize the size of calendar cells using the `--cell-size` CSS variable. You can also make it responsive by using breakpoint-specific values:

```tsx showLineNumbers
<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  className="rounded-lg border [--cell-size:--spacing(11)] md:[--cell-size:--spacing(12)]"
/>
```

Or use fixed values:

```tsx showLineNumbers
<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  className="rounded-lg border [--cell-size:2.75rem] md:[--cell-size:3rem]"
/>
```

### Week Numbers

Use `showWeekNumber` to show week numbers.

<ComponentPreview
  styleName="base-nova"
  name="calendar-week-numbers"
  previewClassName="h-96"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

See also the [Hijri Guide](#persian--hijri--jalali-calendar) for enabling the Persian / Hijri / Jalali calendar.

<ComponentPreview
  styleName="base-nova"
  name="calendar-rtl"
  direction="rtl"
  previewClassName="h-96"
/>

When using RTL, import the locale from `react-day-picker/locale` and pass both the `locale` and `dir` props to the Calendar component:

```tsx showLineNumbers
import { arSA } from "react-day-picker/locale"

;<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  locale={arSA}
  dir="rtl"
/>
```

## API Reference

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information on the `Calendar` component.

## Changelog

### RTL Support

If you're upgrading from a previous version of the `Calendar` component, you'll need to apply the following updates to add locale support:

<Steps>

<Step>Import the `Locale` type.</Step>

Add `Locale` to your imports from `react-day-picker`:

```diff
  import {
    DayPicker,
    getDefaultClassNames,
    type DayButton,
+   type Locale,
  } from "react-day-picker"
```

<Step>Add `locale` prop to the Calendar component.</Step>

Add the `locale` prop to the component's props:

```diff
  function Calendar({
    className,
    classNames,
    showOutsideDays = true,
    captionLayout = "label",
    buttonVariant = "ghost",
+   locale,
    formatters,
    components,
    ...props
  }: React.ComponentProps<typeof DayPicker> & {
    buttonVariant?: React.ComponentProps<typeof Button>["variant"]
  }) {
```

<Step>Pass `locale` to DayPicker.</Step>

Pass the `locale` prop to the `DayPicker` component:

```diff
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn(...)}
      captionLayout={captionLayout}
+     locale={locale}
      formatters={{
        formatMonthDropdown: (date) =>
-         date.toLocaleString("default", { month: "short" }),
+         date.toLocaleString(locale?.code, { month: "short" }),
        ...formatters,
      }}
```

<Step>Update CalendarDayButton to accept locale.</Step>

Update the `CalendarDayButton` component signature and pass `locale`:

```diff
  function CalendarDayButton({
    className,
    day,
    modifiers,
+   locale,
    ...props
- }: React.ComponentProps<typeof DayButton>) {
+ }: React.ComponentProps<typeof DayButton> & { locale?: Partial<Locale> }) {
```

<Step>Update date formatting in CalendarDayButton.</Step>

Use `locale?.code` in the date formatting:

```diff
    <Button
      variant="ghost"
      size="icon"
-     data-day={day.date.toLocaleDateString()}
+     data-day={day.date.toLocaleDateString(locale?.code)}
      ...
    />
```

<Step>Pass locale to DayButton component.</Step>

Update the `DayButton` component usage to pass the `locale` prop:

```diff
      components={{
        ...
-       DayButton: CalendarDayButton,
+       DayButton: ({ ...props }) => (
+         <CalendarDayButton locale={locale} {...props} />
+       ),
        ...
      }}
```

<Step>Update RTL-aware CSS classes.</Step>

Replace directional classes with logical properties for better RTL support:

```diff
  // In the day classNames:
- [&:last-child[data-selected=true]_button]:rounded-r-(--cell-radius)
+ [&:last-child[data-selected=true]_button]:rounded-e-(--cell-radius)
- [&:nth-child(2)[data-selected=true]_button]:rounded-l-(--cell-radius)
+ [&:nth-child(2)[data-selected=true]_button]:rounded-s-(--cell-radius)
- [&:first-child[data-selected=true]_button]:rounded-l-(--cell-radius)
+ [&:first-child[data-selected=true]_button]:rounded-s-(--cell-radius)

  // In range_start classNames:
- rounded-l-(--cell-radius) ... after:right-0
+ rounded-s-(--cell-radius) ... after:end-0

  // In range_end classNames:
- rounded-r-(--cell-radius) ... after:left-0
+ rounded-e-(--cell-radius) ... after:start-0

  // In CalendarDayButton className:
- data-[range-end=true]:rounded-r-(--cell-radius)
+ data-[range-end=true]:rounded-e-(--cell-radius)
- data-[range-start=true]:rounded-l-(--cell-radius)
+ data-[range-start=true]:rounded-s-(--cell-radius)
```

</Steps>

After applying these changes, you can use the `locale` prop to provide locale-specific formatting:

```tsx
import { enUS } from "react-day-picker/locale"

;<Calendar mode="single" selected={date} onSelect={setDate} locale={enUS} />
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/card.mdx -->

## apps/v4/content/docs/components/base/card.mdx

---
title: Card
description: Displays a card with header, content, and footer.
base: base
component: true
---

<ComponentPreview
  name="card-demo"
  styleName="base-nova"
  previewClassName="h-[30rem]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add card
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="card"
  title="components/ui/card.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
```

```tsx showLineNumbers
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card Description</CardDescription>
    <CardAction>Card Action</CardAction>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
```

## Examples

### Size

Use the `size="sm"` prop to set the size of the card to small. The small size variant uses smaller spacing.

<ComponentPreview
  styleName="base-nova"
  name="card-small"
  previewClassName="h-96"
/>

### Image

Add an image before the card header to create a card with an image.

<ComponentPreview
  styleName="base-nova"
  name="card-image"
  previewClassName="h-[32rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="card-rtl"
  direction="rtl"
  previewClassName="h-[30rem]"
/>

## API Reference

### Card

The `Card` component is the root container for card content.

| Prop        | Type                | Default     |
| ----------- | ------------------- | ----------- |
| `size`      | `"default" \| "sm"` | `"default"` |
| `className` | `string`            | -           |

### CardHeader

The `CardHeader` component is used for a title, description, and optional action.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardTitle

The `CardTitle` component is used for the card title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardDescription

The `CardDescription` component is used for helper text under the title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardAction

The `CardAction` component places content in the top-right of the header (for example, a button or a badge).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardContent

The `CardContent` component is used for the main card body.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardFooter

The `CardFooter` component is used for actions and secondary content at the bottom of the card.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |


---

<!-- SOURCE: apps/v4/content/docs/components/base/carousel.mdx -->

## apps/v4/content/docs/components/base/carousel.mdx

---
title: Carousel
description: A carousel with motion and swipe built using Embla.
base: base
component: true
links:
  doc: https://www.embla-carousel.com/get-started/react
  api: https://www.embla-carousel.com/api
---

<ComponentPreview
  styleName="base-nova"
  name="carousel-demo"
  previewClassName="h-80 sm:h-[32rem]"
/>

## About

The carousel component is built using the [Embla Carousel](https://www.embla-carousel.com/) library.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add carousel
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install embla-carousel-react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="carousel"
  title="components/ui/carousel.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
```

```tsx showLineNumbers
<Carousel>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
  <CarouselPrevious />
  <CarouselNext />
</Carousel>
```

## Examples

### Sizes

To set the size of the items, you can use the `basis` utility class on the `<CarouselItem />`.

<ComponentPreview styleName="base-nova" name="carousel-size" />

```tsx showLineNumbers {4-6}
// 33% of the carousel width.
<Carousel>
  <CarouselContent>
    <CarouselItem className="basis-1/3">...</CarouselItem>
    <CarouselItem className="basis-1/3">...</CarouselItem>
    <CarouselItem className="basis-1/3">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

```tsx showLineNumbers {4-6}
// 50% on small screens and 33% on larger screens.
<Carousel>
  <CarouselContent>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

### Spacing

To set the spacing between the items, we use a `pl-[VALUE]` utility on the `<CarouselItem />` and a negative `-ml-[VALUE]` on the `<CarouselContent />`.

<ComponentPreview styleName="base-nova" name="carousel-spacing" />

```tsx showLineNumbers /-ml-4/ /pl-4/
<Carousel>
  <CarouselContent className="-ml-4">
    <CarouselItem className="pl-4">...</CarouselItem>
    <CarouselItem className="pl-4">...</CarouselItem>
    <CarouselItem className="pl-4">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

```tsx showLineNumbers /-ml-2/ /pl-2/ /md:-ml-4/ /md:pl-4/
<Carousel>
  <CarouselContent className="-ml-2 md:-ml-4">
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

### Orientation

Use the `orientation` prop to set the orientation of the carousel.

<ComponentPreview
  styleName="base-nova"
  name="carousel-orientation"
  previewClassName="h-[32rem]"
/>

```tsx showLineNumbers /vertical | horizontal/
<Carousel orientation="vertical | horizontal">
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
</Carousel>
```

## Options

You can pass options to the carousel using the `opts` prop. See the [Embla Carousel docs](https://www.embla-carousel.com/api/options/) for more information.

```tsx showLineNumbers {2-5}
<Carousel
  opts={{
    align: "start",
    loop: true,
  }}
>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
</Carousel>
```

## API

Use a state and the `setApi` prop to get an instance of the carousel API.

<ComponentPreview
  styleName="base-nova"
  name="carousel-api"
  previewClassName="sm:h-[32rem]"
/>

```tsx showLineNumbers {1,4,22}
import { type CarouselApi } from "@/components/ui/carousel"

export function Example() {
  const [api, setApi] = React.useState<CarouselApi>()
  const [current, setCurrent] = React.useState(0)
  const [count, setCount] = React.useState(0)

  React.useEffect(() => {
    if (!api) {
      return
    }

    setCount(api.scrollSnapList().length)
    setCurrent(api.selectedScrollSnap() + 1)

    api.on("select", () => {
      setCurrent(api.selectedScrollSnap() + 1)
    })
  }, [api])

  return (
    <Carousel setApi={setApi}>
      <CarouselContent>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
      </CarouselContent>
    </Carousel>
  )
}
```

## Events

You can listen to events using the api instance from `setApi`.

```tsx showLineNumbers {1,4-14,16}
import { type CarouselApi } from "@/components/ui/carousel"

export function Example() {
  const [api, setApi] = React.useState<CarouselApi>()

  React.useEffect(() => {
    if (!api) {
      return
    }

    api.on("select", () => {
      // Do something on select.
    })
  }, [api])

  return (
    <Carousel setApi={setApi}>
      <CarouselContent>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
      </CarouselContent>
    </Carousel>
  )
}
```

See the [Embla Carousel docs](https://www.embla-carousel.com/api/events/) for more information on using events.

## Plugins

You can use the `plugins` prop to add plugins to the carousel.

```ts showLineNumbers {1,6-10}
import Autoplay from "embla-carousel-autoplay"

export function Example() {
  return (
    <Carousel
      plugins={[
        Autoplay({
          delay: 2000,
        }),
      ]}
    >
      // ...
    </Carousel>
  )
}
```

<ComponentPreview
  styleName="base-nova"
  name="carousel-plugin"
  previewClassName="sm:h-[32rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="carousel-rtl"
  direction="rtl"
  previewClassName="h-80 sm:h-[32rem]"
/>

When localizing the carousel for RTL languages, you need to set the `direction` option in the `opts` prop to match the text direction. This ensures the carousel scrolls in the correct direction.

```tsx showLineNumbers {2-5}
<Carousel
  dir={dir}
  opts={{
    direction: dir,
  }}
>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
  <CarouselPrevious className="rtl:rotate-180" />
  <CarouselNext className="rtl:rotate-180" />
</Carousel>
```

The `direction` option accepts `"ltr"` or `"rtl"` and should match the `dir` prop value. You may also want to rotate the navigation buttons using the `rtl:rotate-180` class to ensure they point in the correct direction.

## API Reference

See the [Embla Carousel docs](https://www.embla-carousel.com/api/) for more information on props and plugins.


---

<!-- SOURCE: apps/v4/content/docs/components/base/chart.mdx -->

## apps/v4/content/docs/components/base/chart.mdx

---
title: Chart
description: Beautiful charts. Built using Recharts. Copy and paste into your apps.
base: base
component: true
---

<Callout className="mt-4">

**Updated:** The `chart` component now uses Recharts v3. If you're upgrading existing chart code, see [Updating to Recharts v3](#updating-to-recharts-v3).

</Callout>

<ComponentPreview
  styleName="base-nova"
  name="chart-demo"
  className="theme-blue [&_.preview]:h-auto [&_.preview]:p-0 [&_.preview]:lg:min-h-[404px] [&_.preview>div]:w-full [&_.preview>div]:border-none [&_.preview>div]:shadow-none"
  hideCode
/>

Introducing **Charts**. A collection of chart components that you can copy and paste into your apps.

Charts are designed to look great out of the box. They work well with the other components and are fully customizable to fit your project.

[Browse the Charts Library](/charts).

## Component

We use [Recharts](https://recharts.org/) under the hood.

We designed the `chart` component with composition in mind. **You build your charts using Recharts components and only bring in custom components, such as `ChartTooltip`, when and where you need it**.

```tsx showLineNumbers /ChartContainer/ /ChartTooltipContent/
import { Bar, BarChart } from "recharts"

import { ChartContainer, ChartTooltipContent } from "@/components/ui/chart"

export function MyChart() {
  return (
    <ChartContainer>
      <BarChart data={data}>
        <Bar dataKey="value" />
        <ChartTooltip content={<ChartTooltipContent />} />
      </BarChart>
    </ChartContainer>
  )
}
```

We do not wrap Recharts. This means you're not locked into an abstraction. When a new Recharts version is released, you can follow the official upgrade path to upgrade your charts.

**The components are yours**.

## Updating to Recharts v3

If you're updating older chart code to Recharts v3:

- Use `var(--chart-1)` instead of `hsl(var(--chart-1))` when you reference chart tokens from your CSS variables.
- Use `ChartTooltip.defaultIndex` for initial tooltip state only. Keep persistent active shapes in your own chart state.
- Remove `layout` from `<Bar>` when the parent `<BarChart>` already defines it.
- Keep a height, `min-h-*`, or `aspect-*` on `ChartContainer` so `ResponsiveContainer` can measure on first render.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add chart
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install recharts
```

<Step>Copy and paste the following code into `components/ui/chart.tsx`.</Step>

<ComponentSource
  name="chart"
  title="components/ui/chart.tsx"
  styleName="base-nova"
/>

<Step>Add the following colors to your CSS file</Step>

```css title="app/globals.css" showLineNumbers
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
    --chart-3: oklch(0.398 0.07 227.392);
    --chart-4: oklch(0.828 0.189 84.429);
    --chart-5: oklch(0.769 0.188 70.08);
  }

  .dark {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
    --chart-3: oklch(0.769 0.188 70.08);
    --chart-4: oklch(0.627 0.265 303.9);
    --chart-5: oklch(0.645 0.246 16.439);
  }
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Your First Chart

Let's build your first chart. We'll build a bar chart, add a grid, axis, tooltip and legend.

<Steps>

<Step>Start by defining your data</Step>

The following data represents the number of desktop and mobile users for each month.

<Callout className="mt-4">

**Note:** Your data can be in any shape. You are not limited to the shape of the data below. Use the `dataKey` prop to map your data to the chart.

</Callout>

```tsx title="components/example-chart.tsx" showLineNumbers
const chartData = [
  { month: "January", desktop: 186, mobile: 80 },
  { month: "February", desktop: 305, mobile: 200 },
  { month: "March", desktop: 237, mobile: 120 },
  { month: "April", desktop: 73, mobile: 190 },
  { month: "May", desktop: 209, mobile: 130 },
  { month: "June", desktop: 214, mobile: 140 },
]
```

<Step>Define your chart config</Step>

The chart config holds configuration for the chart. This is where you place human-readable strings, such as labels, icons and color tokens for theming.

```tsx title="components/example-chart.tsx" showLineNumbers
import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
  mobile: {
    label: "Mobile",
    color: "#60a5fa",
  },
} satisfies ChartConfig
```

<Step>Build your chart</Step>

You can now build your chart using Recharts components.

<Callout className="mt-4 bg-amber-50 border-amber-200 dark:bg-amber-950/50 dark:border-amber-950">

**Important:** Remember to set a `min-h-[VALUE]` on the `ChartContainer` component. This is required for the chart to be responsive.

</Callout>

<ComponentPreview
  styleName="base-nova"
  name="chart-example"
  previewClassName="h-80"
/>

</Steps>

### Add a Grid

Let's add a grid to the chart.

<Steps className="mb-0 pt-2">

<Step>Import the `CartesianGrid` component.</Step>

```tsx /CartesianGrid/
import { Bar, BarChart, CartesianGrid } from "recharts"
```

<Step>Add the `CartesianGrid` component to your chart.</Step>

```tsx showLineNumbers {3}
<ChartContainer config={chartConfig} className="min-h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="base-nova"
  name="chart-example-grid"
  previewClassName="h-80"
/>

</Steps>

### Add an Axis

To add an x-axis to the chart, we'll use the `XAxis` component.

<Steps className="mb-0 pt-2">

<Step>Import the `XAxis` component.</Step>

```tsx /XAxis/
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"
```

<Step>Add the `XAxis` component to your chart.</Step>

```tsx showLineNumbers {4-10}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="base-nova"
  name="chart-example-axis"
  previewClassName="h-80"
/>

</Steps>

### Add Tooltip

So far we've only used components from Recharts. They look great out of the box thanks to some customization in the `chart` component.

To add a tooltip, we'll use the custom `ChartTooltip` and `ChartTooltipContent` components from `chart`.

<Steps className="mb-0 pt-2">

<Step>Import the `ChartTooltip` and `ChartTooltipContent` components.</Step>

```tsx
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

<Step>Add the components to your chart.</Step>

```tsx showLineNumbers {11}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="base-nova"
  name="chart-example-tooltip"
  previewClassName="h-80"
/>

Hover to see the tooltips. Easy, right? Two components, and we've got a beautiful tooltip.

</Steps>

### Add Legend

We'll do the same for the legend. We'll use the `ChartLegend` and `ChartLegendContent` components from `chart`.

<Steps className="mb-0 pt-2">

<Step>Import the `ChartLegend` and `ChartLegendContent` components.</Step>

```tsx
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

<Step>Add the components to your chart.</Step>

```tsx showLineNumbers {12}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <ChartLegend content={<ChartLegendContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="base-nova"
  name="chart-example-legend"
  previewClassName="h-80"
/>

</Steps>

Done. You've built your first chart! What's next?

- [Themes and Colors](/docs/components/chart#theming)
- [Tooltip](/docs/components/chart#tooltip)
- [Legend](/docs/components/chart#legend)

## Chart Config

The chart config is where you define the labels, icons and colors for a chart.

It is intentionally decoupled from chart data.

This allows you to share config and color tokens between charts. It can also work independently for cases where your data or color tokens live remotely or in a different format.

```tsx showLineNumbers /ChartConfig/
import { Monitor } from "lucide-react"

import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    icon: Monitor,
    // A color like 'hsl(220, 98%, 61%)' or 'var(--color-name)'
    color: "#2563eb",
    // OR a theme object with 'light' and 'dark' keys
    theme: {
      light: "#2563eb",
      dark: "#dc2626",
    },
  },
} satisfies ChartConfig
```

## Theming

Charts have built-in support for theming. You can use css variables (recommended) or color values in any color format, such as hex, hsl or oklch.

### CSS Variables

<Steps className="mb-0 pt-2">

<Step>Define your colors in your css file</Step>

```css title="app/globals.css" showLineNumbers
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
  }

  .dark {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
  }
}
```

<Step>Add the color to your `chartConfig`</Step>

```tsx title="components/example-chart.tsx" showLineNumbers
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

</Steps>

### hex, hsl or oklch

You can also define your colors directly in the chart config. Use the color format you prefer.

```tsx title="components/example-chart.tsx" showLineNumbers
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
  mobile: {
    label: "Mobile",
    color: "hsl(220, 98%, 61%)",
  },
  tablet: {
    label: "Tablet",
    color: "oklch(0.5 0.2 240)",
  },
  laptop: {
    label: "Laptop",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

### Using Colors

To use the theme colors in your chart, reference the colors using the format `var(--color-KEY)`.

#### Components

```tsx
<Bar dataKey="desktop" fill="var(--color-desktop)" />
```

#### Chart Data

```tsx title="components/example-chart.tsx" showLineNumbers
const chartData = [
  { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]
```

#### Tailwind

```tsx title="components/example-chart.tsx"
<LabelList className="fill-(--color-desktop)" />
```

## Tooltip

A chart tooltip contains a label, name, indicator and value. You can use a combination of these to customize your tooltip.

<ComponentPreview styleName="base-nova" name="chart-tooltip" hideCode />

You can turn on/off any of these using the `hideLabel`, `hideIndicator` props and customize the indicator style using the `indicator` prop.

Use `labelKey` and `nameKey` to use a custom key for the tooltip label and name.

Chart comes with the `<ChartTooltip>` and `<ChartTooltipContent>` components. You can use these two components to add custom tooltips to your chart.

```tsx title="components/example-chart.tsx"
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

```tsx title="components/example-chart.tsx"
<ChartTooltip content={<ChartTooltipContent />} />
```

### Props

Use the following props to customize the tooltip.

| Prop            | Type                     | Description                                  |
| :-------------- | :----------------------- | :------------------------------------------- |
| `labelKey`      | string                   | The config or data key to use for the label. |
| `nameKey`       | string                   | The config or data key to use for the name.  |
| `indicator`     | `dot` `line` or `dashed` | The indicator style for the tooltip.         |
| `hideLabel`     | boolean                  | Whether to hide the label.                   |
| `hideIndicator` | boolean                  | Whether to hide the indicator.               |

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for tooltip label and names, use the `labelKey` and `nameKey` props.

```tsx showLineNumbers /browser/
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  visitors: {
    label: "Total Visitors",
  },
  chrome: {
    label: "Chrome",
    color: "var(--chart-1)",
  },
  safari: {
    label: "Safari",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

```tsx title="components/example-chart.tsx"
<ChartTooltip
  content={<ChartTooltipContent labelKey="visitors" nameKey="browser" />}
/>
```

This will use `Total Visitors` for label and `Chrome` and `Safari` for the tooltip names.

## Legend

You can use the custom `<ChartLegend>` and `<ChartLegendContent>` components to add a legend to your chart.

```tsx title="components/example-chart.tsx"
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

```tsx title="components/example-chart.tsx"
<ChartLegend content={<ChartLegendContent />} />
```

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for legend names, use the `nameKey` prop.

```tsx showLineNumbers /browser/
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  chrome: {
    label: "Chrome",
    color: "var(--chart-1)",
  },
  safari: {
    label: "Safari",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

```tsx title="components/example-chart.tsx"
<ChartLegend content={<ChartLegendContent nameKey="browser" />} />
```

This will use `Chrome` and `Safari` for the legend names.

## Accessibility

You can turn on the `accessibilityLayer` prop to add an accessible layer to your chart.

This prop adds keyboard access and screen reader support to your charts.

```tsx title="components/example-chart.tsx"
<LineChart accessibilityLayer />
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="chart-rtl"
  direction="rtl"
  previewClassName="h-92"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/base/checkbox.mdx -->

## apps/v4/content/docs/components/base/checkbox.mdx

---
title: Checkbox
description: A control that allows the user to toggle between checked and not checked.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/checkbox
  api: https://base-ui.com/react/components/checkbox#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="checkbox-demo"
  previewClassName="h-80"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add checkbox
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="checkbox"
  title="components/ui/checkbox.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Checkbox } from "@/components/ui/checkbox"
```

```tsx
<Checkbox />
```

## Checked State

Use `defaultChecked` for uncontrolled checkboxes, or `checked` and
`onCheckedChange` to control the state.

```tsx showLineNumbers
import * as React from "react"

export function Example() {
  const [checked, setChecked] = React.useState(false)

  return <Checkbox checked={checked} onCheckedChange={setChecked} />
}
```

## Invalid State

Set `aria-invalid` on the checkbox and `data-invalid` on the field wrapper to
show the invalid styles.

<ComponentPreview styleName="base-nova" name="checkbox-invalid" />

## Examples

### Basic

Pair the checkbox with `Field` and `FieldLabel` for proper layout and labeling.

<ComponentPreview styleName="base-nova" name="checkbox-basic" />

### Description

Use `FieldContent` and `FieldDescription` for helper text.

<ComponentPreview styleName="base-nova" name="checkbox-description" />

### Disabled

Use the `disabled` prop to prevent interaction and add the `data-disabled` attribute to the `<Field>` component for disabled styles.

<ComponentPreview styleName="base-nova" name="checkbox-disabled" />

### Group

Use multiple fields to create a checkbox list.

<ComponentPreview styleName="base-nova" name="checkbox-group" />

### Table

<ComponentPreview
  styleName="base-nova"
  name="checkbox-table"
  previewClassName="p-4 md:p-8"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="checkbox-rtl"
  direction="rtl"
  previewClassName="h-80"
/>

## API Reference

See the [Base UI](https://base-ui.com/react/components/checkbox#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/collapsible.mdx -->

## apps/v4/content/docs/components/base/collapsible.mdx

---
title: Collapsible
description: An interactive component which expands/collapses a panel.
base: base
component: true
featured: true
links:
  doc: https://base-ui.com/react/components/collapsible
  api: https://base-ui.com/react/components/collapsible#api-reference
---

<ComponentPreview styleName="base-nova" name="collapsible-demo" align="start" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add collapsible
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="collapsible"
  title="components/ui/collapsible.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
```

```tsx showLineNumbers
<Collapsible>
  <CollapsibleTrigger>Can I use this in my project?</CollapsibleTrigger>
  <CollapsibleContent>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </CollapsibleContent>
</Collapsible>
```

## Controlled State

Use the `open` and `onOpenChange` props to control the state.

```tsx showLineNumbers
import * as React from "react"

export function Example() {
  const [open, setOpen] = React.useState(false)

  return (
    <Collapsible open={open} onOpenChange={setOpen}>
      <CollapsibleTrigger>Toggle</CollapsibleTrigger>
      <CollapsibleContent>Content</CollapsibleContent>
    </Collapsible>
  )
}
```

## Examples

### Basic

<ComponentPreview
  styleName="base-nova"
  name="collapsible-basic"
  align="start"
/>

### Settings Panel

Use a trigger button to reveal additional settings.

<ComponentPreview styleName="base-nova" name="collapsible-settings" />

### File Tree

Use nested collapsibles to build a file tree.

<ComponentPreview
  styleName="base-nova"
  name="collapsible-file-tree"
  previewClassName="h-[36rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="collapsible-rtl"
  direction="rtl"
  align="start"
/>

## API Reference

See the [Base UI](https://base-ui.com/react/components/collapsible#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/combobox.mdx -->

## apps/v4/content/docs/components/base/combobox.mdx

---
title: Combobox
description: Autocomplete input with a list of suggestions.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/combobox
  api: https://base-ui.com/react/components/combobox#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="combobox-demo"
  description="A combobox with a list of frameworks."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add combobox
```

</TabsContent>
<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="combobox"
  title="components/ui/combobox.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"
```

```tsx showLineNumbers
const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

export function ExampleCombobox() {
  return (
    <Combobox items={frameworks}>
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(item) => (
            <ComboboxItem key={item} value={item}>
              {item}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Custom Items

Use `itemToStringValue` when your items are objects.

```tsx showLineNumbers
import * as React from "react"

import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"

type Framework = {
  label: string
  value: string
}

const frameworks: Framework[] = [
  { label: "Next.js", value: "next" },
  { label: "SvelteKit", value: "sveltekit" },
  { label: "Nuxt", value: "nuxt" },
]

export function ExampleComboboxCustomItems() {
  return (
    <Combobox
      items={frameworks}
      itemToStringValue={(framework) => framework.label}
    >
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(framework) => (
            <ComboboxItem key={framework.value} value={framework}>
              {framework.label}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Multiple Selection

Use `multiple` with chips for multi-select behavior.

```tsx showLineNumbers
import * as React from "react"

import {
  Combobox,
  ComboboxChip,
  ComboboxChips,
  ComboboxChipsInput,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
  ComboboxValue,
} from "@/components/ui/combobox"

const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

export function ExampleComboboxMultiple() {
  const [value, setValue] = React.useState<string[]>([])

  return (
    <Combobox
      items={frameworks}
      multiple
      value={value}
      onValueChange={setValue}
    >
      <ComboboxChips>
        <ComboboxValue>
          {value.map((item) => (
            <ComboboxChip key={item}>{item}</ComboboxChip>
          ))}
        </ComboboxValue>
        <ComboboxChipsInput placeholder="Add framework" />
      </ComboboxChips>
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(item) => (
            <ComboboxItem key={item} value={item}>
              {item}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Examples

### Basic

A simple combobox with a list of frameworks.

<ComponentPreview styleName="base-nova" name="combobox-basic" />

### Multiple

A combobox with multiple selection using `multiple` and `ComboboxChips`.

<ComponentPreview styleName="base-nova" name="combobox-multiple" />

### Clear Button

Use the `showClear` prop to show a clear button.

<ComponentPreview styleName="base-nova" name="combobox-clear" />

### Groups

Use `ComboboxGroup` and `ComboboxSeparator` to group items.

<ComponentPreview styleName="base-nova" name="combobox-groups" />

### Custom Items

You can render a custom component inside `ComboboxItem`.

<ComponentPreview styleName="base-nova" name="combobox-custom" />

### Invalid

Use the `aria-invalid` prop to make the combobox invalid.

<ComponentPreview styleName="base-nova" name="combobox-invalid" />

### Disabled

Use the `disabled` prop to disable the combobox.

<ComponentPreview styleName="base-nova" name="combobox-disabled" />

### Auto Highlight

Use the `autoHighlight` prop to automatically highlight the first item on filter.

<ComponentPreview styleName="base-nova" name="combobox-auto-highlight" />

### Popup

You can trigger the combobox from a button or any other component by using the `render` prop. Move the `ComboboxInput` inside the `ComboboxContent`.

<ComponentPreview styleName="base-nova" name="combobox-popup" />

### Input Group

You can add an addon to the combobox by using the `InputGroupAddon` component inside the `ComboboxInput`.

<ComponentPreview styleName="base-nova" name="combobox-input-group" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="combobox-rtl"
  direction="rtl"
  align="start"
/>

## API Reference

See the [Base UI](https://base-ui.com/react/components/combobox#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/command.mdx -->

## apps/v4/content/docs/components/base/command.mdx

---
title: Command
description: Command menu for search and quick actions.
base: base
component: true
links:
  doc: https://github.com/dip/cmdk
---

<ComponentPreview
  styleName="base-nova"
  name="command-demo"
  align="start"
  previewClassName="h-[24.5rem]"
/>

## About

The `<Command />` component uses the [`cmdk`](https://github.com/dip/cmdk) component by [Dip](https://www.dip.org/).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add command
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install cmdk
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="command"
  title="components/ui/command.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
```

```tsx showLineNumbers
<Command className="max-w-sm rounded-lg border">
  <CommandInput placeholder="Type a command or search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
    <CommandSeparator />
    <CommandGroup heading="Settings">
      <CommandItem>Profile</CommandItem>
      <CommandItem>Billing</CommandItem>
      <CommandItem>Settings</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

## Examples

### Basic

A simple command menu in a dialog.

<ComponentPreview styleName="base-nova" name="command-basic" />

### Shortcuts

<ComponentPreview styleName="base-nova" name="command-shortcuts" />

### Groups

A command menu with groups, icons and separators.

<ComponentPreview styleName="base-nova" name="command-groups" />

### Scrollable

Scrollable command menu with multiple items.

<ComponentPreview styleName="base-nova" name="command-scrollable" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="command-rtl"
  direction="rtl"
  align="start"
  previewClassName="h-[24.5rem]"
/>

## API Reference

See the [cmdk](https://github.com/dip/cmdk) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/context-menu.mdx -->

## apps/v4/content/docs/components/base/context-menu.mdx

---
title: Context Menu
description: Displays a menu of actions triggered by a right click.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/context-menu
  api: https://base-ui.com/react/components/context-menu#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="context-menu-demo"
  description="A context menu with sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add context-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="context-menu"
  title="components/ui/context-menu.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
```

```tsx showLineNumbers
<ContextMenu>
  <ContextMenuTrigger>Right click here</ContextMenuTrigger>
  <ContextMenuContent>
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenuContent>
</ContextMenu>
```

## Examples

### Basic

A simple context menu with a few actions.

<ComponentPreview styleName="base-nova" name="context-menu-basic" />

### Submenu

Use `ContextMenuSub` to nest secondary actions.

<ComponentPreview styleName="base-nova" name="context-menu-submenu" />

### Shortcuts

Add `ContextMenuShortcut` to show keyboard hints.

<ComponentPreview styleName="base-nova" name="context-menu-shortcuts" />

### Groups

Group related actions and separate them with dividers.

<ComponentPreview styleName="base-nova" name="context-menu-groups" />

### Icons

Combine icons with labels for quick scanning.

<ComponentPreview styleName="base-nova" name="context-menu-icons" />

### Checkboxes

Use `ContextMenuCheckboxItem` for toggles.

<ComponentPreview styleName="base-nova" name="context-menu-checkboxes" />

### Radio

Use `ContextMenuRadioItem` for exclusive choices.

<ComponentPreview styleName="base-nova" name="context-menu-radio" />

### Destructive

Use `variant="destructive"` to style the menu item as destructive.

<ComponentPreview styleName="base-nova" name="context-menu-destructive" />

### Sides

Control submenu placement with side and align props.

<ComponentPreview styleName="base-nova" name="context-menu-sides" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="context-menu-rtl"
  direction="rtl"
/>

Use `side="inline-end"` to place the menu on the logical right side of the trigger.

```tsx showLineNumbers
<ContextMenu>
  <ContextMenuTrigger>Right click here</ContextMenuTrigger>
  <ContextMenuContent side="inline-end">
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenuContent>
</ContextMenu>
```

## API Reference

See the [Base UI](https://base-ui.com/react/components/context-menu#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/data-table.mdx -->

## apps/v4/content/docs/components/base/data-table.mdx

---
title: Data Table
description: Powerful table and datagrids built using TanStack Table.
base: base
component: true
links:
  doc: https://tanstack.com/table/v8/docs/introduction
---

<ComponentPreview
  styleName="radix-nova"
  name="data-table-demo"
  align="start"
  previewClassName="items-start h-auto px-4 md:px-8"
  hideCode
/>

## Introduction

Every data table or datagrid I've created has been unique. They all behave differently, have specific sorting and filtering requirements, and work with different data sources.

It doesn't make sense to combine all of these variations into a single component. If we do that, we'll lose the flexibility that [headless UI](https://tanstack.com/table/v8/docs/introduction#what-is-headless-ui) provides.

So instead of a data-table component, I thought it would be more helpful to provide a guide on how to build your own.

We'll start with the basic `<Table />` component and build a complex data table from scratch.

<Callout className="mt-4">

**Tip:** If you find yourself using the same table in multiple places in your app, you can always extract it into a reusable component.

</Callout>

## Table of Contents

This guide will show you how to use [TanStack Table](https://tanstack.com/table) and the `<Table />` component to build your own custom data table. We'll cover the following topics:

- [Basic Table](#basic-table)
- [Row Actions](#row-actions)
- [Pagination](#pagination)
- [Sorting](#sorting)
- [Filtering](#filtering)
- [Visibility](#visibility)
- [Row Selection](#row-selection)
- [Reusable Components](#reusable-components)

## Installation

1. Add the `<Table />` component to your project:

```bash
npx shadcn@latest add table
```

2. Add `tanstack/react-table` dependency:

```bash
npm install @tanstack/react-table
```

## Prerequisites

We are going to build a table to show recent payments. Here's what our data looks like:

```tsx showLineNumbers
type Payment = {
  id: string
  amount: number
  status: "pending" | "processing" | "success" | "failed"
  email: string
}

export const payments: Payment[] = [
  {
    id: "728ed52f",
    amount: 100,
    status: "pending",
    email: "m@example.com",
  },
  {
    id: "489e1d42",
    amount: 125,
    status: "processing",
    email: "example@gmail.com",
  },
  // ...
]
```

## Project Structure

Start by creating the following file structure:

```txt
app
└── payments
    ├── columns.tsx
    ├── data-table.tsx
    └── page.tsx
```

I'm using a Next.js example here but this works for any other React framework.

- `columns.tsx` (client component) will contain our column definitions.
- `data-table.tsx` (client component) will contain our `<DataTable />` component.
- `page.tsx` (server component) is where we'll fetch data and render our table.

## Basic Table

Let's start by building a basic table.

<Steps className="mb-0 pt-2">

### Column Definitions

First, we'll define our columns.

```tsx showLineNumbers title="app/payments/columns.tsx" {3,14-27}
"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Payment = {
  id: string
  amount: number
  status: "pending" | "processing" | "success" | "failed"
  email: string
}

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "status",
    header: "Status",
  },
  {
    accessorKey: "email",
    header: "Email",
  },
  {
    accessorKey: "amount",
    header: "Amount",
  },
]
```

<Callout className="mt-4">

**Note:** Columns are where you define the core of what your table
will look like. They define the data that will be displayed, how it will be
formatted, sorted and filtered.

</Callout>

### `<DataTable />` component

Next, we'll create a `<DataTable />` component to render our table.

```tsx showLineNumbers title="app/payments/data-table.tsx"
"use client"

import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
} from "@tanstack/react-table"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  })

  return (
    <div className="overflow-hidden rounded-md border">
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map((headerGroup) => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map((header) => {
                return (
                  <TableHead key={header.id}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                  </TableHead>
                )
              })}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows?.length ? (
            table.getRowModel().rows.map((row) => (
              <TableRow
                key={row.id}
                data-state={row.getIsSelected() && "selected"}
              >
                {row.getVisibleCells().map((cell) => (
                  <TableCell key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </TableCell>
                ))}
              </TableRow>
            ))
          ) : (
            <TableRow>
              <TableCell colSpan={columns.length} className="h-24 text-center">
                No results.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </div>
  )
}
```

<Callout>

**Tip**: If you find yourself using `<DataTable />` in multiple places, this is the component you could make reusable by extracting it to `components/ui/data-table.tsx`.

`<DataTable columns={columns} data={data} />`

</Callout>

### Render the table

Finally, we'll render our table in our page component.

```tsx showLineNumbers title="app/payments/page.tsx" {22}
import { columns, Payment } from "./columns"
import { DataTable } from "./data-table"

async function getData(): Promise<Payment[]> {
  // Fetch data from your API here.
  return [
    {
      id: "728ed52f",
      amount: 100,
      status: "pending",
      email: "m@example.com",
    },
    // ...
  ]
}

export default async function DemoPage() {
  const data = await getData()

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  )
}
```

</Steps>

## Cell Formatting

Let's format the amount cell to display the dollar amount. We'll also align the cell to the right.

<Steps className="mb-0 pt-2">

### Update columns definition

Update the `header` and `cell` definitions for amount as follows:

```tsx showLineNumbers title="app/payments/columns.tsx" {4-15}
export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "amount",
    header: () => <div className="text-right">Amount</div>,
    cell: ({ row }) => {
      const amount = parseFloat(row.getValue("amount"))
      const formatted = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
      }).format(amount)

      return <div className="text-right font-medium">{formatted}</div>
    },
  },
]
```

You can use the same approach to format other cells and headers.

</Steps>

## Row Actions

Let's add row actions to our table. We'll use a `<DropdownMenu />` component for this.

<Steps className="mb-0 pt-2">

### Update columns definition

Update our columns definition to add a new `actions` column. The `actions` cell returns a `<DropdownMenu />` component.

```tsx showLineNumbers title="app/payments/columns.tsx" {4,6-14,18-45}
"use client"

import { ColumnDef } from "@tanstack/react-table"
import { MoreHorizontal } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export const columns: ColumnDef<Payment>[] = [
  // ...
  {
    id: "actions",
    cell: ({ row }) => {
      const payment = row.original

      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="h-8 w-8 p-0">
              <span className="sr-only">Open menu</span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuLabel>Actions</DropdownMenuLabel>
            <DropdownMenuItem
              onClick={() => navigator.clipboard.writeText(payment.id)}
            >
              Copy payment ID
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>View customer</DropdownMenuItem>
            <DropdownMenuItem>View payment details</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      )
    },
  },
  // ...
]
```

You can access the row data using `row.original` in the `cell` function. Use this to handle actions for your row eg. use the `id` to make a DELETE call to your API.

</Steps>

## Pagination

Next, we'll add pagination to our table.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {5,17}
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  useReactTable,
} from "@tanstack/react-table"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  // ...
}
```

This will automatically paginate your rows into pages of 10. See the [pagination docs](https://tanstack.com/table/v8/docs/api/features/pagination) for more information on customizing page size and implementing manual pagination.

### Add pagination controls

We can add pagination controls to our table using the `<Button />` component and the `table.previousPage()`, `table.nextPage()` API methods.

```tsx showLineNumbers title="app/payments/data-table.tsx" {1,15,21-39}
import { Button } from "@/components/ui/button"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table>
          { // .... }
        </Table>
      </div>
      <div className="flex items-center justify-end space-x-2 py-4">
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
        >
          Previous
        </Button>
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
        >
          Next
        </Button>
      </div>
    </div>
  )
}
```

See [Reusable Components](#reusable-components) section for a more advanced pagination component.

</Steps>

## Sorting

Let's make the email column sortable.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {3,6,10,18,25-29}
"use client"

import * as React from "react"
import {
  ColumnDef,
  SortingState,
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onSortingChange: setSorting,
    getSortedRowModel: getSortedRowModel(),
    state: {
      sorting,
    },
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

### Make header cell sortable

We can now update the `email` header cell to add sorting controls.

```tsx showLineNumbers title="app/payments/columns.tsx" {4,9-19}
"use client"

import { ColumnDef } from "@tanstack/react-table"
import { ArrowUpDown } from "lucide-react"

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "email",
    header: ({ column }) => {
      return (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Email
          <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
      )
    },
  },
]
```

This will automatically sort the table (asc and desc) when the user toggles on the header cell.

</Steps>

## Filtering

Let's add a search input to filter emails in our table.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {6,10,17,24-26,35-36,39,45-54}
"use client"

import * as React from "react"
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    onColumnFiltersChange: setColumnFilters,
    getFilteredRowModel: getFilteredRowModel(),
    state: {
      sorting,
      columnFilters,
    },
  })

  return (
    <div>
      <div className="flex items-center py-4">
        <Input
          placeholder="Filter emails..."
          value={(table.getColumn("email")?.getFilterValue() as string) ?? ""}
          onChange={(event) =>
            table.getColumn("email")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
      </div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

Filtering is now enabled for the `email` column. You can add filters to other columns as well. See the [filtering docs](https://tanstack.com/table/v8/docs/guide/filters) for more information on customizing filters.

</Steps>

## Visibility

Adding column visibility is fairly simple using `@tanstack/react-table` visibility API.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {8,18-23,33-34,45,49,64-91}
"use client"

import * as React from "react"
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({})

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
    },
  })

  return (
    <div>
      <div className="flex items-center py-4">
        <Input
          placeholder="Filter emails..."
          value={table.getColumn("email")?.getFilterValue() as string}
          onChange={(event) =>
            table.getColumn("email")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" className="ml-auto">
              Columns
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {table
              .getAllColumns()
              .filter(
                (column) => column.getCanHide()
              )
              .map((column) => {
                return (
                  <DropdownMenuCheckboxItem
                    key={column.id}
                    className="capitalize"
                    checked={column.getIsVisible()}
                    onCheckedChange={(value) =>
                      column.toggleVisibility(!!value)
                    }
                  >
                    {column.id}
                  </DropdownMenuCheckboxItem>
                )
              })}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

This adds a dropdown menu that you can use to toggle column visibility.

</Steps>

## Row Selection

Next, we're going to add row selection to our table.

<Steps className="mb-0 pt-2">

### Update column definitions

```tsx showLineNumbers title="app/payments/columns.tsx" {6,9-27}
"use client"

import { ColumnDef } from "@tanstack/react-table"

import { Badge } from "@/components/ui/badge"
import { Checkbox } from "@/components/ui/checkbox"

export const columns: ColumnDef<Payment>[] = [
  {
    id: "select",
    header: ({ table }) => (
      <Checkbox
        checked={
          table.getIsAllPageRowsSelected() ||
          (table.getIsSomePageRowsSelected() && "indeterminate")
        }
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
        aria-label="Select all"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(!!value)}
        aria-label="Select row"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },
]
```

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {11,23,28}
export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({})
  const [rowSelection, setRowSelection] = React.useState({})

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange: setRowSelection,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
      rowSelection,
    },
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table />
      </div>
    </div>
  )
}
```

This adds a checkbox to each row and a checkbox in the header to select all rows.

### Show selected rows

You can show the number of selected rows using the `table.getFilteredSelectedRowModel()` API.

```tsx
<div className="flex-1 text-sm text-muted-foreground">
  {table.getFilteredSelectedRowModel().rows.length} of{" "}
  {table.getFilteredRowModel().rows.length} row(s) selected.
</div>
```

</Steps>

## Reusable Components

Here are some components you can use to build your data tables. This is from the [Tasks](/examples/tasks) demo.

### Column header

Make any column header sortable and hideable.

<ComponentSource
  src="/app/(app)/examples/tasks/components/data-table-column-header.tsx"
  title="components/data-table-column-header.tsx"
/>

```tsx showLineNumbers {5}
export const columns = [
  {
    accessorKey: "email",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Email" />
    ),
  },
]
```

### Pagination

Add pagination controls to your table including page size and selection count.

<ComponentSource
  src="/app/(app)/examples/tasks/components/data-table-pagination.tsx"
  styleName="radix-nova"
/>

```tsx
<DataTablePagination table={table} />
```

### Column toggle

A component to toggle column visibility.

<ComponentSource
  src="/app/(app)/examples/tasks/components/data-table-view-options.tsx"
  styleName="radix-nova"
/>

```tsx
<DataTableViewOptions table={table} />
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="data-table-rtl"
  direction="rtl"
  previewClassName="items-start h-auto px-4 md:px-8"
  hideCode
/>


---

<!-- SOURCE: apps/v4/content/docs/components/base/date-picker.mdx -->

## apps/v4/content/docs/components/base/date-picker.mdx

---
title: Date Picker
description: A date picker component with range and presets.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="date-picker-demo" />

## Installation

The Date Picker is built using a composition of the `<Popover />` and the `<Calendar />` components.

See installation instructions for the [Popover](/docs/components/base/popover#installation) and the [Calendar](/docs/components/base/calendar#installation) components.

## Usage

```tsx showLineNumbers title="components/example-date-picker.tsx"
"use client"

import * as React from "react"
import { format } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

export function DatePickerDemo() {
  const [date, setDate] = React.useState<Date>()

  return (
    <Popover>
      <PopoverTrigger
        render={
          <Button
            variant="outline"
            data-empty={!date}
            className="justify-start text-left font-normal data-[empty=true]:text-muted-foreground"
          />
        }
      >
        <CalendarIcon />
        {date ? format(date, "PPP") : <span>Pick a date</span>}
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0">
        <Calendar mode="single" selected={date} onSelect={setDate} />
      </PopoverContent>
    </Popover>
  )
}
```

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information.

## Examples

### Basic

A basic date picker component.

<ComponentPreview styleName="base-nova" name="date-picker-basic" />

### Range Picker

A date picker component for selecting a range of dates.

<ComponentPreview styleName="base-nova" name="date-picker-range" />

### Date of Birth

A date picker component for selecting a date of birth. This component includes a dropdown caption layout for date and month selection.

<ComponentPreview styleName="base-nova" name="date-picker-dob" />

### Input

A date picker component with an input field for selecting a date.

<ComponentPreview styleName="base-nova" name="date-picker-input" />

### Time Picker

A date picker component with a time input field for selecting a time.

<ComponentPreview styleName="base-nova" name="date-picker-time" />

### Natural Language Picker

This component uses the `chrono-node` library to parse natural language dates.

<ComponentPreview styleName="base-nova" name="date-picker-natural-language" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="date-picker-rtl"
  direction="rtl"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/base/dialog.mdx -->

## apps/v4/content/docs/components/base/dialog.mdx

---
title: Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
featured: true
base: base
component: true
links:
  doc: https://base-ui.com/react/components/dialog
  api: https://base-ui.com/react/components/dialog#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="dialog-demo"
  description="A dialog for editing profile details."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add dialog
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="dialog"
  title="components/ui/dialog.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
```

```tsx showLineNumbers
<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Are you absolutely sure?</DialogTitle>
      <DialogDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

## Examples

### Custom Close Button

Replace the default close control with your own button.

<ComponentPreview styleName="base-nova" name="dialog-close-button" />

### No Close Button

Use `showCloseButton={false}` to hide the close button.

<ComponentPreview styleName="base-nova" name="dialog-no-close-button" />

### Sticky Footer

Keep actions visible while the content scrolls.

<ComponentPreview styleName="base-nova" name="dialog-sticky-footer" />

### Scrollable Content

Long content can scroll while the header stays in view.

<ComponentPreview styleName="base-nova" name="dialog-scrollable-content" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="dialog-rtl" direction="rtl" />

## API Reference

See the [Base UI](https://base-ui.com/react/components/dialog#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/direction.mdx -->

## apps/v4/content/docs/components/base/direction.mdx

---
title: Direction
description: A provider component that sets the text direction for your application.
base: base
component: true
links:
  doc: https://base-ui.com/react/utils/direction-provider
  api: https://base-ui.com/react/utils/direction-provider#api-reference
---

The `DirectionProvider` component is used to set the text direction (`ltr` or `rtl`) for your application. This is essential for supporting right-to-left languages like Arabic, Hebrew, and Persian.

Here's a preview of the component in RTL mode. Use the language selector to switch the language. To see more examples, look for the RTL section on components pages.

<ComponentPreview
  styleName="base-nova"
  name="card-rtl"
  direction="rtl"
  previewClassName="h-auto"
  hideCode
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add direction
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="direction"
  title="components/ui/direction.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { DirectionProvider } from "@/components/ui/direction"
```

```tsx showLineNumbers
<html dir="rtl">
  <body>
    <DirectionProvider direction="rtl">
      {/* Your app content */}
    </DirectionProvider>
  </body>
</html>
```

## useDirection

The `useDirection` hook is used to get the current direction of the application.

```tsx showLineNumbers
import { useDirection } from "@/components/ui/direction"

function MyComponent() {
  const direction = useDirection()
  return <div>Current direction: {direction}</div>
}
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/drawer.mdx -->

## apps/v4/content/docs/components/base/drawer.mdx

---
title: Drawer
description: A drawer component for React.
base: base
component: true
links:
  doc: https://vaul.emilkowal.ski/getting-started
---

<ComponentPreview styleName="base-nova" name="drawer-demo" />

## About

Drawer is built on top of [Vaul](https://github.com/emilkowalski/vaul) by [emilkowalski](https://twitter.com/emilkowalski).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add drawer
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install vaul
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="drawer"
  title="components/ui/drawer.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
```

```tsx showLineNumbers
<Drawer>
  <DrawerTrigger>Open</DrawerTrigger>
  <DrawerContent>
    <DrawerHeader>
      <DrawerTitle>Are you absolutely sure?</DrawerTitle>
      <DrawerDescription>This action cannot be undone.</DrawerDescription>
    </DrawerHeader>
    <DrawerFooter>
      <Button>Submit</Button>
      <DrawerClose>
        <Button variant="outline">Cancel</Button>
      </DrawerClose>
    </DrawerFooter>
  </DrawerContent>
</Drawer>
```

## Examples

### Scrollable Content

Keep actions visible while the content scrolls.

<ComponentPreview styleName="base-nova" name="drawer-scrollable-content" />

### Sides

Use the `direction` prop to set the side of the drawer. Available options are `top`, `right`, `bottom`, and `left`.

<ComponentPreview styleName="base-nova" name="drawer-sides" />

### Responsive Dialog

You can combine the `Dialog` and `Drawer` components to create a responsive dialog. This renders a `Dialog` component on desktop and a `Drawer` on mobile.

<ComponentPreview styleName="base-nova" name="drawer-dialog" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="drawer-rtl" direction="rtl" />

## API Reference

See the [Vaul documentation](https://vaul.emilkowal.ski/getting-started) for the full API reference.


---

<!-- SOURCE: apps/v4/content/docs/components/base/dropdown-menu.mdx -->

## apps/v4/content/docs/components/base/dropdown-menu.mdx

---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
featured: true
base: base
component: true
links:
  doc: https://base-ui.com/react/components/menu
  api: https://base-ui.com/react/components/menu#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="dropdown-menu-demo"
  description="A dropdown menu with icons, shortcuts and sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add dropdown-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="dropdown-menu"
  title="components/ui/dropdown-menu.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```

```tsx showLineNumbers
<DropdownMenu>
  <DropdownMenuTrigger render={<Button variant="outline" />}>
    Open
  </DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuGroup>
      <DropdownMenuLabel>My Account</DropdownMenuLabel>
      <DropdownMenuItem>Profile</DropdownMenuItem>
      <DropdownMenuItem>Billing</DropdownMenuItem>
    </DropdownMenuGroup>
    <DropdownMenuSeparator />
    <DropdownMenuGroup>
      <DropdownMenuItem>Team</DropdownMenuItem>
      <DropdownMenuItem>Subscription</DropdownMenuItem>
    </DropdownMenuGroup>
  </DropdownMenuContent>
</DropdownMenu>
```

## Examples

### Basic

A basic dropdown menu with labels and separators.

<ComponentPreview styleName="base-nova" name="dropdown-menu-basic" />

### Submenu

Use `DropdownMenuSub` to nest secondary actions.

<ComponentPreview styleName="base-nova" name="dropdown-menu-submenu" />

### Shortcuts

Add `DropdownMenuShortcut` to show keyboard hints.

<ComponentPreview styleName="base-nova" name="dropdown-menu-shortcuts" />

### Icons

Combine icons with labels for quick scanning.

<ComponentPreview styleName="base-nova" name="dropdown-menu-icons" />

### Checkboxes

Use `DropdownMenuCheckboxItem` for toggles.

<ComponentPreview styleName="base-nova" name="dropdown-menu-checkboxes" />

### Checkboxes Icons

Add icons to checkbox items.

<ComponentPreview styleName="base-nova" name="dropdown-menu-checkboxes-icons" />

### Radio Group

Use `DropdownMenuRadioGroup` for exclusive choices.

<ComponentPreview styleName="base-nova" name="dropdown-menu-radio-group" />

### Radio Icons

Show radio options with icons.

<ComponentPreview styleName="base-nova" name="dropdown-menu-radio-icons" />

### Destructive

Use `variant="destructive"` for irreversible actions.

<ComponentPreview styleName="base-nova" name="dropdown-menu-destructive" />

### Avatar

An account switcher dropdown triggered by an avatar.

<ComponentPreview styleName="base-nova" name="dropdown-menu-avatar" />

### Complex

A richer example combining groups, icons, and submenus.

<ComponentPreview styleName="base-nova" name="dropdown-menu-complex" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="dropdown-menu-rtl"
  direction="rtl"
/>

## API Reference

See the [Base UI documentation](https://base-ui.com/react/components/menu) for the full API reference.


---

<!-- SOURCE: apps/v4/content/docs/components/base/empty.mdx -->

## apps/v4/content/docs/components/base/empty.mdx

---
title: Empty
description: Use the Empty component to display an empty state.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="empty-demo"
  previewClassName="h-96 p-0"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add empty
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="empty"
  title="components/ui/empty.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
```

```tsx
<Empty>
  <EmptyHeader>
    <EmptyMedia variant="icon">
      <Icon />
    </EmptyMedia>
    <EmptyTitle>No data</EmptyTitle>
    <EmptyDescription>No data found</EmptyDescription>
  </EmptyHeader>
  <EmptyContent>
    <Button>Add data</Button>
  </EmptyContent>
</Empty>
```

## Examples

### Outline

Use the `border` utility class to create an outline empty state.

<ComponentPreview
  styleName="base-nova"
  name="empty-outline"
  previewClassName="h-96 p-6 md:p-10"
/>

### Background

Use the `bg-*` and `bg-gradient-*` utilities to add a background to the empty state.

<ComponentPreview
  styleName="base-nova"
  name="empty-background"
  previewClassName="h-96 p-0"
/>

### Avatar

Use the `EmptyMedia` component to display an avatar in the empty state.

<ComponentPreview
  styleName="base-nova"
  name="empty-avatar"
  previewClassName="h-96 p-0"
/>

### Avatar Group

Use the `EmptyMedia` component to display an avatar group in the empty state.

<ComponentPreview
  styleName="base-nova"
  name="empty-avatar-group"
  previewClassName="h-96 p-0"
/>

### InputGroup

You can add an `InputGroup` component to the `EmptyContent` component.

<ComponentPreview
  styleName="base-nova"
  name="empty-input-group"
  previewClassName="h-96 p-0"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="empty-rtl" direction="rtl" />

## API Reference

### Empty

The main component of the empty state. Wraps the `EmptyHeader` and `EmptyContent` components.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<Empty>
  <EmptyHeader />
  <EmptyContent />
</Empty>
```

### EmptyHeader

The `EmptyHeader` component wraps the empty media, title, and description.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyHeader>
  <EmptyMedia />
  <EmptyTitle />
  <EmptyDescription />
</EmptyHeader>
```

### EmptyMedia

Use the `EmptyMedia` component to display the media of the empty state such as an icon or an image. You can also use it to display other components such as an avatar.

| Prop        | Type                  | Default   |
| ----------- | --------------------- | --------- |
| `variant`   | `"default" \| "icon"` | `default` |
| `className` | `string`              |           |

```tsx
<EmptyMedia variant="icon">
  <Icon />
</EmptyMedia>
```

```tsx
<EmptyMedia>
  <Avatar>
    <AvatarImage src="..." />
    <AvatarFallback>CN</AvatarFallback>
  </Avatar>
</EmptyMedia>
```

### EmptyTitle

Use the `EmptyTitle` component to display the title of the empty state.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyTitle>No data</EmptyTitle>
```

### EmptyDescription

Use the `EmptyDescription` component to display the description of the empty state.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyDescription>You do not have any notifications.</EmptyDescription>
```

### EmptyContent

Use the `EmptyContent` component to display the content of the empty state such as a button, input or a link.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyContent>
  <Button>Add Project</Button>
</EmptyContent>
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/field.mdx -->

## apps/v4/content/docs/components/base/field.mdx

---
title: Field
description: Combine labels, controls, and help text to compose accessible form fields and grouped inputs.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="field-demo"
  previewClassName="h-[800px] p-6 md:h-[850px]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add field
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="field"
  title="components/ui/field.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSeparator,
  FieldSet,
  FieldTitle,
} from "@/components/ui/field"
```

```tsx showLineNumbers
<FieldSet>
  <FieldLegend>Profile</FieldLegend>
  <FieldDescription>This appears on invoices and emails.</FieldDescription>
  <FieldGroup>
    <Field>
      <FieldLabel htmlFor="name">Full name</FieldLabel>
      <Input id="name" autoComplete="off" placeholder="Evil Rabbit" />
      <FieldDescription>This appears on invoices and emails.</FieldDescription>
    </Field>
    <Field>
      <FieldLabel htmlFor="username">Username</FieldLabel>
      <Input id="username" autoComplete="off" aria-invalid />
      <FieldError>Choose another username.</FieldError>
    </Field>
    <Field orientation="horizontal">
      <Switch id="newsletter" />
      <FieldLabel htmlFor="newsletter">Subscribe to the newsletter</FieldLabel>
    </Field>
  </FieldGroup>
</FieldSet>
```

## Anatomy

The `Field` family is designed for composing accessible forms. A typical field is structured as follows:

```tsx showLineNumbers
<Field>
  <FieldLabel htmlFor="input-id">Label</FieldLabel>
  {/* Input, Select, Switch, etc. */}
  <FieldDescription>Optional helper text.</FieldDescription>
  <FieldError>Validation message.</FieldError>
</Field>
```

- `Field` is the core wrapper for a single field.
- `FieldContent` is a flex column that groups label and description. Not required if you have no description.
- Wrap related fields with `FieldGroup`, and use `FieldSet` with `FieldLegend` for semantic grouping.

## Form

See the [Form](/docs/forms) documentation for building forms with the `Field` component and [React Hook Form](/docs/forms/react-hook-form) or [Tanstack Form](/docs/forms/tanstack-form).

## Examples

### Input

<ComponentPreview styleName="base-nova" name="field-input" />

### Textarea

<ComponentPreview styleName="base-nova" name="field-textarea" />

### Select

<ComponentPreview styleName="base-nova" name="field-select" />

### Slider

<ComponentPreview styleName="base-nova" name="field-slider" />

### Fieldset

<ComponentPreview styleName="base-nova" name="field-fieldset" />

### Checkbox

<ComponentPreview
  styleName="base-nova"
  name="field-checkbox"
  previewClassName="h-[32rem]"
/>

### Radio

<ComponentPreview styleName="base-nova" name="field-radio" />

### Switch

<ComponentPreview styleName="base-nova" name="field-switch" />

### Choice Card

Wrap `Field` components inside `FieldLabel` to create selectable field groups. This works with `RadioItem`, `Checkbox` and `Switch` components.

<ComponentPreview styleName="base-nova" name="field-choice-card" />

### Field Group

Stack `Field` components with `FieldGroup`. Add `FieldSeparator` to divide them.

<ComponentPreview
  styleName="base-nova"
  name="field-group"
  previewClassName="h-96"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="field-rtl"
  direction="rtl"
  previewClassName="h-auto p-6"
/>

## Responsive Layout

- **Vertical fields:** Default orientation stacks label, control, and helper text—ideal for mobile-first layouts.
- **Horizontal fields:** Set `orientation="horizontal"` on `Field` to align the label and control side-by-side. Pair with `FieldContent` to keep descriptions aligned.
- **Responsive fields:** Set `orientation="responsive"` for automatic column layouts inside container-aware parents. Apply `@container/field-group` classes on `FieldGroup` to switch orientations at specific breakpoints.

<ComponentPreview
  styleName="base-nova"
  name="field-responsive"
  previewClassName="h-[650px] p-6 md:h-[500px] md:p-10"
/>

## Validation and Errors

- Add `data-invalid` to `Field` to switch the entire block into an error state.
- Add `aria-invalid` on the input itself for assistive technologies.
- Render `FieldError` immediately after the control or inside `FieldContent` to keep error messages aligned with the field.

```tsx showLineNumbers /data-invalid/ /aria-invalid/
<Field data-invalid>
  <FieldLabel htmlFor="email">Email</FieldLabel>
  <Input id="email" type="email" aria-invalid />
  <FieldError>Enter a valid email address.</FieldError>
</Field>
```

## Accessibility

- `FieldSet` and `FieldLegend` keep related controls grouped for keyboard and assistive tech users.
- `Field` outputs `role="group"` so nested controls inherit labeling from `FieldLabel` and `FieldLegend` when combined.
- Apply `FieldSeparator` sparingly to ensure screen readers encounter clear section boundaries.

## API Reference

### FieldSet

Container that renders a semantic `fieldset` with spacing presets.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldSet>
  <FieldLegend>Delivery</FieldLegend>
  <FieldGroup>{/* Fields */}</FieldGroup>
</FieldSet>
```

### FieldLegend

Legend element for a `FieldSet`. Switch to the `label` variant to align with label sizing.

| Prop        | Type                  | Default    |
| ----------- | --------------------- | ---------- |
| `variant`   | `"legend" \| "label"` | `"legend"` |
| `className` | `string`              |            |

```tsx
<FieldLegend variant="label">Notification Preferences</FieldLegend>
```

The `FieldLegend` has two variants: `legend` and `label`. The `label` variant applies label sizing and alignment. Handy if you have nested `FieldSet`.

### FieldGroup

Layout wrapper that stacks `Field` components and enables container queries for responsive orientations.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldGroup className="@container/field-group flex flex-col gap-6">
  <Field>{/* ... */}</Field>
  <Field>{/* ... */}</Field>
</FieldGroup>
```

### Field

The core wrapper for a single field. Provides orientation control, invalid state styling, and spacing.

| Prop           | Type                                         | Default      |
| -------------- | -------------------------------------------- | ------------ |
| `orientation`  | `"vertical" \| "horizontal" \| "responsive"` | `"vertical"` |
| `className`    | `string`                                     |              |
| `data-invalid` | `boolean`                                    |              |

```tsx
<Field orientation="horizontal">
  <FieldLabel htmlFor="remember">Remember me</FieldLabel>
  <Switch id="remember" />
</Field>
```

### FieldContent

Flex column that groups control and descriptions when the label sits beside the control. Not required if you have no description.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<Field>
  <Checkbox id="notifications" />
  <FieldContent>
    <FieldLabel htmlFor="notifications">Notifications</FieldLabel>
    <FieldDescription>Email, SMS, and push options.</FieldDescription>
  </FieldContent>
</Field>
```

### FieldLabel

Label styled for both direct inputs and nested `Field` children.

| Prop        | Type      | Default |
| ----------- | --------- | ------- |
| `className` | `string`  |         |
| `asChild`   | `boolean` | `false` |

```tsx
<FieldLabel htmlFor="email">Email</FieldLabel>
```

### FieldTitle

Renders a title with label styling inside `FieldContent`.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldContent>
  <FieldTitle>Enable Touch ID</FieldTitle>
  <FieldDescription>Unlock your device faster.</FieldDescription>
</FieldContent>
```

### FieldDescription

Helper text slot that automatically balances long lines in horizontal layouts.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldDescription>We never share your email with anyone.</FieldDescription>
```

### FieldSeparator

Visual divider to separate sections inside a `FieldGroup`. Accepts optional inline content.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldSeparator>Or continue with</FieldSeparator>
```

### FieldError

Accessible error container that accepts children or an `errors` array (e.g., from `react-hook-form`).

| Prop        | Type                                       | Default |
| ----------- | ------------------------------------------ | ------- |
| `errors`    | `Array<{ message?: string } \| undefined>` |         |
| `className` | `string`                                   |         |

```tsx
<FieldError errors={errors.username} />
```

When the `errors` array contains multiple messages, the component renders a list automatically.

`FieldError` also accepts issues produced by any validator that implements [Standard Schema](https://standardschema.dev/), including Zod, Valibot, and ArkType. Pass the `issues` array from the schema result directly to render a unified error list across libraries.


---

<!-- SOURCE: apps/v4/content/docs/components/base/hover-card.mdx -->

## apps/v4/content/docs/components/base/hover-card.mdx

---
title: Hover Card
description: For sighted users to preview content available behind a link.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/hover-card
  api: https://base-ui.com/react/components/hover-card#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="hover-card-demo"
  previewClassName="h-80"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add hover-card
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="hover-card"
  title="components/ui/hover-card.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"
```

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>
    The React Framework – created and maintained by @vercel.
  </HoverCardContent>
</HoverCard>
```

## Trigger Delays

Use `delay` and `closeDelay` on the trigger to control when the card opens and
closes.

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger delay={100} closeDelay={200}>
    Hover
  </HoverCardTrigger>
  <HoverCardContent>Content</HoverCardContent>
</HoverCard>
```

## Positioning

Use the `side` and `align` props on `HoverCardContent` to control placement.

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent side="top" align="start">
    Content
  </HoverCardContent>
</HoverCard>
```

## Examples

### Basic

<ComponentPreview
  styleName="base-nova"
  name="hover-card-demo"
  previewClassName="h-80"
/>

### Sides

<ComponentPreview
  styleName="base-nova"
  name="hover-card-sides"
  previewClassName="h-[22rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="hover-card-rtl"
  direction="rtl"
  previewClassName="h-80"
/>

## API Reference

See the [Base UI](https://base-ui.com/react/components/hover-card#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/input-group.mdx -->

## apps/v4/content/docs/components/base/input-group.mdx

---
title: Input Group
description: Add addons, buttons, and helper content to inputs.
base: base
component: true
---

import { IconInfoCircle } from "@tabler/icons-react"

<ComponentPreview
  styleName="base-nova"
  name="input-group-demo"
  previewClassName="h-[26rem]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add input-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="input-group"
  title="components/ui/input-group.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group"
```

```tsx showLineNumbers
<InputGroup>
  <InputGroupInput placeholder="Search..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

## Align

Use the `align` prop on `InputGroupAddon` to position the addon relative to the input.

<Callout>
  For proper focus management, `InputGroupAddon` should always be placed after
  `InputGroupInput` or `InputGroupTextarea` in the DOM. Use the `align` prop to
  visually position the addon.
</Callout>

### inline-start

Use `align="inline-start"` to position the addon at the start of the input. This is the default.

<ComponentPreview
  styleName="base-nova"
  name="input-group-inline-start"
  previewClassName="h-48"
/>

### inline-end

Use `align="inline-end"` to position the addon at the end of the input.

<ComponentPreview
  styleName="base-nova"
  name="input-group-inline-end"
  previewClassName="h-48"
/>

### block-start

Use `align="block-start"` to position the addon above the input.

<ComponentPreview
  styleName="base-nova"
  name="input-group-block-start"
  previewClassName="h-96"
/>

### block-end

Use `align="block-end"` to position the addon below the input.

<ComponentPreview
  styleName="base-nova"
  name="input-group-block-end"
  previewClassName="h-[26rem]"
/>

## Examples

### Icon

<ComponentPreview
  styleName="base-nova"
  name="input-group-icon"
  previewClassName="h-80"
/>

### Text

<ComponentPreview
  styleName="base-nova"
  name="input-group-text"
  previewClassName="h-80"
/>

### Button

<ComponentPreview
  styleName="base-nova"
  name="input-group-button"
  previewClassName="h-72"
/>

### Kbd

<ComponentPreview
  styleName="base-nova"
  name="input-group-kbd"
  previewClassName="h-40"
/>

### Dropdown

<ComponentPreview
  styleName="base-nova"
  name="input-group-dropdown"
  previewClassName="h-56"
/>

### Spinner

<ComponentPreview
  styleName="base-nova"
  name="input-group-spinner"
  previewClassName="h-80"
/>

### Textarea

<ComponentPreview
  styleName="base-nova"
  name="input-group-textarea"
  previewClassName="h-96"
/>

### Custom Input

Add the `data-slot="input-group-control"` attribute to your custom input for automatic focus state handling.

Here's an example of a custom resizable textarea from a third-party library.

<ComponentPreview
  styleName="base-nova"
  name="input-group-custom"
  previewClassName="h-56"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="input-group-rtl"
  direction="rtl"
  previewClassName="h-[30rem]"
/>

## API Reference

### InputGroup

The main component that wraps inputs and addons.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<InputGroup>
  <InputGroupInput />
  <InputGroupAddon />
</InputGroup>
```

### InputGroupAddon

Displays icons, text, buttons, or other content alongside inputs.

<Callout icon={<IconInfoCircle />} title="Focus Navigation">
  For proper focus navigation, the `InputGroupAddon` component should be placed
  after the input. Set the `align` prop to position the addon.
</Callout>

| Prop        | Type                                                             | Default          |
| ----------- | ---------------------------------------------------------------- | ---------------- |
| `align`     | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` |
| `className` | `string`                                                         |                  |

```tsx
<InputGroupAddon align="inline-end">
  <SearchIcon />
</InputGroupAddon>
```

**For `<InputGroupInput />`, use the `inline-start` or `inline-end` alignment. For `<InputGroupTextarea />`, use the `block-start` or `block-end` alignment.**

The `InputGroupAddon` component can have multiple `InputGroupButton` components and icons.

```tsx
<InputGroupAddon>
  <InputGroupButton>Button</InputGroupButton>
  <InputGroupButton>Button</InputGroupButton>
</InputGroupAddon>
```

### InputGroupButton

Displays buttons within input groups.

| Prop        | Type                                                                          | Default   |
| ----------- | ----------------------------------------------------------------------------- | --------- |
| `size`      | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"`                                      | `"xs"`    |
| `variant`   | `"default" \| "destructive" \| "outline" \| "secondary" \| "ghost" \| "link"` | `"ghost"` |
| `className` | `string`                                                                      |           |

```tsx
<InputGroupButton>Button</InputGroupButton>
<InputGroupButton size="icon-xs" aria-label="Copy">
  <CopyIcon />
</InputGroupButton>
```

### InputGroupInput

Replacement for `<Input />` when building input groups. This component has the input group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

All other props are passed through to the underlying `<Input />` component.

```tsx
<InputGroup>
  <InputGroupInput placeholder="Enter text..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

### InputGroupTextarea

Replacement for `<Textarea />` when building input groups. This component has the textarea group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

All other props are passed through to the underlying `<Textarea />` component.

```tsx
<InputGroup>
  <InputGroupTextarea placeholder="Enter message..." />
  <InputGroupAddon align="block-end">
    <InputGroupButton>Send</InputGroupButton>
  </InputGroupAddon>
</InputGroup>
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/input-otp.mdx -->

## apps/v4/content/docs/components/base/input-otp.mdx

---
title: Input OTP
description: Accessible one-time password component with copy-paste functionality.
base: base
component: true
links:
  doc: https://input-otp.rodz.dev
---

<ComponentPreview styleName="base-nova" name="input-otp-demo" />

## About

Input OTP is built on top of [input-otp](https://github.com/guilhermerodz/input-otp) by [@guilherme_rodz](https://twitter.com/guilherme_rodz).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add input-otp
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install input-otp
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="input-otp"
  title="components/ui/input-otp.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"
```

```tsx showLineNumbers
<InputOTP maxLength={6}>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    <InputOTPSlot index={1} />
    <InputOTPSlot index={2} />
  </InputOTPGroup>
  <InputOTPSeparator />
  <InputOTPGroup>
    <InputOTPSlot index={3} />
    <InputOTPSlot index={4} />
    <InputOTPSlot index={5} />
  </InputOTPGroup>
</InputOTP>
```

## Pattern

Use the `pattern` prop to define a custom pattern for the OTP input.

```tsx showLineNumbers {1,5}
import { REGEXP_ONLY_DIGITS_AND_CHARS } from "input-otp"

;<InputOTP maxLength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
  ...
</InputOTP>
```

<ComponentPreview styleName="base-nova" name="input-otp-pattern" />

## Examples

### Separator

Use the `<InputOTPSeparator />` component to add a separator between input groups.

<ComponentPreview styleName="base-nova" name="input-otp-separator" />

### Disabled

Use the `disabled` prop to disable the input.

<ComponentPreview styleName="base-nova" name="input-otp-disabled" />

### Controlled

Use the `value` and `onChange` props to control the input value.

<ComponentPreview styleName="base-nova" name="input-otp-controlled" />

### Invalid

Use `aria-invalid` on the slots to show an error state.

<ComponentPreview styleName="base-nova" name="input-otp-invalid" />

### Four Digits

A common pattern for PIN codes. This uses the `pattern={REGEXP_ONLY_DIGITS}` prop.

<ComponentPreview styleName="base-nova" name="input-otp-four-digits" />

### Alphanumeric

Use `REGEXP_ONLY_DIGITS_AND_CHARS` to accept both letters and numbers.

<ComponentPreview styleName="base-nova" name="input-otp-alphanumeric" />

### Form

<ComponentPreview
  styleName="base-nova"
  name="input-otp-form"
  previewClassName="h-[30rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="input-otp-rtl" direction="rtl" />

## API Reference

See the [input-otp](https://input-otp.rodz.dev) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/input.mdx -->

## apps/v4/content/docs/components/base/input.mdx

---
title: Input
description: A text input component for forms and user data entry with built-in styling and accessibility features.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="input-demo"
  previewClassName="*:max-w-xs"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add input
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="input"
  title="components/ui/input.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Input } from "@/components/ui/input"
```

```tsx
<Input />
```

## Examples

### Basic

<ComponentPreview
  styleName="base-nova"
  name="input-basic"
  previewClassName="*:max-w-xs"
/>

### Field

Use `Field`, `FieldLabel`, and `FieldDescription` to create an input with a
label and description.

<ComponentPreview
  styleName="base-nova"
  name="input-field"
  previewClassName="*:max-w-xs"
/>

### Field Group

Use `FieldGroup` to show multiple `Field` blocks and to build forms.

<ComponentPreview
  styleName="base-nova"
  name="input-fieldgroup"
  previewClassName="*:max-w-xs"
/>

### Disabled

Use the `disabled` prop to disable the input. To style the disabled state, add the `data-disabled` attribute to the `Field` component.

<ComponentPreview
  styleName="base-nova"
  name="input-disabled"
  previewClassName="*:max-w-xs"
/>

### Invalid

Use the `aria-invalid` prop to mark the input as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field` component.

<ComponentPreview
  styleName="base-nova"
  name="input-invalid"
  previewClassName="*:max-w-xs"
/>

### File

Use the `type="file"` prop to create a file input.

<ComponentPreview
  styleName="base-nova"
  name="input-file"
  previewClassName="*:max-w-xs"
/>

### Inline

Use `Field` with `orientation="horizontal"` to create an inline input.
Pair with `Button` to create a search input with a button.

<ComponentPreview
  styleName="base-nova"
  name="input-inline"
  previewClassName="*:max-w-xs"
/>

### Grid

Use a grid layout to place multiple inputs side by side.

<ComponentPreview
  styleName="base-nova"
  name="input-grid"
  previewClassName="p-6"
/>

### Required

Use the `required` attribute to indicate required inputs.

<ComponentPreview
  styleName="base-nova"
  name="input-required"
  previewClassName="*:max-w-xs"
/>

### Badge

Use `Badge` in the label to highlight a recommended field.

<ComponentPreview
  styleName="base-nova"
  name="input-badge"
  previewClassName="*:max-w-xs"
/>

### Input Group

To add icons, text, or buttons inside an input, use the `InputGroup` component. See the [Input Group](/docs/components/input-group) component for more examples.

<ComponentPreview
  styleName="base-nova"
  name="input-input-group"
  previewClassName="*:max-w-xs"
/>

### Button Group

To add buttons to an input, use the `ButtonGroup` component. See the [Button Group](/docs/components/button-group) component for more examples.

<ComponentPreview
  styleName="base-nova"
  name="input-button-group"
  previewClassName="*:max-w-xs"
/>

### Form

A full form example with multiple inputs, a select, and a button.

<ComponentPreview
  styleName="base-nova"
  name="input-form"
  previewClassName="h-[32rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="input-rtl"
  direction="rtl"
  previewClassName="*:max-w-xs"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/base/item.mdx -->

## apps/v4/content/docs/components/base/item.mdx

---
title: Item
description: A versatile component for displaying content with media, title, description, and actions.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="item-demo" />

The `Item` component is a straightforward flex container that can house nearly any type of content. Use it to display a title, description, and actions. Group it with the `ItemGroup` component to create a list of items.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add item
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="item"
  title="components/ui/item.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
```

```tsx showLineNumbers
<Item>
  <ItemMedia variant="icon">
    <Icon />
  </ItemMedia>
  <ItemContent>
    <ItemTitle>Title</ItemTitle>
    <ItemDescription>Description</ItemDescription>
  </ItemContent>
  <ItemActions>
    <Button>Action</Button>
  </ItemActions>
</Item>
```

## Item vs Field

Use `Field` if you need to display a form input such as a checkbox, input, radio, or select.

If you only need to display content such as a title, description, and actions, use `Item`.

## Variant

Use the `variant` prop to change the visual style of the item.

<ComponentPreview
  styleName="base-nova"
  name="item-variant"
  previewClassName="h-96"
/>

## Size

Use the `size` prop to change the size of the item. Available sizes are `default`, `sm`, and `xs`.

<ComponentPreview
  styleName="base-nova"
  name="item-size"
  previewClassName="h-96"
/>

## Examples

### Icon

Use `ItemMedia` with `variant="icon"` to display an icon.

<ComponentPreview styleName="base-nova" name="item-icon" />

### Avatar

You can use `ItemMedia` with `variant="avatar"` to display an avatar.

<ComponentPreview styleName="base-nova" name="item-avatar" />

### Image

Use `ItemMedia` with `variant="image"` to display an image.

<ComponentPreview styleName="base-nova" name="item-image" />

### Group

Use `ItemGroup` to group related items together.

<ComponentPreview
  styleName="base-nova"
  name="item-group"
  previewClassName="h-96"
/>

### Header

Use `ItemHeader` to add a header above the item content.

<ComponentPreview
  styleName="base-nova"
  name="item-header"
  previewClassName="h-96"
/>

### Link

Use the `render` prop to render the item as a link. The hover and focus states will be applied to the anchor element.

<ComponentPreview styleName="base-nova" name="item-link" />

```tsx showLineNumbers
<Item render={<a href="/dashboard" />}>
  <ItemMedia variant="icon">
    <HomeIcon />
  </ItemMedia>
  <ItemContent>
    <ItemTitle>Dashboard</ItemTitle>
    <ItemDescription>Overview of your account and activity.</ItemDescription>
  </ItemContent>
</Item>
```

### Dropdown

<ComponentPreview styleName="base-nova" name="item-dropdown" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="item-rtl" direction="rtl" />

## API Reference

### Item

The main component for displaying content with media, title, description, and actions.

| Prop      | Type                                | Default     |
| --------- | ----------------------------------- | ----------- |
| `variant` | `"default" \| "outline" \| "muted"` | `"default"` |
| `size`    | `"default" \| "sm" \| "xs"`         | `"default"` |
| `render`  | `React.ReactElement`                |             |

### ItemGroup

A container that groups related items together with consistent styling.

```tsx
<ItemGroup>
  <Item />
  <Item />
</ItemGroup>
```

### ItemSeparator

A separator between items in a group.

```tsx
<ItemGroup>
  <Item />
  <ItemSeparator />
  <Item />
</ItemGroup>
```

### ItemMedia

Use `ItemMedia` to display media content such as icons, images, or avatars.

| Prop      | Type                             | Default     |
| --------- | -------------------------------- | ----------- |
| `variant` | `"default" \| "icon" \| "image"` | `"default"` |

```tsx
<ItemMedia variant="icon">
  <Icon />
</ItemMedia>
```

```tsx
<ItemMedia variant="image">
  <img src="..." alt="..." />
</ItemMedia>
```

### ItemContent

Wraps the title and description of the item.

```tsx
<ItemContent>
  <ItemTitle>Title</ItemTitle>
  <ItemDescription>Description</ItemDescription>
</ItemContent>
```

### ItemTitle

Displays the title of the item.

```tsx
<ItemTitle>Item Title</ItemTitle>
```

### ItemDescription

Displays the description of the item.

```tsx
<ItemDescription>Item description</ItemDescription>
```

### ItemActions

Container for action buttons or other interactive elements.

```tsx
<ItemActions>
  <Button>Action</Button>
</ItemActions>
```

### ItemHeader

Displays a header above the item content.

```tsx
<Item>
  <ItemHeader>Header</ItemHeader>
  <ItemContent>...</ItemContent>
</Item>
```

### ItemFooter

Displays a footer below the item content.

```tsx
<Item>
  <ItemContent>...</ItemContent>
  <ItemFooter>Footer</ItemFooter>
</Item>
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/kbd.mdx -->

## apps/v4/content/docs/components/base/kbd.mdx

---
title: Kbd
description: Used to display textual user input from keyboard.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="kbd-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add kbd
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="kbd"
  title="components/ui/kbd.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Kbd } from "@/components/ui/kbd"
```

```tsx
<Kbd>Ctrl</Kbd>
```

## Examples

### Group

Use the `KbdGroup` component to group keyboard keys together.

<ComponentPreview styleName="base-nova" name="kbd-group" />

### Button

Use the `Kbd` component inside a `Button` component to display a keyboard key inside a button.

<ComponentPreview styleName="base-nova" name="kbd-button" />

### Tooltip

You can use the `Kbd` component inside a `Tooltip` component to display a tooltip with a keyboard key.

<ComponentPreview styleName="base-nova" name="kbd-tooltip" />

### Input Group

You can use the `Kbd` component inside a `InputGroupAddon` component to display a keyboard key inside an input group.

<ComponentPreview styleName="base-nova" name="kbd-input-group" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="kbd-rtl" direction="rtl" />

## API Reference

### Kbd

Use the `Kbd` component to display a keyboard key.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

```tsx
<Kbd>Ctrl</Kbd>
```

### KbdGroup

Use the `KbdGroup` component to group `Kbd` components together.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

```tsx
<KbdGroup>
  <Kbd>Ctrl</Kbd>
  <Kbd>B</Kbd>
</KbdGroup>
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/label.mdx -->

## apps/v4/content/docs/components/base/label.mdx

---
title: Label
description: Renders an accessible label associated with controls.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/label
  api: https://base-ui.com/react/components/label#api-reference
---

<ComponentPreview styleName="base-nova" name="label-demo" />

<Callout>
  For form fields, use the [Field](/docs/components/base/field) component which
  includes built-in label, description, and error handling.
</Callout>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add label
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="label"
  title="components/ui/label.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Label } from "@/components/ui/label"
```

```tsx
<Label htmlFor="email">Your email address</Label>
```

## Label in Field

For form fields, use the [Field](/docs/components/base/field) component which
includes built-in `FieldLabel`, `FieldDescription`, and `FieldError` components.

```tsx
<Field>
  <FieldLabel htmlFor="email">Your email address</FieldLabel>
  <Input id="email" />
</Field>
```

<ComponentPreview
  styleName="base-nova"
  name="field-demo"
  previewClassName="h-[44rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="label-rtl" direction="rtl" />

## API Reference

See the [Base UI Label](https://base-ui.com/react/components/label#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/menubar.mdx -->

## apps/v4/content/docs/components/base/menubar.mdx

---
title: Menubar
description: A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/menubar
  api: https://base-ui.com/react/components/menubar#api-reference
---

<ComponentPreview styleName="base-nova" name="menubar-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add menubar
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="menubar"
  title="components/ui/menubar.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Menubar,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
```

```tsx showLineNumbers
<Menubar>
  <MenubarMenu>
    <MenubarTrigger>File</MenubarTrigger>
    <MenubarContent>
      <MenubarGroup>
        <MenubarItem>
          New Tab <MenubarShortcut>⌘T</MenubarShortcut>
        </MenubarItem>
        <MenubarItem>New Window</MenubarItem>
      </MenubarGroup>
      <MenubarSeparator />
      <MenubarGroup>
        <MenubarItem>Share</MenubarItem>
        <MenubarItem>Print</MenubarItem>
      </MenubarGroup>
    </MenubarContent>
  </MenubarMenu>
</Menubar>
```

## Examples

### Checkbox

Use `MenubarCheckboxItem` for toggleable options.

<ComponentPreview styleName="base-nova" name="menubar-checkbox" />

### Radio

Use `MenubarRadioGroup` and `MenubarRadioItem` for single-select options.

<ComponentPreview styleName="base-nova" name="menubar-radio" />

### Submenu

Use `MenubarSub`, `MenubarSubTrigger`, and `MenubarSubContent` for nested menus.

<ComponentPreview styleName="base-nova" name="menubar-submenu" />

### With Icons

<ComponentPreview styleName="base-nova" name="menubar-icons" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="menubar-rtl" direction="rtl" />

## API Reference

See the [Base UI Menubar](https://base-ui.com/react/components/menubar#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/native-select.mdx -->

## apps/v4/content/docs/components/base/native-select.mdx

---
title: Native Select
description: A styled native HTML select element with consistent design system integration.
base: base
component: true
---

import { InfoIcon } from "lucide-react"

<Callout variant="info" icon={<InfoIcon className="translate-y-[3px]!" />}>
  For a styled select component, see the [Select](/docs/components/select)
  component.
</Callout>

<ComponentPreview styleName="base-nova" name="native-select-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add native-select
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="native-select"
  title="components/ui/native-select.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  NativeSelect,
  NativeSelectOptGroup,
  NativeSelectOption,
} from "@/components/ui/native-select"
```

```tsx showLineNumbers
<NativeSelect>
  <NativeSelectOption value="">Select a fruit</NativeSelectOption>
  <NativeSelectOption value="apple">Apple</NativeSelectOption>
  <NativeSelectOption value="banana">Banana</NativeSelectOption>
  <NativeSelectOption value="blueberry">Blueberry</NativeSelectOption>
  <NativeSelectOption value="pineapple">Pineapple</NativeSelectOption>
</NativeSelect>
```

## Examples

### Groups

Use `NativeSelectOptGroup` to organize options into categories.

<ComponentPreview styleName="base-nova" name="native-select-groups" />

### Disabled

Add the `disabled` prop to the `NativeSelect` component to disable the select.

<ComponentPreview styleName="base-nova" name="native-select-disabled" />

### Invalid

Use `aria-invalid` to show validation errors and the `data-invalid` attribute to the `Field` component for styling.

<ComponentPreview styleName="base-nova" name="native-select-invalid" />

## Native Select vs Select

- Use `NativeSelect` for native browser behavior, better performance, or mobile-optimized dropdowns.
- Use `Select` for custom styling, animations, or complex interactions.

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="native-select-rtl"
  direction="rtl"
/>

## API Reference

### NativeSelect

The main select component that wraps the native HTML select element.

```tsx
<NativeSelect>
  <NativeSelectOption value="option1">Option 1</NativeSelectOption>
  <NativeSelectOption value="option2">Option 2</NativeSelectOption>
</NativeSelect>
```

### NativeSelectOption

Represents an individual option within the select.

| Prop       | Type      | Default |
| ---------- | --------- | ------- |
| `value`    | `string`  |         |
| `disabled` | `boolean` | `false` |

### NativeSelectOptGroup

Groups related options together for better organization.

| Prop       | Type      | Default |
| ---------- | --------- | ------- |
| `label`    | `string`  |         |
| `disabled` | `boolean` | `false` |

```tsx
<NativeSelectOptGroup label="Fruits">
  <NativeSelectOption value="apple">Apple</NativeSelectOption>
  <NativeSelectOption value="banana">Banana</NativeSelectOption>
</NativeSelectOptGroup>
```


---

<!-- SOURCE: apps/v4/content/docs/components/base/navigation-menu.mdx -->

## apps/v4/content/docs/components/base/navigation-menu.mdx

---
title: Navigation Menu
description: A collection of links for navigating websites.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/navigation-menu
  api: https://base-ui.com/react/components/navigation-menu#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="navigation-menu-demo"
  previewClassName="h-96"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add navigation-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="navigation-menu"
  title="components/ui/navigation-menu.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
```

```tsx showLineNumbers
<NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
      <NavigationMenuTrigger>Item One</NavigationMenuTrigger>
      <NavigationMenuContent>
        <NavigationMenuLink>Link</NavigationMenuLink>
      </NavigationMenuContent>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>
```

## Link Component

Use the `render` prop to compose a custom link component such as Next.js `Link`.

```tsx showLineNumbers
import Link from "next/link"

import {
  NavigationMenuItem,
  NavigationMenuLink,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"

export function NavigationMenuDemo() {
  return (
    <NavigationMenuItem>
      <NavigationMenuLink
        render={<Link href="/docs" />}
        className={navigationMenuTriggerStyle()}
      >
        Documentation
      </NavigationMenuLink>
    </NavigationMenuItem>
  )
}
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="navigation-menu-rtl"
  direction="rtl"
  previewClassName="h-96"
/>

## API Reference

See the [Base UI Navigation Menu](https://base-ui.com/react/components/navigation-menu#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/pagination.mdx -->

## apps/v4/content/docs/components/base/pagination.mdx

---
title: Pagination
description: Pagination with page navigation, next and previous links.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="pagination-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add pagination
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="pagination"
  title="components/ui/pagination.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
```

```tsx showLineNumbers
<Pagination>
  <PaginationContent>
    <PaginationItem>
      <PaginationPrevious href="#" />
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">1</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#" isActive>
        2
      </PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">3</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationEllipsis />
    </PaginationItem>
    <PaginationItem>
      <PaginationNext href="#" />
    </PaginationItem>
  </PaginationContent>
</Pagination>
```

## Examples

### Simple

A simple pagination with only page numbers.

<ComponentPreview styleName="base-nova" name="pagination-simple" />

### Icons Only

Use just the previous and next buttons without page numbers. This is useful for data tables with a rows per page selector.

<ComponentPreview styleName="base-nova" name="pagination-icons-only" />

## Next.js

By default the `<PaginationLink />` component will render an `<a />` tag.

To use the Next.js `<Link />` component, make the following updates to `pagination.tsx`.

```diff showLineNumbers /typeof Link/ {1}
+ import Link from "next/link"

- type PaginationLinkProps = ... & React.ComponentProps<"a">
+ type PaginationLinkProps = ... & React.ComponentProps<typeof Link>

const PaginationLink = ({...props }: ) => (
  <PaginationItem>
-   <a>
+   <Link>
      // ...
-   </a>
+   </Link>
  </PaginationItem>
)

```

<Callout className="mt-6">

**Note:** We are making updates to the cli to automatically do this for you.

</Callout>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="pagination-rtl" direction="rtl" />

## Changelog

### RTL Support

If you're upgrading from a previous version of the `Pagination` component, you'll need to apply the following updates to add the `text` prop:

<Steps>

<Step>Update `PaginationPrevious`.</Step>

```diff
  function PaginationPrevious({
    className,
+   text = "Previous",
    ...props
- }: React.ComponentProps<typeof PaginationLink>) {
+ }: React.ComponentProps<typeof PaginationLink> & { text?: string }) {
    return (
      <PaginationLink
        aria-label="Go to previous page"
        size="default"
        className={cn("cn-pagination-previous", className)}
        {...props}
      >
        <ChevronLeftIcon />
        <span className="cn-pagination-previous-text hidden sm:block">
-         Previous
+         {text}
        </span>
      </PaginationLink>
    )
  }
```

<Step>Update `PaginationNext`.</Step>

```diff
  function PaginationNext({
    className,
+   text = "Next",
    ...props
- }: React.ComponentProps<typeof PaginationLink>) {
+ }: React.ComponentProps<typeof PaginationLink> & { text?: string }) {
    return (
      <PaginationLink
        aria-label="Go to next page"
        size="default"
        className={cn("cn-pagination-next", className)}
        {...props}
      >
-       <span className="cn-pagination-next-text hidden sm:block">Next</span>
+       <span className="cn-pagination-next-text hidden sm:block">{text}</span>
        <ChevronRightIcon />
      </PaginationLink>
    )
  }
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/components/base/popover.mdx -->

## apps/v4/content/docs/components/base/popover.mdx

---
title: Popover
description: Displays rich content in a portal, triggered by a button.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/popover
  api: https://base-ui.com/react/components/popover#api-reference
---

<ComponentPreview styleName="base-nova" name="popover-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add popover
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="popover"
  title="components/ui/popover.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Popover,
  PopoverContent,
  PopoverDescription,
  PopoverHeader,
  PopoverTitle,
  PopoverTrigger,
} from "@/components/ui/popover"
```

```tsx showLineNumbers
<Popover>
  <PopoverTrigger render={<Button variant="outline" />}>
    Open Popover
  </PopoverTrigger>
  <PopoverContent>
    <PopoverHeader>
      <PopoverTitle>Title</PopoverTitle>
      <PopoverDescription>Description text here.</PopoverDescription>
    </PopoverHeader>
  </PopoverContent>
</Popover>
```

## Examples

### Basic

A simple popover with a header, title, and description.

<ComponentPreview styleName="base-nova" name="popover-basic" />

### Align

Use the `align` prop on `PopoverContent` to control the horizontal alignment.

<ComponentPreview styleName="base-nova" name="popover-alignments" />

### With Form

A popover with form fields inside.

<ComponentPreview styleName="base-nova" name="popover-form" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="popover-rtl" direction="rtl" />

## API Reference

See the [Base UI Popover](https://base-ui.com/react/components/popover#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/progress.mdx -->

## apps/v4/content/docs/components/base/progress.mdx

---
title: Progress
description: Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/progress
  api: https://base-ui.com/react/components/progress#api-reference
---

<ComponentPreview styleName="base-nova" name="progress-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add progress
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="progress"
  title="components/ui/progress.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Progress } from "@/components/ui/progress"
```

```tsx showLineNumbers
<Progress value={33} />
```

## Examples

### Label

Use `ProgressLabel` and `ProgressValue` to add a label and value display.

<ComponentPreview styleName="base-nova" name="progress-label" />

### Controlled

A progress bar that can be controlled by a slider.

<ComponentPreview styleName="base-nova" name="progress-controlled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="progress-rtl" direction="rtl" />

## API Reference

See the [Base UI Progress](https://base-ui.com/react/components/progress#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/radio-group.mdx -->

## apps/v4/content/docs/components/base/radio-group.mdx

---
title: Radio Group
description: A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/radio-group
  api: https://base-ui.com/react/components/radio-group#api-reference
---

<ComponentPreview styleName="base-nova" name="radio-group-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add radio-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="radio-group"
  title="components/ui/radio-group.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
```

```tsx showLineNumbers
<RadioGroup defaultValue="option-one">
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-one" id="option-one" />
    <Label htmlFor="option-one">Option One</Label>
  </div>
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-two" id="option-two" />
    <Label htmlFor="option-two">Option Two</Label>
  </div>
</RadioGroup>
```

## Examples

### Description

Radio group items with a description using the `Field` component.

<ComponentPreview styleName="base-nova" name="radio-group-description" />

### Choice Card

Use `FieldLabel` to wrap the entire `Field` for a clickable card-style selection.

<ComponentPreview styleName="base-nova" name="radio-group-choice-card" />

### Fieldset

Use `FieldSet` and `FieldLegend` to group radio items with a label and description.

<ComponentPreview styleName="base-nova" name="radio-group-fieldset" />

### Disabled

Use the `disabled` prop on `RadioGroup` to disable all items.

<ComponentPreview styleName="base-nova" name="radio-group-disabled" />

### Invalid

Use `aria-invalid` on `RadioGroupItem` and `data-invalid` on `Field` to show validation errors.

<ComponentPreview styleName="base-nova" name="radio-group-invalid" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="radio-group-rtl"
  direction="rtl"
/>

## API Reference

See the [Base UI Radio Group](https://base-ui.com/react/components/radio-group#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/resizable.mdx -->

## apps/v4/content/docs/components/base/resizable.mdx

---
title: Resizable
description: Accessible resizable panel groups and layouts with keyboard support.
base: base
component: true
links:
  doc: https://github.com/bvaughn/react-resizable-panels
  api: https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels
---

<ComponentPreview
  styleName="base-nova"
  name="resizable-demo"
  previewClassName="h-80"
/>

## About

The `Resizable` component is built on top of [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels) by [bvaughn](https://github.com/bvaughn).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add resizable
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install react-resizable-panels
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="resizable"
  title="components/ui/resizable.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
```

```tsx showLineNumbers
<ResizablePanelGroup orientation="horizontal">
  <ResizablePanel>One</ResizablePanel>
  <ResizableHandle />
  <ResizablePanel>Two</ResizablePanel>
</ResizablePanelGroup>
```

## Examples

### Vertical

Use `orientation="vertical"` for vertical resizing.

<ComponentPreview styleName="base-nova" name="resizable-vertical" />

### Handle

Use the `withHandle` prop on `ResizableHandle` to show a visible handle.

<ComponentPreview styleName="base-nova" name="resizable-handle" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="resizable-rtl" direction="rtl" />

## API Reference

See the [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels) documentation.

## Changelog

### 2025-02-02 `react-resizable-panels` v4

Updated to `react-resizable-panels` v4. See the [v4.0.0 release notes](https://github.com/bvaughn/react-resizable-panels/releases/tag/4.0.0) for full details.

If you're using `react-resizable-panels` primitives directly, note the following changes:

| v3                           | v4                      |
| ---------------------------- | ----------------------- |
| `PanelGroup`                 | `Group`                 |
| `PanelResizeHandle`          | `Separator`             |
| `direction` prop             | `orientation` prop      |
| `defaultSize={50}`           | `defaultSize="50%"`     |
| `onLayout`                   | `onLayoutChange`        |
| `ImperativePanelHandle`      | `PanelImperativeHandle` |
| `ref` prop on Panel          | `panelRef` prop         |
| `data-panel-group-direction` | `aria-orientation`      |

<Callout>
  The shadcn/ui wrapper components (`ResizablePanelGroup`, `ResizablePanel`,
  `ResizableHandle`) remain unchanged.
</Callout>


---

<!-- SOURCE: apps/v4/content/docs/components/base/scroll-area.mdx -->

## apps/v4/content/docs/components/base/scroll-area.mdx

---
title: Scroll Area
description: Augments native scroll functionality for custom, cross-browser styling.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/scroll-area
  api: https://base-ui.com/react/components/scroll-area#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="scroll-area-demo"
  previewClassName="h-96"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add scroll-area
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="scroll-area"
  title="components/ui/scroll-area.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
```

```tsx showLineNumbers
<ScrollArea className="h-[200px] w-[350px] rounded-md border p-4">
  Your scrollable content here.
</ScrollArea>
```

## Examples

### Horizontal

Use `ScrollBar` with `orientation="horizontal"` for horizontal scrolling.

<ComponentPreview styleName="base-nova" name="scroll-area-horizontal-demo" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="scroll-area-rtl"
  direction="rtl"
  previewClassName="h-auto"
/>

## API Reference

See the [Base UI Scroll Area](https://base-ui.com/react/components/scroll-area#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/select.mdx -->

## apps/v4/content/docs/components/base/select.mdx

---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
base: base
component: true
featured: true
links:
  doc: https://base-ui.com/react/components/select
  api: https://base-ui.com/react/components/select#api-reference
---

<ComponentPreview styleName="base-nova" name="select-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add select
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="select"
  title="components/ui/select.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

```tsx showLineNumbers
const items = [
  { label: "Light", value: "light" },
  { label: "Dark", value: "dark" },
  { label: "System", value: "system" },
]

<Select items={items}>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      {items.map((item) => (
        <SelectItem key={item.value} value={item.value}>
          {item.label}
        </SelectItem>
      ))}
    </SelectGroup>
  </SelectContent>
</Select>
```

## Examples

### Align Item With Trigger

Use `alignItemWithTrigger` on `SelectContent` to control whether the selected item aligns with the trigger. When `true` (default), the popup positions so the selected item appears over the trigger. When `false`, the popup aligns to the trigger edge.

<ComponentPreview styleName="base-nova" name="select-align-item" />

### Groups

Use `SelectGroup`, `SelectLabel`, and `SelectSeparator` to organize items.

<ComponentPreview styleName="base-nova" name="select-groups" />

### Scrollable

A select with many items that scrolls.

<ComponentPreview styleName="base-nova" name="select-scrollable" />

### Disabled

<ComponentPreview styleName="base-nova" name="select-disabled" />

### Invalid

Add the `data-invalid` attribute to the `Field` component and the `aria-invalid` attribute to the `SelectTrigger` component to show an error state.

```tsx showLineNumbers /data-invalid/ /aria-invalid/
<Field data-invalid>
  <FieldLabel>Fruit</FieldLabel>
  <SelectTrigger aria-invalid>
    <SelectValue />
  </SelectTrigger>
</Field>
```

<ComponentPreview styleName="base-nova" name="select-invalid" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="select-rtl" direction="rtl" />

## API Reference

See the [Base UI Select](https://base-ui.com/react/components/select#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/separator.mdx -->

## apps/v4/content/docs/components/base/separator.mdx

---
title: Separator
description: Visually or semantically separates content.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/separator
  api: https://base-ui.com/react/components/separator#api-reference
---

<ComponentPreview styleName="base-nova" name="separator-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add separator
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="separator"
  title="components/ui/separator.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Separator } from "@/components/ui/separator"
```

```tsx showLineNumbers
<Separator />
```

## Examples

### Vertical

Use `orientation="vertical"` for a vertical separator.

<ComponentPreview styleName="base-nova" name="separator-vertical" />

### Menu

Vertical separators between menu items with descriptions.

<ComponentPreview styleName="base-nova" name="separator-menu" />

### List

Horizontal separators between list items.

<ComponentPreview styleName="base-nova" name="separator-list" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="separator-rtl" direction="rtl" />

## API Reference

See the [Base UI Separator](https://base-ui.com/react/components/separator#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/sheet.mdx -->

## apps/v4/content/docs/components/base/sheet.mdx

---
title: Sheet
description: Extends the Dialog component to display content that complements the main content of the screen.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/dialog
  api: https://base-ui.com/react/components/dialog#api-reference
---

<ComponentPreview styleName="base-nova" name="sheet-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add sheet
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="sheet"
  title="components/ui/sheet.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"
```

```tsx showLineNumbers
<Sheet>
  <SheetTrigger>Open</SheetTrigger>
  <SheetContent>
    <SheetHeader>
      <SheetTitle>Are you absolutely sure?</SheetTitle>
      <SheetDescription>This action cannot be undone.</SheetDescription>
    </SheetHeader>
  </SheetContent>
</Sheet>
```

## Examples

### Side

Use the `side` prop on `SheetContent` to set the edge of the screen where the sheet appears. Values are `top`, `right`, `bottom`, or `left`.

<ComponentPreview styleName="base-nova" name="sheet-side" />

### No Close Button

Use `showCloseButton={false}` on `SheetContent` to hide the close button.

<ComponentPreview styleName="base-nova" name="sheet-no-close-button" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="sheet-rtl" direction="rtl" />

## API Reference

See the [Base UI Dialog](https://base-ui.com/react/components/dialog#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/sidebar.mdx -->

## apps/v4/content/docs/components/base/sidebar.mdx

---
title: Sidebar
description: A composable, themeable and customizable sidebar component.
base: base
component: true
---

import { ExternalLinkIcon } from "lucide-react"

<figure className="flex flex-col gap-4">
  <ComponentPreview
    styleName="base-nova"
    name="sidebar-demo"
    type="block"
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar that collapses to icons.
  </figcaption>
</figure>

Sidebars are one of the most complex components to build. They are central
to any application and often contain a lot of moving parts.

We now have a solid foundation to build on top of. Composable. Themeable.
Customizable.

[Browse the Blocks Library](/blocks).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add sidebar
```

</TabsContent>

<TabsContent value="manual">

<ComponentSource
  name="sidebar"
  title="components/ui/sidebar.tsx"
  styleName="base-nova"
/>

</TabsContent>

</CodeTabs>

## Structure

A `Sidebar` component is composed of the following parts:

- `SidebarProvider` - Handles collapsible state.
- `Sidebar` - The sidebar container.
- `SidebarHeader` and `SidebarFooter` - Sticky at the top and bottom of the sidebar.
- `SidebarContent` - Scrollable content.
- `SidebarGroup` - Section within the `SidebarContent`.
- `SidebarTrigger` - Trigger for the `Sidebar`.

<Image
  src="/images/sidebar-structure.png"
  width="716"
  height="420"
  alt="Sidebar Structure"
  className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
/>
<Image
  src="/images/sidebar-structure-dark.png"
  width="716"
  height="420"
  alt="Sidebar Structure"
  className="mt-6 hidden w-full overflow-hidden rounded-lg border dark:block"
/>

## Usage

```tsx showLineNumbers title="app/layout.tsx"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main>
        <SidebarTrigger />
        {children}
      </main>
    </SidebarProvider>
  )
}
```

```tsx showLineNumbers title="components/app-sidebar.tsx"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
} from "@/components/ui/sidebar"

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader />
      <SidebarContent>
        <SidebarGroup />
        <SidebarGroup />
      </SidebarContent>
      <SidebarFooter />
    </Sidebar>
  )
}
```

## SidebarProvider

The `SidebarProvider` component is used to provide the sidebar context to the `Sidebar` component. You should always wrap your application in a `SidebarProvider` component.

### Props

| Name           | Type                      | Description                                  |
| -------------- | ------------------------- | -------------------------------------------- |
| `defaultOpen`  | `boolean`                 | Default open state of the sidebar.           |
| `open`         | `boolean`                 | Open state of the sidebar (controlled).      |
| `onOpenChange` | `(open: boolean) => void` | Sets open state of the sidebar (controlled). |

### Width

If you have a single sidebar in your application, you can use the `SIDEBAR_WIDTH` and `SIDEBAR_WIDTH_MOBILE` variables in `sidebar.tsx` to set the width of the sidebar.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
```

For multiple sidebars in your application, you can use the `--sidebar-width` and `--sidebar-width-mobile` CSS variables in the `style` prop.

```tsx showLineNumbers
<SidebarProvider
  style={
    {
      "--sidebar-width": "20rem",
      "--sidebar-width-mobile": "20rem",
    } as React.CSSProperties
  }
>
  <Sidebar />
</SidebarProvider>
```

### Keyboard Shortcut

To trigger the sidebar, you use the `cmd+b` keyboard shortcut on Mac and `ctrl+b` on Windows.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
const SIDEBAR_KEYBOARD_SHORTCUT = "b"
```

## Sidebar

The main `Sidebar` component used to render a collapsible sidebar.

### Props

| Property      | Type                              | Description                       |
| ------------- | --------------------------------- | --------------------------------- |
| `side`        | `left` or `right`                 | The side of the sidebar.          |
| `variant`     | `sidebar`, `floating`, or `inset` | The variant of the sidebar.       |
| `collapsible` | `offcanvas`, `icon`, or `none`    | Collapsible state of the sidebar. |

| Prop        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `offcanvas` | A collapsible sidebar that slides in from the left or right. |
| `icon`      | A sidebar that collapses to icons.                           |
| `none`      | A non-collapsible sidebar.                                   |

<Callout>
  **Note:** If you use the `inset` variant, remember to wrap your main content
  in a `SidebarInset` component.
</Callout>

```tsx showLineNumbers
<SidebarProvider>
  <Sidebar variant="inset" />
  <SidebarInset>
    <main>{children}</main>
  </SidebarInset>
</SidebarProvider>
```

## useSidebar

The `useSidebar` hook is used to control the sidebar.

```tsx showLineNumbers
import { useSidebar } from "@/components/ui/sidebar"

export function AppSidebar() {
  const {
    state,
    open,
    setOpen,
    openMobile,
    setOpenMobile,
    isMobile,
    toggleSidebar,
  } = useSidebar()
}
```

| Property        | Type                      | Description                                   |
| --------------- | ------------------------- | --------------------------------------------- |
| `state`         | `expanded` or `collapsed` | The current state of the sidebar.             |
| `open`          | `boolean`                 | Whether the sidebar is open.                  |
| `setOpen`       | `(open: boolean) => void` | Sets the open state of the sidebar.           |
| `openMobile`    | `boolean`                 | Whether the sidebar is open on mobile.        |
| `setOpenMobile` | `(open: boolean) => void` | Sets the open state of the sidebar on mobile. |
| `isMobile`      | `boolean`                 | Whether the sidebar is on mobile.             |
| `toggleSidebar` | `() => void`              | Toggles the sidebar. Desktop and mobile.      |

## SidebarHeader

Use the `SidebarHeader` component to add a sticky header to the sidebar.

```tsx showLineNumbers title="components/app-sidebar.tsx"
<Sidebar>
  <SidebarHeader>
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <SidebarMenuButton>
              Select Workspace
              <ChevronDown className="ml-auto" />
            </SidebarMenuButton>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-[--radix-popper-anchor-width]">
            <DropdownMenuItem>
              <span>Acme Inc</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarHeader>
</Sidebar>
```

## SidebarFooter

Use the `SidebarFooter` component to add a sticky footer to the sidebar.

```tsx showLineNumbers
<Sidebar>
  <SidebarFooter>
    <SidebarMenu>
      <SidebarMenuItem>
        <SidebarMenuButton>
          <User2 /> Username
        </SidebarMenuButton>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarFooter>
</Sidebar>
```

## SidebarContent

The `SidebarContent` component is used to wrap the content of the sidebar. This is where you add your `SidebarGroup` components. It is scrollable.

```tsx showLineNumbers
<Sidebar>
  <SidebarContent>
    <SidebarGroup />
    <SidebarGroup />
  </SidebarContent>
</Sidebar>
```

## SidebarGroup

Use the `SidebarGroup` component to create a section within the sidebar.

A `SidebarGroup` has a `SidebarGroupLabel`, a `SidebarGroupContent` and an optional `SidebarGroupAction`.

```tsx showLineNumbers
<SidebarGroup>
  <SidebarGroupLabel>Application</SidebarGroupLabel>
  <SidebarGroupAction>
    <Plus /> <span className="sr-only">Add Project</span>
  </SidebarGroupAction>
  <SidebarGroupContent></SidebarGroupContent>
</SidebarGroup>
```

To make a `SidebarGroup` collapsible, wrap it in a `Collapsible`.

```tsx showLineNumbers
<Collapsible defaultOpen className="group/collapsible">
  <SidebarGroup>
    <SidebarGroupLabel asChild>
      <CollapsibleTrigger>
        Help
        <ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" />
      </CollapsibleTrigger>
    </SidebarGroupLabel>
    <CollapsibleContent>
      <SidebarGroupContent />
    </CollapsibleContent>
  </SidebarGroup>
</Collapsible>
```

## SidebarMenu

The `SidebarMenu` component is used for building a menu within a `SidebarGroup`.

<Image
  src="/images/sidebar-menu.png"
  width="716"
  height="420"
  alt="Sidebar Menu"
  className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
/>
<Image
  src="/images/sidebar-menu-dark.png"
  width="716"
  height="420"
  alt="Sidebar Menu"
  className="mt-6 hidden w-full overflow-hidden rounded-lg border dark:block"
/>

```tsx showLineNumbers
<SidebarMenu>
  {projects.map((project) => (
    <SidebarMenuItem key={project.name}>
      <SidebarMenuButton asChild>
        <a href={project.url}>
          <project.icon />
          <span>{project.name}</span>
        </a>
      </SidebarMenuButton>
    </SidebarMenuItem>
  ))}
</SidebarMenu>
```

## SidebarMenuButton

The `SidebarMenuButton` component is used to render a menu button within a `SidebarMenuItem`.

By default, the `SidebarMenuButton` renders a button but you can use the `asChild` prop to render a different component such as a `Link` or an `a` tag.

Use the `isActive` prop to mark a menu item as active.

```tsx showLineNumbers
<SidebarMenuButton asChild isActive>
  <a href="#">Home</a>
</SidebarMenuButton>
```

## SidebarMenuAction

The `SidebarMenuAction` component is used to render a menu action within a `SidebarMenuItem`.

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton asChild>
    <a href="#">
      <Home />
      <span>Home</span>
    </a>
  </SidebarMenuButton>
  <SidebarMenuAction>
    <Plus /> <span className="sr-only">Add Project</span>
  </SidebarMenuAction>
</SidebarMenuItem>
```

## SidebarMenuSub

The `SidebarMenuSub` component is used to render a submenu within a `SidebarMenu`.

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuSub>
    <SidebarMenuSubItem>
      <SidebarMenuSubButton />
    </SidebarMenuSubItem>
  </SidebarMenuSub>
</SidebarMenuItem>
```

## SidebarMenuBadge

The `SidebarMenuBadge` component is used to render a badge within a `SidebarMenuItem`.

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuBadge>24</SidebarMenuBadge>
</SidebarMenuItem>
```

## SidebarMenuSkeleton

The `SidebarMenuSkeleton` component is used to render a skeleton for a `SidebarMenu`.

```tsx showLineNumbers
<SidebarMenu>
  {Array.from({ length: 5 }).map((_, index) => (
    <SidebarMenuItem key={index}>
      <SidebarMenuSkeleton />
    </SidebarMenuItem>
  ))}
</SidebarMenu>
```

## SidebarTrigger

Use the `SidebarTrigger` component to render a button that toggles the sidebar.

```tsx showLineNumbers
import { useSidebar } from "@/components/ui/sidebar"

export function CustomTrigger() {
  const { toggleSidebar } = useSidebar()

  return <button onClick={toggleSidebar}>Toggle Sidebar</button>
}
```

## SidebarRail

The `SidebarRail` component is used to render a rail within a `Sidebar`. This rail can be used to toggle the sidebar.

```tsx showLineNumbers
<Sidebar>
  <SidebarHeader />
  <SidebarContent>
    <SidebarGroup />
  </SidebarContent>
  <SidebarFooter />
  <SidebarRail />
</Sidebar>
```

## Controlled Sidebar

Use the `open` and `onOpenChange` props to control the sidebar.

```tsx showLineNumbers
export function AppSidebar() {
  const [open, setOpen] = React.useState(false)

  return (
    <SidebarProvider open={open} onOpenChange={setOpen}>
      <Sidebar />
    </SidebarProvider>
  )
}
```

## Theming

We use the following CSS variables to theme the sidebar.

```css
@layer base {
  :root {
    --sidebar-background: 0 0% 98%;
    --sidebar-foreground: 240 5.3% 26.1%;
    --sidebar-primary: 240 5.9% 10%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 4.8% 95.9%;
    --sidebar-accent-foreground: 240 5.9% 10%;
    --sidebar-border: 220 13% 91%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }

  .dark {
    --sidebar-background: 240 5.9% 10%;
    --sidebar-foreground: 240 4.8% 95.9%;
    --sidebar-primary: 0 0% 98%;
    --sidebar-primary-foreground: 240 5.9% 10%;
    --sidebar-accent: 240 3.7% 15.9%;
    --sidebar-accent-foreground: 240 4.8% 95.9%;
    --sidebar-border: 240 3.7% 15.9%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
}
```

## Styling

Here are some tips for styling the sidebar based on different states.

```tsx
<Sidebar collapsible="icon">
  <SidebarContent>
    <SidebarGroup className="group-data-[collapsible=icon]:hidden" />
  </SidebarContent>
</Sidebar>
```

```tsx
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuAction className="peer-data-[active=true]/menu-button:opacity-100" />
</SidebarMenuItem>
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

{/* prettier-ignore */}
<Button asChild size="sm" className="mt-6">
  <a href="/view/base-nova/sidebar-rtl" target="_blank">View RTL Sidebar <ExternalLinkIcon /></a>
</Button>

## Changelog

### RTL Support

If you're upgrading from a previous version of the `Sidebar` component, you'll need to apply the following updates to add RTL support:

<Steps>

<Step>Add `dir` prop to Sidebar component.</Step>

Add `dir` to the destructured props and pass it to `SheetContent` for mobile:

```diff
  function Sidebar({
    side = "left",
    variant = "sidebar",
    collapsible = "offcanvas",
    className,
    children,
+   dir,
    ...props
  }: React.ComponentProps<"div"> & {
    side?: "left" | "right"
    variant?: "sidebar" | "floating" | "inset"
    collapsible?: "offcanvas" | "icon" | "none"
  }) {
```

Then pass it to `SheetContent` in the mobile view:

```diff
  <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}>
    <SheetContent
+     dir={dir}
      data-sidebar="sidebar"
      data-slot="sidebar"
      data-mobile="true"
```

<Step>Add `data-side` attribute to sidebar container.</Step>

Add `data-side={side}` to the sidebar container element:

```diff
  <div
    data-slot="sidebar-container"
+   data-side={side}
    className={cn(
```

<Step>Update sidebar container positioning classes.</Step>

Replace JavaScript ternary conditional classes with CSS data attribute selectors:

```diff
  className={cn(
-   "fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex",
-   side === "left"
-     ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
-     : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
+   "fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex data-[side=left]:left-0 data-[side=right]:right-0 data-[side=left]:group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)] data-[side=right]:group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
```

<Step>Update SidebarRail positioning classes.</Step>

Update the `SidebarRail` component to use physical positioning for the rail:

```diff
  className={cn(
-   "hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear group-data-[side=left]:-end-4 group-data-[side=right]:start-0 after:absolute after:inset-y-0 after:start-1/2 after:w-[2px] sm:flex",
+   "hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 ltr:-translate-x-1/2 rtl:-translate-x-1/2 transition-all ease-linear group-data-[side=left]:-right-4 group-data-[side=right]:left-0 after:absolute after:inset-y-0 after:start-1/2 after:w-[2px] sm:flex",
```

<Step>Add RTL flip to SidebarTrigger icon.</Step>

Add `className="rtl:rotate-180"` to the icon in `SidebarTrigger` to flip it in RTL mode:

```diff
  <Button ...>
-   <PanelLeftIcon />
+   <PanelLeftIcon className="rtl:rotate-180" />
    <span className="sr-only">Toggle Sidebar</span>
  </Button>
```

</Steps>

After applying these changes, you can use the `dir` prop to set the direction:

```tsx
<Sidebar dir="rtl" side="right">
  {/* ... */}
</Sidebar>
```

The sidebar will correctly position itself and handle interactions in both LTR and RTL layouts.


---

<!-- SOURCE: apps/v4/content/docs/components/base/skeleton.mdx -->

## apps/v4/content/docs/components/base/skeleton.mdx

---
title: Skeleton
description: Use to show a placeholder while content is loading.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="skeleton-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add skeleton
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="skeleton"
  title="components/ui/skeleton.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Skeleton } from "@/components/ui/skeleton"
```

```tsx
<Skeleton className="h-[20px] w-[100px] rounded-full" />
```

## Examples

### Avatar

<ComponentPreview styleName="base-nova" name="skeleton-avatar" />

### Card

<ComponentPreview
  styleName="base-nova"
  name="skeleton-card"
  previewClassName="h-80"
/>

### Text

<ComponentPreview styleName="base-nova" name="skeleton-text" />

### Form

<ComponentPreview styleName="base-nova" name="skeleton-form" />

### Table

<ComponentPreview styleName="base-nova" name="skeleton-table" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="skeleton-rtl" direction="rtl" />


---

<!-- SOURCE: apps/v4/content/docs/components/base/slider.mdx -->

## apps/v4/content/docs/components/base/slider.mdx

---
title: Slider
description: An input where the user selects a value from within a given range.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/slider
  api: https://base-ui.com/react/components/slider#api-reference
---

<ComponentPreview styleName="base-nova" name="slider-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add slider
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="slider"
  title="components/ui/slider.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Slider } from "@/components/ui/slider"
```

```tsx
<Slider defaultValue={[33]} max={100} step={1} />
```

## Examples

### Range

Use an array with two values for a range slider.

<ComponentPreview styleName="base-nova" name="slider-range" />

### Multiple Thumbs

Use an array with multiple values for multiple thumbs.

<ComponentPreview styleName="base-nova" name="slider-multiple" />

### Vertical

Use `orientation="vertical"` for a vertical slider.

<ComponentPreview styleName="base-nova" name="slider-vertical" />

### Controlled

<ComponentPreview styleName="base-nova" name="slider-controlled" />

### Disabled

Use the `disabled` prop to disable the slider.

<ComponentPreview styleName="base-nova" name="slider-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="slider-rtl" direction="rtl" />

## API Reference

See the [Base UI Slider](https://base-ui.com/react/components/slider#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/sonner.mdx -->

## apps/v4/content/docs/components/base/sonner.mdx

---
title: Sonner
description: An opinionated toast component for React.
base: base
component: true
links:
  doc: https://sonner.emilkowal.ski
---

<ComponentPreview styleName="base-nova" name="sonner-demo" />

## About

Sonner is built and maintained by [emilkowalski](https://twitter.com/emilkowalski).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps className="mb-0 pt-2">

<Step>Run the following command:</Step>

```bash
npx shadcn@latest add sonner
```

<Step>Add the Toaster component.</Step>

```tsx title="app/layout.tsx" {1,9} showLineNumbers
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install sonner next-themes
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="sonner"
  title="components/ui/sonner.tsx"
  styleName="base-nova"
/>

<Step>Add the Toaster component.</Step>

```tsx showLineNumbers title="app/layout.tsx" {1,8}
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <Toaster />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { toast } from "sonner"
```

```tsx
toast("Event has been created.")
```

## Examples

### Types

<ComponentPreview styleName="base-nova" name="sonner-types" />

### Description

<ComponentPreview styleName="base-nova" name="sonner-description" />

### Position

Use the `position` prop to change the position of the toast.

<ComponentPreview styleName="base-nova" name="sonner-position" />

## API Reference

See the [Sonner API Reference](https://sonner.emilkowal.ski/getting-started) for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/base/spinner.mdx -->

## apps/v4/content/docs/components/base/spinner.mdx

---
title: Spinner
description: An indicator that can be used to show a loading state.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="spinner-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add spinner
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="spinner"
  title="components/ui/spinner.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Spinner } from "@/components/ui/spinner"
```

```tsx
<Spinner />
```

## Customization

You can replace the default spinner icon with any other icon by editing the `Spinner` component.

<ComponentPreview styleName="base-nova" name="spinner-custom" />

```tsx showLineNumbers title="components/ui/spinner.tsx"
import { LoaderIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <LoaderIcon
      role="status"
      aria-label="Loading"
      className={cn("size-4 animate-spin", className)}
      {...props}
    />
  )
}

export { Spinner }
```

## Examples

### Size

Use the `size-*` utility class to change the size of the spinner.

<ComponentPreview styleName="base-nova" name="spinner-size" />

### Button

Add a spinner to a button to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

<ComponentPreview styleName="base-nova" name="spinner-button" />

### Badge

Add a spinner to a badge to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

<ComponentPreview styleName="base-nova" name="spinner-badge" />

### Input Group

<ComponentPreview styleName="base-nova" name="spinner-input-group" />

### Empty

<ComponentPreview styleName="base-nova" name="spinner-empty" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="spinner-rtl" direction="rtl" />


---

<!-- SOURCE: apps/v4/content/docs/components/base/switch.mdx -->

## apps/v4/content/docs/components/base/switch.mdx

---
title: Switch
description: A control that allows the user to toggle between checked and not checked.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/switch
  api: https://base-ui.com/react/components/switch#api-reference
---

<ComponentPreview styleName="base-nova" name="switch-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add switch
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="switch"
  title="components/ui/switch.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Switch } from "@/components/ui/switch"
```

```tsx
<Switch />
```

## Examples

### Description

<ComponentPreview styleName="base-nova" name="switch-description" />

### Choice Card

Card-style selection where `FieldLabel` wraps the entire `Field` for a clickable card pattern.

<ComponentPreview styleName="base-nova" name="switch-choice-card" />

### Disabled

Add the `disabled` prop to the `Switch` component to disable the switch. Add the `data-disabled` prop to the `Field` component for styling.

<ComponentPreview styleName="base-nova" name="switch-disabled" />

### Invalid

Add the `aria-invalid` prop to the `Switch` component to indicate an invalid state. Add the `data-invalid` prop to the `Field` component for styling.

<ComponentPreview styleName="base-nova" name="switch-invalid" />

### Size

Use the `size` prop to change the size of the switch.

<ComponentPreview styleName="base-nova" name="switch-sizes" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="switch-rtl" direction="rtl" />

## API Reference

See the [Base UI Switch](https://base-ui.com/react/components/switch#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/table.mdx -->

## apps/v4/content/docs/components/base/table.mdx

---
title: Table
description: A responsive table component.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="table-demo"
  previewClassName="h-[30rem]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add table
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="table"
  title="components/ui/table.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
```

```tsx showLineNumbers
<Table>
  <TableCaption>A list of your recent invoices.</TableCaption>
  <TableHeader>
    <TableRow>
      <TableHead className="w-[100px]">Invoice</TableHead>
      <TableHead>Status</TableHead>
      <TableHead>Method</TableHead>
      <TableHead className="text-right">Amount</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell className="font-medium">INV001</TableCell>
      <TableCell>Paid</TableCell>
      <TableCell>Credit Card</TableCell>
      <TableCell className="text-right">$250.00</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

## Examples

### Footer

Use the `<TableFooter />` component to add a footer to the table.

<ComponentPreview styleName="base-nova" name="table-footer" />

### Actions

A table showing actions for each row using a `<DropdownMenu />` component.

<ComponentPreview styleName="base-nova" name="table-actions" />

## Data Table

You can use the `<Table />` component to build more complex data tables. Combine it with [@tanstack/react-table](https://tanstack.com/table/v8) to create tables with sorting, filtering and pagination.

See the [Data Table](/docs/components/data-table) documentation for more information.

You can also see an example of a data table in the [Tasks](/examples/tasks) demo.

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="table-rtl"
  direction="rtl"
  previewClassName="h-auto"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/base/tabs.mdx -->

## apps/v4/content/docs/components/base/tabs.mdx

---
title: Tabs
description: A set of layered sections of content—known as tab panels—that are displayed one at a time.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/tabs
  api: https://base-ui.com/react/components/tabs#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="tabs-demo"
  previewClassName="h-96"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add tabs
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="tabs"
  title="components/ui/tabs.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
```

```tsx showLineNumbers
<Tabs defaultValue="account" className="w-[400px]">
  <TabsList>
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent value="account">Make changes to your account here.</TabsContent>
  <TabsContent value="password">Change your password here.</TabsContent>
</Tabs>
```

## Examples

### Line

Use the `variant="line"` prop on `TabsList` for a line style.

<ComponentPreview styleName="base-nova" name="tabs-line" />

### Vertical

Use `orientation="vertical"` for vertical tabs.

<ComponentPreview styleName="base-nova" name="tabs-vertical" />

### Disabled

<ComponentPreview styleName="base-nova" name="tabs-disabled" />

### Icons

<ComponentPreview styleName="base-nova" name="tabs-icons" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="tabs-rtl" direction="rtl" />

## API Reference

See the [Base UI Tabs](https://base-ui.com/react/components/tabs#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/textarea.mdx -->

## apps/v4/content/docs/components/base/textarea.mdx

---
title: Textarea
description: Displays a form textarea or a component that looks like a textarea.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="textarea-demo"
  previewClassName="*:max-w-xs"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add textarea
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="textarea"
  title="components/ui/textarea.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Textarea } from "@/components/ui/textarea"
```

```tsx
<Textarea />
```

## Examples

### Field

Use `Field`, `FieldLabel`, and `FieldDescription` to create a textarea with a label and description.

<ComponentPreview
  styleName="base-nova"
  name="textarea-field"
  previewClassName="*:max-w-xs"
/>

### Disabled

Use the `disabled` prop to disable the textarea. To style the disabled state, add the `data-disabled` attribute to the `Field` component.

<ComponentPreview
  styleName="base-nova"
  name="textarea-disabled"
  previewClassName="*:max-w-xs"
/>

### Invalid

Use the `aria-invalid` prop to mark the textarea as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field` component.

<ComponentPreview
  styleName="base-nova"
  name="textarea-invalid"
  previewClassName="*:max-w-xs"
/>

### Button

Pair with `Button` to create a textarea with a submit button.

<ComponentPreview
  styleName="base-nova"
  name="textarea-button"
  previewClassName="*:max-w-xs"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="textarea-rtl" direction="rtl" />


---

<!-- SOURCE: apps/v4/content/docs/components/base/toast.mdx -->

## apps/v4/content/docs/components/base/toast.mdx

---
title: Toast
description: A succinct message that is displayed temporarily.
base: base
component: true
---

The toast component has been deprecated. Use the [sonner](/docs/components/sonner) component instead.


---

<!-- SOURCE: apps/v4/content/docs/components/base/toggle-group.mdx -->

## apps/v4/content/docs/components/base/toggle-group.mdx

---
title: Toggle Group
description: A set of two-state buttons that can be toggled on or off.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/toggle-group
  api: https://base-ui.com/react/components/toggle-group#api-reference
---

<ComponentPreview styleName="base-nova" name="toggle-group-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="toggle-group"
  title="components/ui/toggle-group.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
```

```tsx
<ToggleGroup type="single">
  <ToggleGroupItem value="a">A</ToggleGroupItem>
  <ToggleGroupItem value="b">B</ToggleGroupItem>
  <ToggleGroupItem value="c">C</ToggleGroupItem>
</ToggleGroup>
```

## Examples

### Outline

Use `variant="outline"` for an outline style.

<ComponentPreview styleName="base-nova" name="toggle-group-outline" />

### Size

Use the `size` prop to change the size of the toggle group.

<ComponentPreview styleName="base-nova" name="toggle-group-sizes" />

### Spacing

Use `spacing` to add spacing between toggle group items.

<ComponentPreview styleName="base-nova" name="toggle-group-spacing" />

### Vertical

Use `orientation="vertical"` for vertical toggle groups.

<ComponentPreview styleName="base-nova" name="toggle-group-vertical" />

### Disabled

<ComponentPreview styleName="base-nova" name="toggle-group-disabled" />

### Custom

A custom toggle group example.

<ComponentPreview
  styleName="base-nova"
  name="toggle-group-font-weight-selector"
  previewClassName="*:data-[slot=field]:max-w-xs"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="toggle-group-rtl"
  direction="rtl"
/>

## API Reference

See the [Base UI Toggle Group](https://base-ui.com/react/components/toggle-group#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/toggle.mdx -->

## apps/v4/content/docs/components/base/toggle.mdx

---
title: Toggle
description: A two-state button that can be either on or off.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/toggle
  api: https://base-ui.com/react/components/toggle#api-reference
---

<ComponentPreview styleName="base-nova" name="toggle-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="toggle"
  title="components/ui/toggle.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Toggle } from "@/components/ui/toggle"
```

```tsx
<Toggle>Toggle</Toggle>
```

## Examples

### Outline

Use `variant="outline"` for an outline style.

<ComponentPreview styleName="base-nova" name="toggle-outline" />

### With Text

<ComponentPreview styleName="base-nova" name="toggle-text" />

### Size

Use the `size` prop to change the size of the toggle.

<ComponentPreview styleName="base-nova" name="toggle-sizes" />

### Disabled

<ComponentPreview styleName="base-nova" name="toggle-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="toggle-rtl" direction="rtl" />

## API Reference

See the [Base UI Toggle](https://base-ui.com/react/components/toggle#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/tooltip.mdx -->

## apps/v4/content/docs/components/base/tooltip.mdx

---
title: Tooltip
description: A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/tooltip
  api: https://base-ui.com/react/components/tooltip#api-reference
---

<ComponentPreview styleName="base-nova" name="tooltip-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps className="mb-0 pt-2">

<Step>Run the following command:</Step>

```bash
npx shadcn@latest add tooltip
```

<Step>Add the `TooltipProvider` to the root of your app.</Step>

```tsx title="app/layout.tsx" showLineNumbers {1,7}
import { TooltipProvider } from "@/components/ui/tooltip"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <TooltipProvider>{children}</TooltipProvider>
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="tooltip"
  title="components/ui/tooltip.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

<Step>Add the `TooltipProvider` to the root of your app.</Step>

```tsx title="app/layout.tsx" showLineNumbers {1,7}
import { TooltipProvider } from "@/components/ui/tooltip"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <TooltipProvider>{children}</TooltipProvider>
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
```

```tsx showLineNumbers
<Tooltip>
  <TooltipTrigger>Hover</TooltipTrigger>
  <TooltipContent>
    <p>Add to library</p>
  </TooltipContent>
</Tooltip>
```

## Examples

### Side

Use the `side` prop to change the position of the tooltip.

<ComponentPreview styleName="base-nova" name="tooltip-sides" />

### With Keyboard Shortcut

<ComponentPreview styleName="base-nova" name="tooltip-keyboard" />

### Disabled Button

Show a tooltip on a disabled button by wrapping it with a span.

<ComponentPreview styleName="base-nova" name="tooltip-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="tooltip-rtl" direction="rtl" />

## API Reference

See the [Base UI Tooltip](https://base-ui.com/react/components/tooltip#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/base/typography.mdx -->

## apps/v4/content/docs/components/base/typography.mdx

---
title: Typography
description: Styles for headings, paragraphs, lists, etc.
base: base
component: true
---

We do not ship any typography styles by default. This page is an example of how you can use utility classes to style your text.

<ComponentPreview
  styleName="base-nova"
  name="typography-demo"
  className="[&_.preview]:h-auto!"
  hideCode
/>

## h1

<ComponentPreview styleName="base-nova" name="typography-h1" />

## h2

<ComponentPreview styleName="base-nova" name="typography-h2" />

## h3

<ComponentPreview styleName="base-nova" name="typography-h3" />

## h4

<ComponentPreview styleName="base-nova" name="typography-h4" />

## p

<ComponentPreview styleName="base-nova" name="typography-p" />

## blockquote

<ComponentPreview styleName="base-nova" name="typography-blockquote" />

## table

<ComponentPreview styleName="base-nova" name="typography-table" />

## list

<ComponentPreview styleName="base-nova" name="typography-list" />

## Inline code

<ComponentPreview styleName="base-nova" name="typography-inline-code" />

## Lead

<ComponentPreview styleName="base-nova" name="typography-lead" />

## Large

<ComponentPreview styleName="base-nova" name="typography-large" />

## Small

<ComponentPreview styleName="base-nova" name="typography-small" />

## Muted

<ComponentPreview styleName="base-nova" name="typography-muted" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="typography-rtl"
  direction="rtl"
  className="[&_.preview]:h-auto!"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/index.mdx -->

## apps/v4/content/docs/components/index.mdx

---
title: Components
description: Here you can find all the components available in the library. We are working on adding more components.
---

<ComponentsList />

---

Can't find what you need? Try the [registry directory](/docs/directory) for community-maintained components.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/accordion.mdx -->

## apps/v4/content/docs/components/radix/accordion.mdx

---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/primitives/docs/components/accordion
  api: https://www.radix-ui.com/primitives/docs/components/accordion#api-reference
---

<ComponentPreview
  name="accordion-demo"
  styleName="radix-nova"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add accordion
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="accordion"
  title="components/ui/accordion.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"
```

```tsx showLineNumbers
<Accordion type="single" collapsible defaultValue="item-1">
  <AccordionItem value="item-1">
    <AccordionTrigger>Is it accessible?</AccordionTrigger>
    <AccordionContent>
      Yes. It adheres to the WAI-ARIA design pattern.
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

## Examples

### Basic

A basic accordion that shows one item at a time. The first item is open by default.

<ComponentPreview
  name="accordion-basic"
  styleName="radix-nova"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Multiple

Use `type="multiple"` to allow multiple items to be open at the same time.

<ComponentPreview
  name="accordion-multiple"
  styleName="radix-nova"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[36rem] md:h-[30rem]"
/>

### Disabled

Use the `disabled` prop on `AccordionItem` to disable individual items.

<ComponentPreview
  name="accordion-disabled"
  styleName="radix-nova"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Borders

Add `border` to the `Accordion` and `border-b last:border-b-0` to the `AccordionItem` to add borders to the items.

<ComponentPreview
  name="accordion-borders"
  styleName="radix-nova"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-96 md:h-80"
/>

### Card

Wrap the `Accordion` in a `Card` component.

<ComponentPreview
  name="accordion-card"
  styleName="radix-nova"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[32rem] md:h-[28rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="accordion-rtl"
  align="start"
  direction="rtl"
/>

## API Reference

See the [Radix UI](https://www.radix-ui.com/primitives/docs/components/accordion#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/alert-dialog.mdx -->

## apps/v4/content/docs/components/radix/alert-dialog.mdx

---
title: Alert Dialog
description: A modal dialog that interrupts the user with important content and expects a response.
featured: true
base: radix
component: true
links:
  doc: https://www.radix-ui.com/primitives/docs/components/alert-dialog
  api: https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference
---

<ComponentPreview
  name="alert-dialog-demo"
  styleName="radix-nova"
  previewClassName="h-56"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add alert-dialog
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="alert-dialog"
  title="components/ui/alert-dialog.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
```

```tsx showLineNumbers
<AlertDialog>
  <AlertDialogTrigger asChild>
    <Button variant="outline">Show Dialog</Button>
  </AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
      <AlertDialogDescription>
        This action cannot be undone. This will permanently delete your account
        from our servers.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction>Continue</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

## Examples

### Basic

A basic alert dialog with a title, description, and cancel and continue buttons.

<ComponentPreview
  name="alert-dialog-basic"
  styleName="radix-nova"
  previewClassName="h-56"
/>

### Small

Use the `size="sm"` prop to make the alert dialog smaller.

<ComponentPreview
  name="alert-dialog-small"
  styleName="radix-nova"
  previewClassName="h-56"
/>

### Media

Use the `AlertDialogMedia` component to add a media element such as an icon or image to the alert dialog.

<ComponentPreview
  name="alert-dialog-media"
  styleName="radix-nova"
  previewClassName="h-56"
/>

### Small with Media

Use the `size="sm"` prop to make the alert dialog smaller and the `AlertDialogMedia` component to add a media element such as an icon or image to the alert dialog.

<ComponentPreview
  name="alert-dialog-small-media"
  styleName="radix-nova"
  previewClassName="h-56"
/>

### Destructive

Use the `AlertDialogAction` component to add a destructive action button to the alert dialog.

<ComponentPreview
  name="alert-dialog-destructive"
  styleName="radix-nova"
  previewClassName="h-56"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="alert-dialog-rtl"
  direction="rtl"
  previewClassName="h-56"
/>

## API Reference

### size

Use the `size` prop on the `AlertDialogContent` component to control the size of the alert dialog. It accepts the following values:

| Prop   | Type                | Default     |
| ------ | ------------------- | ----------- |
| `size` | `"default" \| "sm"` | `"default"` |

For more information about the other components and their props, see the [Radix UI documentation](https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference).


---

<!-- SOURCE: apps/v4/content/docs/components/radix/alert.mdx -->

## apps/v4/content/docs/components/radix/alert.mdx

---
title: Alert
description: Displays a callout for user attention.
base: radix
component: true
---

<ComponentPreview
  name="alert-demo"
  styleName="radix-nova"
  previewClassName="h-auto sm:h-72 p-6"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add alert
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="alert"
  title="components/ui/alert.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Alert,
  AlertAction,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert"
```

```tsx showLineNumbers
<Alert>
  <InfoIcon />
  <AlertTitle>Heads up!</AlertTitle>
  <AlertDescription>
    You can add components and dependencies to your app using the cli.
  </AlertDescription>
  <AlertAction>
    <Button variant="outline">Enable</Button>
  </AlertAction>
</Alert>
```

## Examples

### Basic

A basic alert with an icon, title and description.

<ComponentPreview
  name="alert-basic"
  styleName="radix-nova"
  previewClassName="h-auto sm:h-72 p-6"
/>

### Destructive

Use `variant="destructive"` to create a destructive alert.

<ComponentPreview
  name="alert-destructive"
  styleName="radix-nova"
  previewClassName="h-auto sm:h-72 p-6"
/>

### Action

Use `AlertAction` to add a button or other action element to the alert.

<ComponentPreview
  name="alert-action"
  styleName="radix-nova"
  previewClassName="h-auto sm:h-72 p-6"
/>

### Custom Colors

You can customize the alert colors by adding custom classes such as `bg-amber-50 dark:bg-amber-950` to the `Alert` component.

<ComponentPreview
  name="alert-colors"
  styleName="radix-nova"
  previewClassName="h-auto sm:h-72 p-6"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="alert-rtl"
  direction="rtl"
  previewClassName="h-auto sm:h-72 p-6"
/>

## API Reference

### Alert

The `Alert` component displays a callout for user attention.

| Prop      | Type                         | Default     |
| --------- | ---------------------------- | ----------- |
| `variant` | `"default" \| "destructive"` | `"default"` |

### AlertTitle

The `AlertTitle` component displays the title of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AlertDescription

The `AlertDescription` component displays the description or content of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AlertAction

The `AlertAction` component displays an action element (like a button) positioned absolutely in the top-right corner of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |


---

<!-- SOURCE: apps/v4/content/docs/components/radix/aspect-ratio.mdx -->

## apps/v4/content/docs/components/radix/aspect-ratio.mdx

---
title: Aspect Ratio
description: Displays content within a desired ratio.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/primitives/docs/components/aspect-ratio
  api: https://www.radix-ui.com/primitives/docs/components/aspect-ratio#api-reference
---

<ComponentPreview name="aspect-ratio-demo" styleName="radix-nova" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add aspect-ratio
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="aspect-ratio"
  title="components/ui/aspect-ratio.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { AspectRatio } from "@/components/ui/aspect-ratio"
```

```tsx showLineNumbers
<AspectRatio ratio={16 / 9}>
  <Image src="..." alt="Image" className="rounded-md object-cover" />
</AspectRatio>
```

## Examples

### Square

A square aspect ratio component using the `ratio={1 / 1}` prop. This is useful for displaying images in a square format.

<ComponentPreview name="aspect-ratio-square" styleName="radix-nova" />

### Portrait

A portrait aspect ratio component using the `ratio={9 / 16}` prop. This is useful for displaying images in a portrait format.

<ComponentPreview
  name="aspect-ratio-portrait"
  styleName="radix-nova"
  previewClassName="h-96"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="aspect-ratio-rtl"
  direction="rtl"
  previewClassName="h-96"
/>

## API Reference

### AspectRatio

The `AspectRatio` component displays content within a desired ratio.

| Prop        | Type     | Default | Required |
| ----------- | -------- | ------- | -------- |
| `ratio`     | `number` | -       | Yes      |
| `className` | `string` | -       | No       |

For more information, see the [Radix UI documentation](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#api-reference).


---

<!-- SOURCE: apps/v4/content/docs/components/radix/avatar.mdx -->

## apps/v4/content/docs/components/radix/avatar.mdx

---
title: Avatar
description: An image element with a fallback for representing the user.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/primitives/docs/components/avatar
  api: https://www.radix-ui.com/primitives/docs/components/avatar#api-reference
---

<ComponentPreview styleName="radix-nova" name="avatar-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add avatar
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="avatar"
  title="components/ui/avatar.tsx"

/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
```

```tsx showLineNumbers
<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" />
  <AvatarFallback>CN</AvatarFallback>
</Avatar>
```

## Examples

### Basic

A basic avatar component with an image and a fallback.

<ComponentPreview styleName="radix-nova" name="avatar-basic" />

### Badge

Use the `AvatarBadge` component to add a badge to the avatar. The badge is positioned at the bottom right of the avatar.

<ComponentPreview styleName="radix-nova" name="avatar-badge" />

Use the `className` prop to add custom styles to the badge such as custom colors, sizes, etc.

```tsx showLineNumbers
<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
  <AvatarFallback>CN</AvatarFallback>
  <AvatarBadge className="bg-green-600 dark:bg-green-800" />
</Avatar>
```

### Badge with Icon

You can also use an icon inside `<AvatarBadge>`.

<ComponentPreview
  name="avatar-badge-icon"
  styleName="radix-nova"

/>

### Avatar Group

Use the `AvatarGroup` component to add a group of avatars.

<ComponentPreview
  name="avatar-group"
  styleName="radix-nova"

/>

### Avatar Group Count

Use `<AvatarGroupCount>` to add a count to the group.

<ComponentPreview
  name="avatar-group-count"
  styleName="radix-nova"

/>

### Avatar Group with Icon

You can also use an icon inside `<AvatarGroupCount>`.

<ComponentPreview
  name="avatar-group-count-icon"
  styleName="radix-nova"

/>

### Sizes

Use the `size` prop to change the size of the avatar.

<ComponentPreview
  name="avatar-size"
  styleName="radix-nova"

/>

### Dropdown

You can use the `Avatar` component as a trigger for a dropdown menu.

<ComponentPreview styleName="radix-nova" name="avatar-dropdown" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="avatar-rtl"
  direction="rtl"
  previewClassName="h-72"
/>

## API Reference

### Avatar

The `Avatar` component is the root component that wraps the avatar image and fallback.

| Prop        | Type                        | Default     |
| ----------- | --------------------------- | ----------- |
| `size`      | `"default" \| "sm" \| "lg"` | `"default"` |
| `className` | `string`                    | -           |

### AvatarImage

The `AvatarImage` component displays the avatar image. It accepts all Radix UI Avatar Image props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `src`       | `string` | -       |
| `alt`       | `string` | -       |
| `className` | `string` | -       |

### AvatarFallback

The `AvatarFallback` component displays a fallback when the image fails to load. It accepts all Radix UI Avatar Fallback props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarBadge

The `AvatarBadge` component displays a badge indicator on the avatar, typically positioned at the bottom right.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarGroup

The `AvatarGroup` component displays a group of avatars with overlapping styling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarGroupCount

The `AvatarGroupCount` component displays a count indicator in an avatar group, typically showing the number of additional avatars.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

For more information about Radix UI Avatar props, see the [Radix UI documentation](https://www.radix-ui.com/primitives/docs/components/avatar#api-reference).


---

<!-- SOURCE: apps/v4/content/docs/components/radix/badge.mdx -->

## apps/v4/content/docs/components/radix/badge.mdx

---
title: Badge
description: Displays a badge or a component that looks like a badge.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="badge-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add badge
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="badge" title="components/ui/badge.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Badge } from "@/components/ui/badge"
```

```tsx
<Badge variant="default | outline | secondary | destructive">Badge</Badge>
```

## Examples

### Variants

Use the `variant` prop to change the variant of the badge.

<ComponentPreview styleName="radix-nova" name="badge-variants" />

### With Icon

You can render an icon inside the badge. Use `data-icon="inline-start"` to render the icon on the left and `data-icon="inline-end"` to render the icon on the right.

<ComponentPreview styleName="radix-nova" name="badge-icon" />

### With Spinner

You can render a spinner inside the badge. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` prop to the spinner.

<ComponentPreview styleName="radix-nova" name="badge-spinner" />

### Link

Use the `asChild` prop to render a link as a badge.

<ComponentPreview styleName="radix-nova" name="badge-link" />

### Custom Colors

You can customize the colors of a badge by adding custom classes such as `bg-green-50 dark:bg-green-800` to the `Badge` component.

<ComponentPreview styleName="radix-nova" name="badge-colors" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="badge-rtl" direction="rtl" />

## API Reference

### Badge

The `Badge` component displays a badge or a component that looks like a badge.

| Prop        | Type                                                                          | Default     |
| ----------- | ----------------------------------------------------------------------------- | ----------- |
| `variant`   | `"default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link"` | `"default"` |
| `className` | `string`                                                                      | -           |


---

<!-- SOURCE: apps/v4/content/docs/components/radix/breadcrumb.mdx -->

## apps/v4/content/docs/components/radix/breadcrumb.mdx

---
title: Breadcrumb
description: Displays the path to the current resource using a hierarchy of links.
base: radix
component: true
---

<ComponentPreview
  styleName="radix-nova"
  name="breadcrumb-demo"
  previewClassName="p-2"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add breadcrumb
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="breadcrumb" title="components/ui/breadcrumb.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
```

```tsx showLineNumbers
<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink href="/">Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbLink href="/components">Components</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

## Examples

### Basic

A basic breadcrumb with a home link and a components link.

<ComponentPreview styleName="radix-nova" name="breadcrumb-basic" />

### Custom separator

Use a custom component as `children` for `<BreadcrumbSeparator />` to create a custom separator.

<ComponentPreview styleName="radix-nova" name="breadcrumb-separator" />

### Dropdown

You can compose `<BreadcrumbItem />` with a `<DropdownMenu />` to create a dropdown in the breadcrumb.

<ComponentPreview styleName="radix-nova" name="breadcrumb-dropdown" />

### Collapsed

We provide a `<BreadcrumbEllipsis />` component to show a collapsed state when the breadcrumb is too long.

<ComponentPreview
  styleName="radix-nova"
  name="breadcrumb-ellipsis"
  previewClassName="p-2"
/>

### Link component

To use a custom link component from your routing library, you can use the `asChild` prop on `<BreadcrumbLink />`.

<ComponentPreview styleName="radix-nova" name="breadcrumb-link" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="breadcrumb-rtl"
  direction="rtl"
  previewClassName="p-2"
/>

## API Reference

### Breadcrumb

The `Breadcrumb` component is the root navigation element that wraps all breadcrumb components.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbList

The `BreadcrumbList` component displays the ordered list of breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbItem

The `BreadcrumbItem` component wraps individual breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbLink

The `BreadcrumbLink` component displays a clickable link in the breadcrumb.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbPage

The `BreadcrumbPage` component displays the current page in the breadcrumb (non-clickable).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbSeparator

The `BreadcrumbSeparator` component displays a separator between breadcrumb items. You can pass custom children to override the default separator icon.

| Prop        | Type              | Default |
| ----------- | ----------------- | ------- |
| `children`  | `React.ReactNode` | -       |
| `className` | `string`          | -       |

### BreadcrumbEllipsis

The `BreadcrumbEllipsis` component displays an ellipsis indicator for collapsed breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |


---

<!-- SOURCE: apps/v4/content/docs/components/radix/button-group.mdx -->

## apps/v4/content/docs/components/radix/button-group.mdx

---
title: Button Group
description: A container that groups related buttons together with consistent styling.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="button-group-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add button-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="button-group"
  title="components/ui/button-group.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import {
  ButtonGroup,
  ButtonGroupSeparator,
  ButtonGroupText,
} from "@/components/ui/button-group"
```

```tsx
<ButtonGroup>
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

## Accessibility

- The `ButtonGroup` component has the `role` attribute set to `group`.
- Use <Kbd>Tab</Kbd> to navigate between the buttons in the group.
- Use `aria-label` or `aria-labelledby` to label the button group.

```tsx showLineNumbers
<ButtonGroup aria-label="Button group">
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

## ButtonGroup vs ToggleGroup

- Use the `ButtonGroup` component when you want to group buttons that perform an action.
- Use the `ToggleGroup` component when you want to group buttons that toggle a state.

## Examples

### Orientation

Set the `orientation` prop to change the button group layout.

<ComponentPreview styleName="radix-nova" name="button-group-orientation" />

### Size

Control the size of buttons using the `size` prop on individual buttons.

<ComponentPreview styleName="radix-nova" name="button-group-size" />

### Nested

Nest `<ButtonGroup>` components to create button groups with spacing.

<ComponentPreview styleName="radix-nova" name="button-group-nested" />

### Separator

The `ButtonGroupSeparator` component visually divides buttons within a group.

Buttons with variant `outline` do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.

<ComponentPreview styleName="radix-nova" name="button-group-separator" />

### Split

Create a split button group by adding two buttons separated by a `ButtonGroupSeparator`.

<ComponentPreview styleName="radix-nova" name="button-group-split" />

### Input

Wrap an `Input` component with buttons.

<ComponentPreview styleName="radix-nova" name="button-group-input" />

### Input Group

Wrap an `InputGroup` component to create complex input layouts.

<ComponentPreview styleName="radix-nova" name="button-group-input-group" />

### Dropdown Menu

Create a split button group with a `DropdownMenu` component.

<ComponentPreview styleName="radix-nova" name="button-group-dropdown" />

### Select

Pair with a `Select` component.

<ComponentPreview styleName="radix-nova" name="button-group-select" />

### Popover

Use with a `Popover` component.

<ComponentPreview styleName="radix-nova" name="button-group-popover" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="button-group-rtl"
  direction="rtl"
/>

## API Reference

### ButtonGroup

The `ButtonGroup` component is a container that groups related buttons together with consistent styling.

| Prop          | Type                         | Default        |
| ------------- | ---------------------------- | -------------- |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` |

```tsx
<ButtonGroup>
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

Nest multiple button groups to create complex layouts with spacing. See the [nested](#nested) example for more details.

```tsx
<ButtonGroup>
  <ButtonGroup />
  <ButtonGroup />
</ButtonGroup>
```

### ButtonGroupSeparator

The `ButtonGroupSeparator` component visually divides buttons within a group.

| Prop          | Type                         | Default      |
| ------------- | ---------------------------- | ------------ |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` |

```tsx
<ButtonGroup>
  <Button>Button 1</Button>
  <ButtonGroupSeparator />
  <Button>Button 2</Button>
</ButtonGroup>
```

### ButtonGroupText

Use this component to display text within a button group.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

```tsx
<ButtonGroup>
  <ButtonGroupText>Text</ButtonGroupText>
  <Button>Button</Button>
</ButtonGroup>
```

Use the `asChild` prop to render a custom component as the text, for example a label.

```tsx showLineNumbers
import { ButtonGroupText } from "@/components/ui/button-group"
import { Label } from "@/components/ui/label"

export function ButtonGroupTextDemo() {
  return (
    <ButtonGroup>
      <ButtonGroupText asChild>
        <Label htmlFor="name">Text</Label>
      </ButtonGroupText>
      <Input placeholder="Type something here..." id="name" />
    </ButtonGroup>
  )
}
```


---

<!-- SOURCE: apps/v4/content/docs/components/radix/button.mdx -->

## apps/v4/content/docs/components/radix/button.mdx

---
title: Button
description: Displays a button or a component that looks like a button.
featured: true
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="button-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add button
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="button"
  title="components/ui/button.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Button } from "@/components/ui/button"
```

```tsx
<Button variant="outline">Button</Button>
```

## Cursor

Tailwind v4 [switched](https://tailwindcss.com/docs/upgrade-guide#buttons-use-the-default-cursor) from `cursor: pointer` to `cursor: default` for the button component.

If you want to keep the `cursor: pointer` behavior, add the following code to your CSS file:

```css showLineNumbers title="globals.css"
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

## Examples

### Size

Use the `size` prop to change the size of the button.

<ComponentPreview styleName="radix-nova" name="button-size" />

### Default

<ComponentPreview styleName="radix-nova" name="button-default" />

### Outline

<ComponentPreview styleName="radix-nova" name="button-outline" />

### Secondary

<ComponentPreview styleName="radix-nova" name="button-secondary" />

### Ghost

<ComponentPreview styleName="radix-nova" name="button-ghost" />

### Destructive

<ComponentPreview styleName="radix-nova" name="button-destructive" />

### Link

<ComponentPreview styleName="radix-nova" name="button-link" />

### Icon

<ComponentPreview styleName="radix-nova" name="button-icon" />

### With Icon

Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the icon for the correct spacing.

<ComponentPreview styleName="radix-nova" name="button-with-icon" />

### Rounded

Use the `rounded-full` class to make the button rounded.

<ComponentPreview styleName="radix-nova" name="button-rounded" />

### Spinner

Render a `<Spinner />` component inside the button to show a loading state. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the spinner for the correct spacing.

<ComponentPreview styleName="radix-nova" name="button-spinner" />

### Button Group

To create a button group, use the `ButtonGroup` component. See the [Button Group](/docs/components/radix/button-group) documentation for more details.

<ComponentPreview styleName="radix-nova" name="button-group-demo" />

### As Child

You can use the `asChild` prop on `<Button />` to make another component look like a button. Here's an example of a link that looks like a button.

<ComponentPreview styleName="radix-nova" name="button-aschild" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="button-rtl" direction="rtl" />

## API Reference

### Button

The `Button` component is a wrapper around the `button` element that adds a variety of styles and functionality.

| Prop      | Type                                                                                 | Default     |
| --------- | ------------------------------------------------------------------------------------ | ----------- |
| `variant` | `"default" \| "outline" \| "ghost" \| "destructive" \| "secondary" \| "link"`        | `"default"` |
| `size`    | `"default" \| "xs" \| "sm" \| "lg" \| "icon" \| "icon-xs" \| "icon-sm" \| "icon-lg"` | `"default"` |
| `asChild` | `boolean`                                                                            | `false`     |


---

<!-- SOURCE: apps/v4/content/docs/components/radix/calendar.mdx -->

## apps/v4/content/docs/components/radix/calendar.mdx

---
title: Calendar
description: A calendar component that allows users to select a date or a range of dates.
base: radix
component: true
links:
  doc: https://react-day-picker.js.org
---

<ComponentPreview
  styleName="radix-nova"
  name="calendar-demo"
  previewClassName="h-96"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add calendar
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install react-day-picker date-fns
```

<Step>Add the `Button` component to your project.</Step>

The `Calendar` component uses the `Button` component. Make sure you have it installed in your project.

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="calendar"
  title="components/ui/calendar.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Calendar } from "@/components/ui/calendar"
```

```tsx showLineNumbers
const [date, setDate] = React.useState<Date | undefined>(new Date())

return (
  <Calendar
    mode="single"
    selected={date}
    onSelect={setDate}
    className="rounded-lg border"
  />
)
```

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information.

## About

The `Calendar` component is built on top of [React DayPicker](https://react-day-picker.js.org).

## Date Picker

You can use the `<Calendar>` component to build a date picker. See the [Date Picker](/docs/components/radix/date-picker) page for more information.

## Persian / Hijri / Jalali Calendar

To use the Persian calendar, edit `components/ui/calendar.tsx` and replace `react-day-picker` with `react-day-picker/persian`.

```diff
- import { DayPicker } from "react-day-picker"
+ import { DayPicker } from "react-day-picker/persian"
```

<ComponentPreview
  styleName="radix-nova"
  name="calendar-hijri"
  title="Persian / Hijri / Jalali Calendar"
  description="A Persian calendar."
  previewClassName="h-[400px]"
/>

## Selected Date (With TimeZone)

The Calendar component accepts a `timeZone` prop to ensure dates are displayed and selected in the user's local timezone.

```tsx showLineNumbers
export function CalendarWithTimezone() {
  const [date, setDate] = React.useState<Date | undefined>(undefined)
  const [timeZone, setTimeZone] = React.useState<string | undefined>(undefined)

  React.useEffect(() => {
    setTimeZone(Intl.DateTimeFormat().resolvedOptions().timeZone)
  }, [])

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
      timeZone={timeZone}
    />
  )
}
```

**Note:** If you notice a selected date offset (for example, selecting the 20th highlights the 19th), make sure the `timeZone` prop is set to the user's local timezone.

**Why client-side?** The timezone is detected using `Intl.DateTimeFormat().resolvedOptions().timeZone` inside a `useEffect` to ensure compatibility with server-side rendering. Detecting the timezone during render would cause hydration mismatches, as the server and client may be in different timezones.

## Examples

### Basic

A basic calendar component. We used `className="rounded-lg border"` to style the calendar.

<ComponentPreview
  styleName="radix-nova"
  name="calendar-basic"
  previewClassName="h-96"
/>

### Range Calendar

Use the `mode="range"` prop to enable range selection.

<ComponentPreview
  styleName="radix-nova"
  name="calendar-range"
  previewClassName="h-[36rem] md:h-96"
/>

### Month and Year Selector

Use `captionLayout="dropdown"` to show month and year dropdowns.

<ComponentPreview
  styleName="radix-nova"
  name="calendar-caption"
  previewClassName="h-96"
/>

### Presets

<ComponentPreview
  styleName="radix-nova"
  name="calendar-presets"
  previewClassName="h-[650px]"
/>

### Date and Time Picker

<ComponentPreview
  styleName="radix-nova"
  name="calendar-time"
  previewClassName="h-[600px]"
/>

### Booked dates

<ComponentPreview
  styleName="radix-nova"
  name="calendar-booked-dates"
  previewClassName="h-96"
/>

### Custom Cell Size

<ComponentPreview
  styleName="radix-nova"
  name="calendar-custom-days"
  title="Custom Cell Size"
  description="A calendar with custom cell size that's responsive."
  className="**:[.preview]:h-[560px]"
/>

You can customize the size of calendar cells using the `--cell-size` CSS variable. You can also make it responsive by using breakpoint-specific values:

```tsx showLineNumbers
<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  className="rounded-lg border [--cell-size:--spacing(11)] md:[--cell-size:--spacing(12)]"
/>
```

Or use fixed values:

```tsx showLineNumbers
<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  className="rounded-lg border [--cell-size:2.75rem] md:[--cell-size:3rem]"
/>
```

### Week Numbers

Use `showWeekNumber` to show week numbers.

<ComponentPreview
  styleName="radix-nova"
  name="calendar-week-numbers"
  previewClassName="h-96"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

See also the [Hijri Guide](#persian--hijri--jalali-calendar) for enabling the Persian / Hijri / Jalali calendar.

<ComponentPreview
  styleName="radix-nova"
  name="calendar-rtl"
  direction="rtl"
  previewClassName="h-96"
/>

When using RTL, import the locale from `react-day-picker/locale` and pass both the `locale` and `dir` props to the Calendar component:

```tsx showLineNumbers
import { arSA } from "react-day-picker/locale"

;<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  locale={arSA}
  dir="rtl"
/>
```

## API Reference

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information on the `Calendar` component.

## Changelog

### RTL Support

If you're upgrading from a previous version of the `Calendar` component, you'll need to apply the following updates to add locale support:

<Steps>

<Step>Import the `Locale` type.</Step>

Add `Locale` to your imports from `react-day-picker`:

```diff
  import {
    DayPicker,
    getDefaultClassNames,
    type DayButton,
+   type Locale,
  } from "react-day-picker"
```

<Step>Add `locale` prop to the Calendar component.</Step>

Add the `locale` prop to the component's props:

```diff
  function Calendar({
    className,
    classNames,
    showOutsideDays = true,
    captionLayout = "label",
    buttonVariant = "ghost",
+   locale,
    formatters,
    components,
    ...props
  }: React.ComponentProps<typeof DayPicker> & {
    buttonVariant?: React.ComponentProps<typeof Button>["variant"]
  }) {
```

<Step>Pass `locale` to DayPicker.</Step>

Pass the `locale` prop to the `DayPicker` component:

```diff
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn(...)}
      captionLayout={captionLayout}
+     locale={locale}
      formatters={{
        formatMonthDropdown: (date) =>
-         date.toLocaleString("default", { month: "short" }),
+         date.toLocaleString(locale?.code, { month: "short" }),
        ...formatters,
      }}
```

<Step>Update CalendarDayButton to accept locale.</Step>

Update the `CalendarDayButton` component signature and pass `locale`:

```diff
  function CalendarDayButton({
    className,
    day,
    modifiers,
+   locale,
    ...props
- }: React.ComponentProps<typeof DayButton>) {
+ }: React.ComponentProps<typeof DayButton> & { locale?: Partial<Locale> }) {
```

<Step>Update date formatting in CalendarDayButton.</Step>

Use `locale?.code` in the date formatting:

```diff
    <Button
      variant="ghost"
      size="icon"
-     data-day={day.date.toLocaleDateString()}
+     data-day={day.date.toLocaleDateString(locale?.code)}
      ...
    />
```

<Step>Pass locale to DayButton component.</Step>

Update the `DayButton` component usage to pass the `locale` prop:

```diff
      components={{
        ...
-       DayButton: CalendarDayButton,
+       DayButton: ({ ...props }) => (
+         <CalendarDayButton locale={locale} {...props} />
+       ),
        ...
      }}
```

<Step>Update RTL-aware CSS classes.</Step>

Replace directional classes with logical properties for better RTL support:

```diff
  // In the day classNames:
- [&:last-child[data-selected=true]_button]:rounded-r-(--cell-radius)
+ [&:last-child[data-selected=true]_button]:rounded-e-(--cell-radius)
- [&:nth-child(2)[data-selected=true]_button]:rounded-l-(--cell-radius)
+ [&:nth-child(2)[data-selected=true]_button]:rounded-s-(--cell-radius)
- [&:first-child[data-selected=true]_button]:rounded-l-(--cell-radius)
+ [&:first-child[data-selected=true]_button]:rounded-s-(--cell-radius)

  // In range_start classNames:
- rounded-l-(--cell-radius) ... after:right-0
+ rounded-s-(--cell-radius) ... after:end-0

  // In range_end classNames:
- rounded-r-(--cell-radius) ... after:left-0
+ rounded-e-(--cell-radius) ... after:start-0

  // In CalendarDayButton className:
- data-[range-end=true]:rounded-r-(--cell-radius)
+ data-[range-end=true]:rounded-e-(--cell-radius)
- data-[range-start=true]:rounded-l-(--cell-radius)
+ data-[range-start=true]:rounded-s-(--cell-radius)
```

</Steps>

After applying these changes, you can use the `locale` prop to provide locale-specific formatting:

```tsx
import { enUS } from "react-day-picker/locale"

;<Calendar mode="single" selected={date} onSelect={setDate} locale={enUS} />
```


---

<!-- SOURCE: apps/v4/content/docs/components/radix/card.mdx -->

## apps/v4/content/docs/components/radix/card.mdx

---
title: Card
description: Displays a card with header, content, and footer.
base: radix
component: true
---

<ComponentPreview
  name="card-demo"
  styleName="radix-nova"
  previewClassName="h-[30rem]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add card
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="card"
  title="components/ui/card.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
```

```tsx showLineNumbers
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card Description</CardDescription>
    <CardAction>Card Action</CardAction>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
```

## Examples

### Size

Use the `size="sm"` prop to set the size of the card to small. The small size variant uses smaller spacing.

<ComponentPreview
  styleName="radix-nova"
  name="card-small"
  previewClassName="h-96"
/>

### Image

Add an image before the card header to create a card with an image.

<ComponentPreview
  styleName="radix-nova"
  name="card-image"
  previewClassName="h-[32rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="card-rtl"
  direction="rtl"
  previewClassName="h-[30rem]"
/>

## API Reference

### Card

The `Card` component is the root container for card content.

| Prop        | Type                | Default     |
| ----------- | ------------------- | ----------- |
| `size`      | `"default" \| "sm"` | `"default"` |
| `className` | `string`            | -           |

### CardHeader

The `CardHeader` component is used for a title, description, and optional action.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardTitle

The `CardTitle` component is used for the card title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardDescription

The `CardDescription` component is used for helper text under the title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardAction

The `CardAction` component places content in the top-right of the header (for example, a button or a badge).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardContent

The `CardContent` component is used for the main card body.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardFooter

The `CardFooter` component is used for actions and secondary content at the bottom of the card.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |


---

<!-- SOURCE: apps/v4/content/docs/components/radix/carousel.mdx -->

## apps/v4/content/docs/components/radix/carousel.mdx

---
title: Carousel
description: A carousel with motion and swipe built using Embla.
base: radix
component: true
links:
  doc: https://www.embla-carousel.com/get-started/react
  api: https://www.embla-carousel.com/api
---

<ComponentPreview
  styleName="radix-nova"
  name="carousel-demo"
  previewClassName="h-80 sm:h-[32rem]"
/>

## About

The carousel component is built using the [Embla Carousel](https://www.embla-carousel.com/) library.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add carousel
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install embla-carousel-react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="carousel"
  title="components/ui/carousel.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
```

```tsx showLineNumbers
<Carousel>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
  <CarouselPrevious />
  <CarouselNext />
</Carousel>
```

## Examples

### Sizes

To set the size of the items, you can use the `basis` utility class on the `<CarouselItem />`.

<ComponentPreview styleName="radix-nova" name="carousel-size" />

```tsx showLineNumbers {4-6}
// 33% of the carousel width.
<Carousel>
  <CarouselContent>
    <CarouselItem className="basis-1/3">...</CarouselItem>
    <CarouselItem className="basis-1/3">...</CarouselItem>
    <CarouselItem className="basis-1/3">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

```tsx showLineNumbers {4-6}
// 50% on small screens and 33% on larger screens.
<Carousel>
  <CarouselContent>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

### Spacing

To set the spacing between the items, we use a `pl-[VALUE]` utility on the `<CarouselItem />` and a negative `-ml-[VALUE]` on the `<CarouselContent />`.

<ComponentPreview styleName="radix-nova" name="carousel-spacing" />

```tsx showLineNumbers /-ml-4/ /pl-4/
<Carousel>
  <CarouselContent className="-ml-4">
    <CarouselItem className="pl-4">...</CarouselItem>
    <CarouselItem className="pl-4">...</CarouselItem>
    <CarouselItem className="pl-4">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

```tsx showLineNumbers /-ml-2/ /pl-2/ /md:-ml-4/ /md:pl-4/
<Carousel>
  <CarouselContent className="-ml-2 md:-ml-4">
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

### Orientation

Use the `orientation` prop to set the orientation of the carousel.

<ComponentPreview
  styleName="radix-nova"
  name="carousel-orientation"
  previewClassName="h-[32rem]"
/>

```tsx showLineNumbers /vertical | horizontal/
<Carousel orientation="vertical | horizontal">
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
</Carousel>
```

## Options

You can pass options to the carousel using the `opts` prop. See the [Embla Carousel docs](https://www.embla-carousel.com/api/options/) for more information.

```tsx showLineNumbers {2-5}
<Carousel
  opts={{
    align: "start",
    loop: true,
  }}
>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
</Carousel>
```

## API

Use a state and the `setApi` props to get an instance of the carousel API.

<ComponentPreview
  styleName="radix-nova"
  name="carousel-api"
  previewClassName="sm:h-[32rem]"
/>

```tsx showLineNumbers {1,4,22}
import { type CarouselApi } from "@/components/ui/carousel"

export function Example() {
  const [api, setApi] = React.useState<CarouselApi>()
  const [current, setCurrent] = React.useState(0)
  const [count, setCount] = React.useState(0)

  React.useEffect(() => {
    if (!api) {
      return
    }

    setCount(api.scrollSnapList().length)
    setCurrent(api.selectedScrollSnap() + 1)

    api.on("select", () => {
      setCurrent(api.selectedScrollSnap() + 1)
    })
  }, [api])

  return (
    <Carousel setApi={setApi}>
      <CarouselContent>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
      </CarouselContent>
    </Carousel>
  )
}
```

## Events

You can listen to events using the api instance from `setApi`.

```tsx showLineNumbers {1,4-14,16}
import { type CarouselApi } from "@/components/ui/carousel"

export function Example() {
  const [api, setApi] = React.useState<CarouselApi>()

  React.useEffect(() => {
    if (!api) {
      return
    }

    api.on("select", () => {
      // Do something on select.
    })
  }, [api])

  return (
    <Carousel setApi={setApi}>
      <CarouselContent>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
      </CarouselContent>
    </Carousel>
  )
}
```

See the [Embla Carousel docs](https://www.embla-carousel.com/api/events/) for more information on using events.

## Plugins

You can use the `plugins` prop to add plugins to the carousel.

```ts showLineNumbers {1,6-10}
import Autoplay from "embla-carousel-autoplay"

export function Example() {
  return (
    <Carousel
      plugins={[
        Autoplay({
          delay: 2000,
        }),
      ]}
    >
      // ...
    </Carousel>
  )
}
```

<ComponentPreview
  styleName="radix-nova"
  name="carousel-plugin"
  previewClassName="sm:h-[32rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="carousel-rtl"
  direction="rtl"
  previewClassName="h-80 sm:h-[32rem]"
/>

When localizing the carousel for RTL languages, you need to set the `direction` option in the `opts` prop to match the text direction. This ensures the carousel scrolls in the correct direction.

```tsx showLineNumbers {2-5}
<Carousel
  dir={dir}
  opts={{
    direction: dir,
  }}
>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
  <CarouselPrevious className="rtl:rotate-180" />
  <CarouselNext className="rtl:rotate-180" />
</Carousel>
```

The `direction` option accepts `"ltr"` or `"rtl"` and should match the `dir` prop value. You may also want to rotate the navigation buttons using the `rtl:rotate-180` class to ensure they point in the correct direction.

## API Reference

See the [Embla Carousel docs](https://www.embla-carousel.com/api/) for more information on props and plugins.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/chart.mdx -->

## apps/v4/content/docs/components/radix/chart.mdx

---
title: Chart
description: Beautiful charts. Built using Recharts. Copy and paste into your apps.
base: radix
component: true
---

<Callout className="mt-4">

**Updated:** The `chart` component now uses Recharts v3. If you're upgrading existing chart code, see [Updating to Recharts v3](#updating-to-recharts-v3).

</Callout>

<ComponentPreview
  styleName="radix-nova"
  name="chart-demo"
  className="theme-blue [&_.preview]:h-auto [&_.preview]:p-0 [&_.preview]:lg:min-h-[404px] [&_.preview>div]:w-full [&_.preview>div]:border-none [&_.preview>div]:shadow-none"
  hideCode
/>

Introducing **Charts**. A collection of chart components that you can copy and paste into your apps.

Charts are designed to look great out of the box. They work well with the other components and are fully customizable to fit your project.

[Browse the Charts Library](/charts).

## Component

We use [Recharts](https://recharts.org/) under the hood.

We designed the `chart` component with composition in mind. **You build your charts using Recharts components and only bring in custom components, such as `ChartTooltip`, when and where you need it**.

```tsx showLineNumbers /ChartContainer/ /ChartTooltipContent/
import { Bar, BarChart } from "recharts"

import { ChartContainer, ChartTooltipContent } from "@/components/ui/chart"

export function MyChart() {
  return (
    <ChartContainer>
      <BarChart data={data}>
        <Bar dataKey="value" />
        <ChartTooltip content={<ChartTooltipContent />} />
      </BarChart>
    </ChartContainer>
  )
}
```

We do not wrap Recharts. This means you're not locked into an abstraction. When a new Recharts version is released, you can follow the official upgrade path to upgrade your charts.

**The components are yours**.

## Updating to Recharts v3

If you're updating older chart code to Recharts v3:

- Use `var(--chart-1)` instead of `hsl(var(--chart-1))` when you reference chart tokens from your CSS variables.
- Use `ChartTooltip.defaultIndex` for initial tooltip state only. Keep persistent active shapes in your own chart state.
- Remove `layout` from `<Bar>` when the parent `<BarChart>` already defines it.
- Keep a height, `min-h-*`, or `aspect-*` on `ChartContainer` so `ResponsiveContainer` can measure on first render.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add chart
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install recharts
```

<Step>Copy and paste the following code into `components/ui/chart.tsx`.</Step>

<ComponentSource
  name="chart"
  title="components/ui/chart.tsx"
  styleName="radix-nova"
/>

<Step>Add the following colors to your CSS file</Step>

```css title="app/globals.css" showLineNumbers
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
    --chart-3: oklch(0.398 0.07 227.392);
    --chart-4: oklch(0.828 0.189 84.429);
    --chart-5: oklch(0.769 0.188 70.08);
  }

  .dark {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
    --chart-3: oklch(0.769 0.188 70.08);
    --chart-4: oklch(0.627 0.265 303.9);
    --chart-5: oklch(0.645 0.246 16.439);
  }
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Your First Chart

Let's build your first chart. We'll build a bar chart, add a grid, axis, tooltip and legend.

<Steps>

<Step>Start by defining your data</Step>

The following data represents the number of desktop and mobile users for each month.

<Callout className="mt-4">

**Note:** Your data can be in any shape. You are not limited to the shape of the data below. Use the `dataKey` prop to map your data to the chart.

</Callout>

```tsx title="components/example-chart.tsx" showLineNumbers
const chartData = [
  { month: "January", desktop: 186, mobile: 80 },
  { month: "February", desktop: 305, mobile: 200 },
  { month: "March", desktop: 237, mobile: 120 },
  { month: "April", desktop: 73, mobile: 190 },
  { month: "May", desktop: 209, mobile: 130 },
  { month: "June", desktop: 214, mobile: 140 },
]
```

<Step>Define your chart config</Step>

The chart config holds configuration for the chart. This is where you place human-readable strings, such as labels, icons and color tokens for theming.

```tsx title="components/example-chart.tsx" showLineNumbers
import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
  mobile: {
    label: "Mobile",
    color: "#60a5fa",
  },
} satisfies ChartConfig
```

<Step>Build your chart</Step>

You can now build your chart using Recharts components.

<Callout className="mt-4 bg-amber-50 border-amber-200 dark:bg-amber-950/50 dark:border-amber-950">

**Important:** Remember to set a `min-h-[VALUE]` on the `ChartContainer` component. This is required for the chart to be responsive.

</Callout>

<ComponentPreview
  styleName="radix-nova"
  name="chart-example"
  previewClassName="h-80"
/>

</Steps>

### Add a Grid

Let's add a grid to the chart.

<Steps className="mb-0 pt-2">

<Step>Import the `CartesianGrid` component.</Step>

```tsx /CartesianGrid/
import { Bar, BarChart, CartesianGrid } from "recharts"
```

<Step>Add the `CartesianGrid` component to your chart.</Step>

```tsx showLineNumbers {3}
<ChartContainer config={chartConfig} className="min-h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="radix-nova"
  name="chart-example-grid"
  previewClassName="h-80"
/>

</Steps>

### Add an Axis

To add an x-axis to the chart, we'll use the `XAxis` component.

<Steps className="mb-0 pt-2">

<Step>Import the `XAxis` component.</Step>

```tsx /XAxis/
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"
```

<Step>Add the `XAxis` component to your chart.</Step>

```tsx showLineNumbers {4-10}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="radix-nova"
  name="chart-example-axis"
  previewClassName="h-80"
/>

</Steps>

### Add Tooltip

So far we've only used components from Recharts. They look great out of the box thanks to some customization in the `chart` component.

To add a tooltip, we'll use the custom `ChartTooltip` and `ChartTooltipContent` components from `chart`.

<Steps className="mb-0 pt-2">

<Step>Import the `ChartTooltip` and `ChartTooltipContent` components.</Step>

```tsx
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

<Step>Add the components to your chart.</Step>

```tsx showLineNumbers {11}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="radix-nova"
  name="chart-example-tooltip"
  previewClassName="h-80"
/>

Hover to see the tooltips. Easy, right? Two components, and we've got a beautiful tooltip.

</Steps>

### Add Legend

We'll do the same for the legend. We'll use the `ChartLegend` and `ChartLegendContent` components from `chart`.

<Steps className="mb-0 pt-2">

<Step>Import the `ChartLegend` and `ChartLegendContent` components.</Step>

```tsx
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

<Step>Add the components to your chart.</Step>

```tsx showLineNumbers {12}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <ChartLegend content={<ChartLegendContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  styleName="radix-nova"
  name="chart-example-legend"
  previewClassName="h-80"
/>

</Steps>

Done. You've built your first chart! What's next?

- [Themes and Colors](/docs/components/chart#theming)
- [Tooltip](/docs/components/chart#tooltip)
- [Legend](/docs/components/chart#legend)

## Chart Config

The chart config is where you define the labels, icons and colors for a chart.

It is intentionally decoupled from chart data.

This allows you to share config and color tokens between charts. It can also work independently for cases where your data or color tokens live remotely or in a different format.

```tsx showLineNumbers /ChartConfig/
import { Monitor } from "lucide-react"

import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    icon: Monitor,
    // A color like 'hsl(220, 98%, 61%)' or 'var(--color-name)'
    color: "#2563eb",
    // OR a theme object with 'light' and 'dark' keys
    theme: {
      light: "#2563eb",
      dark: "#dc2626",
    },
  },
} satisfies ChartConfig
```

## Theming

Charts have built-in support for theming. You can use css variables (recommended) or color values in any color format, such as hex, hsl or oklch.

### CSS Variables

<Steps className="mb-0 pt-2">

<Step>Define your colors in your css file</Step>

```css title="app/globals.css" showLineNumbers
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
  }

  .dark {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
  }
}
```

<Step>Add the color to your `chartConfig`</Step>

```tsx title="components/example-chart.tsx" showLineNumbers
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

</Steps>

### hex, hsl or oklch

You can also define your colors directly in the chart config. Use the color format you prefer.

```tsx title="components/example-chart.tsx" showLineNumbers
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
  mobile: {
    label: "Mobile",
    color: "hsl(220, 98%, 61%)",
  },
  tablet: {
    label: "Tablet",
    color: "oklch(0.5 0.2 240)",
  },
  laptop: {
    label: "Laptop",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

### Using Colors

To use the theme colors in your chart, reference the colors using the format `var(--color-KEY)`.

#### Components

```tsx
<Bar dataKey="desktop" fill="var(--color-desktop)" />
```

#### Chart Data

```tsx title="components/example-chart.tsx" showLineNumbers
const chartData = [
  { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]
```

#### Tailwind

```tsx title="components/example-chart.tsx"
<LabelList className="fill-(--color-desktop)" />
```

## Tooltip

A chart tooltip contains a label, name, indicator and value. You can use a combination of these to customize your tooltip.

<ComponentPreview styleName="radix-nova" name="chart-tooltip" hideCode />

You can turn on/off any of these using the `hideLabel`, `hideIndicator` props and customize the indicator style using the `indicator` prop.

Use `labelKey` and `nameKey` to use a custom key for the tooltip label and name.

Chart comes with the `<ChartTooltip>` and `<ChartTooltipContent>` components. You can use these two components to add custom tooltips to your chart.

```tsx title="components/example-chart.tsx"
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

```tsx title="components/example-chart.tsx"
<ChartTooltip content={<ChartTooltipContent />} />
```

### Props

Use the following props to customize the tooltip.

| Prop            | Type                     | Description                                  |
| :-------------- | :----------------------- | :------------------------------------------- |
| `labelKey`      | string                   | The config or data key to use for the label. |
| `nameKey`       | string                   | The config or data key to use for the name.  |
| `indicator`     | `dot` `line` or `dashed` | The indicator style for the tooltip.         |
| `hideLabel`     | boolean                  | Whether to hide the label.                   |
| `hideIndicator` | boolean                  | Whether to hide the indicator.               |

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for tooltip label and names, use the `labelKey` and `nameKey` props.

```tsx showLineNumbers /browser/
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  visitors: {
    label: "Total Visitors",
  },
  chrome: {
    label: "Chrome",
    color: "var(--chart-1)",
  },
  safari: {
    label: "Safari",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

```tsx title="components/example-chart.tsx"
<ChartTooltip
  content={<ChartTooltipContent labelKey="visitors" nameKey="browser" />}
/>
```

This will use `Total Visitors` for label and `Chrome` and `Safari` for the tooltip names.

## Legend

You can use the custom `<ChartLegend>` and `<ChartLegendContent>` components to add a legend to your chart.

```tsx title="components/example-chart.tsx"
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

```tsx title="components/example-chart.tsx"
<ChartLegend content={<ChartLegendContent />} />
```

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for legend names, use the `nameKey` prop.

```tsx showLineNumbers /browser/
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  chrome: {
    label: "Chrome",
    color: "var(--chart-1)",
  },
  safari: {
    label: "Safari",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

```tsx title="components/example-chart.tsx"
<ChartLegend content={<ChartLegendContent nameKey="browser" />} />
```

This will use `Chrome` and `Safari` for the legend names.

## Accessibility

You can turn on the `accessibilityLayer` prop to add an accessible layer to your chart.

This prop adds keyboard access and screen reader support to your charts.

```tsx title="components/example-chart.tsx"
<LineChart accessibilityLayer />
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="chart-rtl"
  direction="rtl"
  previewClassName="h-92"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/radix/checkbox.mdx -->

## apps/v4/content/docs/components/radix/checkbox.mdx

---
title: Checkbox
description: A control that allows the user to toggle between checked and not checked.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/checkbox
  api: https://www.radix-ui.com/docs/primitives/components/checkbox#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="checkbox-demo"
  previewClassName="h-80"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add checkbox
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="checkbox"
  title="components/ui/checkbox.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Checkbox } from "@/components/ui/checkbox"
```

```tsx
<Checkbox />
```

## Checked State

Use `defaultChecked` for uncontrolled checkboxes, or `checked` and
`onCheckedChange` to control the state.

```tsx showLineNumbers
import * as React from "react"

export function Example() {
  const [checked, setChecked] = React.useState(false)

  return <Checkbox checked={checked} onCheckedChange={setChecked} />
}
```

## Invalid State

Set `aria-invalid` on the checkbox and `data-invalid` on the field wrapper to
show the invalid styles.

<ComponentPreview styleName="radix-nova" name="checkbox-invalid" />

## Examples

### Basic

Pair the checkbox with `Field` and `FieldLabel` for proper layout and labeling.

<ComponentPreview styleName="radix-nova" name="checkbox-basic" />

### Description

Use `FieldContent` and `FieldDescription` for helper text.

<ComponentPreview styleName="radix-nova" name="checkbox-description" />

### Disabled

Use the `disabled` prop to prevent interaction and add the `data-disabled` attribute to the `<Field>` component for disabled styles.

<ComponentPreview styleName="radix-nova" name="checkbox-disabled" />

### Group

Use multiple fields to create a checkbox list.

<ComponentPreview styleName="radix-nova" name="checkbox-group" />

### Table

<ComponentPreview
  styleName="radix-nova"
  name="checkbox-table"
  previewClassName="p-4 md:p-8"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="checkbox-rtl"
  direction="rtl"
  previewClassName="h-80"
/>

## API Reference

See the [Radix UI](https://www.radix-ui.com/docs/primitives/components/checkbox#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/collapsible.mdx -->

## apps/v4/content/docs/components/radix/collapsible.mdx

---
title: Collapsible
description: An interactive component which expands/collapses a panel.
base: radix
component: true
featured: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/collapsible
  api: https://www.radix-ui.com/docs/primitives/components/collapsible#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="collapsible-demo"
  align="start"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add collapsible
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="collapsible"
  title="components/ui/collapsible.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
```

```tsx showLineNumbers
<Collapsible>
  <CollapsibleTrigger>Can I use this in my project?</CollapsibleTrigger>
  <CollapsibleContent>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </CollapsibleContent>
</Collapsible>
```

## Controlled State

Use the `open` and `onOpenChange` props to control the state.

```tsx showLineNumbers
import * as React from "react"

export function Example() {
  const [open, setOpen] = React.useState(false)

  return (
    <Collapsible open={open} onOpenChange={setOpen}>
      <CollapsibleTrigger>Toggle</CollapsibleTrigger>
      <CollapsibleContent>Content</CollapsibleContent>
    </Collapsible>
  )
}
```

## Examples

### Basic

<ComponentPreview
  styleName="radix-nova"
  name="collapsible-basic"
  align="start"
/>

### Settings Panel

Use a trigger button to reveal additional settings.

<ComponentPreview styleName="radix-nova" name="collapsible-settings" />

### File Tree

Use nested collapsibles to build a file tree.

<ComponentPreview
  styleName="radix-nova"
  name="collapsible-file-tree"
  previewClassName="h-[36rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="collapsible-rtl"
  direction="rtl"
  align="start"
/>

## API Reference

See the [Radix UI](https://www.radix-ui.com/docs/primitives/components/collapsible#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/combobox.mdx -->

## apps/v4/content/docs/components/radix/combobox.mdx

---
title: Combobox
description: Autocomplete input with a list of suggestions.
base: radix
component: true
links:
  doc: https://base-ui.com/react/components/combobox
  api: https://base-ui.com/react/components/combobox#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="combobox-demo"
  description="A combobox with a list of frameworks."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add combobox
```

</TabsContent>
<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="combobox"
  title="components/ui/combobox.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"
```

```tsx showLineNumbers
const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

export function ExampleCombobox() {
  return (
    <Combobox items={frameworks}>
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(item) => (
            <ComboboxItem key={item} value={item}>
              {item}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Custom Items

Use `itemToStringValue` when your items are objects.

```tsx showLineNumbers
import * as React from "react"

import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"

type Framework = {
  label: string
  value: string
}

const frameworks: Framework[] = [
  { label: "Next.js", value: "next" },
  { label: "SvelteKit", value: "sveltekit" },
  { label: "Nuxt", value: "nuxt" },
]

export function ExampleComboboxCustomItems() {
  return (
    <Combobox
      items={frameworks}
      itemToStringValue={(framework) => framework.label}
    >
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(framework) => (
            <ComboboxItem key={framework.value} value={framework}>
              {framework.label}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Multiple Selection

Use `multiple` with chips for multi-select behavior.

```tsx showLineNumbers
import * as React from "react"

import {
  Combobox,
  ComboboxChip,
  ComboboxChips,
  ComboboxChipsInput,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
  ComboboxValue,
} from "@/components/ui/combobox"

const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

export function ExampleComboboxMultiple() {
  const [value, setValue] = React.useState<string[]>([])

  return (
    <Combobox
      items={frameworks}
      multiple
      value={value}
      onValueChange={setValue}
    >
      <ComboboxChips>
        <ComboboxValue>
          {value.map((item) => (
            <ComboboxChip key={item}>{item}</ComboboxChip>
          ))}
        </ComboboxValue>
        <ComboboxChipsInput placeholder="Add framework" />
      </ComboboxChips>
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(item) => (
            <ComboboxItem key={item} value={item}>
              {item}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Examples

### Basic

A simple combobox with a list of frameworks.

<ComponentPreview styleName="base-nova" name="combobox-basic" />

### Multiple

A combobox with multiple selection using `multiple` and `ComboboxChips`.

<ComponentPreview styleName="base-nova" name="combobox-multiple" />

### Clear Button

Use the `showClear` prop to show a clear button.

<ComponentPreview styleName="base-nova" name="combobox-clear" />

### Groups

Use `ComboboxGroup` and `ComboboxSeparator` to group items.

<ComponentPreview styleName="base-nova" name="combobox-groups" />

### Custom Items

You can render a custom component inside `ComboboxItem`.

<ComponentPreview styleName="base-nova" name="combobox-custom" />

### Invalid

Use the `aria-invalid` prop to make the combobox invalid.

<ComponentPreview styleName="base-nova" name="combobox-invalid" />

### Disabled

Use the `disabled` prop to disable the combobox.

<ComponentPreview styleName="base-nova" name="combobox-disabled" />

### Auto Highlight

Use the `autoHighlight` prop to automatically highlight the first item on filter.

<ComponentPreview styleName="base-nova" name="combobox-auto-highlight" />

### Popup

You can trigger the combobox from a button or any other component by using the `render` prop. Move the `ComboboxInput` inside the `ComboboxContent`.

<ComponentPreview styleName="base-nova" name="combobox-popup" />

### Input Group

You can add an addon to the combobox by using the `InputGroupAddon` component inside the `ComboboxInput`.

<ComponentPreview styleName="radix-nova" name="combobox-input-group" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="combobox-rtl"
  direction="rtl"
  align="start"
/>

## API Reference

See the [Base UI](https://base-ui.com/react/components/combobox#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/command.mdx -->

## apps/v4/content/docs/components/radix/command.mdx

---
title: Command
description: Command menu for search and quick actions.
base: radix
component: true
links:
  doc: https://github.com/dip/cmdk
---

<ComponentPreview
  styleName="radix-nova"
  name="command-demo"
  align="start"
  previewClassName="h-[24.5rem]"
/>

## About

The `<Command />` component uses the [`cmdk`](https://github.com/dip/cmdk) component by [Dip](https://www.dip.org/).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add command
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install cmdk
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="command"
  title="components/ui/command.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
```

```tsx showLineNumbers
<Command className="max-w-sm rounded-lg border">
  <CommandInput placeholder="Type a command or search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
    <CommandSeparator />
    <CommandGroup heading="Settings">
      <CommandItem>Profile</CommandItem>
      <CommandItem>Billing</CommandItem>
      <CommandItem>Settings</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

## Examples

### Basic

A simple command menu in a dialog.

<ComponentPreview styleName="radix-nova" name="command-basic" />

### Shortcuts

<ComponentPreview styleName="radix-nova" name="command-shortcuts" />

### Groups

A command menu with groups, icons and separators.

<ComponentPreview styleName="radix-nova" name="command-groups" />

### Scrollable

Scrollable command menu with multiple items.

<ComponentPreview styleName="radix-nova" name="command-scrollable" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="command-rtl"
  direction="rtl"
  align="start"
  previewClassName="h-[24.5rem]"
/>

## API Reference

See the [cmdk](https://github.com/dip/cmdk) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/context-menu.mdx -->

## apps/v4/content/docs/components/radix/context-menu.mdx

---
title: Context Menu
description: Displays a menu of actions triggered by a right click.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/context-menu
  api: https://www.radix-ui.com/docs/primitives/components/context-menu#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="context-menu-demo"
  description="A context menu with sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add context-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="context-menu"
  title="components/ui/context-menu.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
```

```tsx showLineNumbers
<ContextMenu>
  <ContextMenuTrigger>Right click here</ContextMenuTrigger>
  <ContextMenuContent>
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenuContent>
</ContextMenu>
```

## Examples

### Basic

A simple context menu with a few actions.

<ComponentPreview styleName="radix-nova" name="context-menu-basic" />

### Submenu

Use `ContextMenuSub` to nest secondary actions.

<ComponentPreview styleName="radix-nova" name="context-menu-submenu" />

### Shortcuts

Add `ContextMenuShortcut` to show keyboard hints.

<ComponentPreview styleName="radix-nova" name="context-menu-shortcuts" />

### Groups

Group related actions and separate them with dividers.

<ComponentPreview styleName="radix-nova" name="context-menu-groups" />

### Icons

Combine icons with labels for quick scanning.

<ComponentPreview styleName="radix-nova" name="context-menu-icons" />

### Checkboxes

Use `ContextMenuCheckboxItem` for toggles.

<ComponentPreview styleName="radix-nova" name="context-menu-checkboxes" />

### Radio

Use `ContextMenuRadioItem` for exclusive choices.

<ComponentPreview styleName="radix-nova" name="context-menu-radio" />

### Destructive

Use `variant="destructive"` to style the menu item as destructive.

<ComponentPreview styleName="radix-nova" name="context-menu-destructive" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="context-menu-rtl"
  direction="rtl"
/>

## API Reference

See the [Radix UI](https://www.radix-ui.com/docs/primitives/components/context-menu#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/data-table.mdx -->

## apps/v4/content/docs/components/radix/data-table.mdx

---
title: Data Table
description: Powerful table and datagrids built using TanStack Table.
base: base
component: true
links:
  doc: https://tanstack.com/table/v8/docs/introduction
---

<ComponentPreview
  styleName="radix-nova"
  name="data-table-demo"
  align="start"
  previewClassName="items-start h-auto px-4 md:px-8"
  hideCode
/>

## Introduction

Every data table or datagrid I've created has been unique. They all behave differently, have specific sorting and filtering requirements, and work with different data sources.

It doesn't make sense to combine all of these variations into a single component. If we do that, we'll lose the flexibility that [headless UI](https://tanstack.com/table/v8/docs/introduction#what-is-headless-ui) provides.

So instead of a data-table component, I thought it would be more helpful to provide a guide on how to build your own.

We'll start with the basic `<Table />` component and build a complex data table from scratch.

<Callout className="mt-4">

**Tip:** If you find yourself using the same table in multiple places in your app, you can always extract it into a reusable component.

</Callout>

## Table of Contents

This guide will show you how to use [TanStack Table](https://tanstack.com/table) and the `<Table />` component to build your own custom data table. We'll cover the following topics:

- [Basic Table](#basic-table)
- [Row Actions](#row-actions)
- [Pagination](#pagination)
- [Sorting](#sorting)
- [Filtering](#filtering)
- [Visibility](#visibility)
- [Row Selection](#row-selection)
- [Reusable Components](#reusable-components)

## Installation

1. Add the `<Table />` component to your project:

```bash
npx shadcn@latest add table
```

2. Add `tanstack/react-table` dependency:

```bash
npm install @tanstack/react-table
```

## Prerequisites

We are going to build a table to show recent payments. Here's what our data looks like:

```tsx showLineNumbers
type Payment = {
  id: string
  amount: number
  status: "pending" | "processing" | "success" | "failed"
  email: string
}

export const payments: Payment[] = [
  {
    id: "728ed52f",
    amount: 100,
    status: "pending",
    email: "m@example.com",
  },
  {
    id: "489e1d42",
    amount: 125,
    status: "processing",
    email: "example@gmail.com",
  },
  // ...
]
```

## Project Structure

Start by creating the following file structure:

```txt
app
└── payments
    ├── columns.tsx
    ├── data-table.tsx
    └── page.tsx
```

I'm using a Next.js example here but this works for any other React framework.

- `columns.tsx` (client component) will contain our column definitions.
- `data-table.tsx` (client component) will contain our `<DataTable />` component.
- `page.tsx` (server component) is where we'll fetch data and render our table.

## Basic Table

Let's start by building a basic table.

<Steps className="mb-0 pt-2">

### Column Definitions

First, we'll define our columns.

```tsx showLineNumbers title="app/payments/columns.tsx" {3,14-27}
"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Payment = {
  id: string
  amount: number
  status: "pending" | "processing" | "success" | "failed"
  email: string
}

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "status",
    header: "Status",
  },
  {
    accessorKey: "email",
    header: "Email",
  },
  {
    accessorKey: "amount",
    header: "Amount",
  },
]
```

<Callout className="mt-4">

**Note:** Columns are where you define the core of what your table
will look like. They define the data that will be displayed, how it will be
formatted, sorted and filtered.

</Callout>

### `<DataTable />` component

Next, we'll create a `<DataTable />` component to render our table.

```tsx showLineNumbers title="app/payments/data-table.tsx"
"use client"

import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
} from "@tanstack/react-table"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  })

  return (
    <div className="overflow-hidden rounded-md border">
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map((headerGroup) => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map((header) => {
                return (
                  <TableHead key={header.id}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                  </TableHead>
                )
              })}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows?.length ? (
            table.getRowModel().rows.map((row) => (
              <TableRow
                key={row.id}
                data-state={row.getIsSelected() && "selected"}
              >
                {row.getVisibleCells().map((cell) => (
                  <TableCell key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </TableCell>
                ))}
              </TableRow>
            ))
          ) : (
            <TableRow>
              <TableCell colSpan={columns.length} className="h-24 text-center">
                No results.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </div>
  )
}
```

<Callout>

**Tip**: If you find yourself using `<DataTable />` in multiple places, this is the component you could make reusable by extracting it to `components/ui/data-table.tsx`.

`<DataTable columns={columns} data={data} />`

</Callout>

### Render the table

Finally, we'll render our table in our page component.

```tsx showLineNumbers title="app/payments/page.tsx" {22}
import { columns, Payment } from "./columns"
import { DataTable } from "./data-table"

async function getData(): Promise<Payment[]> {
  // Fetch data from your API here.
  return [
    {
      id: "728ed52f",
      amount: 100,
      status: "pending",
      email: "m@example.com",
    },
    // ...
  ]
}

export default async function DemoPage() {
  const data = await getData()

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  )
}
```

</Steps>

## Cell Formatting

Let's format the amount cell to display the dollar amount. We'll also align the cell to the right.

<Steps className="mb-0 pt-2">

### Update columns definition

Update the `header` and `cell` definitions for amount as follows:

```tsx showLineNumbers title="app/payments/columns.tsx" {4-15}
export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "amount",
    header: () => <div className="text-right">Amount</div>,
    cell: ({ row }) => {
      const amount = parseFloat(row.getValue("amount"))
      const formatted = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
      }).format(amount)

      return <div className="text-right font-medium">{formatted}</div>
    },
  },
]
```

You can use the same approach to format other cells and headers.

</Steps>

## Row Actions

Let's add row actions to our table. We'll use a `<DropdownMenu />` component for this.

<Steps className="mb-0 pt-2">

### Update columns definition

Update our columns definition to add a new `actions` column. The `actions` cell returns a `<DropdownMenu />` component.

```tsx showLineNumbers title="app/payments/columns.tsx" {4,6-14,18-45}
"use client"

import { ColumnDef } from "@tanstack/react-table"
import { MoreHorizontal } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export const columns: ColumnDef<Payment>[] = [
  // ...
  {
    id: "actions",
    cell: ({ row }) => {
      const payment = row.original

      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="h-8 w-8 p-0">
              <span className="sr-only">Open menu</span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuLabel>Actions</DropdownMenuLabel>
            <DropdownMenuItem
              onClick={() => navigator.clipboard.writeText(payment.id)}
            >
              Copy payment ID
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>View customer</DropdownMenuItem>
            <DropdownMenuItem>View payment details</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      )
    },
  },
  // ...
]
```

You can access the row data using `row.original` in the `cell` function. Use this to handle actions for your row eg. use the `id` to make a DELETE call to your API.

</Steps>

## Pagination

Next, we'll add pagination to our table.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {5,17}
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  useReactTable,
} from "@tanstack/react-table"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  // ...
}
```

This will automatically paginate your rows into pages of 10. See the [pagination docs](https://tanstack.com/table/v8/docs/api/features/pagination) for more information on customizing page size and implementing manual pagination.

### Add pagination controls

We can add pagination controls to our table using the `<Button />` component and the `table.previousPage()`, `table.nextPage()` API methods.

```tsx showLineNumbers title="app/payments/data-table.tsx" {1,15,21-39}
import { Button } from "@/components/ui/button"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table>
          { // .... }
        </Table>
      </div>
      <div className="flex items-center justify-end space-x-2 py-4">
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
        >
          Previous
        </Button>
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
        >
          Next
        </Button>
      </div>
    </div>
  )
}
```

See [Reusable Components](#reusable-components) section for a more advanced pagination component.

</Steps>

## Sorting

Let's make the email column sortable.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {3,6,10,18,25-28}
"use client"

import * as React from "react"
import {
  ColumnDef,
  SortingState,
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onSortingChange: setSorting,
    getSortedRowModel: getSortedRowModel(),
    state: {
      sorting,
    },
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

### Make header cell sortable

We can now update the `email` header cell to add sorting controls.

```tsx showLineNumbers title="app/payments/columns.tsx" {4,9-19}
"use client"

import { ColumnDef } from "@tanstack/react-table"
import { ArrowUpDown } from "lucide-react"

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "email",
    header: ({ column }) => {
      return (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Email
          <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
      )
    },
  },
]
```

This will automatically sort the table (asc and desc) when the user toggles on the header cell.

</Steps>

## Filtering

Let's add a search input to filter emails in our table.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {6,10,17,24-26,35-36,39,45-54}
"use client"

import * as React from "react"
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    onColumnFiltersChange: setColumnFilters,
    getFilteredRowModel: getFilteredRowModel(),
    state: {
      sorting,
      columnFilters,
    },
  })

  return (
    <div>
      <div className="flex items-center py-4">
        <Input
          placeholder="Filter emails..."
          value={(table.getColumn("email")?.getFilterValue() as string) ?? ""}
          onChange={(event) =>
            table.getColumn("email")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
      </div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

Filtering is now enabled for the `email` column. You can add filters to other columns as well. See the [filtering docs](https://tanstack.com/table/v8/docs/guide/filters) for more information on customizing filters.

</Steps>

## Visibility

Adding column visibility is fairly simple using `@tanstack/react-table` visibility API.

<Steps className="mb-0 pt-2">

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {8,18-23,33-34,45,49,64-91}
"use client"

import * as React from "react"
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({})

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
    },
  })

  return (
    <div>
      <div className="flex items-center py-4">
        <Input
          placeholder="Filter emails..."
          value={table.getColumn("email")?.getFilterValue() as string}
          onChange={(event) =>
            table.getColumn("email")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" className="ml-auto">
              Columns
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {table
              .getAllColumns()
              .filter(
                (column) => column.getCanHide()
              )
              .map((column) => {
                return (
                  <DropdownMenuCheckboxItem
                    key={column.id}
                    className="capitalize"
                    checked={column.getIsVisible()}
                    onCheckedChange={(value) =>
                      column.toggleVisibility(!!value)
                    }
                  >
                    {column.id}
                  </DropdownMenuCheckboxItem>
                )
              })}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

This adds a dropdown menu that you can use to toggle column visibility.

</Steps>

## Row Selection

Next, we're going to add row selection to our table.

<Steps className="mb-0 pt-2">

### Update column definitions

```tsx showLineNumbers title="app/payments/columns.tsx" {6,9-27}
"use client"

import { ColumnDef } from "@tanstack/react-table"

import { Badge } from "@/components/ui/badge"
import { Checkbox } from "@/components/ui/checkbox"

export const columns: ColumnDef<Payment>[] = [
  {
    id: "select",
    header: ({ table }) => (
      <Checkbox
        checked={
          table.getIsAllPageRowsSelected() ||
          (table.getIsSomePageRowsSelected() && "indeterminate")
        }
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
        aria-label="Select all"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(!!value)}
        aria-label="Select row"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },
]
```

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {11,23,28}
export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({})
  const [rowSelection, setRowSelection] = React.useState({})

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange: setRowSelection,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
      rowSelection,
    },
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table />
      </div>
    </div>
  )
}
```

This adds a checkbox to each row and a checkbox in the header to select all rows.

### Show selected rows

You can show the number of selected rows using the `table.getFilteredSelectedRowModel()` API.

```tsx
<div className="flex-1 text-sm text-muted-foreground">
  {table.getFilteredSelectedRowModel().rows.length} of{" "}
  {table.getFilteredRowModel().rows.length} row(s) selected.
</div>
```

</Steps>

## Reusable Components

Here are some components you can use to build your data tables. This is from the [Tasks](/examples/tasks) demo.

### Column header

Make any column header sortable and hideable.

<ComponentSource
  src="/app/(app)/examples/tasks/components/data-table-column-header.tsx"
  title="components/data-table-column-header.tsx"
/>

```tsx showLineNumbers {5}
export const columns = [
  {
    accessorKey: "email",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Email" />
    ),
  },
]
```

### Pagination

Add pagination controls to your table including page size and selection count.

<ComponentSource
  src="/app/(app)/examples/tasks/components/data-table-pagination.tsx"
  styleName="radix-nova"
/>

```tsx
<DataTablePagination table={table} />
```

### Column toggle

A component to toggle column visibility.

<ComponentSource
  src="/app/(app)/examples/tasks/components/data-table-view-options.tsx"
  styleName="radix-nova"
/>

```tsx
<DataTableViewOptions table={table} />
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="data-table-rtl"
  direction="rtl"
  previewClassName="items-start h-auto px-4 md:px-8"
  hideCode
/>


---

<!-- SOURCE: apps/v4/content/docs/components/radix/date-picker.mdx -->

## apps/v4/content/docs/components/radix/date-picker.mdx

---
title: Date Picker
description: A date picker component with range and presets.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="date-picker-demo" />

## Installation

The Date Picker is built using a composition of the `<Popover />` and the `<Calendar />` components.

See installation instructions for the [Popover](/docs/components/radix/popover#installation) and the [Calendar](/docs/components/radix/calendar#installation) components.

## Usage

```tsx showLineNumbers title="components/example-date-picker.tsx"
"use client"

import * as React from "react"
import { format } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

export function DatePickerDemo() {
  const [date, setDate] = React.useState<Date>()

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          data-empty={!date}
          className="w-[280px] justify-start text-left font-normal data-[empty=true]:text-muted-foreground"
        >
          <CalendarIcon />
          {date ? format(date, "PPP") : <span>Pick a date</span>}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0">
        <Calendar mode="single" selected={date} onSelect={setDate} />
      </PopoverContent>
    </Popover>
  )
}
```

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information.

## Examples

### Basic

A basic date picker component.

<ComponentPreview styleName="radix-nova" name="date-picker-basic" />

### Range Picker

A date picker component for selecting a range of dates.

<ComponentPreview styleName="radix-nova" name="date-picker-range" />

### Date of Birth

A date picker component for selecting a date of birth. This component includes a dropdown caption layout for date and month selection.

<ComponentPreview styleName="radix-nova" name="date-picker-dob" />

### Input

A date picker component with an input field for selecting a date.

<ComponentPreview styleName="radix-nova" name="date-picker-input" />

### Time Picker

A date picker component with a time input field for selecting a time.

<ComponentPreview styleName="radix-nova" name="date-picker-time" />

### Natural Language Picker

This component uses the `chrono-node` library to parse natural language dates.

<ComponentPreview styleName="radix-nova" name="date-picker-natural-language" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="date-picker-rtl"
  direction="rtl"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/radix/dialog.mdx -->

## apps/v4/content/docs/components/radix/dialog.mdx

---
title: Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
featured: true
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/dialog
  api: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="dialog-demo"
  description="A dialog for editing profile details."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add dialog
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="dialog"
  title="components/ui/dialog.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
```

```tsx showLineNumbers
<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Are you absolutely sure?</DialogTitle>
      <DialogDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

## Examples

### Custom Close Button

Replace the default close control with your own button.

<ComponentPreview styleName="radix-nova" name="dialog-close-button" />

### No Close Button

Use `showCloseButton={false}` to hide the close button.

<ComponentPreview styleName="radix-nova" name="dialog-no-close-button" />

### Sticky Footer

Keep actions visible while the content scrolls.

<ComponentPreview styleName="radix-nova" name="dialog-sticky-footer" />

### Scrollable Content

Long content can scroll while the header stays in view.

<ComponentPreview styleName="radix-nova" name="dialog-scrollable-content" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="dialog-rtl" direction="rtl" />

## API Reference

See the [Radix UI](https://www.radix-ui.com/docs/primitives/components/dialog#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/direction.mdx -->

## apps/v4/content/docs/components/radix/direction.mdx

---
title: Direction
description: A provider component that sets the text direction for your application.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/primitives/docs/utilities/direction-provider
  api: https://www.radix-ui.com/primitives/docs/utilities/direction-provider#api-reference
---

The `DirectionProvider` component is used to set the text direction (`ltr` or `rtl`) for your application. This is essential for supporting right-to-left languages like Arabic, Hebrew, and Persian.

Here's a preview of the component in RTL mode. Use the language selector to switch the language. To see more examples, look for the RTL section on components pages.

<ComponentPreview
  styleName="radix-nova"
  name="card-rtl"
  direction="rtl"
  previewClassName="h-auto"
  hideCode
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add direction
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="direction"
  title="components/ui/direction.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { DirectionProvider } from "@/components/ui/direction"
```

```tsx showLineNumbers
<html dir="rtl">
  <body>
    <DirectionProvider direction="rtl">
      {/* Your app content */}
    </DirectionProvider>
  </body>
</html>
```

## useDirection

The `useDirection` hook is used to get the current direction of the application.

```tsx showLineNumbers
import { useDirection } from "@/components/ui/direction"

function MyComponent() {
  const direction = useDirection()
  return <div>Current direction: {direction}</div>
}
```


---

<!-- SOURCE: apps/v4/content/docs/components/radix/drawer.mdx -->

## apps/v4/content/docs/components/radix/drawer.mdx

---
title: Drawer
description: A drawer component for React.
base: radix
component: true
links:
  doc: https://vaul.emilkowal.ski/getting-started
---

<ComponentPreview styleName="radix-nova" name="drawer-demo" />

## About

Drawer is built on top of [Vaul](https://github.com/emilkowalski/vaul) by [emilkowalski](https://twitter.com/emilkowalski).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add drawer
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install vaul
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="drawer"
  title="components/ui/drawer.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
```

```tsx showLineNumbers
<Drawer>
  <DrawerTrigger>Open</DrawerTrigger>
  <DrawerContent>
    <DrawerHeader>
      <DrawerTitle>Are you absolutely sure?</DrawerTitle>
      <DrawerDescription>This action cannot be undone.</DrawerDescription>
    </DrawerHeader>
    <DrawerFooter>
      <Button>Submit</Button>
      <DrawerClose>
        <Button variant="outline">Cancel</Button>
      </DrawerClose>
    </DrawerFooter>
  </DrawerContent>
</Drawer>
```

## Examples

### Scrollable Content

Keep actions visible while the content scrolls.

<ComponentPreview styleName="radix-nova" name="drawer-scrollable-content" />

### Sides

Use the `direction` prop to set the side of the drawer. Available options are `top`, `right`, `bottom`, and `left`.

<ComponentPreview styleName="radix-nova" name="drawer-sides" />

### Responsive Dialog

You can combine the `Dialog` and `Drawer` components to create a responsive dialog. This renders a `Dialog` component on desktop and a `Drawer` on mobile.

<ComponentPreview styleName="radix-nova" name="drawer-dialog" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="drawer-rtl" direction="rtl" />

## API Reference

See the [Vaul documentation](https://vaul.emilkowal.ski/getting-started) for the full API reference.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/dropdown-menu.mdx -->

## apps/v4/content/docs/components/radix/dropdown-menu.mdx

---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
featured: true
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/dropdown-menu
  api: https://www.radix-ui.com/docs/primitives/components/dropdown-menu#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="dropdown-menu-demo"
  description="A dropdown menu with icons, shortcuts and sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add dropdown-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="dropdown-menu"
  title="components/ui/dropdown-menu.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```

```tsx showLineNumbers
<DropdownMenu>
  <DropdownMenuTrigger asChild>
    <Button variant="outline">Open</Button>
  </DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuGroup>
      <DropdownMenuLabel>My Account</DropdownMenuLabel>
      <DropdownMenuItem>Profile</DropdownMenuItem>
      <DropdownMenuItem>Billing</DropdownMenuItem>
    </DropdownMenuGroup>
    <DropdownMenuSeparator />
    <DropdownMenuGroup>
      <DropdownMenuItem>Team</DropdownMenuItem>
      <DropdownMenuItem>Subscription</DropdownMenuItem>
    </DropdownMenuGroup>
  </DropdownMenuContent>
</DropdownMenu>
```

## Examples

### Basic

A basic dropdown menu with labels and separators.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-basic" />

### Submenu

Use `DropdownMenuSub` to nest secondary actions.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-submenu" />

### Shortcuts

Add `DropdownMenuShortcut` to show keyboard hints.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-shortcuts" />

### Icons

Combine icons with labels for quick scanning.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-icons" />

### Checkboxes

Use `DropdownMenuCheckboxItem` for toggles.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-checkboxes" />

### Checkboxes Icons

Add icons to checkbox items.

<ComponentPreview
  styleName="radix-nova"
  name="dropdown-menu-checkboxes-icons"
/>

### Radio Group

Use `DropdownMenuRadioGroup` for exclusive choices.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-radio-group" />

### Radio Icons

Show radio options with icons.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-radio-icons" />

### Destructive

Use `variant="destructive"` for irreversible actions.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-destructive" />

### Avatar

An account switcher dropdown triggered by an avatar.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-avatar" />

### Complex

A richer example combining groups, icons, and submenus.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-complex" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="dropdown-menu-rtl"
  direction="rtl"
/>

## API Reference

See the [Radix UI documentation](https://www.radix-ui.com/docs/primitives/components/dropdown-menu) for the full API reference.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/empty.mdx -->

## apps/v4/content/docs/components/radix/empty.mdx

---
title: Empty
description: Use the Empty component to display an empty state.
base: radix
component: true
---

<ComponentPreview
  styleName="radix-nova"
  name="empty-demo"
  previewClassName="h-96 p-0"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add empty
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="empty"
  title="components/ui/empty.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
```

```tsx
<Empty>
  <EmptyHeader>
    <EmptyMedia variant="icon">
      <Icon />
    </EmptyMedia>
    <EmptyTitle>No data</EmptyTitle>
    <EmptyDescription>No data found</EmptyDescription>
  </EmptyHeader>
  <EmptyContent>
    <Button>Add data</Button>
  </EmptyContent>
</Empty>
```

## Examples

### Outline

Use the `border` utility class to create an outline empty state.

<ComponentPreview
  styleName="radix-nova"
  name="empty-outline"
  previewClassName="h-96 p-6 md:p-10"
/>

### Background

Use the `bg-*` and `bg-gradient-*` utilities to add a background to the empty state.

<ComponentPreview
  styleName="radix-nova"
  name="empty-background"
  previewClassName="h-96 p-0"
/>

### Avatar

Use the `EmptyMedia` component to display an avatar in the empty state.

<ComponentPreview
  styleName="radix-nova"
  name="empty-avatar"
  previewClassName="h-96 p-0"
/>

### Avatar Group

Use the `EmptyMedia` component to display an avatar group in the empty state.

<ComponentPreview
  styleName="radix-nova"
  name="empty-avatar-group"
  previewClassName="h-96 p-0"
/>

### InputGroup

You can add an `InputGroup` component to the `EmptyContent` component.

<ComponentPreview
  styleName="radix-nova"
  name="empty-input-group"
  previewClassName="h-96 p-0"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="empty-rtl" direction="rtl" />

## API Reference

### Empty

The main component of the empty state. Wraps the `EmptyHeader` and `EmptyContent` components.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<Empty>
  <EmptyHeader />
  <EmptyContent />
</Empty>
```

### EmptyHeader

The `EmptyHeader` component wraps the empty media, title, and description.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyHeader>
  <EmptyMedia />
  <EmptyTitle />
  <EmptyDescription />
</EmptyHeader>
```

### EmptyMedia

Use the `EmptyMedia` component to display the media of the empty state such as an icon or an image. You can also use it to display other components such as an avatar.

| Prop        | Type                  | Default   |
| ----------- | --------------------- | --------- |
| `variant`   | `"default" \| "icon"` | `default` |
| `className` | `string`              |           |

```tsx
<EmptyMedia variant="icon">
  <Icon />
</EmptyMedia>
```

```tsx
<EmptyMedia>
  <Avatar>
    <AvatarImage src="..." />
    <AvatarFallback>CN</AvatarFallback>
  </Avatar>
</EmptyMedia>
```

### EmptyTitle

Use the `EmptyTitle` component to display the title of the empty state.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyTitle>No data</EmptyTitle>
```

### EmptyDescription

Use the `EmptyDescription` component to display the description of the empty state.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyDescription>You do not have any notifications.</EmptyDescription>
```

### EmptyContent

Use the `EmptyContent` component to display the content of the empty state such as a button, input or a link.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<EmptyContent>
  <Button>Add Project</Button>
</EmptyContent>
```


---

<!-- SOURCE: apps/v4/content/docs/components/radix/field.mdx -->

## apps/v4/content/docs/components/radix/field.mdx

---
title: Field
description: Combine labels, controls, and help text to compose accessible form fields and grouped inputs.
base: radix
component: true
---

<ComponentPreview
  styleName="radix-nova"
  name="field-demo"
  previewClassName="h-[800px] p-6 md:h-[850px]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add field
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="field"
  title="components/ui/field.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSeparator,
  FieldSet,
  FieldTitle,
} from "@/components/ui/field"
```

```tsx showLineNumbers
<FieldSet>
  <FieldLegend>Profile</FieldLegend>
  <FieldDescription>This appears on invoices and emails.</FieldDescription>
  <FieldGroup>
    <Field>
      <FieldLabel htmlFor="name">Full name</FieldLabel>
      <Input id="name" autoComplete="off" placeholder="Evil Rabbit" />
      <FieldDescription>This appears on invoices and emails.</FieldDescription>
    </Field>
    <Field>
      <FieldLabel htmlFor="username">Username</FieldLabel>
      <Input id="username" autoComplete="off" aria-invalid />
      <FieldError>Choose another username.</FieldError>
    </Field>
    <Field orientation="horizontal">
      <Switch id="newsletter" />
      <FieldLabel htmlFor="newsletter">Subscribe to the newsletter</FieldLabel>
    </Field>
  </FieldGroup>
</FieldSet>
```

## Anatomy

The `Field` family is designed for composing accessible forms. A typical field is structured as follows:

```tsx showLineNumbers
<Field>
  <FieldLabel htmlFor="input-id">Label</FieldLabel>
  {/* Input, Select, Switch, etc. */}
  <FieldDescription>Optional helper text.</FieldDescription>
  <FieldError>Validation message.</FieldError>
</Field>
```

- `Field` is the core wrapper for a single field.
- `FieldContent` is a flex column that groups label and description. Not required if you have no description.
- Wrap related fields with `FieldGroup`, and use `FieldSet` with `FieldLegend` for semantic grouping.

## Form

See the [Form](/docs/forms) documentation for building forms with the `Field` component and [React Hook Form](/docs/forms/react-hook-form) or [Tanstack Form](/docs/forms/tanstack-form).

## Examples

### Input

<ComponentPreview styleName="radix-nova" name="field-input" />

### Textarea

<ComponentPreview styleName="radix-nova" name="field-textarea" />

### Select

<ComponentPreview styleName="radix-nova" name="field-select" />

### Slider

<ComponentPreview styleName="radix-nova" name="field-slider" />

### Fieldset

<ComponentPreview styleName="radix-nova" name="field-fieldset" />

### Checkbox

<ComponentPreview
  styleName="radix-nova"
  name="field-checkbox"
  previewClassName="h-[32rem]"
/>

### Radio

<ComponentPreview styleName="radix-nova" name="field-radio" />

### Switch

<ComponentPreview styleName="radix-nova" name="field-switch" />

### Choice Card

Wrap `Field` components inside `FieldLabel` to create selectable field groups. This works with `RadioItem`, `Checkbox` and `Switch` components.

<ComponentPreview styleName="radix-nova" name="field-choice-card" />

### Field Group

Stack `Field` components with `FieldGroup`. Add `FieldSeparator` to divide them.

<ComponentPreview
  styleName="radix-nova"
  name="field-group"
  previewClassName="h-96"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="field-rtl"
  direction="rtl"
  previewClassName="h-auto p-6"
/>

## Responsive Layout

- **Vertical fields:** Default orientation stacks label, control, and helper text—ideal for mobile-first layouts.
- **Horizontal fields:** Set `orientation="horizontal"` on `Field` to align the label and control side-by-side. Pair with `FieldContent` to keep descriptions aligned.
- **Responsive fields:** Set `orientation="responsive"` for automatic column layouts inside container-aware parents. Apply `@container/field-group` classes on `FieldGroup` to switch orientations at specific breakpoints.

<ComponentPreview
  styleName="radix-nova"
  name="field-responsive"
  previewClassName="h-[650px] p-6 md:h-[500px] md:p-10"
/>

## Validation and Errors

- Add `data-invalid` to `Field` to switch the entire block into an error state.
- Add `aria-invalid` on the input itself for assistive technologies.
- Render `FieldError` immediately after the control or inside `FieldContent` to keep error messages aligned with the field.

```tsx showLineNumbers /data-invalid/ /aria-invalid/
<Field data-invalid>
  <FieldLabel htmlFor="email">Email</FieldLabel>
  <Input id="email" type="email" aria-invalid />
  <FieldError>Enter a valid email address.</FieldError>
</Field>
```

## Accessibility

- `FieldSet` and `FieldLegend` keep related controls grouped for keyboard and assistive tech users.
- `Field` outputs `role="group"` so nested controls inherit labeling from `FieldLabel` and `FieldLegend` when combined.
- Apply `FieldSeparator` sparingly to ensure screen readers encounter clear section boundaries.

## API Reference

### FieldSet

Container that renders a semantic `fieldset` with spacing presets.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldSet>
  <FieldLegend>Delivery</FieldLegend>
  <FieldGroup>{/* Fields */}</FieldGroup>
</FieldSet>
```

### FieldLegend

Legend element for a `FieldSet`. Switch to the `label` variant to align with label sizing.

| Prop        | Type                  | Default    |
| ----------- | --------------------- | ---------- |
| `variant`   | `"legend" \| "label"` | `"legend"` |
| `className` | `string`              |            |

```tsx
<FieldLegend variant="label">Notification Preferences</FieldLegend>
```

The `FieldLegend` has two variants: `legend` and `label`. The `label` variant applies label sizing and alignment. Handy if you have nested `FieldSet`.

### FieldGroup

Layout wrapper that stacks `Field` components and enables container queries for responsive orientations.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldGroup className="@container/field-group flex flex-col gap-6">
  <Field>{/* ... */}</Field>
  <Field>{/* ... */}</Field>
</FieldGroup>
```

### Field

The core wrapper for a single field. Provides orientation control, invalid state styling, and spacing.

| Prop           | Type                                         | Default      |
| -------------- | -------------------------------------------- | ------------ |
| `orientation`  | `"vertical" \| "horizontal" \| "responsive"` | `"vertical"` |
| `className`    | `string`                                     |              |
| `data-invalid` | `boolean`                                    |              |

```tsx
<Field orientation="horizontal">
  <FieldLabel htmlFor="remember">Remember me</FieldLabel>
  <Switch id="remember" />
</Field>
```

### FieldContent

Flex column that groups control and descriptions when the label sits beside the control. Not required if you have no description.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<Field>
  <Checkbox id="notifications" />
  <FieldContent>
    <FieldLabel htmlFor="notifications">Notifications</FieldLabel>
    <FieldDescription>Email, SMS, and push options.</FieldDescription>
  </FieldContent>
</Field>
```

### FieldLabel

Label styled for both direct inputs and nested `Field` children.

| Prop        | Type      | Default |
| ----------- | --------- | ------- |
| `className` | `string`  |         |
| `asChild`   | `boolean` | `false` |

```tsx
<FieldLabel htmlFor="email">Email</FieldLabel>
```

### FieldTitle

Renders a title with label styling inside `FieldContent`.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldContent>
  <FieldTitle>Enable Touch ID</FieldTitle>
  <FieldDescription>Unlock your device faster.</FieldDescription>
</FieldContent>
```

### FieldDescription

Helper text slot that automatically balances long lines in horizontal layouts.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldDescription>We never share your email with anyone.</FieldDescription>
```

### FieldSeparator

Visual divider to separate sections inside a `FieldGroup`. Accepts optional inline content.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<FieldSeparator>Or continue with</FieldSeparator>
```

### FieldError

Accessible error container that accepts children or an `errors` array (e.g., from `react-hook-form`).

| Prop        | Type                                       | Default |
| ----------- | ------------------------------------------ | ------- |
| `errors`    | `Array<{ message?: string } \| undefined>` |         |
| `className` | `string`                                   |         |

```tsx
<FieldError errors={errors.username} />
```

When the `errors` array contains multiple messages, the component renders a list automatically.

`FieldError` also accepts issues produced by any validator that implements [Standard Schema](https://standardschema.dev/), including Zod, Valibot, and ArkType. Pass the `issues` array from the schema result directly to render a unified error list across libraries.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/hover-card.mdx -->

## apps/v4/content/docs/components/radix/hover-card.mdx

---
title: Hover Card
description: For sighted users to preview content available behind a link.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/hover-card
  api: https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-demo"
  previewClassName="h-80"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add hover-card
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="hover-card"
  title="components/ui/hover-card.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"
```

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>
    The React Framework – created and maintained by @vercel.
  </HoverCardContent>
</HoverCard>
```

## Trigger Delays

Use `openDelay` and `closeDelay` on the `HoverCard` to control when the card opens and
closes.

```tsx showLineNumbers
<HoverCard openDelay={100} closeDelay={200}>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>Content</HoverCardContent>
</HoverCard>
```

## Positioning

Use the `side` and `align` props on `HoverCardContent` to control placement.

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent side="top" align="start">
    Content
  </HoverCardContent>
</HoverCard>
```

## Examples

### Basic

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-demo"
  previewClassName="h-80"
/>

### Sides

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-sides"
  previewClassName="h-[22rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-rtl"
  direction="rtl"
  previewClassName="h-80"
/>

## API Reference

See the [Radix UI](https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/input-group.mdx -->

## apps/v4/content/docs/components/radix/input-group.mdx

---
title: Input Group
description: Add addons, buttons, and helper content to inputs.
base: radix
component: true
---

import { IconInfoCircle } from "@tabler/icons-react"

<ComponentPreview
  styleName="radix-nova"
  name="input-group-demo"
  previewClassName="h-[26rem]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add input-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="input-group"
  title="components/ui/input-group.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group"
```

```tsx showLineNumbers
<InputGroup>
  <InputGroupInput placeholder="Search..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

## Align

Use the `align` prop on `InputGroupAddon` to position the addon relative to the input.

<Callout>
  For proper focus management, `InputGroupAddon` should always be placed after
  `InputGroupInput` or `InputGroupTextarea` in the DOM. Use the `align` prop to
  visually position the addon.
</Callout>

### inline-start

Use `align="inline-start"` to position the addon at the start of the input. This is the default.

<ComponentPreview
  styleName="radix-nova"
  name="input-group-inline-start"
  previewClassName="h-48"
/>

### inline-end

Use `align="inline-end"` to position the addon at the end of the input.

<ComponentPreview
  styleName="radix-nova"
  name="input-group-inline-end"
  previewClassName="h-48"
/>

### block-start

Use `align="block-start"` to position the addon above the input.

<ComponentPreview
  styleName="radix-nova"
  name="input-group-block-start"
  previewClassName="h-96"
/>

### block-end

Use `align="block-end"` to position the addon below the input.

<ComponentPreview
  styleName="radix-nova"
  name="input-group-block-end"
  previewClassName="h-[26rem]"
/>

## Examples

### Icon

<ComponentPreview
  styleName="radix-nova"
  name="input-group-icon"
  previewClassName="h-80"
/>

### Text

<ComponentPreview
  styleName="radix-nova"
  name="input-group-text"
  previewClassName="h-80"
/>

### Button

<ComponentPreview
  styleName="radix-nova"
  name="input-group-button"
  previewClassName="h-72"
/>

### Kbd

<ComponentPreview
  styleName="radix-nova"
  name="input-group-kbd"
  previewClassName="h-40"
/>

### Dropdown

<ComponentPreview
  styleName="radix-nova"
  name="input-group-dropdown"
  previewClassName="h-56"
/>

### Spinner

<ComponentPreview
  styleName="radix-nova"
  name="input-group-spinner"
  previewClassName="h-80"
/>

### Textarea

<ComponentPreview
  styleName="radix-nova"
  name="input-group-textarea"
  previewClassName="h-96"
/>

### Custom Input

Add the `data-slot="input-group-control"` attribute to your custom input for automatic focus state handling.

Here's an example of a custom resizable textarea from a third-party library.

<ComponentPreview
  styleName="radix-nova"
  name="input-group-custom"
  previewClassName="h-56"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="input-group-rtl"
  direction="rtl"
  previewClassName="h-[30rem]"
/>

## API Reference

### InputGroup

The main component that wraps inputs and addons.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

```tsx
<InputGroup>
  <InputGroupInput />
  <InputGroupAddon />
</InputGroup>
```

### InputGroupAddon

Displays icons, text, buttons, or other content alongside inputs.

<Callout icon={<IconInfoCircle />} title="Focus Navigation">
  For proper focus navigation, the `InputGroupAddon` component should be placed
  after the input. Set the `align` prop to position the addon.
</Callout>

| Prop        | Type                                                             | Default          |
| ----------- | ---------------------------------------------------------------- | ---------------- |
| `align`     | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` |
| `className` | `string`                                                         |                  |

```tsx
<InputGroupAddon align="inline-end">
  <SearchIcon />
</InputGroupAddon>
```

**For `<InputGroupInput />`, use the `inline-start` or `inline-end` alignment. For `<InputGroupTextarea />`, use the `block-start` or `block-end` alignment.**

The `InputGroupAddon` component can have multiple `InputGroupButton` components and icons.

```tsx
<InputGroupAddon>
  <InputGroupButton>Button</InputGroupButton>
  <InputGroupButton>Button</InputGroupButton>
</InputGroupAddon>
```

### InputGroupButton

Displays buttons within input groups.

| Prop        | Type                                                                          | Default   |
| ----------- | ----------------------------------------------------------------------------- | --------- |
| `size`      | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"`                                      | `"xs"`    |
| `variant`   | `"default" \| "destructive" \| "outline" \| "secondary" \| "ghost" \| "link"` | `"ghost"` |
| `className` | `string`                                                                      |           |

```tsx
<InputGroupButton>Button</InputGroupButton>
<InputGroupButton size="icon-xs" aria-label="Copy">
  <CopyIcon />
</InputGroupButton>
```

### InputGroupInput

Replacement for `<Input />` when building input groups. This component has the input group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

All other props are passed through to the underlying `<Input />` component.

```tsx
<InputGroup>
  <InputGroupInput placeholder="Enter text..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

### InputGroupTextarea

Replacement for `<Textarea />` when building input groups. This component has the textarea group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

All other props are passed through to the underlying `<Textarea />` component.

```tsx
<InputGroup>
  <InputGroupTextarea placeholder="Enter message..." />
  <InputGroupAddon align="block-end">
    <InputGroupButton>Send</InputGroupButton>
  </InputGroupAddon>
</InputGroup>
```

## Changelog

### 2025-10-06 `InputGroup`

Add the `min-w-0` class to the `InputGroup` component. See [diff](https://github.com/shadcn-ui/ui/pull/8341/files#diff-0e2ee95d0050ca4c5d82339df86c54e14a6739dc4638fdda0eec8f73aebc2da9).


---

<!-- SOURCE: apps/v4/content/docs/components/radix/input-otp.mdx -->

## apps/v4/content/docs/components/radix/input-otp.mdx

---
title: Input OTP
description: Accessible one-time password component with copy-paste functionality.
base: radix
component: true
links:
  doc: https://input-otp.rodz.dev
---

<ComponentPreview styleName="radix-nova" name="input-otp-demo" />

## About

Input OTP is built on top of [input-otp](https://github.com/guilhermerodz/input-otp) by [@guilherme_rodz](https://twitter.com/guilherme_rodz).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add input-otp
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install input-otp
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="input-otp"
  title="components/ui/input-otp.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"
```

```tsx showLineNumbers
<InputOTP maxLength={6}>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    <InputOTPSlot index={1} />
    <InputOTPSlot index={2} />
  </InputOTPGroup>
  <InputOTPSeparator />
  <InputOTPGroup>
    <InputOTPSlot index={3} />
    <InputOTPSlot index={4} />
    <InputOTPSlot index={5} />
  </InputOTPGroup>
</InputOTP>
```

## Pattern

Use the `pattern` prop to define a custom pattern for the OTP input.

```tsx showLineNumbers {1,5}
import { REGEXP_ONLY_DIGITS_AND_CHARS } from "input-otp"

;<InputOTP maxLength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
  ...
</InputOTP>
```

<ComponentPreview styleName="radix-nova" name="input-otp-pattern" />

## Examples

### Separator

Use the `<InputOTPSeparator />` component to add a separator between input groups.

<ComponentPreview styleName="radix-nova" name="input-otp-separator" />

### Disabled

Use the `disabled` prop to disable the input.

<ComponentPreview styleName="radix-nova" name="input-otp-disabled" />

### Controlled

Use the `value` and `onChange` props to control the input value.

<ComponentPreview styleName="radix-nova" name="input-otp-controlled" />

### Invalid

Use `aria-invalid` on the slots to show an error state.

<ComponentPreview styleName="radix-nova" name="input-otp-invalid" />

### Four Digits

A common pattern for PIN codes. This uses the `pattern={REGEXP_ONLY_DIGITS}` prop.

<ComponentPreview styleName="radix-nova" name="input-otp-four-digits" />

### Alphanumeric

Use `REGEXP_ONLY_DIGITS_AND_CHARS` to accept both letters and numbers.

<ComponentPreview styleName="radix-nova" name="input-otp-alphanumeric" />

### Form

<ComponentPreview
  styleName="radix-nova"
  name="input-otp-form"
  previewClassName="h-[30rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="input-otp-rtl" direction="rtl" />

## API Reference

See the [input-otp](https://input-otp.rodz.dev) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/input.mdx -->

## apps/v4/content/docs/components/radix/input.mdx

---
title: Input
description: A text input component for forms and user data entry with built-in styling and accessibility features.
base: radix
component: true
---

<ComponentPreview
  styleName="radix-nova"
  name="input-demo"
  previewClassName="*:max-w-xs"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add input
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="input"
  title="components/ui/input.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Input } from "@/components/ui/input"
```

```tsx
<Input />
```

## Examples

### Basic

<ComponentPreview
  styleName="radix-nova"
  name="input-basic"
  previewClassName="*:max-w-xs"
/>

### Field

Use `Field`, `FieldLabel`, and `FieldDescription` to create an input with a
label and description.

<ComponentPreview
  styleName="radix-nova"
  name="input-field"
  previewClassName="*:max-w-xs"
/>

### Field Group

Use `FieldGroup` to show multiple `Field` blocks and to build forms.

<ComponentPreview
  styleName="radix-nova"
  name="input-fieldgroup"
  previewClassName="*:max-w-xs"
/>

### Disabled

Use the `disabled` prop to disable the input. To style the disabled state, add the `data-disabled` attribute to the `Field` component.

<ComponentPreview
  styleName="radix-nova"
  name="input-disabled"
  previewClassName="*:max-w-xs"
/>

### Invalid

Use the `aria-invalid` prop to mark the input as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field` component.

<ComponentPreview
  styleName="radix-nova"
  name="input-invalid"
  previewClassName="*:max-w-xs"
/>

### File

Use the `type="file"` prop to create a file input.

<ComponentPreview
  styleName="radix-nova"
  name="input-file"
  previewClassName="*:max-w-xs"
/>

### Inline

Use `Field` with `orientation="horizontal"` to create an inline input.
Pair with `Button` to create a search input with a button.

<ComponentPreview
  styleName="radix-nova"
  name="input-inline"
  previewClassName="*:max-w-xs"
/>

### Grid

Use a grid layout to place multiple inputs side by side.

<ComponentPreview
  styleName="radix-nova"
  name="input-grid"
  previewClassName="p-6"
/>

### Required

Use the `required` attribute to indicate required inputs.

<ComponentPreview
  styleName="radix-nova"
  name="input-required"
  previewClassName="*:max-w-xs"
/>

### Badge

Use `Badge` in the label to highlight a recommended field.

<ComponentPreview
  styleName="radix-nova"
  name="input-badge"
  previewClassName="*:max-w-xs"
/>

### Input Group

To add icons, text, or buttons inside an input, use the `InputGroup` component. See the [Input Group](/docs/components/input-group) component for more examples.

<ComponentPreview
  styleName="radix-nova"
  name="input-input-group"
  previewClassName="*:max-w-xs"
/>

### Button Group

To add buttons to an input, use the `ButtonGroup` component. See the [Button Group](/docs/components/button-group) component for more examples.

<ComponentPreview
  styleName="radix-nova"
  name="input-button-group"
  previewClassName="*:max-w-xs"
/>

### Form

A full form example with multiple inputs, a select, and a button.

<ComponentPreview
  styleName="radix-nova"
  name="input-form"
  previewClassName="h-[32rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="input-rtl"
  direction="rtl"
  previewClassName="*:max-w-xs"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/radix/item.mdx -->

## apps/v4/content/docs/components/radix/item.mdx

---
title: Item
description: A versatile component for displaying content with media, title, description, and actions.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="item-demo" />

The `Item` component is a straightforward flex container that can house nearly any type of content. Use it to display a title, description, and actions. Group it with the `ItemGroup` component to create a list of items.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add item
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="item"
  title="components/ui/item.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
```

```tsx showLineNumbers
<Item>
  <ItemMedia variant="icon">
    <Icon />
  </ItemMedia>
  <ItemContent>
    <ItemTitle>Title</ItemTitle>
    <ItemDescription>Description</ItemDescription>
  </ItemContent>
  <ItemActions>
    <Button>Action</Button>
  </ItemActions>
</Item>
```

## Item vs Field

Use `Field` if you need to display a form input such as a checkbox, input, radio, or select.

If you only need to display content such as a title, description, and actions, use `Item`.

## Variant

Use the `variant` prop to change the visual style of the item.

<ComponentPreview
  styleName="radix-nova"
  name="item-variant"
  previewClassName="h-96"
/>

## Size

Use the `size` prop to change the size of the item. Available sizes are `default`, `sm`, and `xs`.

<ComponentPreview
  styleName="radix-nova"
  name="item-size"
  previewClassName="h-96"
/>

## Examples

### Icon

Use `ItemMedia` with `variant="icon"` to display an icon.

<ComponentPreview styleName="radix-nova" name="item-icon" />

### Avatar

You can use `ItemMedia` with `variant="avatar"` to display an avatar.

<ComponentPreview styleName="radix-nova" name="item-avatar" />

### Image

Use `ItemMedia` with `variant="image"` to display an image.

<ComponentPreview styleName="radix-nova" name="item-image" />

### Group

Use `ItemGroup` to group related items together.

<ComponentPreview
  styleName="radix-nova"
  name="item-group"
  previewClassName="h-96"
/>

### Header

Use `ItemHeader` to add a header above the item content.

<ComponentPreview
  styleName="radix-nova"
  name="item-header"
  previewClassName="h-96"
/>

### Link

Use the `asChild` prop to render the item as a link. The hover and focus states will be applied to the anchor element.

<ComponentPreview styleName="radix-nova" name="item-link" />

```tsx showLineNumbers
<Item asChild>
  <a href="/dashboard">
    <ItemMedia variant="icon">
      <HomeIcon />
    </ItemMedia>
    <ItemContent>
      <ItemTitle>Dashboard</ItemTitle>
      <ItemDescription>Overview of your account and activity.</ItemDescription>
    </ItemContent>
  </a>
</Item>
```

### Dropdown

<ComponentPreview styleName="radix-nova" name="item-dropdown" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="item-rtl" direction="rtl" />

## API Reference

### Item

The main component for displaying content with media, title, description, and actions.

| Prop      | Type                                | Default     |
| --------- | ----------------------------------- | ----------- |
| `variant` | `"default" \| "outline" \| "muted"` | `"default"` |
| `size`    | `"default" \| "sm" \| "xs"`         | `"default"` |
| `asChild` | `boolean`                           | `false`     |

### ItemGroup

A container that groups related items together with consistent styling.

```tsx
<ItemGroup>
  <Item />
  <Item />
</ItemGroup>
```

### ItemSeparator

A separator between items in a group.

```tsx
<ItemGroup>
  <Item />
  <ItemSeparator />
  <Item />
</ItemGroup>
```

### ItemMedia

Use `ItemMedia` to display media content such as icons, images, or avatars.

| Prop      | Type                             | Default     |
| --------- | -------------------------------- | ----------- |
| `variant` | `"default" \| "icon" \| "image"` | `"default"` |

```tsx
<ItemMedia variant="icon">
  <Icon />
</ItemMedia>
```

```tsx
<ItemMedia variant="image">
  <img src="..." alt="..." />
</ItemMedia>
```

### ItemContent

Wraps the title and description of the item.

```tsx
<ItemContent>
  <ItemTitle>Title</ItemTitle>
  <ItemDescription>Description</ItemDescription>
</ItemContent>
```

### ItemTitle

Displays the title of the item.

```tsx
<ItemTitle>Item Title</ItemTitle>
```

### ItemDescription

Displays the description of the item.

```tsx
<ItemDescription>Item description</ItemDescription>
```

### ItemActions

Container for action buttons or other interactive elements.

```tsx
<ItemActions>
  <Button>Action</Button>
</ItemActions>
```

### ItemHeader

Displays a header above the item content.

```tsx
<Item>
  <ItemHeader>Header</ItemHeader>
  <ItemContent>...</ItemContent>
</Item>
```

### ItemFooter

Displays a footer below the item content.

```tsx
<Item>
  <ItemContent>...</ItemContent>
  <ItemFooter>Footer</ItemFooter>
</Item>
```


---

<!-- SOURCE: apps/v4/content/docs/components/radix/kbd.mdx -->

## apps/v4/content/docs/components/radix/kbd.mdx

---
title: Kbd
description: Used to display textual user input from keyboard.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="kbd-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add kbd
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="kbd"
  title="components/ui/kbd.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Kbd } from "@/components/ui/kbd"
```

```tsx
<Kbd>Ctrl</Kbd>
```

## Examples

### Group

Use the `KbdGroup` component to group keyboard keys together.

<ComponentPreview styleName="radix-nova" name="kbd-group" />

### Button

Use the `Kbd` component inside a `Button` component to display a keyboard key inside a button.

<ComponentPreview styleName="radix-nova" name="kbd-button" />

### Tooltip

You can use the `Kbd` component inside a `Tooltip` component to display a tooltip with a keyboard key.

<ComponentPreview styleName="radix-nova" name="kbd-tooltip" />

### Input Group

You can use the `Kbd` component inside a `InputGroupAddon` component to display a keyboard key inside an input group.

<ComponentPreview styleName="radix-nova" name="kbd-input-group" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="kbd-rtl" direction="rtl" />

## API Reference

### Kbd

Use the `Kbd` component to display a keyboard key.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

```tsx
<Kbd>Ctrl</Kbd>
```

### KbdGroup

Use the `KbdGroup` component to group `Kbd` components together.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

```tsx
<KbdGroup>
  <Kbd>Ctrl</Kbd>
  <Kbd>B</Kbd>
</KbdGroup>
```


---

<!-- SOURCE: apps/v4/content/docs/components/radix/label.mdx -->

## apps/v4/content/docs/components/radix/label.mdx

---
title: Label
description: Renders an accessible label associated with controls.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/label
  api: https://www.radix-ui.com/docs/primitives/components/label#api-reference
---

<ComponentPreview styleName="radix-nova" name="label-demo" />

<Callout>
  For form fields, use the [Field](/docs/components/radix/field) component which
  includes built-in label, description, and error handling.
</Callout>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add label
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="label"
  title="components/ui/label.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Label } from "@/components/ui/label"
```

```tsx
<Label htmlFor="email">Your email address</Label>
```

## Label in Field

For form fields, use the [Field](/docs/components/radix/field) component which
includes built-in `FieldLabel`, `FieldDescription`, and `FieldError` components.

```tsx
<Field>
  <FieldLabel htmlFor="email">Your email address</FieldLabel>
  <Input id="email" />
</Field>
```

<ComponentPreview
  styleName="radix-nova"
  name="field-demo"
  previewClassName="h-[44rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="label-rtl" direction="rtl" />

## API Reference

See the [Radix UI Label](https://www.radix-ui.com/docs/primitives/components/label#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/menubar.mdx -->

## apps/v4/content/docs/components/radix/menubar.mdx

---
title: Menubar
description: A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/menubar
  api: https://www.radix-ui.com/docs/primitives/components/menubar#api-reference
---

<ComponentPreview styleName="radix-nova" name="menubar-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add menubar
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="menubar"
  title="components/ui/menubar.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Menubar,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
```

```tsx showLineNumbers
<Menubar>
  <MenubarMenu>
    <MenubarTrigger>File</MenubarTrigger>
    <MenubarContent>
      <MenubarGroup>
        <MenubarItem>
          New Tab <MenubarShortcut>⌘T</MenubarShortcut>
        </MenubarItem>
        <MenubarItem>New Window</MenubarItem>
      </MenubarGroup>
      <MenubarSeparator />
      <MenubarGroup>
        <MenubarItem>Share</MenubarItem>
        <MenubarItem>Print</MenubarItem>
      </MenubarGroup>
    </MenubarContent>
  </MenubarMenu>
</Menubar>
```

## Examples

### Checkbox

Use `MenubarCheckboxItem` for toggleable options.

<ComponentPreview styleName="radix-nova" name="menubar-checkbox" />

### Radio

Use `MenubarRadioGroup` and `MenubarRadioItem` for single-select options.

<ComponentPreview styleName="radix-nova" name="menubar-radio" />

### Submenu

Use `MenubarSub`, `MenubarSubTrigger`, and `MenubarSubContent` for nested menus.

<ComponentPreview styleName="radix-nova" name="menubar-submenu" />

### With Icons

<ComponentPreview styleName="radix-nova" name="menubar-icons" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="menubar-rtl" direction="rtl" />

## API Reference

See the [Radix UI Menubar](https://www.radix-ui.com/docs/primitives/components/menubar#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/native-select.mdx -->

## apps/v4/content/docs/components/radix/native-select.mdx

---
title: Native Select
description: A styled native HTML select element with consistent design system integration.
base: radix
component: true
---

import { InfoIcon } from "lucide-react"

<Callout variant="info" icon={<InfoIcon className="translate-y-[3px]!" />}>
  For a styled select component, see the [Select](/docs/components/select)
  component.
</Callout>

<ComponentPreview styleName="radix-nova" name="native-select-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add native-select
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="native-select"
  title="components/ui/native-select.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  NativeSelect,
  NativeSelectOptGroup,
  NativeSelectOption,
} from "@/components/ui/native-select"
```

```tsx showLineNumbers
<NativeSelect>
  <NativeSelectOption value="">Select a fruit</NativeSelectOption>
  <NativeSelectOption value="apple">Apple</NativeSelectOption>
  <NativeSelectOption value="banana">Banana</NativeSelectOption>
  <NativeSelectOption value="blueberry">Blueberry</NativeSelectOption>
  <NativeSelectOption value="pineapple">Pineapple</NativeSelectOption>
</NativeSelect>
```

## Examples

### Groups

Use `NativeSelectOptGroup` to organize options into categories.

<ComponentPreview styleName="radix-nova" name="native-select-groups" />

### Disabled

Add the `disabled` prop to the `NativeSelect` component to disable the select.

<ComponentPreview styleName="radix-nova" name="native-select-disabled" />

### Invalid

Use `aria-invalid` to show validation errors and the `data-invalid` attribute to the `Field` component for styling.

<ComponentPreview styleName="radix-nova" name="native-select-invalid" />

## Native Select vs Select

- Use `NativeSelect` for native browser behavior, better performance, or mobile-optimized dropdowns.
- Use `Select` for custom styling, animations, or complex interactions.

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="native-select-rtl"
  direction="rtl"
/>

## API Reference

### NativeSelect

The main select component that wraps the native HTML select element.

```tsx
<NativeSelect>
  <NativeSelectOption value="option1">Option 1</NativeSelectOption>
  <NativeSelectOption value="option2">Option 2</NativeSelectOption>
</NativeSelect>
```

### NativeSelectOption

Represents an individual option within the select.

| Prop       | Type      | Default |
| ---------- | --------- | ------- |
| `value`    | `string`  |         |
| `disabled` | `boolean` | `false` |

### NativeSelectOptGroup

Groups related options together for better organization.

| Prop       | Type      | Default |
| ---------- | --------- | ------- |
| `label`    | `string`  |         |
| `disabled` | `boolean` | `false` |

```tsx
<NativeSelectOptGroup label="Fruits">
  <NativeSelectOption value="apple">Apple</NativeSelectOption>
  <NativeSelectOption value="banana">Banana</NativeSelectOption>
</NativeSelectOptGroup>
```


---

<!-- SOURCE: apps/v4/content/docs/components/radix/navigation-menu.mdx -->

## apps/v4/content/docs/components/radix/navigation-menu.mdx

---
title: Navigation Menu
description: A collection of links for navigating websites.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/navigation-menu
  api: https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="navigation-menu-demo"
  previewClassName="h-96"
  className="overflow-visible"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add navigation-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="navigation-menu"
  title="components/ui/navigation-menu.tsx"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
```

```tsx showLineNumbers
<NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
      <NavigationMenuTrigger>Item One</NavigationMenuTrigger>
      <NavigationMenuContent>
        <NavigationMenuLink>Link</NavigationMenuLink>
      </NavigationMenuContent>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>
```

## Link Component

Use the `asChild` prop to compose a custom link component such as Next.js `Link`.

```tsx showLineNumbers
import Link from "next/link"

import {
  NavigationMenuItem,
  NavigationMenuLink,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"

export function NavigationMenuDemo() {
  return (
    <NavigationMenuItem>
      <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
        <Link href="/docs">Documentation</Link>
      </NavigationMenuLink>
    </NavigationMenuItem>
  )
}
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="navigation-menu-rtl"
  direction="rtl"
  previewClassName="h-96"
  className="overflow-visible"
/>

## API Reference

See the [Radix UI Navigation Menu](https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference) documentation for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/pagination.mdx -->

## apps/v4/content/docs/components/radix/pagination.mdx

---
title: Pagination
description: Pagination with page navigation, next and previous links.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="pagination-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add pagination
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="pagination"
  title="components/ui/pagination.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
```

```tsx showLineNumbers
<Pagination>
  <PaginationContent>
    <PaginationItem>
      <PaginationPrevious href="#" />
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">1</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#" isActive>
        2
      </PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">3</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationEllipsis />
    </PaginationItem>
    <PaginationItem>
      <PaginationNext href="#" />
    </PaginationItem>
  </PaginationContent>
</Pagination>
```

## Examples

### Simple

A simple pagination with only page numbers.

<ComponentPreview styleName="radix-nova" name="pagination-simple" />

### Icons Only

Use just the previous and next buttons without page numbers. This is useful for data tables with a rows per page selector.

<ComponentPreview styleName="radix-nova" name="pagination-icons-only" />

## Next.js

By default the `<PaginationLink />` component will render an `<a />` tag.

To use the Next.js `<Link />` component, make the following updates to `pagination.tsx`.

```diff showLineNumbers /typeof Link/ {1}
+ import Link from "next/link"

- type PaginationLinkProps = ... & React.ComponentProps<"a">
+ type PaginationLinkProps = ... & React.ComponentProps<typeof Link>

const PaginationLink = ({...props }: ) => (
  <PaginationItem>
-   <a>
+   <Link>
      // ...
-   </a>
+   </Link>
  </PaginationItem>
)

```

<Callout className="mt-6">

**Note:** We are making updates to the cli to automatically do this for you.

</Callout>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="pagination-rtl"
  direction="rtl"
/>

## Changelog

### RTL Support

If you're upgrading from a previous version of the `Pagination` component, you'll need to apply the following updates to add the `text` prop:

<Steps>

<Step>Update `PaginationPrevious`.</Step>

```diff
  function PaginationPrevious({
    className,
+   text = "Previous",
    ...props
- }: React.ComponentProps<typeof PaginationLink>) {
+ }: React.ComponentProps<typeof PaginationLink> & { text?: string }) {
    return (
      <PaginationLink
        aria-label="Go to previous page"
        size="default"
        className={cn("cn-pagination-previous", className)}
        {...props}
      >
        <ChevronLeftIcon />
        <span className="cn-pagination-previous-text hidden sm:block">
-         Previous
+         {text}
        </span>
      </PaginationLink>
    )
  }
```

<Step>Update `PaginationNext`.</Step>

```diff
  function PaginationNext({
    className,
+   text = "Next",
    ...props
- }: React.ComponentProps<typeof PaginationLink>) {
+ }: React.ComponentProps<typeof PaginationLink> & { text?: string }) {
    return (
      <PaginationLink
        aria-label="Go to next page"
        size="default"
        className={cn("cn-pagination-next", className)}
        {...props}
      >
-       <span className="cn-pagination-next-text hidden sm:block">Next</span>
+       <span className="cn-pagination-next-text hidden sm:block">{text}</span>
        <ChevronRightIcon />
      </PaginationLink>
    )
  }
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/components/radix/popover.mdx -->

## apps/v4/content/docs/components/radix/popover.mdx

---
title: Popover
description: Displays rich content in a portal, triggered by a button.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/popover
  api: https://www.radix-ui.com/docs/primitives/components/popover#api-reference
---

<ComponentPreview styleName="radix-nova" name="popover-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add popover
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="popover"
  title="components/ui/popover.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Popover,
  PopoverContent,
  PopoverDescription,
  PopoverHeader,
  PopoverTitle,
  PopoverTrigger,
} from "@/components/ui/popover"
```

```tsx showLineNumbers
<Popover>
  <PopoverTrigger asChild>
    <Button variant="outline">Open Popover</Button>
  </PopoverTrigger>
  <PopoverContent>
    <PopoverHeader>
      <PopoverTitle>Title</PopoverTitle>
      <PopoverDescription>Description text here.</PopoverDescription>
    </PopoverHeader>
  </PopoverContent>
</Popover>
```

## Examples

### Basic

A simple popover with a header, title, and description.

<ComponentPreview styleName="radix-nova" name="popover-basic" />

### Align

Use the `align` prop on `PopoverContent` to control the horizontal alignment.

<ComponentPreview styleName="radix-nova" name="popover-alignments" />

### With Form

A popover with form fields inside.

<ComponentPreview styleName="radix-nova" name="popover-form" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="popover-rtl" direction="rtl" />

## API Reference

See the [Radix UI Popover](https://www.radix-ui.com/docs/primitives/components/popover#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/progress.mdx -->

## apps/v4/content/docs/components/radix/progress.mdx

---
title: Progress
description: Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/progress
  api: https://www.radix-ui.com/docs/primitives/components/progress#api-reference
---

<ComponentPreview styleName="radix-nova" name="progress-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add progress
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="progress"
  title="components/ui/progress.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Progress } from "@/components/ui/progress"
```

```tsx showLineNumbers
<Progress value={33} />
```

## Examples

### Label

Use a `Field` component to add a label to the progress bar.

<ComponentPreview styleName="radix-nova" name="progress-label" />

### Controlled

A progress bar that can be controlled by a slider.

<ComponentPreview styleName="radix-nova" name="progress-controlled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="progress-rtl" direction="rtl" />

## API Reference

See the [Radix UI Progress](https://www.radix-ui.com/docs/primitives/components/progress#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/radio-group.mdx -->

## apps/v4/content/docs/components/radix/radio-group.mdx

---
title: Radio Group
description: A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/radio-group
  api: https://www.radix-ui.com/docs/primitives/components/radio-group#api-reference
---

<ComponentPreview styleName="radix-nova" name="radio-group-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add radio-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="radio-group"
  title="components/ui/radio-group.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
```

```tsx showLineNumbers
<RadioGroup defaultValue="option-one">
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-one" id="option-one" />
    <Label htmlFor="option-one">Option One</Label>
  </div>
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-two" id="option-two" />
    <Label htmlFor="option-two">Option Two</Label>
  </div>
</RadioGroup>
```

## Examples

### Description

Radio group items with a description using the `Field` component.

<ComponentPreview styleName="radix-nova" name="radio-group-description" />

### Choice Card

Use `FieldLabel` to wrap the entire `Field` for a clickable card-style selection.

<ComponentPreview styleName="radix-nova" name="radio-group-choice-card" />

### Fieldset

Use `FieldSet` and `FieldLegend` to group radio items with a label and description.

<ComponentPreview styleName="radix-nova" name="radio-group-fieldset" />

### Disabled

Use the `disabled` prop on `RadioGroupItem` to disable individual items.

<ComponentPreview styleName="radix-nova" name="radio-group-disabled" />

### Invalid

Use `aria-invalid` on `RadioGroupItem` and `data-invalid` on `Field` to show validation errors.

<ComponentPreview styleName="radix-nova" name="radio-group-invalid" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="radio-group-rtl"
  direction="rtl"
/>

## API Reference

See the [Radix UI Radio Group](https://www.radix-ui.com/docs/primitives/components/radio-group#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/resizable.mdx -->

## apps/v4/content/docs/components/radix/resizable.mdx

---
title: Resizable
description: Accessible resizable panel groups and layouts with keyboard support.
base: radix
component: true
links:
  doc: https://github.com/bvaughn/react-resizable-panels
  api: https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels
---

<ComponentPreview
  styleName="radix-nova"
  name="resizable-demo"
  previewClassName="h-80"
/>

## About

The `Resizable` component is built on top of [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels) by [bvaughn](https://github.com/bvaughn).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add resizable
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install react-resizable-panels
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="resizable"
  title="components/ui/resizable.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
```

```tsx showLineNumbers
<ResizablePanelGroup orientation="horizontal">
  <ResizablePanel>One</ResizablePanel>
  <ResizableHandle />
  <ResizablePanel>Two</ResizablePanel>
</ResizablePanelGroup>
```

## Examples

### Vertical

Use `orientation="vertical"` for vertical resizing.

<ComponentPreview styleName="radix-nova" name="resizable-vertical" />

### Handle

Use the `withHandle` prop on `ResizableHandle` to show a visible handle.

<ComponentPreview styleName="radix-nova" name="resizable-handle" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="resizable-rtl" direction="rtl" />

## API Reference

See the [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels) documentation.

## Changelog

### 2025-02-02 `react-resizable-panels` v4

Updated to `react-resizable-panels` v4. See the [v4.0.0 release notes](https://github.com/bvaughn/react-resizable-panels/releases/tag/4.0.0) for full details.

If you're using `react-resizable-panels` primitives directly, note the following changes:

| v3                           | v4                      |
| ---------------------------- | ----------------------- |
| `PanelGroup`                 | `Group`                 |
| `PanelResizeHandle`          | `Separator`             |
| `direction` prop             | `orientation` prop      |
| `defaultSize={50}`           | `defaultSize="50%"`     |
| `onLayout`                   | `onLayoutChange`        |
| `ImperativePanelHandle`      | `PanelImperativeHandle` |
| `ref` prop on Panel          | `panelRef` prop         |
| `data-panel-group-direction` | `aria-orientation`      |

<Callout>
  The shadcn/ui wrapper components (`ResizablePanelGroup`, `ResizablePanel`,
  `ResizableHandle`) remain unchanged.
</Callout>


---

<!-- SOURCE: apps/v4/content/docs/components/radix/scroll-area.mdx -->

## apps/v4/content/docs/components/radix/scroll-area.mdx

---
title: Scroll Area
description: Augments native scroll functionality for custom, cross-browser styling.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/scroll-area
  api: https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="scroll-area-demo"
  previewClassName="h-96"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add scroll-area
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="scroll-area"
  title="components/ui/scroll-area.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
```

```tsx showLineNumbers
<ScrollArea className="h-[200px] w-[350px] rounded-md border p-4">
  Your scrollable content here.
</ScrollArea>
```

## Examples

### Horizontal

Use `ScrollBar` with `orientation="horizontal"` for horizontal scrolling.

<ComponentPreview styleName="radix-nova" name="scroll-area-horizontal-demo" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="scroll-area-rtl"
  direction="rtl"
  previewClassName="h-auto"
/>

## API Reference

See the [Radix UI Scroll Area](https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/select.mdx -->

## apps/v4/content/docs/components/radix/select.mdx

---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
base: radix
component: true
featured: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/select
  api: https://www.radix-ui.com/docs/primitives/components/select#api-reference
---

<ComponentPreview styleName="radix-nova" name="select-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add select
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="select"
  title="components/ui/select.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

```tsx showLineNumbers
<Select>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      <SelectItem value="light">Light</SelectItem>
      <SelectItem value="dark">Dark</SelectItem>
      <SelectItem value="system">System</SelectItem>
    </SelectGroup>
  </SelectContent>
</Select>
```

## Examples

### Align Item With Trigger

Use the `position` prop on `SelectContent` to control alignment. When `position="item-aligned"` (default), the popup positions so the selected item appears over the trigger. When `position="popper"`, the popup aligns to the trigger edge.

<ComponentPreview styleName="radix-nova" name="select-align-item" />

### Groups

Use `SelectGroup`, `SelectLabel`, and `SelectSeparator` to organize items.

<ComponentPreview styleName="radix-nova" name="select-groups" />

### Scrollable

A select with many items that scrolls.

<ComponentPreview styleName="radix-nova" name="select-scrollable" />

### Disabled

<ComponentPreview styleName="radix-nova" name="select-disabled" />

### Invalid

Add the `data-invalid` attribute to the `Field` component and the `aria-invalid` attribute to the `SelectTrigger` component to show an error state.

```tsx showLineNumbers /data-invalid/ /aria-invalid/
<Field data-invalid>
  <FieldLabel>Fruit</FieldLabel>
  <SelectTrigger aria-invalid>
    <SelectValue />
  </SelectTrigger>
</Field>
```

<ComponentPreview styleName="radix-nova" name="select-invalid" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="select-rtl" direction="rtl" />

## API Reference

See the [Radix UI Select](https://www.radix-ui.com/docs/primitives/components/select#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/separator.mdx -->

## apps/v4/content/docs/components/radix/separator.mdx

---
title: Separator
description: Visually or semantically separates content.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/separator
  api: https://www.radix-ui.com/docs/primitives/components/separator#api-reference
---

<ComponentPreview styleName="radix-nova" name="separator-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add separator
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="separator"
  title="components/ui/separator.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Separator } from "@/components/ui/separator"
```

```tsx showLineNumbers
<Separator />
```

## Examples

### Vertical

Use `orientation="vertical"` for a vertical separator.

<ComponentPreview styleName="radix-nova" name="separator-vertical" />

### Menu

Vertical separators between menu items with descriptions.

<ComponentPreview styleName="radix-nova" name="separator-menu" />

### List

Horizontal separators between list items.

<ComponentPreview styleName="radix-nova" name="separator-list" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="separator-rtl" direction="rtl" />

## API Reference

See the [Radix UI Separator](https://www.radix-ui.com/docs/primitives/components/separator#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/sheet.mdx -->

## apps/v4/content/docs/components/radix/sheet.mdx

---
title: Sheet
description: Extends the Dialog component to display content that complements the main content of the screen.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/dialog
  api: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
---

<ComponentPreview styleName="radix-nova" name="sheet-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add sheet
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="sheet"
  title="components/ui/sheet.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"
```

```tsx showLineNumbers
<Sheet>
  <SheetTrigger>Open</SheetTrigger>
  <SheetContent>
    <SheetHeader>
      <SheetTitle>Are you absolutely sure?</SheetTitle>
      <SheetDescription>This action cannot be undone.</SheetDescription>
    </SheetHeader>
  </SheetContent>
</Sheet>
```

## Examples

### Side

Use the `side` prop on `SheetContent` to set the edge of the screen where the sheet appears. Values are `top`, `right`, `bottom`, or `left`.

<ComponentPreview styleName="radix-nova" name="sheet-side" />

### No Close Button

Use `showCloseButton={false}` on `SheetContent` to hide the close button.

<ComponentPreview styleName="radix-nova" name="sheet-no-close-button" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="sheet-rtl" direction="rtl" />

## API Reference

See the [Radix UI Dialog](https://www.radix-ui.com/docs/primitives/components/dialog#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/sidebar.mdx -->

## apps/v4/content/docs/components/radix/sidebar.mdx

---
title: Sidebar
description: A composable, themeable and customizable sidebar component.
base: radix
component: true
---

import { ExternalLinkIcon } from "lucide-react"

<figure className="flex flex-col gap-4">
  <ComponentPreview
    styleName="radix-nova"
    name="sidebar-demo"
    type="block"
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar that collapses to icons.
  </figcaption>
</figure>

Sidebars are one of the most complex components to build. They are central
to any application and often contain a lot of moving parts.

We now have a solid foundation to build on top of. Composable. Themeable.
Customizable.

[Browse the Blocks Library](/blocks).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add sidebar
```

</TabsContent>

<TabsContent value="manual">

<ComponentSource
  name="sidebar"
  title="components/ui/sidebar.tsx"
  styleName="radix-nova"
/>

</TabsContent>

</CodeTabs>

## Structure

A `Sidebar` component is composed of the following parts:

- `SidebarProvider` - Handles collapsible state.
- `Sidebar` - The sidebar container.
- `SidebarHeader` and `SidebarFooter` - Sticky at the top and bottom of the sidebar.
- `SidebarContent` - Scrollable content.
- `SidebarGroup` - Section within the `SidebarContent`.
- `SidebarTrigger` - Trigger for the `Sidebar`.

<Image
  src="/images/sidebar-structure.png"
  width="716"
  height="420"
  alt="Sidebar Structure"
  className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
/>
<Image
  src="/images/sidebar-structure-dark.png"
  width="716"
  height="420"
  alt="Sidebar Structure"
  className="mt-6 hidden w-full overflow-hidden rounded-lg border dark:block"
/>

## Usage

```tsx showLineNumbers title="app/layout.tsx"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main>
        <SidebarTrigger />
        {children}
      </main>
    </SidebarProvider>
  )
}
```

```tsx showLineNumbers title="components/app-sidebar.tsx"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
} from "@/components/ui/sidebar"

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader />
      <SidebarContent>
        <SidebarGroup />
        <SidebarGroup />
      </SidebarContent>
      <SidebarFooter />
    </Sidebar>
  )
}
```

## SidebarProvider

The `SidebarProvider` component is used to provide the sidebar context to the `Sidebar` component. You should always wrap your application in a `SidebarProvider` component.

### Props

| Name           | Type                      | Description                                  |
| -------------- | ------------------------- | -------------------------------------------- |
| `defaultOpen`  | `boolean`                 | Default open state of the sidebar.           |
| `open`         | `boolean`                 | Open state of the sidebar (controlled).      |
| `onOpenChange` | `(open: boolean) => void` | Sets open state of the sidebar (controlled). |

### Width

If you have a single sidebar in your application, you can use the `SIDEBAR_WIDTH` and `SIDEBAR_WIDTH_MOBILE` variables in `sidebar.tsx` to set the width of the sidebar.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
```

For multiple sidebars in your application, you can use the `--sidebar-width` and `--sidebar-width-mobile` CSS variables in the `style` prop.

```tsx showLineNumbers
<SidebarProvider
  style={
    {
      "--sidebar-width": "20rem",
      "--sidebar-width-mobile": "20rem",
    } as React.CSSProperties
  }
>
  <Sidebar />
</SidebarProvider>
```

### Keyboard Shortcut

To trigger the sidebar, you use the `cmd+b` keyboard shortcut on Mac and `ctrl+b` on Windows.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
const SIDEBAR_KEYBOARD_SHORTCUT = "b"
```

## Sidebar

The main `Sidebar` component used to render a collapsible sidebar.

### Props

| Property      | Type                              | Description                       |
| ------------- | --------------------------------- | --------------------------------- |
| `side`        | `left` or `right`                 | The side of the sidebar.          |
| `variant`     | `sidebar`, `floating`, or `inset` | The variant of the sidebar.       |
| `collapsible` | `offcanvas`, `icon`, or `none`    | Collapsible state of the sidebar. |

| Prop        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `offcanvas` | A collapsible sidebar that slides in from the left or right. |
| `icon`      | A sidebar that collapses to icons.                           |
| `none`      | A non-collapsible sidebar.                                   |

<Callout>
  **Note:** If you use the `inset` variant, remember to wrap your main content
  in a `SidebarInset` component.
</Callout>

```tsx showLineNumbers
<SidebarProvider>
  <Sidebar variant="inset" />
  <SidebarInset>
    <main>{children}</main>
  </SidebarInset>
</SidebarProvider>
```

## useSidebar

The `useSidebar` hook is used to control the sidebar.

```tsx showLineNumbers
import { useSidebar } from "@/components/ui/sidebar"

export function AppSidebar() {
  const {
    state,
    open,
    setOpen,
    openMobile,
    setOpenMobile,
    isMobile,
    toggleSidebar,
  } = useSidebar()
}
```

| Property        | Type                      | Description                                   |
| --------------- | ------------------------- | --------------------------------------------- |
| `state`         | `expanded` or `collapsed` | The current state of the sidebar.             |
| `open`          | `boolean`                 | Whether the sidebar is open.                  |
| `setOpen`       | `(open: boolean) => void` | Sets the open state of the sidebar.           |
| `openMobile`    | `boolean`                 | Whether the sidebar is open on mobile.        |
| `setOpenMobile` | `(open: boolean) => void` | Sets the open state of the sidebar on mobile. |
| `isMobile`      | `boolean`                 | Whether the sidebar is on mobile.             |
| `toggleSidebar` | `() => void`              | Toggles the sidebar. Desktop and mobile.      |

## SidebarHeader

Use the `SidebarHeader` component to add a sticky header to the sidebar.

```tsx showLineNumbers title="components/app-sidebar.tsx"
<Sidebar>
  <SidebarHeader>
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <SidebarMenuButton>
              Select Workspace
              <ChevronDown className="ml-auto" />
            </SidebarMenuButton>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-[--radix-popper-anchor-width]">
            <DropdownMenuItem>
              <span>Acme Inc</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarHeader>
</Sidebar>
```

## SidebarFooter

Use the `SidebarFooter` component to add a sticky footer to the sidebar.

```tsx showLineNumbers
<Sidebar>
  <SidebarFooter>
    <SidebarMenu>
      <SidebarMenuItem>
        <SidebarMenuButton>
          <User2 /> Username
        </SidebarMenuButton>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarFooter>
</Sidebar>
```

## SidebarContent

The `SidebarContent` component is used to wrap the content of the sidebar. This is where you add your `SidebarGroup` components. It is scrollable.

```tsx showLineNumbers
<Sidebar>
  <SidebarContent>
    <SidebarGroup />
    <SidebarGroup />
  </SidebarContent>
</Sidebar>
```

## SidebarGroup

Use the `SidebarGroup` component to create a section within the sidebar.

A `SidebarGroup` has a `SidebarGroupLabel`, a `SidebarGroupContent` and an optional `SidebarGroupAction`.

```tsx showLineNumbers
<SidebarGroup>
  <SidebarGroupLabel>Application</SidebarGroupLabel>
  <SidebarGroupAction>
    <Plus /> <span className="sr-only">Add Project</span>
  </SidebarGroupAction>
  <SidebarGroupContent></SidebarGroupContent>
</SidebarGroup>
```

To make a `SidebarGroup` collapsible, wrap it in a `Collapsible`.

```tsx showLineNumbers
<Collapsible defaultOpen className="group/collapsible">
  <SidebarGroup>
    <SidebarGroupLabel asChild>
      <CollapsibleTrigger>
        Help
        <ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" />
      </CollapsibleTrigger>
    </SidebarGroupLabel>
    <CollapsibleContent>
      <SidebarGroupContent />
    </CollapsibleContent>
  </SidebarGroup>
</Collapsible>
```

## SidebarMenu

The `SidebarMenu` component is used for building a menu within a `SidebarGroup`.

<Image
  src="/images/sidebar-menu.png"
  width="716"
  height="420"
  alt="Sidebar Menu"
  className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
/>
<Image
  src="/images/sidebar-menu-dark.png"
  width="716"
  height="420"
  alt="Sidebar Menu"
  className="mt-6 hidden w-full overflow-hidden rounded-lg border dark:block"
/>

```tsx showLineNumbers
<SidebarMenu>
  {projects.map((project) => (
    <SidebarMenuItem key={project.name}>
      <SidebarMenuButton asChild>
        <a href={project.url}>
          <project.icon />
          <span>{project.name}</span>
        </a>
      </SidebarMenuButton>
    </SidebarMenuItem>
  ))}
</SidebarMenu>
```

## SidebarMenuButton

The `SidebarMenuButton` component is used to render a menu button within a `SidebarMenuItem`.

By default, the `SidebarMenuButton` renders a button but you can use the `asChild` prop to render a different component such as a `Link` or an `a` tag.

Use the `isActive` prop to mark a menu item as active.

```tsx showLineNumbers
<SidebarMenuButton asChild isActive>
  <a href="#">Home</a>
</SidebarMenuButton>
```

## SidebarMenuAction

The `SidebarMenuAction` component is used to render a menu action within a `SidebarMenuItem`.

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton asChild>
    <a href="#">
      <Home />
      <span>Home</span>
    </a>
  </SidebarMenuButton>
  <SidebarMenuAction>
    <Plus /> <span className="sr-only">Add Project</span>
  </SidebarMenuAction>
</SidebarMenuItem>
```

## SidebarMenuSub

The `SidebarMenuSub` component is used to render a submenu within a `SidebarMenu`.

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuSub>
    <SidebarMenuSubItem>
      <SidebarMenuSubButton />
    </SidebarMenuSubItem>
  </SidebarMenuSub>
</SidebarMenuItem>
```

## SidebarMenuBadge

The `SidebarMenuBadge` component is used to render a badge within a `SidebarMenuItem`.

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuBadge>24</SidebarMenuBadge>
</SidebarMenuItem>
```

## SidebarMenuSkeleton

The `SidebarMenuSkeleton` component is used to render a skeleton for a `SidebarMenu`.

```tsx showLineNumbers
<SidebarMenu>
  {Array.from({ length: 5 }).map((_, index) => (
    <SidebarMenuItem key={index}>
      <SidebarMenuSkeleton />
    </SidebarMenuItem>
  ))}
</SidebarMenu>
```

## SidebarTrigger

Use the `SidebarTrigger` component to render a button that toggles the sidebar.

```tsx showLineNumbers
import { useSidebar } from "@/components/ui/sidebar"

export function CustomTrigger() {
  const { toggleSidebar } = useSidebar()

  return <button onClick={toggleSidebar}>Toggle Sidebar</button>
}
```

## SidebarRail

The `SidebarRail` component is used to render a rail within a `Sidebar`. This rail can be used to toggle the sidebar.

```tsx showLineNumbers
<Sidebar>
  <SidebarHeader />
  <SidebarContent>
    <SidebarGroup />
  </SidebarContent>
  <SidebarFooter />
  <SidebarRail />
</Sidebar>
```

## Controlled Sidebar

Use the `open` and `onOpenChange` props to control the sidebar.

```tsx showLineNumbers
export function AppSidebar() {
  const [open, setOpen] = React.useState(false)

  return (
    <SidebarProvider open={open} onOpenChange={setOpen}>
      <Sidebar />
    </SidebarProvider>
  )
}
```

## Theming

We use the following CSS variables to theme the sidebar.

```css
@layer base {
  :root {
    --sidebar-background: 0 0% 98%;
    --sidebar-foreground: 240 5.3% 26.1%;
    --sidebar-primary: 240 5.9% 10%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 4.8% 95.9%;
    --sidebar-accent-foreground: 240 5.9% 10%;
    --sidebar-border: 220 13% 91%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }

  .dark {
    --sidebar-background: 240 5.9% 10%;
    --sidebar-foreground: 240 4.8% 95.9%;
    --sidebar-primary: 0 0% 98%;
    --sidebar-primary-foreground: 240 5.9% 10%;
    --sidebar-accent: 240 3.7% 15.9%;
    --sidebar-accent-foreground: 240 4.8% 95.9%;
    --sidebar-border: 240 3.7% 15.9%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
}
```

## Styling

Here are some tips for styling the sidebar based on different states.

```tsx
<Sidebar collapsible="icon">
  <SidebarContent>
    <SidebarGroup className="group-data-[collapsible=icon]:hidden" />
  </SidebarContent>
</Sidebar>
```

```tsx
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuAction className="peer-data-[active=true]/menu-button:opacity-100" />
</SidebarMenuItem>
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

{/* prettier-ignore */}
<Button asChild size="sm" className="mt-6">
  <a href="/view/radix-nova/sidebar-rtl" target="_blank">View RTL Sidebar <ExternalLinkIcon /></a>
</Button>

## Changelog

### RTL Support

If you're upgrading from a previous version of the `Sidebar` component, you'll need to apply the following updates to add RTL support:

<Steps>

<Step>Add `dir` prop to Sidebar component.</Step>

Add `dir` to the destructured props and pass it to `SheetContent` for mobile:

```diff
  function Sidebar({
    side = "left",
    variant = "sidebar",
    collapsible = "offcanvas",
    className,
    children,
+   dir,
    ...props
  }: React.ComponentProps<"div"> & {
    side?: "left" | "right"
    variant?: "sidebar" | "floating" | "inset"
    collapsible?: "offcanvas" | "icon" | "none"
  }) {
```

Then pass it to `SheetContent` in the mobile view:

```diff
  <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}>
    <SheetContent
+     dir={dir}
      data-sidebar="sidebar"
      data-slot="sidebar"
      data-mobile="true"
```

<Step>Add `data-side` attribute to sidebar container.</Step>

Add `data-side={side}` to the sidebar container element:

```diff
  <div
    data-slot="sidebar-container"
+   data-side={side}
    className={cn(
```

<Step>Update sidebar container positioning classes.</Step>

Replace JavaScript ternary conditional classes with CSS data attribute selectors:

```diff
  className={cn(
-   "fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex",
-   side === "left"
-     ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
-     : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
+   "fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex data-[side=left]:left-0 data-[side=right]:right-0 data-[side=left]:group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)] data-[side=right]:group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
```

<Step>Update SidebarRail positioning classes.</Step>

Update the `SidebarRail` component to use physical positioning for the rail:

```diff
  className={cn(
-   "hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear group-data-[side=left]:-end-4 group-data-[side=right]:start-0 after:absolute after:inset-y-0 after:start-1/2 after:w-[2px] sm:flex",
+   "hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 ltr:-translate-x-1/2 rtl:-translate-x-1/2 transition-all ease-linear group-data-[side=left]:-right-4 group-data-[side=right]:left-0 after:absolute after:inset-y-0 after:start-1/2 after:w-[2px] sm:flex",
```

<Step>Add RTL flip to SidebarTrigger icon.</Step>

Add `className="rtl:rotate-180"` to the icon in `SidebarTrigger` to flip it in RTL mode:

```diff
  <Button ...>
-   <PanelLeftIcon />
+   <PanelLeftIcon className="rtl:rotate-180" />
    <span className="sr-only">Toggle Sidebar</span>
  </Button>
```

</Steps>

After applying these changes, you can use the `dir` prop to set the direction:

```tsx
<Sidebar dir="rtl" side="right">
  {/* ... */}
</Sidebar>
```

The sidebar will correctly position itself and handle interactions in both LTR and RTL layouts.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/skeleton.mdx -->

## apps/v4/content/docs/components/radix/skeleton.mdx

---
title: Skeleton
description: Use to show a placeholder while content is loading.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="skeleton-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add skeleton
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="skeleton"
  title="components/ui/skeleton.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Skeleton } from "@/components/ui/skeleton"
```

```tsx
<Skeleton className="h-[20px] w-[100px] rounded-full" />
```

## Examples

### Avatar

<ComponentPreview styleName="radix-nova" name="skeleton-avatar" />

### Card

<ComponentPreview
  styleName="radix-nova"
  name="skeleton-card"
  previewClassName="h-80"
/>

### Text

<ComponentPreview styleName="radix-nova" name="skeleton-text" />

### Form

<ComponentPreview styleName="radix-nova" name="skeleton-form" />

### Table

<ComponentPreview styleName="radix-nova" name="skeleton-table" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="skeleton-rtl" direction="rtl" />


---

<!-- SOURCE: apps/v4/content/docs/components/radix/slider.mdx -->

## apps/v4/content/docs/components/radix/slider.mdx

---
title: Slider
description: An input where the user selects a value from within a given range.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/slider
  api: https://www.radix-ui.com/docs/primitives/components/slider#api-reference
---

<ComponentPreview styleName="radix-nova" name="slider-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add slider
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="slider"
  title="components/ui/slider.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Slider } from "@/components/ui/slider"
```

```tsx
<Slider defaultValue={[33]} max={100} step={1} />
```

## Examples

### Range

Use an array with two values for a range slider.

<ComponentPreview styleName="radix-nova" name="slider-range" />

### Multiple Thumbs

Use an array with multiple values for multiple thumbs.

<ComponentPreview styleName="radix-nova" name="slider-multiple" />

### Vertical

Use `orientation="vertical"` for a vertical slider.

<ComponentPreview styleName="radix-nova" name="slider-vertical" />

### Controlled

<ComponentPreview styleName="radix-nova" name="slider-controlled" />

### Disabled

Use the `disabled` prop to disable the slider.

<ComponentPreview styleName="radix-nova" name="slider-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="slider-rtl" direction="rtl" />

## API Reference

See the [Radix UI Slider](https://www.radix-ui.com/docs/primitives/components/slider#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/sonner.mdx -->

## apps/v4/content/docs/components/radix/sonner.mdx

---
title: Sonner
description: An opinionated toast component for React.
base: radix
component: true
links:
  doc: https://sonner.emilkowal.ski
---

<ComponentPreview styleName="radix-nova" name="sonner-demo" />

## About

Sonner is built and maintained by [emilkowalski](https://twitter.com/emilkowalski).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps className="mb-0 pt-2">

<Step>Run the following command:</Step>

```bash
npx shadcn@latest add sonner
```

<Step>Add the Toaster component</Step>

```tsx title="app/layout.tsx" {1,9} showLineNumbers
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install sonner next-themes
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="sonner"
  title="components/ui/sonner.tsx"
  styleName="radix-nova"
/>

<Step>Add the Toaster component</Step>

```tsx showLineNumbers title="app/layout.tsx" {1,8}
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <Toaster />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { toast } from "sonner"
```

```tsx
toast("Event has been created.")
```

## Examples

### Types

<ComponentPreview styleName="radix-nova" name="sonner-types" />

### Description

<ComponentPreview styleName="radix-nova" name="sonner-description" />

### Position

Use the `position` prop to change the position of the toast.

<ComponentPreview styleName="radix-nova" name="sonner-position" />

## API Reference

See the [Sonner API Reference](https://sonner.emilkowal.ski/getting-started) for more information.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/spinner.mdx -->

## apps/v4/content/docs/components/radix/spinner.mdx

---
title: Spinner
description: An indicator that can be used to show a loading state.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="spinner-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add spinner
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="spinner"
  title="components/ui/spinner.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Spinner } from "@/components/ui/spinner"
```

```tsx
<Spinner />
```

## Customization

You can replace the default spinner icon with any other icon by editing the `Spinner` component.

<ComponentPreview styleName="radix-nova" name="spinner-custom" />

```tsx showLineNumbers title="components/ui/spinner.tsx"
import { LoaderIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <LoaderIcon
      role="status"
      aria-label="Loading"
      className={cn("size-4 animate-spin", className)}
      {...props}
    />
  )
}

export { Spinner }
```

## Examples

### Size

Use the `size-*` utility class to change the size of the spinner.

<ComponentPreview styleName="radix-nova" name="spinner-size" />

### Button

Add a spinner to a button to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

<ComponentPreview styleName="radix-nova" name="spinner-button" />

### Badge

Add a spinner to a badge to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

<ComponentPreview styleName="radix-nova" name="spinner-badge" />

### Input Group

<ComponentPreview styleName="radix-nova" name="spinner-input-group" />

### Empty

<ComponentPreview styleName="radix-nova" name="spinner-empty" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="spinner-rtl" direction="rtl" />


---

<!-- SOURCE: apps/v4/content/docs/components/radix/switch.mdx -->

## apps/v4/content/docs/components/radix/switch.mdx

---
title: Switch
description: A control that allows the user to toggle between checked and not checked.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/switch
  api: https://www.radix-ui.com/docs/primitives/components/switch#api-reference
---

<ComponentPreview styleName="radix-nova" name="switch-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add switch
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="switch"
  title="components/ui/switch.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Switch } from "@/components/ui/switch"
```

```tsx
<Switch />
```

## Examples

### Description

<ComponentPreview styleName="radix-nova" name="switch-description" />

### Choice Card

Card-style selection where `FieldLabel` wraps the entire `Field` for a clickable card pattern.

<ComponentPreview styleName="radix-nova" name="switch-choice-card" />

### Disabled

Add the `disabled` prop to the `Switch` component to disable the switch. Add the `data-disabled` prop to the `Field` component for styling.

<ComponentPreview styleName="radix-nova" name="switch-disabled" />

### Invalid

Add the `aria-invalid` prop to the `Switch` component to indicate an invalid state. Add the `data-invalid` prop to the `Field` component for styling.

<ComponentPreview styleName="radix-nova" name="switch-invalid" />

### Size

Use the `size` prop to change the size of the switch.

<ComponentPreview styleName="radix-nova" name="switch-sizes" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="switch-rtl" direction="rtl" />

## API Reference

See the [Radix Switch](https://www.radix-ui.com/docs/primitives/components/switch#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/table.mdx -->

## apps/v4/content/docs/components/radix/table.mdx

---
title: Table
description: A responsive table component.
base: radix
component: true
---

<ComponentPreview
  styleName="radix-nova"
  name="table-demo"
  previewClassName="h-[30rem]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add table
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="table"
  title="components/ui/table.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
```

```tsx showLineNumbers
<Table>
  <TableCaption>A list of your recent invoices.</TableCaption>
  <TableHeader>
    <TableRow>
      <TableHead className="w-[100px]">Invoice</TableHead>
      <TableHead>Status</TableHead>
      <TableHead>Method</TableHead>
      <TableHead className="text-right">Amount</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell className="font-medium">INV001</TableCell>
      <TableCell>Paid</TableCell>
      <TableCell>Credit Card</TableCell>
      <TableCell className="text-right">$250.00</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

## Examples

### Footer

Use the `<TableFooter />` component to add a footer to the table.

<ComponentPreview styleName="radix-nova" name="table-footer" />

### Actions

A table showing actions for each row using a `<DropdownMenu />` component.

<ComponentPreview styleName="radix-nova" name="table-actions" />

## Data Table

You can use the `<Table />` component to build more complex data tables. Combine it with [@tanstack/react-table](https://tanstack.com/table/v8) to create tables with sorting, filtering and pagination.

See the [Data Table](/docs/components/data-table) documentation for more information.

You can also see an example of a data table in the [Tasks](/examples/tasks) demo.

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="table-rtl"
  direction="rtl"
  previewClassName="h-auto"
/>


---

<!-- SOURCE: apps/v4/content/docs/components/radix/tabs.mdx -->

## apps/v4/content/docs/components/radix/tabs.mdx

---
title: Tabs
description: A set of layered sections of content—known as tab panels—that are displayed one at a time.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/tabs
  api: https://www.radix-ui.com/docs/primitives/components/tabs#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="tabs-demo"
  previewClassName="h-96"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add tabs
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="tabs"
  title="components/ui/tabs.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
```

```tsx showLineNumbers
<Tabs defaultValue="account" className="w-[400px]">
  <TabsList>
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent value="account">Make changes to your account here.</TabsContent>
  <TabsContent value="password">Change your password here.</TabsContent>
</Tabs>
```

## Examples

### Line

Use the `variant="line"` prop on `TabsList` for a line style.

<ComponentPreview styleName="radix-nova" name="tabs-line" />

### Vertical

Use `orientation="vertical"` for vertical tabs.

<ComponentPreview styleName="radix-nova" name="tabs-vertical" />

### Disabled

<ComponentPreview styleName="radix-nova" name="tabs-disabled" />

### Icons

<ComponentPreview styleName="radix-nova" name="tabs-icons" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="tabs-rtl" direction="rtl" />

## API Reference

See the [Radix Tabs](https://www.radix-ui.com/docs/primitives/components/tabs#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/textarea.mdx -->

## apps/v4/content/docs/components/radix/textarea.mdx

---
title: Textarea
description: Displays a form textarea or a component that looks like a textarea.
base: radix
component: true
---

<ComponentPreview
  styleName="radix-nova"
  name="textarea-demo"
  previewClassName="*:max-w-xs"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add textarea
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="textarea"
  title="components/ui/textarea.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Textarea } from "@/components/ui/textarea"
```

```tsx
<Textarea />
```

## Examples

### Field

Use `Field`, `FieldLabel`, and `FieldDescription` to create a textarea with a label and description.

<ComponentPreview
  styleName="radix-nova"
  name="textarea-field"
  previewClassName="*:max-w-xs"
/>

### Disabled

Use the `disabled` prop to disable the textarea. To style the disabled state, add the `data-disabled` attribute to the `Field` component.

<ComponentPreview
  styleName="radix-nova"
  name="textarea-disabled"
  previewClassName="*:max-w-xs"
/>

### Invalid

Use the `aria-invalid` prop to mark the textarea as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field` component.

<ComponentPreview
  styleName="radix-nova"
  name="textarea-invalid"
  previewClassName="*:max-w-xs"
/>

### Button

Pair with `Button` to create a textarea with a submit button.

<ComponentPreview
  styleName="radix-nova"
  name="textarea-button"
  previewClassName="*:max-w-xs"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="textarea-rtl" direction="rtl" />


---

<!-- SOURCE: apps/v4/content/docs/components/radix/toast.mdx -->

## apps/v4/content/docs/components/radix/toast.mdx

---
title: Toast
description: A succinct message that is displayed temporarily.
base: base
component: true
---

The toast component has been deprecated. Use the [sonner](/docs/components/sonner) component instead.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/toggle-group.mdx -->

## apps/v4/content/docs/components/radix/toggle-group.mdx

---
title: Toggle Group
description: A set of two-state buttons that can be toggled on or off.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/toggle-group
  api: https://www.radix-ui.com/docs/primitives/components/toggle-group#api-reference
---

<ComponentPreview styleName="radix-nova" name="toggle-group-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle-group
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="toggle-group"
  title="components/ui/toggle-group.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
```

```tsx
<ToggleGroup type="single">
  <ToggleGroupItem value="a">A</ToggleGroupItem>
  <ToggleGroupItem value="b">B</ToggleGroupItem>
  <ToggleGroupItem value="c">C</ToggleGroupItem>
</ToggleGroup>
```

## Examples

### Outline

Use `variant="outline"` for an outline style.

<ComponentPreview styleName="radix-nova" name="toggle-group-outline" />

### Size

Use the `size` prop to change the size of the toggle group.

<ComponentPreview styleName="radix-nova" name="toggle-group-sizes" />

### Spacing

Use `spacing` to add spacing between toggle group items.

<ComponentPreview styleName="radix-nova" name="toggle-group-spacing" />

### Vertical

Use `orientation="vertical"` for vertical toggle groups.

<ComponentPreview styleName="radix-nova" name="toggle-group-vertical" />

### Disabled

<ComponentPreview styleName="radix-nova" name="toggle-group-disabled" />

### Custom

A custom toggle group example.

<ComponentPreview
  styleName="radix-nova"
  name="toggle-group-font-weight-selector"
  previewClassName="*:data-[slot=field]:max-w-xs"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="toggle-group-rtl"
  direction="rtl"
/>

## API Reference

See the [Radix Toggle Group](https://www.radix-ui.com/docs/primitives/components/toggle-group#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/toggle.mdx -->

## apps/v4/content/docs/components/radix/toggle.mdx

---
title: Toggle
description: A two-state button that can be either on or off.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/toggle
  api: https://www.radix-ui.com/docs/primitives/components/toggle#api-reference
---

<ComponentPreview styleName="radix-nova" name="toggle-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="toggle"
  title="components/ui/toggle.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Toggle } from "@/components/ui/toggle"
```

```tsx
<Toggle>Toggle</Toggle>
```

## Examples

### Outline

Use `variant="outline"` for an outline style.

<ComponentPreview styleName="radix-nova" name="toggle-outline" />

### With Text

<ComponentPreview styleName="radix-nova" name="toggle-text" />

### Size

Use the `size` prop to change the size of the toggle.

<ComponentPreview styleName="radix-nova" name="toggle-sizes" />

### Disabled

<ComponentPreview styleName="radix-nova" name="toggle-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="toggle-rtl" direction="rtl" />

## API Reference

See the [Radix Toggle](https://www.radix-ui.com/docs/primitives/components/toggle#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/tooltip.mdx -->

## apps/v4/content/docs/components/radix/tooltip.mdx

---
title: Tooltip
description: A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/tooltip
  api: https://www.radix-ui.com/docs/primitives/components/tooltip#api-reference
---

<ComponentPreview styleName="radix-nova" name="tooltip-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps className="mb-0 pt-2">

<Step>Run the following command:</Step>

```bash
npx shadcn@latest add tooltip
```

<Step>Add the `TooltipProvider` to the root of your app.</Step>

```tsx title="app/layout.tsx" showLineNumbers {1,7}
import { TooltipProvider } from "@/components/ui/tooltip"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <TooltipProvider>{children}</TooltipProvider>
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="tooltip"
  title="components/ui/tooltip.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

<Step>Add the `TooltipProvider` to the root of your app.</Step>

```tsx title="app/layout.tsx" showLineNumbers {1,7}
import { TooltipProvider } from "@/components/ui/tooltip"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <TooltipProvider>{children}</TooltipProvider>
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
```

```tsx showLineNumbers
<Tooltip>
  <TooltipTrigger>Hover</TooltipTrigger>
  <TooltipContent>
    <p>Add to library</p>
  </TooltipContent>
</Tooltip>
```

## Examples

### Side

Use the `side` prop to change the position of the tooltip.

<ComponentPreview styleName="radix-nova" name="tooltip-sides" />

### With Keyboard Shortcut

<ComponentPreview styleName="radix-nova" name="tooltip-keyboard" />

### Disabled Button

Show a tooltip on a disabled button by wrapping it with a span.

<ComponentPreview styleName="radix-nova" name="tooltip-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="tooltip-rtl" direction="rtl" />

## API Reference

See the [Radix Tooltip](https://www.radix-ui.com/docs/primitives/components/tooltip#api-reference) documentation.


---

<!-- SOURCE: apps/v4/content/docs/components/radix/typography.mdx -->

## apps/v4/content/docs/components/radix/typography.mdx

---
title: Typography
description: Styles for headings, paragraphs, lists, etc.
base: radix
component: true
---

We do not ship any typography styles by default. This page is an example of how you can use utility classes to style your text.

<ComponentPreview
  styleName="radix-nova"
  name="typography-demo"
  className="[&_.preview]:h-auto!"
  hideCode
/>

## h1

<ComponentPreview styleName="radix-nova" name="typography-h1" />

## h2

<ComponentPreview styleName="radix-nova" name="typography-h2" />

## h3

<ComponentPreview styleName="radix-nova" name="typography-h3" />

## h4

<ComponentPreview styleName="radix-nova" name="typography-h4" />

## p

<ComponentPreview styleName="radix-nova" name="typography-p" />

## blockquote

<ComponentPreview styleName="radix-nova" name="typography-blockquote" />

## table

<ComponentPreview styleName="radix-nova" name="typography-table" />

## list

<ComponentPreview styleName="radix-nova" name="typography-list" />

## Inline code

<ComponentPreview styleName="radix-nova" name="typography-inline-code" />

## Lead

<ComponentPreview styleName="radix-nova" name="typography-lead" />

## Large

<ComponentPreview styleName="radix-nova" name="typography-large" />

## Small

<ComponentPreview styleName="radix-nova" name="typography-small" />

## Muted

<ComponentPreview styleName="radix-nova" name="typography-muted" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="typography-rtl"
  direction="rtl"
  className="[&_.preview]:h-auto!"
/>


---

<!-- SOURCE: apps/v4/content/docs/dark-mode/astro.mdx -->

## apps/v4/content/docs/dark-mode/astro.mdx

---
title: Astro
description: Adding dark mode to your astro app.
---

## Create an inline theme script

```astro title="src/pages/index.astro"
---
import '../styles/globals.css'
---

<script is:inline>
	const getThemePreference = () => {
		if (typeof localStorage !== 'undefined' && localStorage.getItem('theme')) {
			return localStorage.getItem('theme');
		}
		return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
	};
	const isDark = getThemePreference() === 'dark';
	document.documentElement.classList[isDark ? 'add' : 'remove']('dark');

	if (typeof localStorage !== 'undefined') {
		const observer = new MutationObserver(() => {
			const isDark = document.documentElement.classList.contains('dark');
			localStorage.setItem('theme', isDark ? 'dark' : 'light');
		});
		observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
	}
</script>

<html lang="en">
	<body>
      <h1>Astro</h1>
	</body>
</html>
```

## Add a mode toggle

```tsx title="src/components/ModeToggle.tsx"
import * as React from "react"
import { Moon, Sun } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function ModeToggle() {
  const [theme, setThemeState] = React.useState<
    "theme-light" | "dark" | "system"
  >("theme-light")

  React.useEffect(() => {
    const isDarkMode = document.documentElement.classList.contains("dark")
    setThemeState(isDarkMode ? "dark" : "theme-light")
  }, [])

  React.useEffect(() => {
    const isDark =
      theme === "dark" ||
      (theme === "system" &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
    document.documentElement.classList[isDark ? "add" : "remove"]("dark")
  }, [theme])

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <Sun className="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
          <Moon className="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
          <span className="sr-only">Toggle theme</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setThemeState("theme-light")}>
          Light
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setThemeState("dark")}>
          Dark
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setThemeState("system")}>
          System
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

## Display the mode toggle

Place a mode toggle on your site to toggle between light and dark mode.

```astro title="src/pages/index.astro"
---
import '../styles/globals.css'
import { ModeToggle } from '@/components/ModeToggle';
---

<!-- Inline script -->

<html lang="en">
	<body>
      <h1>Astro</h1>
      <ModeToggle client:load />
	</body>
</html>
```


---

<!-- SOURCE: apps/v4/content/docs/dark-mode/index.mdx -->

## apps/v4/content/docs/dark-mode/index.mdx

---
title: Dark Mode
description: Adding dark mode to your site.
---

<div className="grid gap-4 sm:grid-cols-2 sm:gap-6">
  <LinkedCard href="/docs/dark-mode/next">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Next.js</title>
      <path d="M11.5725 0c-.1763 0-.3098.0013-.3584.0067-.0516.0053-.2159.021-.3636.0328-3.4088.3073-6.6017 2.1463-8.624 4.9728C1.1004 6.584.3802 8.3666.1082 10.255c-.0962.659-.108.8537-.108 1.7474s.012 1.0884.108 1.7476c.652 4.506 3.8591 8.2919 8.2087 9.6945.7789.2511 1.6.4223 2.5337.5255.3636.04 1.9354.04 2.299 0 1.6117-.1783 2.9772-.577 4.3237-1.2643.2065-.1056.2464-.1337.2183-.1573-.0188-.0139-.8987-1.1938-1.9543-2.62l-1.919-2.592-2.4047-3.5583c-1.3231-1.9564-2.4117-3.556-2.4211-3.556-.0094-.0026-.0187 1.5787-.0235 3.509-.0067 3.3802-.0093 3.5162-.0516 3.596-.061.115-.108.1618-.2064.2134-.075.0374-.1408.0445-.495.0445h-.406l-.1078-.068a.4383.4383 0 01-.1572-.1712l-.0493-.1056.0053-4.703.0067-4.7054.0726-.0915c.0376-.0493.1174-.1125.1736-.143.0962-.047.1338-.0517.5396-.0517.4787 0 .5584.0187.6827.1547.0353.0377 1.3373 1.9987 2.895 4.3608a10760.433 10760.433 0 004.7344 7.1706l1.9002 2.8782.096-.0633c.8518-.5536 1.7525-1.3418 2.4657-2.1627 1.5179-1.7429 2.4963-3.868 2.8247-6.134.0961-.6591.1078-.854.1078-1.7475 0-.8937-.012-1.0884-.1078-1.7476-.6522-4.506-3.8592-8.2919-8.2087-9.6945-.7672-.2487-1.5836-.42-2.4985-.5232-.169-.0176-1.0835-.0366-1.6123-.037zm4.0685 7.217c.3473 0 .4082.0053.4857.047.1127.0562.204.1642.237.2767.0186.061.0234 1.3653.0186 4.3044l-.0067 4.2175-.7436-1.14-.7461-1.14v-3.066c0-1.982.0093-3.0963.0234-3.1502.0375-.1313.1196-.2346.2323-.2955.0961-.0494.1313-.054.4997-.054z" />
    </svg>
    <p className="mt-2 font-medium">Next.js</p>
  </LinkedCard>
  <LinkedCard href="/docs/dark-mode/vite">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Vite</title>
      <path d="m8.286 10.578.512-8.657a.306.306 0 0 1 .247-.282L17.377.006a.306.306 0 0 1 .353.385l-1.558 5.403a.306.306 0 0 0 .352.385l2.388-.46a.306.306 0 0 1 .332.438l-6.79 13.55-.123.19a.294.294 0 0 1-.252.14c-.177 0-.35-.152-.305-.369l1.095-5.301a.306.306 0 0 0-.388-.355l-1.433.435a.306.306 0 0 1-.389-.354l.69-3.375a.306.306 0 0 0-.37-.36l-2.32.536a.306.306 0 0 1-.374-.316zm14.976-7.926L17.284 3.74l-.544 1.887 2.077-.4a.8.8 0 0 1 .84.369.8.8 0 0 1 .034.783L12.9 19.93l-.013.025-.015.023-.122.19a.801.801 0 0 1-.672.37.826.826 0 0 1-.634-.302.8.8 0 0 1-.16-.67l1.029-4.981-1.12.34a.81.81 0 0 1-.86-.262.802.802 0 0 1-.165-.67l.63-3.08-2.027.468a.808.808 0 0 1-.768-.233.81.81 0 0 1-.217-.6l.389-6.57-7.44-1.33a.612.612 0 0 0-.64.906L11.58 23.691a.612.612 0 0 0 1.066-.004l11.26-20.135a.612.612 0 0 0-.644-.9z" />
    </svg>
    <p className="mt-2 font-medium">Vite</p>
  </LinkedCard>
  <LinkedCard href="/docs/dark-mode/astro">
    <svg
      role="img"
      viewBox="0 0 64 79"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <path d="M19.9924 65.9282C16.1165 62.432 14.9851 55.0859 16.5999 49.7638C19.3998 53.1193 23.2793 54.1822 27.2977 54.7822C33.5013 55.7081 39.5937 55.3618 45.3565 52.5637C46.0158 52.2434 46.625 51.8174 47.3454 51.386C47.8861 52.9341 48.0268 54.497 47.838 56.0877C47.3787 59.9617 45.4251 62.9542 42.3177 65.2227C41.0752 66.13 39.7604 66.9411 38.4771 67.7967C34.5346 70.4262 33.4679 73.5095 34.9494 77.9946C34.9846 78.1038 35.0161 78.2131 35.0957 78.4797C33.0828 77.5909 31.6124 76.2965 30.4921 74.5946C29.3088 72.7984 28.7458 70.8114 28.7162 68.6615C28.7014 67.6152 28.7014 66.5597 28.5588 65.5282C28.2107 63.0135 27.0144 61.8876 24.7608 61.8227C22.4479 61.7561 20.6183 63.1672 20.1331 65.3893C20.0961 65.5597 20.0424 65.7282 19.9887 65.9263L19.9924 65.9282Z" />
      <path d="M0.5 51.3932C0.5 51.3932 11.0979 46.2433 21.7254 46.2433L29.7382 21.5069C30.0381 20.3106 30.9141 19.4977 31.9029 19.4977C32.8918 19.4977 33.7677 20.3106 34.0677 21.5069L42.0804 46.2433C54.6672 46.2433 63.3058 51.3932 63.3058 51.3932C63.3058 51.3932 45.3044 2.47586 45.2692 2.37772C44.7526 0.931458 43.8804 0 42.7045 0H21.1032C19.9273 0 19.0903 0.931458 18.5384 2.37772C18.4995 2.47401 0.5 51.3932 0.5 51.3932Z" />
    </svg>
    <p className="mt-2 font-medium">Astro</p>
  </LinkedCard>
  <LinkedCard href="/docs/dark-mode/remix">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Remix</title>
      <path d="M21.511 18.508c.216 2.773.216 4.073.216 5.492H15.31c0-.309.006-.592.011-.878.018-.892.036-1.821-.109-3.698-.19-2.747-1.374-3.358-3.55-3.358H1.574v-5h10.396c2.748 0 4.122-.835 4.122-3.049 0-1.946-1.374-3.125-4.122-3.125H1.573V0h11.541c6.221 0 9.313 2.938 9.313 7.632 0 3.511-2.176 5.8-5.114 6.182 2.48.497 3.93 1.909 4.198 4.694ZM1.573 24v-3.727h6.784c1.133 0 1.379.84 1.379 1.342V24Z" />
    </svg>
    <p className="mt-2 font-medium">Remix</p>
  </LinkedCard>
</div>


---

<!-- SOURCE: apps/v4/content/docs/dark-mode/next.mdx -->

## apps/v4/content/docs/dark-mode/next.mdx

---
title: Next.js
description: Adding dark mode to your Next.js app.
---

<Steps>

## Install next-themes

Start by installing `next-themes`:

```bash
npm install next-themes
```

## Create a theme provider

```tsx title="components/theme-provider.tsx" showLineNumbers
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"

export function ThemeProvider({
  children,
  ...props
}: React.ComponentProps<typeof NextThemesProvider>) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

## Wrap your root layout

Add the `ThemeProvider` to your root layout and add the `suppressHydrationWarning` prop to the `html` tag.

```tsx {1,6,9-14,16} title="app/layout.tsx" showLineNumbers
import { ThemeProvider } from "@/components/theme-provider"

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <>
      <html lang="en" suppressHydrationWarning>
        <head />
        <body>
          <ThemeProvider
            attribute="class"
            defaultTheme="system"
            enableSystem
            disableTransitionOnChange
          >
            {children}
          </ThemeProvider>
        </body>
      </html>
    </>
  )
}
```

## Add a mode toggle

Place a mode toggle on your site to toggle between light and dark mode.

<ComponentPreview name="mode-toggle" className="[&_.preview]:items-start" />

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/dark-mode/remix.mdx -->

## apps/v4/content/docs/dark-mode/remix.mdx

---
title: Remix
description: Adding dark mode to your Remix app.
---

<Steps>

## Modify your tailwind.css file

Add `:root[class~="dark"]` to your tailwind.css file. This will allow you to use the `dark` class on your html element to apply dark mode styles.

```css {2} title="app/tailwind.css" showLineNumbers
.dark,
:root[class~="dark"] {
  ...;
}
```

## Install remix-themes

Start by installing `remix-themes`:

```bash
npm install remix-themes
```

## Create a session storage and theme session resolver

```tsx title="app/sessions.server.tsx" showLineNumbers
import { createThemeSessionResolver } from "remix-themes"

// You can default to 'development' if process.env.NODE_ENV is not set
const isProduction = process.env.NODE_ENV === "production"

const sessionStorage = createCookieSessionStorage({
  cookie: {
    name: "theme",
    path: "/",
    httpOnly: true,
    sameSite: "lax",
    secrets: ["s3cr3t"],
    // Set domain and secure only if in production
    ...(isProduction
      ? { domain: "your-production-domain.com", secure: true }
      : {}),
  },
})

export const themeSessionResolver = createThemeSessionResolver(sessionStorage)
```

## Set up Remix Themes

Add the `ThemeProvider` to your root layout.

```tsx {1-3,6-11,15-22,25-26,28,33} title="app/root.tsx" showLineNumbers
import clsx from "clsx"
import { PreventFlashOnWrongTheme, ThemeProvider, useTheme } from "remix-themes"

import { themeSessionResolver } from "./sessions.server"

// Return the theme from the session storage using the loader
export async function loader({ request }: LoaderFunctionArgs) {
  const { getTheme } = await themeSessionResolver(request)
  return {
    theme: getTheme(),
  }
}
// Wrap your app with ThemeProvider.
// `specifiedTheme` is the stored theme in the session storage.
// `themeAction` is the action name that's used to change the theme in the session storage.
export default function AppWithProviders() {
  const data = useLoaderData<typeof loader>()
  return (
    <ThemeProvider specifiedTheme={data.theme} themeAction="/action/set-theme">
      <App />
    </ThemeProvider>
  )
}

export function App() {
  const data = useLoaderData<typeof loader>()
  const [theme] = useTheme()
  return (
    <html lang="en" className={clsx(theme)}>
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <PreventFlashOnWrongTheme ssrTheme={Boolean(data.theme)} />
        <Links />
      </head>
      <body>
        <Outlet />
        <ScrollRestoration />
        <Scripts />
        <LiveReload />
      </body>
    </html>
  )
}
```

## Add an action route

Create a file in `/routes/action.set-theme.ts`. Ensure that you pass the filename to the ThemeProvider component. This route is used to store the preferred theme in the session storage when the user changes it.

```tsx title="app/routes/action.set-theme.ts" showLineNumbers
import { createThemeAction } from "remix-themes"

import { themeSessionResolver } from "./sessions.server"

export const action = createThemeAction(themeSessionResolver)
```

## Add a mode toggle

Place a mode toggle on your site to toggle between light and dark mode.

```tsx title="components/mode-toggle.tsx" showLineNumbers
import { Moon, Sun } from "lucide-react"
import { Theme, useTheme } from "remix-themes"

import { Button } from "./ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "./ui/dropdown-menu"

export function ModeToggle() {
  const [, setTheme] = useTheme()

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <Sun className="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
          <Moon className="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
          <span className="sr-only">Toggle theme</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setTheme(Theme.LIGHT)}>
          Light
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme(Theme.DARK)}>
          Dark
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/dark-mode/vite.mdx -->

## apps/v4/content/docs/dark-mode/vite.mdx

---
title: Vite
description: Adding dark mode to your Vite app.
---

## Create a theme provider

```tsx title="components/theme-provider.tsx" showLineNumbers
import { createContext, useContext, useEffect, useState } from "react"

type Theme = "dark" | "light" | "system"

type ThemeProviderProps = {
  children: React.ReactNode
  defaultTheme?: Theme
  storageKey?: string
}

type ThemeProviderState = {
  theme: Theme
  setTheme: (theme: Theme) => void
}

const initialState: ThemeProviderState = {
  theme: "system",
  setTheme: () => null,
}

const ThemeProviderContext = createContext<ThemeProviderState>(initialState)

export function ThemeProvider({
  children,
  defaultTheme = "system",
  storageKey = "vite-ui-theme",
  ...props
}: ThemeProviderProps) {
  const [theme, setTheme] = useState<Theme>(
    () => (localStorage.getItem(storageKey) as Theme) || defaultTheme
  )

  useEffect(() => {
    const root = window.document.documentElement

    root.classList.remove("light", "dark")

    if (theme === "system") {
      const systemTheme = window.matchMedia("(prefers-color-scheme: dark)")
        .matches
        ? "dark"
        : "light"

      root.classList.add(systemTheme)
      return
    }

    root.classList.add(theme)
  }, [theme])

  const value = {
    theme,
    setTheme: (theme: Theme) => {
      localStorage.setItem(storageKey, theme)
      setTheme(theme)
    },
  }

  return (
    <ThemeProviderContext.Provider {...props} value={value}>
      {children}
    </ThemeProviderContext.Provider>
  )
}

export const useTheme = () => {
  const context = useContext(ThemeProviderContext)

  if (context === undefined)
    throw new Error("useTheme must be used within a ThemeProvider")

  return context
}
```

## Wrap your root layout

Add the `ThemeProvider` to your root layout.

```tsx {1,5-7} title="App.tsx" showLineNumbers
import { ThemeProvider } from "@/components/theme-provider"

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      {children}
    </ThemeProvider>
  )
}

export default App
```

## Add a mode toggle

Place a mode toggle on your site to toggle between light and dark mode.

```tsx title="components/mode-toggle.tsx" showLineNumbers
import { Moon, Sun } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { useTheme } from "@/components/theme-provider"

export function ModeToggle() {
  const { setTheme } = useTheme()

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <Sun className="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
          <Moon className="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
          <span className="sr-only">Toggle theme</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setTheme("light")}>
          Light
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("dark")}>
          Dark
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("system")}>
          System
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```


---

<!-- SOURCE: apps/v4/content/docs/forms/index.mdx -->

## apps/v4/content/docs/forms/index.mdx

---
title: Forms
description: Build forms with React and shadcn/ui.
---

import { ClipboardListIcon } from "lucide-react"

## Pick Your Framework

Start by selecting your framework. Then follow the instructions to learn how to build forms with shadcn/ui and the form library of your choice.

<div className="mt-8 grid gap-4 sm:grid-cols-2 sm:gap-6">
  <LinkedCard href="/docs/forms/react-hook-form">
    <ClipboardListIcon className="size-10" />
    <p className="mt-2 font-medium">React Hook Form</p>
  </LinkedCard>
  <LinkedCard href="/docs/forms/tanstack-form">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      className="size-10"
      fill="currentColor"
    >
      <path d="M6.93 13.688a.343.343 0 0 1 .468.132l.063.106c.48.851.98 1.66 1.5 2.426a35.65 35.65 0 0 0 2.074 2.742.345.345 0 0 1-.039.484l-.074.066c-2.543 2.223-4.191 2.665-4.953 1.333-.746-1.305-.477-3.672.808-7.11a.344.344 0 0 1 .153-.18ZM17.75 16.3a.34.34 0 0 1 .395.27l.02.1c.628 3.286.187 4.93-1.325 4.93-1.48 0-3.36-1.402-5.649-4.203a.327.327 0 0 1-.074-.222c0-.188.156-.34.344-.34h.121a32.984 32.984 0 0 0 2.809-.098c1.07-.086 2.191-.23 3.359-.437zm.871-6.977a.353.353 0 0 1 .445-.21l.102.034c3.262 1.11 4.504 2.332 3.719 3.664-.766 1.305-2.993 2.254-6.684 2.848a.362.362 0 0 1-.238-.047.343.343 0 0 1-.125-.476l.062-.106a34.07 34.07 0 0 0 1.367-2.523c.477-.989.93-2.051 1.352-3.184zM7.797 8.34a.362.362 0 0 1 .238.047.343.343 0 0 1 .125.476l-.062.106a34.088 34.088 0 0 0-1.367 2.523c-.477.988-.93 2.051-1.352 3.184a.353.353 0 0 1-.445.21l-.102-.034C1.57 13.742.328 12.52 1.113 11.188 1.88 9.883 4.106 8.934 7.797 8.34Zm5.281-3.984c2.543-2.223 4.192-2.664 4.953-1.332.746 1.304.477 3.671-.808 7.109a.344.344 0 0 1-.153.18.343.343 0 0 1-.468-.133l-.063-.106a34.64 34.64 0 0 0-1.5-2.426 35.65 35.65 0 0 0-2.074-2.742.345.345 0 0 1 .039-.484ZM7.285 2.274c1.48 0 3.364 1.402 5.649 4.203a.349.349 0 0 1 .078.218.348.348 0 0 1-.348.344l-.117-.004a34.584 34.584 0 0 0-2.809.102 35.54 35.54 0 0 0-3.363.437.343.343 0 0 1-.394-.273l-.02-.098c-.629-3.285-.188-4.93 1.324-4.93Zm2.871 5.812h3.688a.638.638 0 0 1 .55.316l1.848 3.22a.644.644 0 0 1 0 .628l-1.847 3.223a.638.638 0 0 1-.551.316h-3.688a.627.627 0 0 1-.547-.316L7.758 12.25a.644.644 0 0 1 0-.629L9.61 8.402a.627.627 0 0 1 .546-.316Zm3.23.793a.638.638 0 0 1 .552.316l1.39 2.426a.644.644 0 0 1 0 .629l-1.39 2.43a.638.638 0 0 1-.551.316h-2.774a.627.627 0 0 1-.546-.316l-1.395-2.43a.644.644 0 0 1 0-.629l1.395-2.426a.627.627 0 0 1 .546-.316Zm-.491.867h-1.79a.624.624 0 0 0-.546.316l-.899 1.56a.644.644 0 0 0 0 .628l.899 1.563a.632.632 0 0 0 .547.316h1.789a.632.632 0 0 0 .547-.316l.898-1.563a.644.644 0 0 0 0-.629l-.898-1.558a.624.624 0 0 0-.547-.317Zm-.477.828c.227 0 .438.121.547.317l.422.73a.625.625 0 0 1 0 .629l-.422.734a.627.627 0 0 1-.547.317h-.836a.632.632 0 0 1-.547-.317l-.422-.734a.625.625 0 0 1 0-.629l.422-.73a.632.632 0 0 1 .547-.317zm-.418.817a.548.548 0 0 0-.473.273.547.547 0 0 0 0 .547.544.544 0 0 0 .473.27.544.544 0 0 0 .473-.27.547.547 0 0 0 0-.547.548.548 0 0 0-.473-.273Zm-4.422.546h.98M18.98 7.75c.391-1.895.477-3.344.223-4.398-.148-.63-.422-1.137-.84-1.508-.441-.39-1-.582-1.625-.582-1.035 0-2.12.472-3.281 1.367a14.9 14.9 0 0 0-1.473 1.316 1.206 1.206 0 0 0-.136-.144c-1.446-1.285-2.66-2.082-3.7-2.39-.617-.184-1.195-.2-1.722-.024-.559.187-1.004.574-1.317 1.117-.515.894-.652 2.074-.46 3.527.078.59.214 1.235.402 1.934a1.119 1.119 0 0 0-.215.047C3.008 8.62 1.71 9.269.926 10.015c-.465.442-.77.938-.883 1.481-.113.578 0 1.156.312 1.7.516.894 1.465 1.597 2.817 2.155.543.223 1.156.426 1.844.61a1.023 1.023 0 0 0-.07.226c-.391 1.891-.477 3.344-.223 4.395.148.629.425 1.14.84 1.508.44.39 1 .582 1.625.582 1.035 0 2.12-.473 3.28-1.364.477-.37.973-.816 1.489-1.336a1.2 1.2 0 0 0 .195.227c1.446 1.285 2.66 2.082 3.7 2.39.617.184 1.195.2 1.722.024.559-.187 1.004-.574 1.317-1.117.515-.894.652-2.074.46-3.527a14.941 14.941 0 0 0-.425-2.012 1.225 1.225 0 0 0 .238-.047c1.828-.61 3.125-1.258 3.91-2.004.465-.441.77-.937.883-1.48.113-.578 0-1.157-.313-1.7-.515-.894-1.464-1.597-2.816-2.156a14.576 14.576 0 0 0-1.906-.625.865.865 0 0 0 .059-.195z" />
    </svg>
    <p className="mt-2 font-medium">TanStack Form</p>
  </LinkedCard>
  <LinkedCard href="#" className="border border-dashed bg-transparent">
    <svg
      role="img"
      viewBox="0 0 24 24"
      className="size-10"
      fill="currentColor"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>React</title>
      <path d="M14.23 12.004a2.236 2.236 0 0 1-2.235 2.236 2.236 2.236 0 0 1-2.236-2.236 2.236 2.236 0 0 1 2.235-2.236 2.236 2.236 0 0 1 2.236 2.236zm2.648-10.69c-1.346 0-3.107.96-4.888 2.622-1.78-1.653-3.542-2.602-4.887-2.602-.41 0-.783.093-1.106.278-1.375.793-1.683 3.264-.973 6.365C1.98 8.917 0 10.42 0 12.004c0 1.59 1.99 3.097 5.043 4.03-.704 3.113-.39 5.588.988 6.38.32.187.69.275 1.102.275 1.345 0 3.107-.96 4.888-2.624 1.78 1.654 3.542 2.603 4.887 2.603.41 0 .783-.09 1.106-.275 1.374-.792 1.683-3.263.973-6.365C22.02 15.096 24 13.59 24 12.004c0-1.59-1.99-3.097-5.043-4.032.704-3.11.39-5.587-.988-6.38-.318-.184-.688-.277-1.092-.278zm-.005 1.09v.006c.225 0 .406.044.558.127.666.382.955 1.835.73 3.704-.054.46-.142.945-.25 1.44-.96-.236-2.006-.417-3.107-.534-.66-.905-1.345-1.727-2.035-2.447 1.592-1.48 3.087-2.292 4.105-2.295zm-9.77.02c1.012 0 2.514.808 4.11 2.28-.686.72-1.37 1.537-2.02 2.442-1.107.117-2.154.298-3.113.538-.112-.49-.195-.964-.254-1.42-.23-1.868.054-3.32.714-3.707.19-.09.4-.127.563-.132zm4.882 3.05c.455.468.91.992 1.36 1.564-.44-.02-.89-.034-1.345-.034-.46 0-.915.01-1.36.034.44-.572.895-1.096 1.345-1.565zM12 8.1c.74 0 1.477.034 2.202.093.406.582.802 1.203 1.183 1.86.372.64.71 1.29 1.018 1.946-.308.655-.646 1.31-1.013 1.95-.38.66-.773 1.288-1.18 1.87-.728.063-1.466.098-2.21.098-.74 0-1.477-.035-2.202-.093-.406-.582-.802-1.204-1.183-1.86-.372-.64-.71-1.29-1.018-1.946.303-.657.646-1.313 1.013-1.954.38-.66.773-1.286 1.18-1.868.728-.064 1.466-.098 2.21-.098zm-3.635.254c-.24.377-.48.763-.704 1.16-.225.39-.435.782-.635 1.174-.265-.656-.49-1.31-.676-1.947.64-.15 1.315-.283 2.015-.386zm7.26 0c.695.103 1.365.23 2.006.387-.18.632-.405 1.282-.66 1.933-.2-.39-.41-.783-.64-1.174-.225-.392-.465-.774-.705-1.146zm3.063.675c.484.15.944.317 1.375.498 1.732.74 2.852 1.708 2.852 2.476-.005.768-1.125 1.74-2.857 2.475-.42.18-.88.342-1.355.493-.28-.958-.646-1.956-1.1-2.98.45-1.017.81-2.01 1.085-2.964zm-13.395.004c.278.96.645 1.957 1.1 2.98-.45 1.017-.812 2.01-1.086 2.964-.484-.15-.944-.318-1.37-.5-1.732-.737-2.852-1.706-2.852-2.474 0-.768 1.12-1.742 2.852-2.476.42-.18.88-.342 1.356-.494zm11.678 4.28c.265.657.49 1.312.676 1.948-.64.157-1.316.29-2.016.39.24-.375.48-.762.705-1.158.225-.39.435-.788.636-1.18zm-9.945.02c.2.392.41.783.64 1.175.23.39.465.772.705 1.143-.695-.102-1.365-.23-2.006-.386.18-.63.406-1.282.66-1.933zM17.92 16.32c.112.493.2.968.254 1.423.23 1.868-.054 3.32-.714 3.708-.147.09-.338.128-.563.128-1.012 0-2.514-.807-4.11-2.28.686-.72 1.37-1.536 2.02-2.44 1.107-.118 2.154-.3 3.113-.54zm-11.83.01c.96.234 2.006.415 3.107.532.66.905 1.345 1.727 2.035 2.446-1.595 1.483-3.092 2.295-4.11 2.295-.22-.005-.406-.05-.553-.132-.666-.38-.955-1.834-.73-3.703.054-.46.142-.944.25-1.438zm4.56.64c.44.02.89.034 1.345.034.46 0 .915-.01 1.36-.034-.44.572-.895 1.095-1.345 1.565-.455-.47-.91-.993-1.36-1.565z" />
    </svg>
    <p className="mt-2 font-medium">useActionState</p>
    <p className="mt-1 text-xs text-muted-foreground">(Coming Soon)</p>
  </LinkedCard>
</div>


---

<!-- SOURCE: apps/v4/content/docs/forms/next.mdx -->

## apps/v4/content/docs/forms/next.mdx

---
title: Next.js
description: Build forms in React using useActionState and Server Actions.
---

import { InfoIcon } from "lucide-react"

In this guide, we will take a look at building forms with Next.js using `useActionState` and Server Actions. We'll cover building forms, validation, pending states, accessibility, and more.

## Demo

We are going to build the following form with a simple text input and a textarea. On submit, we'll use a server action to validate the form data and update the form state.

<ComponentPreview
  name="form-next-demo"
  className="[&_.preview]:h-[700px] [&_pre]:h-[700px]!"
/>

<Callout icon={<InfoIcon />}>
  **Note:** The examples on this page intentionally disable browser validation
  to show how schema validation and form errors work in server actions.
</Callout>

## Approach

This form leverages Next.js and React's built-in capabilities for form handling. We'll build our form using the `<Field />` component, which gives you **complete flexibility over the markup and styling**.

- Uses Next.js `<Form />` component for navigation and progressive enhancement.
- `<Field />` components for building accessible forms.
- `useActionState` for managing form state and errors.
- Handles loading states with the pending prop.
- Server Actions for handling form submissions.
- Server-side validation using Zod.

## Anatomy

Here's a basic example of a form using the `<Field />` component.

```tsx showLineNumbers
<Form action={formAction}>
  <FieldGroup>
    <Field data-invalid={!!formState.errors?.title?.length}>
      <FieldLabel htmlFor="title">Bug Title</FieldLabel>
      <Input
        id="title"
        name="title"
        defaultValue={formState.values.title}
        disabled={pending}
        aria-invalid={!!formState.errors?.title?.length}
        placeholder="Login button not working on mobile"
        autoComplete="off"
      />
      <FieldDescription>
        Provide a concise title for your bug report.
      </FieldDescription>
      {formState.errors?.title && (
        <FieldError>{formState.errors.title[0]}</FieldError>
      )}
    </Field>
  </FieldGroup>
  <Button type="submit">Submit</Button>
</Form>
```

## Usage

### Create a form schema

We'll start by defining the shape of our form using a Zod schema in a `schema.ts` file.

<Callout icon={<InfoIcon />}>
  **Note:** This example uses `zod v3` for schema validation, but you can
  replace it with any other schema validation library. Make sure your schema
  library conforms to the Standard Schema specification.
</Callout>

```tsx showLineNumbers title="schema.ts"
import { z } from "zod"

export const formSchema = z.object({
  title: z
    .string()
    .min(5, "Bug title must be at least 5 characters.")
    .max(32, "Bug title must be at most 32 characters."),
  description: z
    .string()
    .min(20, "Description must be at least 20 characters.")
    .max(100, "Description must be at most 100 characters."),
})
```

### Define the form state type

Next, we'll create a type for our form state that includes values, errors, and success status. This will be used to type the form state on the client and server.

```tsx showLineNumbers title="schema.ts"
import { z } from "zod"

export type FormState = {
  values?: z.infer<typeof formSchema>
  errors: null | Partial<Record<keyof z.infer<typeof formSchema>, string[]>>
  success: boolean
}
```

**Important:** We define the schema and the `FormState` type in a separate file so we can import them into both the client and server components.

### Create the Server Action

A server action is a function that runs on the server and can be called from the client. We'll use it to validate the form data and update the form state.

<ComponentSource
  src="/registry/new-york-v4/examples/form-next-demo-action.ts"
  title="actions.ts"
/>

**Note:** We're returning `values` for error cases. This is because we want to keep the user submitted values in the form state. For success cases, we're returning empty values to reset the form.

### Build the form

We can now build the form using the `<Field />` component. We'll use the `useActionState` hook to manage the form state, server action, and pending state.

<ComponentSource
  src="/registry/new-york-v4/examples/form-next-demo.tsx"
  title="form.tsx"
/>

### Done

That's it. You now have a fully accessible form with client and server-side validation.

When you submit the form, the `formAction` function will be called on the server. The server action will validate the form data and update the form state.

If the form data is invalid, the server action will return the errors to the client. If the form data is valid, the server action will return the success status and update the form state.

## Pending States

Use the `pending` prop from `useActionState` to show loading indicators and disable form inputs.

```tsx showLineNumbers {11,26-34}
"use client"

import * as React from "react"
import Form from "next/form"

import { Spinner } from "@/components/ui/spinner"

import { bugReportFormAction } from "./actions"

export function BugReportForm() {
  const [formState, formAction, pending] = React.useActionState(
    bugReportFormAction,
    {
      errors: null,
      success: false,
    }
  )

  return (
    <Form action={formAction}>
      <FieldGroup>
        <Field data-disabled={pending}>
          <FieldLabel htmlFor="name">Name</FieldLabel>
          <Input id="name" name="name" disabled={pending} />
        </Field>
        <Field>
          <Button type="submit" disabled={pending}>
            {pending && <Spinner />} Submit
          </Button>
        </Field>
      </FieldGroup>
    </Form>
  )
}
```

## Disabled States

### Submit Button

To disable the submit button, use the `pending` prop on the button's `disabled` prop.

```tsx showLineNumbers
<Button type="submit" disabled={pending}>
  {pending && <Spinner />} Submit
</Button>
```

### Field

To apply a disabled state and styling to a `<Field />` component, use the `data-disabled` prop on the `<Field />` component.

```tsx showLineNumbers
<Field data-disabled={pending}>
  <FieldLabel htmlFor="name">Name</FieldLabel>
  <Input id="name" name="name" disabled={pending} />
</Field>
```

## Validation

### Server-side Validation

Use `safeParse()` on your schema in your server action to validate the form data.

```tsx showLineNumbers title="actions.ts" {12-20}
"use server"

export async function bugReportFormAction(
  _prevState: FormState,
  formData: FormData
) {
  const values = {
    title: formData.get("title") as string,
    description: formData.get("description") as string,
  }

  const result = formSchema.safeParse(values)

  if (!result.success) {
    return {
      values,
      success: false,
      errors: result.error.flatten().fieldErrors,
    }
  }

  return {
    errors: null,
    success: true,
  }
}
```

### Business Logic Validation

You can add additional custom validation logic in your server action.

Make sure to return the values on validation errors. This is to ensure that the form state maintains the user's input.

```tsx showLineNumbers title="actions.ts" {22-35}
"use server"

export async function bugReportFormAction(
  _prevState: FormState,
  formData: FormData
) {
  const values = {
    title: formData.get("title") as string,
    description: formData.get("description") as string,
  }

  const result = formSchema.safeParse(values)

  if (!result.success) {
    return {
      values,
      success: false,
      errors: result.error.flatten().fieldErrors,
    }
  }

  // Check if email already exists in database.
  const existingUser = await db.user.findUnique({
    where: { email: result.data.email },
  })

  if (existingUser) {
    return {
      values,
      success: false,
      errors: {
        email: ["This email is already registered"],
      },
    }
  }

  return {
    errors: null,
    success: true,
  }
}
```

## Displaying Errors

Display errors next to the field using `<FieldError />`. Make sure to add the `data-invalid` prop to the `<Field />` component and `aria-invalid` prop to the input.

```tsx showLineNumbers
<Field data-invalid={!!formState.errors?.email?.length}>
  <FieldLabel htmlFor="email">Email</FieldLabel>
  <Input
    id="email"
    name="email"
    type="email"
    aria-invalid={!!formState.errors?.email?.length}
  />
  {formState.errors?.email && (
    <FieldError>{formState.errors.email[0]}</FieldError>
  )}
</Field>
```

## Resetting the Form

When you submit a form with a server action, React will automatically reset the form state to the initial values.

### Reset on Success

To reset the form on success, you can omit the `values` from the server action and React will automatically reset the form state to the initial values. This is standard React behavior.

```tsx showLineNumbers title="actions.ts" {22-26}
export async function demoFormAction(
  _prevState: FormState,
  formData: FormData
) {
  const values = {
    title: formData.get("title") as string,
    description: formData.get("description") as string,
  }

  // Validation.
  if (!result.success) {
    return {
      values,
      success: false,
      errors: result.error.flatten().fieldErrors,
    }
  }

  // Business logic.
  callYourDatabaseOrAPI(values)

  // Omit the values on success to reset the form state.
  return {
    errors: null,
    success: true,
  }
}
```

### Preserve on Validation Errors

To prevent the form from being reset on failure, you can return the values in the server action. This is to ensure that the form state maintains the user's input.

```tsx showLineNumbers title="actions.ts" {12-17}
export async function demoFormAction(
  _prevState: FormState,
  formData: FormData
) {
  const values = {
    title: formData.get("title") as string,
    description: formData.get("description") as string,
  }

  // Validation.
  if (!result.success) {
    return {
      // Return the values on validation errors.
      values,
      success: false,
      errors: result.error.flatten().fieldErrors,
    }
  }
}
```

## Complex Forms

Here is an example of a more complex form with multiple fields and validation.

<ComponentPreview
  name="form-next-complex"
  className="[&_.preview]:h-[1100px] [&_pre]:h-[1100px]!"
  hideCode
/>

### Schema

<ComponentSource
  src="/registry/new-york-v4/examples/form-next-complex-schema.ts"
  title="schema.ts"
/>

### Form

<ComponentSource
  src="/registry/new-york-v4/examples/form-next-complex.tsx"
  title="form.tsx"
/>

### Server Action

<ComponentSource
  src="/registry/new-york-v4/examples/form-next-complex-action.ts"
  title="actions.ts"
/>


---

<!-- SOURCE: apps/v4/content/docs/forms/react-hook-form.mdx -->

## apps/v4/content/docs/forms/react-hook-form.mdx

---
title: React Hook Form
description: Build forms in React using React Hook Form and Zod.
links:
  doc: https://react-hook-form.com
---

import { InfoIcon } from "lucide-react"

In this guide, we will take a look at building forms with React Hook Form. We'll cover building forms with the `<Field />` component, adding schema validation using Zod, error handling, accessibility, and more.

## Demo

We are going to build the following form. It has a simple text input and a textarea. On submit, we'll validate the form data and display any errors.

<Callout icon={<InfoIcon />}>
  **Note:** For the purpose of this demo, we have intentionally disabled browser
  validation to show how schema validation and form errors work in React Hook
  Form. It is recommended to add basic browser validation in your production
  code.
</Callout>

<ComponentPreview
  name="form-rhf-demo"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

## Approach

This form leverages React Hook Form for performant, flexible form handling. We'll build our form using the `<Field />` component, which gives you **complete flexibility over the markup and styling**.

- Uses React Hook Form's `useForm` hook for form state management.
- `<Controller />` component for controlled inputs.
- `<Field />` components for building accessible forms.
- Client-side validation using Zod with `zodResolver`.

## Anatomy

Here's a basic example of a form using the `<Controller />` component from React Hook Form and the `<Field />` component.

```tsx showLineNumbers {5-18}
<Controller
  name="title"
  control={form.control}
  render={({ field, fieldState }) => (
    <Field data-invalid={fieldState.invalid}>
      <FieldLabel htmlFor={field.name}>Bug Title</FieldLabel>
      <Input
        {...field}
        id={field.name}
        aria-invalid={fieldState.invalid}
        placeholder="Login button not working on mobile"
        autoComplete="off"
      />
      <FieldDescription>
        Provide a concise title for your bug report.
      </FieldDescription>
      {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
    </Field>
  )}
/>
```

## Form

### Create a form schema

We'll start by defining the shape of our form using a Zod schema.

<Callout icon={<InfoIcon />}>
  **Note:** This example uses `zod v3` for schema validation, but you can
  replace it with any other Standard Schema validation library supported by
  React Hook Form.
</Callout>

```tsx showLineNumbers title="form.tsx"
import * as z from "zod"

const formSchema = z.object({
  title: z
    .string()
    .min(5, "Bug title must be at least 5 characters.")
    .max(32, "Bug title must be at most 32 characters."),
  description: z
    .string()
    .min(20, "Description must be at least 20 characters.")
    .max(100, "Description must be at most 100 characters."),
})
```

### Set up the form

Next, we'll use the `useForm` hook from React Hook Form to create our form instance. We'll also add the Zod resolver to validate the form data.

```tsx showLineNumbers title="form.tsx" {17-23}
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import * as z from "zod"

const formSchema = z.object({
  title: z
    .string()
    .min(5, "Bug title must be at least 5 characters.")
    .max(32, "Bug title must be at most 32 characters."),
  description: z
    .string()
    .min(20, "Description must be at least 20 characters.")
    .max(100, "Description must be at most 100 characters."),
})

export function BugReportForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      title: "",
      description: "",
    },
  })

  function onSubmit(data: z.infer<typeof formSchema>) {
    // Do something with the form values.
    console.log(data)
  }

  return (
    <form onSubmit={form.handleSubmit(onSubmit)}>
      {/* ... */}
      {/* Build the form here */}
      {/* ... */}
    </form>
  )
}
```

### Build the form

We can now build the form using the `<Controller />` component from React Hook Form and the `<Field />` component.

<ComponentSource
  src="/registry/new-york-v4/examples/form-rhf-demo.tsx"
  title="form.tsx"
/>

### Done

That's it. You now have a fully accessible form with client-side validation.

When you submit the form, the `onSubmit` function will be called with the validated form data. If the form data is invalid, React Hook Form will display the errors next to each field.

## Validation

### Client-side Validation

React Hook Form validates your form data using the Zod schema. Define a schema and pass it to the `resolver` option of the `useForm` hook.

```tsx showLineNumbers title="example-form.tsx" {5-8,12}
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import * as z from "zod"

const formSchema = z.object({
  title: z.string(),
  description: z.string().optional(),
})

export function ExampleForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      title: "",
      description: "",
    },
  })
}
```

### Validation Modes

React Hook Form supports different validation modes.

```tsx showLineNumbers title="form.tsx" {3}
const form = useForm<z.infer<typeof formSchema>>({
  resolver: zodResolver(formSchema),
  mode: "onChange",
})
```

| Mode          | Description                                              |
| ------------- | -------------------------------------------------------- |
| `"onChange"`  | Validation triggers on every change.                     |
| `"onBlur"`    | Validation triggers on blur.                             |
| `"onSubmit"`  | Validation triggers on submit (default).                 |
| `"onTouched"` | Validation triggers on first blur, then on every change. |
| `"all"`       | Validation triggers on blur and change.                  |

## Displaying Errors

Display errors next to the field using `<FieldError />`. For styling and accessibility:

- Add the `data-invalid` prop to the `<Field />` component.
- Add the `aria-invalid` prop to the form control such as `<Input />`, `<SelectTrigger />`, `<Checkbox />`, etc.

```tsx showLineNumbers title="form.tsx" {5,11,13}
<Controller
  name="email"
  control={form.control}
  render={({ field, fieldState }) => (
    <Field data-invalid={fieldState.invalid}>
      <FieldLabel htmlFor={field.name}>Email</FieldLabel>
      <Input
        {...field}
        id={field.name}
        type="email"
        aria-invalid={fieldState.invalid}
      />
      {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
    </Field>
  )}
/>
```

## Working with Different Field Types

### Input

- For input fields, spread the `field` object onto the `<Input />` component.
- To show errors, add the `aria-invalid` prop to the `<Input />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-rhf-input"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

For simple text inputs, spread the `field` object onto the input.

```tsx showLineNumbers title="form.tsx" {5,7,8}
<Controller
  name="name"
  control={form.control}
  render={({ field, fieldState }) => (
    <Field data-invalid={fieldState.invalid}>
      <FieldLabel htmlFor={field.name}>Name</FieldLabel>
      <Input {...field} id={field.name} aria-invalid={fieldState.invalid} />
      {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
    </Field>
  )}
/>
```

### Textarea

- For textarea fields, spread the `field` object onto the `<Textarea />` component.
- To show errors, add the `aria-invalid` prop to the `<Textarea />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-rhf-textarea"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

For textarea fields, spread the `field` object onto the textarea.

```tsx showLineNumbers title="form.tsx" {5,10,18}
<Controller
  name="about"
  control={form.control}
  render={({ field, fieldState }) => (
    <Field data-invalid={fieldState.invalid}>
      <FieldLabel htmlFor="form-rhf-textarea-about">More about you</FieldLabel>
      <Textarea
        {...field}
        id="form-rhf-textarea-about"
        aria-invalid={fieldState.invalid}
        placeholder="I'm a software engineer..."
        className="min-h-[120px]"
      />
      <FieldDescription>
        Tell us more about yourself. This will be used to help us personalize
        your experience.
      </FieldDescription>
      {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
    </Field>
  )}
/>
```

### Select

- For select components, use `field.value` and `field.onChange` on the `<Select />` component.
- To show errors, add the `aria-invalid` prop to the `<SelectTrigger />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-rhf-select"
  className="sm:[&_.preview]:h-[500px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {5,13,22}
<Controller
  name="language"
  control={form.control}
  render={({ field, fieldState }) => (
    <Field orientation="responsive" data-invalid={fieldState.invalid}>
      <FieldContent>
        <FieldLabel htmlFor="form-rhf-select-language">
          Spoken Language
        </FieldLabel>
        <FieldDescription>
          For best results, select the language you speak.
        </FieldDescription>
        {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
      </FieldContent>
      <Select
        name={field.name}
        value={field.value}
        onValueChange={field.onChange}
      >
        <SelectTrigger
          id="form-rhf-select-language"
          aria-invalid={fieldState.invalid}
          className="min-w-[120px]"
        >
          <SelectValue placeholder="Select" />
        </SelectTrigger>
        <SelectContent position="item-aligned">
          <SelectItem value="auto">Auto</SelectItem>
          <SelectItem value="en">English</SelectItem>
        </SelectContent>
      </Select>
    </Field>
  )}
/>
```

### Checkbox

- For checkbox arrays, use `field.value` and `field.onChange` with array manipulation.
- To show errors, add the `aria-invalid` prop to the `<Checkbox />` component and the `data-invalid` prop to the `<Field />` component.
- Remember to add `data-slot="checkbox-group"` to the `<FieldGroup />` component for proper styling and spacing.

<ComponentPreview
  name="form-rhf-checkbox"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {10,15,20-22,38}
<Controller
  name="tasks"
  control={form.control}
  render={({ field, fieldState }) => (
    <FieldSet>
      <FieldLegend variant="label">Tasks</FieldLegend>
      <FieldDescription>
        Get notified when tasks you&apos;ve created have updates.
      </FieldDescription>
      <FieldGroup data-slot="checkbox-group">
        {tasks.map((task) => (
          <Field
            key={task.id}
            orientation="horizontal"
            data-invalid={fieldState.invalid}
          >
            <Checkbox
              id={`form-rhf-checkbox-${task.id}`}
              name={field.name}
              aria-invalid={fieldState.invalid}
              checked={field.value.includes(task.id)}
              onCheckedChange={(checked) => {
                const newValue = checked
                  ? [...field.value, task.id]
                  : field.value.filter((value) => value !== task.id)
                field.onChange(newValue)
              }}
            />
            <FieldLabel
              htmlFor={`form-rhf-checkbox-${task.id}`}
              className="font-normal"
            >
              {task.label}
            </FieldLabel>
          </Field>
        ))}
      </FieldGroup>
      {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
    </FieldSet>
  )}
/>
```

### Radio Group

- For radio groups, use `field.value` and `field.onChange` on the `<RadioGroup />` component.
- To show errors, add the `aria-invalid` prop to the `<RadioGroupItem />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-rhf-radiogroup"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {12-13,17,25,31}
<Controller
  name="plan"
  control={form.control}
  render={({ field, fieldState }) => (
    <FieldSet>
      <FieldLegend>Plan</FieldLegend>
      <FieldDescription>
        You can upgrade or downgrade your plan at any time.
      </FieldDescription>
      <RadioGroup
        name={field.name}
        value={field.value}
        onValueChange={field.onChange}
      >
        {plans.map((plan) => (
          <FieldLabel key={plan.id} htmlFor={`form-rhf-radiogroup-${plan.id}`}>
            <Field orientation="horizontal" data-invalid={fieldState.invalid}>
              <FieldContent>
                <FieldTitle>{plan.title}</FieldTitle>
                <FieldDescription>{plan.description}</FieldDescription>
              </FieldContent>
              <RadioGroupItem
                value={plan.id}
                id={`form-rhf-radiogroup-${plan.id}`}
                aria-invalid={fieldState.invalid}
              />
            </Field>
          </FieldLabel>
        ))}
      </RadioGroup>
      {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
    </FieldSet>
  )}
/>
```

### Switch

- For switches, use `field.value` and `field.onChange` on the `<Switch />` component.
- To show errors, add the `aria-invalid` prop to the `<Switch />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-rhf-switch"
  className="sm:[&_.preview]:h-[500px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {5,13,18-19}
<Controller
  name="twoFactor"
  control={form.control}
  render={({ field, fieldState }) => (
    <Field orientation="horizontal" data-invalid={fieldState.invalid}>
      <FieldContent>
        <FieldLabel htmlFor="form-rhf-switch-twoFactor">
          Multi-factor authentication
        </FieldLabel>
        <FieldDescription>
          Enable multi-factor authentication to secure your account.
        </FieldDescription>
        {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
      </FieldContent>
      <Switch
        id="form-rhf-switch-twoFactor"
        name={field.name}
        checked={field.value}
        onCheckedChange={field.onChange}
        aria-invalid={fieldState.invalid}
      />
    </Field>
  )}
/>
```

### Complex Forms

Here is an example of a more complex form with multiple fields and validation.

<ComponentPreview
  name="form-rhf-complex"
  className="sm:[&_.preview]:h-[1300px]"
  chromeLessOnMobile
/>

## Resetting the Form

Use `form.reset()` to reset the form to its default values.

```tsx showLineNumbers
<Button type="button" variant="outline" onClick={() => form.reset()}>
  Reset
</Button>
```

## Array Fields

React Hook Form provides a `useFieldArray` hook for managing dynamic array fields. This is useful when you need to add or remove fields dynamically.

<ComponentPreview
  name="form-rhf-array"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

### Using useFieldArray

Use the `useFieldArray` hook to manage array fields. It provides `fields`, `append`, and `remove` methods.

```tsx showLineNumbers title="form.tsx" {8-11}
import { useFieldArray, useForm } from "react-hook-form"

export function ExampleForm() {
  const form = useForm({
    // ... form config
  })

  const { fields, append, remove } = useFieldArray({
    control: form.control,
    name: "emails",
  })
}
```

### Array Field Structure

Wrap your array fields in a `<FieldSet />` with a `<FieldLegend />` and `<FieldDescription />`.

```tsx showLineNumbers title="form.tsx"
<FieldSet className="gap-4">
  <FieldLegend variant="label">Email Addresses</FieldLegend>
  <FieldDescription>
    Add up to 5 email addresses where we can contact you.
  </FieldDescription>
  <FieldGroup className="gap-4">{/* Array items go here */}</FieldGroup>
</FieldSet>
```

### Controller Pattern for Array Items

Map over the `fields` array and use `<Controller />` for each item. **Make sure to use `field.id` as the key**.

```tsx showLineNumbers title="form.tsx"
{
  fields.map((field, index) => (
    <Controller
      key={field.id}
      name={`emails.${index}.address`}
      control={form.control}
      render={({ field: controllerField, fieldState }) => (
        <Field orientation="horizontal" data-invalid={fieldState.invalid}>
          <FieldContent>
            <InputGroup>
              <InputGroupInput
                {...controllerField}
                id={`form-rhf-array-email-${index}`}
                aria-invalid={fieldState.invalid}
                placeholder="name@example.com"
                type="email"
                autoComplete="email"
              />
              {/* Remove button */}
            </InputGroup>
            {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
          </FieldContent>
        </Field>
      )}
    />
  ))
}
```

### Adding Items

Use the `append` method to add new items to the array.

```tsx showLineNumbers title="form.tsx"
<Button
  type="button"
  variant="outline"
  size="sm"
  onClick={() => append({ address: "" })}
  disabled={fields.length >= 5}
>
  Add Email Address
</Button>
```

### Removing Items

Use the `remove` method to remove items from the array. Add the remove button conditionally.

```tsx showLineNumbers title="form.tsx"
{
  fields.length > 1 && (
    <InputGroupAddon align="inline-end">
      <InputGroupButton
        type="button"
        variant="ghost"
        size="icon-xs"
        onClick={() => remove(index)}
        aria-label={`Remove email ${index + 1}`}
      >
        <XIcon />
      </InputGroupButton>
    </InputGroupAddon>
  )
}
```

### Array Validation

Use Zod's `array` method to validate array fields.

```tsx showLineNumbers title="form.tsx"
const formSchema = z.object({
  emails: z
    .array(
      z.object({
        address: z.string().email("Enter a valid email address."),
      })
    )
    .min(1, "Add at least one email address.")
    .max(5, "You can add up to 5 email addresses."),
})
```


---

<!-- SOURCE: apps/v4/content/docs/forms/tanstack-form.mdx -->

## apps/v4/content/docs/forms/tanstack-form.mdx

---
title: TanStack Form
description: Build forms in React using TanStack Form and Zod.
links:
  doc: https://tanstack.com/form
---

import { InfoIcon } from "lucide-react"

This guide explores how to build forms using TanStack Form. You'll learn to create forms with the `<Field />` component, implement schema validation with Zod, handle errors, and ensure accessibility.

## Demo

We'll start by building the following form. It has a simple text input and a textarea. On submit, we'll validate the form data and display any errors.

<Callout icon={<InfoIcon />}>
  **Note:** For the purpose of this demo, we have intentionally disabled browser
  validation to show how schema validation and form errors work in TanStack
  Form. It is recommended to add basic browser validation in your production
  code.
</Callout>

<ComponentPreview
  name="form-tanstack-demo"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

## Approach

This form leverages TanStack Form for powerful, headless form handling. We'll build our form using the `<Field />` component, which gives you **complete flexibility over the markup and styling**.

- Uses TanStack Form's `useForm` hook for form state management.
- `form.Field` component with render prop pattern for controlled inputs.
- `<Field />` components for building accessible forms.
- Client-side validation using Zod.
- Real-time validation feedback.

## Anatomy

Here's a basic example of a form using TanStack Form with the `<Field />` component.

```tsx showLineNumbers {15-31}
<form
  onSubmit={(e) => {
    e.preventDefault()
    form.handleSubmit()
  }}
>
  <FieldGroup>
    <form.Field
      name="title"
      children={(field) => {
        const isInvalid =
          field.state.meta.isTouched && !field.state.meta.isValid
        return (
          <Field data-invalid={isInvalid}>
            <FieldLabel htmlFor={field.name}>Bug Title</FieldLabel>
            <Input
              id={field.name}
              name={field.name}
              value={field.state.value}
              onBlur={field.handleBlur}
              onChange={(e) => field.handleChange(e.target.value)}
              aria-invalid={isInvalid}
              placeholder="Login button not working on mobile"
              autoComplete="off"
            />
            <FieldDescription>
              Provide a concise title for your bug report.
            </FieldDescription>
            {isInvalid && <FieldError errors={field.state.meta.errors} />}
          </Field>
        )
      }}
    />
  </FieldGroup>
  <Button type="submit">Submit</Button>
</form>
```

## Form

### Create a schema

We'll start by defining the shape of our form using a Zod schema.

<Callout icon={<InfoIcon />}>
  **Note:** This example uses `zod v3` for schema validation. TanStack Form
  integrates seamlessly with Zod and other Standard Schema validation libraries
  through its validators API.
</Callout>

```tsx showLineNumbers title="form.tsx"
import * as z from "zod"

const formSchema = z.object({
  title: z
    .string()
    .min(5, "Bug title must be at least 5 characters.")
    .max(32, "Bug title must be at most 32 characters."),
  description: z
    .string()
    .min(20, "Description must be at least 20 characters.")
    .max(100, "Description must be at most 100 characters."),
})
```

### Set up the form

Use the `useForm` hook from TanStack Form to create your form instance with Zod validation.

```tsx showLineNumbers title="form.tsx" {10-21}
import { useForm } from "@tanstack/react-form"
import { toast } from "sonner"
import * as z from "zod"

const formSchema = z.object({
  // ...
})

export function BugReportForm() {
  const form = useForm({
    defaultValues: {
      title: "",
      description: "",
    },
    validators: {
      onSubmit: formSchema,
    },
    onSubmit: async ({ value }) => {
      toast.success("Form submitted successfully")
    },
  })

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        form.handleSubmit()
      }}
    >
      {/* ... */}
    </form>
  )
}
```

We are using `onSubmit` to validate the form data here. TanStack Form supports other validation modes, which you can read about in the [documentation](https://tanstack.com/form/latest/docs/framework/react/guides/dynamic-validation).

### Build the form

We can now build the form using the `form.Field` component from TanStack Form and the `<Field />` component.

<ComponentSource
  src="/registry/new-york-v4/examples/form-tanstack-demo.tsx"
  title="form.tsx"
/>

### Done

That's it. You now have a fully accessible form with client-side validation.

When you submit the form, the `onSubmit` function will be called with the validated form data. If the form data is invalid, TanStack Form will display the errors next to each field.

## Validation

### Client-side Validation

TanStack Form validates your form data using the Zod schema. Validation happens in real-time as the user types.

```tsx showLineNumbers title="form.tsx" {13-15}
import { useForm } from "@tanstack/react-form"

const formSchema = z.object({
  // ...
})

export function BugReportForm() {
  const form = useForm({
    defaultValues: {
      title: "",
      description: "",
    },
    validators: {
      onSubmit: formSchema,
    },
    onSubmit: async ({ value }) => {
      console.log(value)
    },
  })

  return <form onSubmit={/* ... */}>{/* ... */}</form>
}
```

### Validation Modes

TanStack Form supports different validation strategies through the `validators` option:

| Mode         | Description                          |
| ------------ | ------------------------------------ |
| `"onChange"` | Validation triggers on every change. |
| `"onBlur"`   | Validation triggers on blur.         |
| `"onSubmit"` | Validation triggers on submit.       |

```tsx showLineNumbers title="form.tsx" {6-9}
const form = useForm({
  defaultValues: {
    title: "",
    description: "",
  },
  validators: {
    onSubmit: formSchema,
    onChange: formSchema,
    onBlur: formSchema,
  },
})
```

## Displaying Errors

Display errors next to the field using `<FieldError />`. For styling and accessibility:

- Add the `data-invalid` prop to the `<Field />` component.
- Add the `aria-invalid` prop to the form control such as `<Input />`, `<SelectTrigger />`, `<Checkbox />`, etc.

```tsx showLineNumbers title="form.tsx" {4,18}
<form.Field
  name="email"
  children={(field) => {
    const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid

    return (
      <Field data-invalid={isInvalid}>
        <FieldLabel htmlFor={field.name}>Email</FieldLabel>
        <Input
          id={field.name}
          name={field.name}
          value={field.state.value}
          onBlur={field.handleBlur}
          onChange={(e) => field.handleChange(e.target.value)}
          type="email"
          aria-invalid={isInvalid}
        />
        {isInvalid && <FieldError errors={field.state.meta.errors} />}
      </Field>
    )
  }}
/>
```

## Working with Different Field Types

### Input

- For input fields, use `field.state.value` and `field.handleChange` on the `<Input />` component.
- To show errors, add the `aria-invalid` prop to the `<Input />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-tanstack-input"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {6,11-14,22}
<form.Field
  name="username"
  children={(field) => {
    const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
    return (
      <Field data-invalid={isInvalid}>
        <FieldLabel htmlFor="form-tanstack-input-username">Username</FieldLabel>
        <Input
          id="form-tanstack-input-username"
          name={field.name}
          value={field.state.value}
          onBlur={field.handleBlur}
          onChange={(e) => field.handleChange(e.target.value)}
          aria-invalid={isInvalid}
          placeholder="shadcn"
          autoComplete="username"
        />
        <FieldDescription>
          This is your public display name. Must be between 3 and 10 characters.
          Must only contain letters, numbers, and underscores.
        </FieldDescription>
        {isInvalid && <FieldError errors={field.state.meta.errors} />}
      </Field>
    )
  }}
/>
```

### Textarea

- For textarea fields, use `field.state.value` and `field.handleChange` on the `<Textarea />` component.
- To show errors, add the `aria-invalid` prop to the `<Textarea />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-tanstack-textarea"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {6,13-16,24}
<form.Field
  name="about"
  children={(field) => {
    const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
    return (
      <Field data-invalid={isInvalid}>
        <FieldLabel htmlFor="form-tanstack-textarea-about">
          More about you
        </FieldLabel>
        <Textarea
          id="form-tanstack-textarea-about"
          name={field.name}
          value={field.state.value}
          onBlur={field.handleBlur}
          onChange={(e) => field.handleChange(e.target.value)}
          aria-invalid={isInvalid}
          placeholder="I'm a software engineer..."
          className="min-h-[120px]"
        />
        <FieldDescription>
          Tell us more about yourself. This will be used to help us personalize
          your experience.
        </FieldDescription>
        {isInvalid && <FieldError errors={field.state.meta.errors} />}
      </Field>
    )
  }}
/>
```

### Select

- For select components, use `field.state.value` and `field.handleChange` on the `<Select />` component.
- To show errors, add the `aria-invalid` prop to the `<SelectTrigger />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-tanstack-select"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {6,18-19,23}
<form.Field
  name="language"
  children={(field) => {
    const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
    return (
      <Field orientation="responsive" data-invalid={isInvalid}>
        <FieldContent>
          <FieldLabel htmlFor="form-tanstack-select-language">
            Spoken Language
          </FieldLabel>
          <FieldDescription>
            For best results, select the language you speak.
          </FieldDescription>
          {isInvalid && <FieldError errors={field.state.meta.errors} />}
        </FieldContent>
        <Select
          name={field.name}
          value={field.state.value}
          onValueChange={field.handleChange}
        >
          <SelectTrigger
            id="form-tanstack-select-language"
            aria-invalid={isInvalid}
            className="min-w-[120px]"
          >
            <SelectValue placeholder="Select" />
          </SelectTrigger>
          <SelectContent position="item-aligned">
            <SelectItem value="auto">Auto</SelectItem>
            <SelectItem value="en">English</SelectItem>
          </SelectContent>
        </Select>
      </Field>
    )
  }}
/>
```

### Checkbox

- For checkbox, use `field.state.value` and `field.handleChange` on the `<Checkbox />` component.
- To show errors, add the `aria-invalid` prop to the `<Checkbox />` component and the `data-invalid` prop to the `<Field />` component.
- For checkbox arrays, use `mode="array"` on the `<form.Field />` component and TanStack Form's array helpers.
- Remember to add `data-slot="checkbox-group"` to the `<FieldGroup />` component for proper styling and spacing.

<ComponentPreview
  name="form-tanstack-checkbox"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {12,17,22-24,44}
<form.Field
  name="tasks"
  mode="array"
  children={(field) => {
    const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
    return (
      <FieldSet>
        <FieldLegend variant="label">Tasks</FieldLegend>
        <FieldDescription>
          Get notified when tasks you&apos;ve created have updates.
        </FieldDescription>
        <FieldGroup data-slot="checkbox-group">
          {tasks.map((task) => (
            <Field
              key={task.id}
              orientation="horizontal"
              data-invalid={isInvalid}
            >
              <Checkbox
                id={`form-tanstack-checkbox-${task.id}`}
                name={field.name}
                aria-invalid={isInvalid}
                checked={field.state.value.includes(task.id)}
                onCheckedChange={(checked) => {
                  if (checked) {
                    field.pushValue(task.id)
                  } else {
                    const index = field.state.value.indexOf(task.id)
                    if (index > -1) {
                      field.removeValue(index)
                    }
                  }
                }}
              />
              <FieldLabel
                htmlFor={`form-tanstack-checkbox-${task.id}`}
                className="font-normal"
              >
                {task.label}
              </FieldLabel>
            </Field>
          ))}
        </FieldGroup>
        {isInvalid && <FieldError errors={field.state.meta.errors} />}
      </FieldSet>
    )
  }}
/>
```

### Radio Group

- For radio groups, use `field.state.value` and `field.handleChange` on the `<RadioGroup />` component.
- To show errors, add the `aria-invalid` prop to the `<RadioGroupItem />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-tanstack-radiogroup"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {21,29,35}
<form.Field
  name="plan"
  children={(field) => {
    const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
    return (
      <FieldSet>
        <FieldLegend>Plan</FieldLegend>
        <FieldDescription>
          You can upgrade or downgrade your plan at any time.
        </FieldDescription>
        <RadioGroup
          name={field.name}
          value={field.state.value}
          onValueChange={field.handleChange}
        >
          {plans.map((plan) => (
            <FieldLabel
              key={plan.id}
              htmlFor={`form-tanstack-radiogroup-${plan.id}`}
            >
              <Field orientation="horizontal" data-invalid={isInvalid}>
                <FieldContent>
                  <FieldTitle>{plan.title}</FieldTitle>
                  <FieldDescription>{plan.description}</FieldDescription>
                </FieldContent>
                <RadioGroupItem
                  value={plan.id}
                  id={`form-tanstack-radiogroup-${plan.id}`}
                  aria-invalid={isInvalid}
                />
              </Field>
            </FieldLabel>
          ))}
        </RadioGroup>
        {isInvalid && <FieldError errors={field.state.meta.errors} />}
      </FieldSet>
    )
  }}
/>
```

### Switch

- For switches, use `field.state.value` and `field.handleChange` on the `<Switch />` component.
- To show errors, add the `aria-invalid` prop to the `<Switch />` component and the `data-invalid` prop to the `<Field />` component.

<ComponentPreview
  name="form-tanstack-switch"
  className="sm:[&_.preview]:h-[500px]"
  chromeLessOnMobile
/>

```tsx showLineNumbers title="form.tsx" {6,14,19-21}
<form.Field
  name="twoFactor"
  children={(field) => {
    const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
    return (
      <Field orientation="horizontal" data-invalid={isInvalid}>
        <FieldContent>
          <FieldLabel htmlFor="form-tanstack-switch-twoFactor">
            Multi-factor authentication
          </FieldLabel>
          <FieldDescription>
            Enable multi-factor authentication to secure your account.
          </FieldDescription>
          {isInvalid && <FieldError errors={field.state.meta.errors} />}
        </FieldContent>
        <Switch
          id="form-tanstack-switch-twoFactor"
          name={field.name}
          checked={field.state.value}
          onCheckedChange={field.handleChange}
          aria-invalid={isInvalid}
        />
      </Field>
    )
  }}
/>
```

### Complex Forms

Here is an example of a more complex form with multiple fields and validation.

<ComponentPreview
  name="form-tanstack-complex"
  className="sm:[&_.preview]:h-[1100px]"
  chromeLessOnMobile
/>

## Resetting the Form

Use `form.reset()` to reset the form to its default values.

```tsx showLineNumbers
<Button type="button" variant="outline" onClick={() => form.reset()}>
  Reset
</Button>
```

## Array Fields

TanStack Form provides powerful array field management with `mode="array"`. This allows you to dynamically add, remove, and update array items with full validation support.

<ComponentPreview
  name="form-tanstack-array"
  className="sm:[&_.preview]:h-[700px]"
  chromeLessOnMobile
/>

This example demonstrates managing multiple email addresses with array fields. Users can add up to 5 email addresses, remove individual addresses, and each address is validated independently.

### Array Field Structure

Use `mode="array"` on the parent field to enable array field management.

```tsx showLineNumbers title="form.tsx" {3,12-14}
<form.Field
  name="emails"
  mode="array"
  children={(field) => {
    return (
      <FieldSet>
        <FieldLegend variant="label">Email Addresses</FieldLegend>
        <FieldDescription>
          Add up to 5 email addresses where we can contact you.
        </FieldDescription>
        <FieldGroup>
          {field.state.value.map((_, index) => (
            // Nested field for each array item
          ))}
        </FieldGroup>
      </FieldSet>
    )
  }}
/>
```

### Nested Fields

Access individual array items using bracket notation: `fieldName[index].propertyName`. This example uses `InputGroup` to display the remove button inline with the input.

```tsx showLineNumbers title="form.tsx"
<form.Field
  name={`emails[${index}].address`}
  children={(subField) => {
    const isSubFieldInvalid =
      subField.state.meta.isTouched && !subField.state.meta.isValid
    return (
      <Field orientation="horizontal" data-invalid={isSubFieldInvalid}>
        <FieldContent>
          <InputGroup>
            <InputGroupInput
              id={`form-tanstack-array-email-${index}`}
              name={subField.name}
              value={subField.state.value}
              onBlur={subField.handleBlur}
              onChange={(e) => subField.handleChange(e.target.value)}
              aria-invalid={isSubFieldInvalid}
              placeholder="name@example.com"
              type="email"
            />
            {field.state.value.length > 1 && (
              <InputGroupAddon align="inline-end">
                <InputGroupButton
                  type="button"
                  variant="ghost"
                  size="icon-xs"
                  onClick={() => field.removeValue(index)}
                  aria-label={`Remove email ${index + 1}`}
                >
                  <XIcon />
                </InputGroupButton>
              </InputGroupAddon>
            )}
          </InputGroup>
          {isSubFieldInvalid && (
            <FieldError errors={subField.state.meta.errors} />
          )}
        </FieldContent>
      </Field>
    )
  }}
/>
```

### Adding Items

Use `field.pushValue(item)` to add items to an array field. You can disable the button when the array reaches its maximum length.

```tsx showLineNumbers title="form.tsx"
<Button
  type="button"
  variant="outline"
  size="sm"
  onClick={() => field.pushValue({ address: "" })}
  disabled={field.state.value.length >= 5}
>
  Add Email Address
</Button>
```

### Removing Items

Use `field.removeValue(index)` to remove items from an array field. You can conditionally show the remove button only when there's more than one item.

```tsx showLineNumbers title="form.tsx"
{
  field.state.value.length > 1 && (
    <InputGroupButton
      onClick={() => field.removeValue(index)}
      aria-label={`Remove email ${index + 1}`}
    >
      <XIcon />
    </InputGroupButton>
  )
}
```

### Array Validation

Validate array fields using Zod's array methods.

```tsx showLineNumbers title="form.tsx"
const formSchema = z.object({
  emails: z
    .array(
      z.object({
        address: z.string().email("Enter a valid email address."),
      })
    )
    .min(1, "Add at least one email address.")
    .max(5, "You can add up to 5 email addresses."),
})
```


---

<!-- SOURCE: apps/v4/content/docs/installation/astro.mdx -->

## apps/v4/content/docs/installation/astro.mdx

---
title: Astro
description: Install and configure shadcn/ui for Astro.
---

Choose the setup that matches your starting point.

<div className="mt-6 grid gap-4 sm:grid-cols-3 sm:gap-6">
  <LinkedCard
    href="#scaffold-with-create"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use shadcn/create</div>
    <div className="leading-relaxed text-muted-foreground">
      Build your preset and generate an Astro project command.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#scaffold-with-cli"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use the CLI</div>
    <div className="leading-relaxed text-muted-foreground">
      Scaffold a new Astro project directly from the terminal.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#existing-astro-project"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Existing Project</div>
    <div className="leading-relaxed text-muted-foreground">
      Configure shadcn/ui manually in an existing Astro project.
    </div>
  </LinkedCard>
</div>

<div id="scaffold-with-create" className="scroll-mt-24" />
## Use shadcn/create

<Steps>

### Build Your Preset

Open [shadcn/create](/create?template=astro) and build your preset visually. Choose your style, colors, fonts, icons, and more.

<Button asChild size="sm">
  <Link
    href="/create?template=astro"
    target="_blank"
    rel="noopener noreferrer"
    className="mt-6 no-underline!"
  >
    Open shadcn/create
  </Link>
</Button>

### Create Project

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```bash
npx shadcn@latest init --preset [CODE] --template astro
```

The exact command will include your selected options such as `--base`, `--monorepo`, or `--rtl`.

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```astro title="src/pages/index.astro" showLineNumbers
---
import Layout from "@/layouts/main.astro"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
---

<Layout>
  <Card className="max-w-sm">
    <CardHeader>
      <CardTitle>Project Overview</CardTitle>
      <CardDescription>
        Track progress and recent activity for your Astro app.
      </CardDescription>
    </CardHeader>
    <CardContent>
      Your design system is ready. Start building your next component.
    </CardContent>
  </Card>
</Layout>
```

If you created a monorepo, update `apps/web/src/pages/index.astro` and import from `@workspace/ui/components/card` instead. The monorepo layout at `apps/web/src/layouts/main.astro` already imports `@workspace/ui/globals.css` for you.

</Steps>

<div id="scaffold-with-cli" className="scroll-mt-24" />
## Use the CLI

<Steps>

### Create Project

Run the `init` command to scaffold a new Astro project. Follow the prompts to configure your project: base, preset, monorepo, and more.

```bash
npx shadcn@latest init -t astro
```

**For a monorepo project, use `--monorepo` flag:**

```bash
npx shadcn@latest init -t astro --monorepo
```

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```astro title="src/pages/index.astro" showLineNumbers
---
import Layout from "@/layouts/main.astro"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
---

<Layout>
  <Card className="max-w-sm">
    <CardHeader>
      <CardTitle>Project Overview</CardTitle>
      <CardDescription>
        Track progress and recent activity for your Astro app.
      </CardDescription>
    </CardHeader>
    <CardContent>
      Your design system is ready. Start building your next component.
    </CardContent>
  </Card>
</Layout>
```

If you created a monorepo, update `apps/web/src/pages/index.astro` and import from `@workspace/ui/components/card` instead. The monorepo layout at `apps/web/src/layouts/main.astro` already imports `@workspace/ui/globals.css` for you.

</Steps>

<div id="existing-astro-project" className="scroll-mt-24" />
## Existing Project

<Steps>

### Create Project

If you need a new Astro project, create one first. Otherwise, skip this step.

```bash
npm create astro@latest astro-app -- --template with-tailwindcss --install --add react --git
```

This command sets up Tailwind CSS and the React integration for you. If you're adding shadcn/ui to an older or custom Astro app, make sure both are configured before continuing.

The Tailwind starter loads your global stylesheet through `src/layouts/main.astro`. Keep that layout in place, or make sure your page imports `@/styles/global.css`.

### Edit tsconfig.json file

If your project already has the `@/*` alias configured, skip this step.

Add the following code to the `tsconfig.json` file to resolve paths:

```ts title="tsconfig.json" {4-9} showLineNumbers
{
  "compilerOptions": {
    // ...
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
    // ...
  }
}
```

### Run the CLI

Run the `shadcn` init command to set up your project:

```bash
npx shadcn@latest init
```

### Add Components

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```astro title="src/pages/index.astro" showLineNumbers
---
import Layout from "@/layouts/main.astro"
import { Button } from "@/components/ui/button"
---

<Layout>
  <div class="grid h-screen place-items-center content-center">
    <Button>Button</Button>
  </div>
</Layout>
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/gatsby.mdx -->

## apps/v4/content/docs/installation/gatsby.mdx

---
title: Gatsby
description: Install and configure shadcn/ui for Gatsby.
---

<Callout className="mb-6 border-blue-600 bg-blue-50 dark:border-blue-900 dark:bg-blue-950 [&_code]:bg-blue-100 dark:[&_code]:bg-blue-900">
  **Note:** This guide is for Gatsby with Tailwind CSS v3. For new projects, we
  recommend using one of the other frameworks that support Tailwind CSS v4.
</Callout>

<Steps>

### Create project

Start by creating a new Gatsby project using `create-gatsby`:

```bash
npm init gatsby
```

### Configure your Gatsby project to use TypeScript and Tailwind CSS

You will be asked a few questions to configure your project:

```txt showLineNumbers
✔ What would you like to call your site?
· your-app-name
✔ What would you like to name the folder where your site will be created?
· your-app-name
✔ Will you be using JavaScript or TypeScript?
· TypeScript
✔ Will you be using a CMS?
· Choose whatever you want
✔ Would you like to install a styling system?
· Tailwind CSS
✔ Would you like to install additional features with other plugins?
· Choose whatever you want
✔ Shall we do this? (Y/n) · Yes
```

### Edit tsconfig.json file

Add the following code to the `tsconfig.json` file to resolve paths:

```ts {4-9} showLineNumbers
{
  "compilerOptions": {
    // ...
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
    // ...
  }
}
```

### Create gatsby-node.ts file

Create a `gatsby-node.ts` file at the root of your project if it doesn’t already exist, and add the code below to the `gatsby-node` file so your app can resolve paths:

```ts
import * as path from "path"

export const onCreateWebpackConfig = ({ actions }) => {
  actions.setWebpackConfig({
    resolve: {
      alias: {
        "@/components": path.resolve(__dirname, "src/components"),
        "@/lib/utils": path.resolve(__dirname, "src/lib/utils"),
      },
    },
  })
}
```

### Run the CLI

Run the `shadcn` init command to set up your project:

```bash
npx shadcn@latest init
```

### That's it

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx {1,6} showLineNumbers
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/index.mdx -->

## apps/v4/content/docs/installation/index.mdx

---
title: Installation
description: How to install dependencies and structure your app.
---

<Callout className="mb-6 border-emerald-600 bg-emerald-100 dark:border-emerald-400 dark:bg-emerald-900">

**Recommended for new projects:** Use [shadcn/create](/create) to build your preset visually and generate the right setup command for your framework.

</Callout>

Choose the setup that matches your starting point.

<div className="mt-6 grid gap-4 sm:grid-cols-3 sm:gap-6">
  <LinkedCard
    href="#use-create"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use shadcn/create</div>
    <div className="leading-relaxed text-muted-foreground">
      Build your preset visually and generate a setup command.
    </div>
  </LinkedCard>
  <LinkedCard href="#use-cli" className="items-start gap-1 p-6 text-sm md:p-6">
    <div className="font-medium">Use the CLI</div>
    <div className="leading-relaxed text-muted-foreground">
      Scaffold a supported template directly from the terminal.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#existing-project"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Existing Project</div>
    <div className="leading-relaxed text-muted-foreground">
      Add shadcn/ui to an app you already created.
    </div>
  </LinkedCard>
</div>

<div id="use-create" className="scroll-mt-24" />
## Use shadcn/create

Build your preset visually, preview your choices, and generate a framework-specific setup command.

<Button asChild size="sm">
  <Link
    href="/create"
    target="_blank"
    rel="noopener noreferrer"
    className="mt-6 no-underline!"
  >
    Open shadcn/create
  </Link>
</Button>

Available for Next.js, Vite, Laravel, React Router, Astro, and TanStack Start.

<div id="use-cli" className="scroll-mt-24" />
## Use the CLI

Use the CLI to scaffold a new project directly from the terminal:

```bash
npx shadcn@latest init -t [framework]
```

Supported templates: `next`, `vite`, `start`, `react-router`, and `astro`.

For Laravel, create the app first with `laravel new`, then run `npx shadcn@latest init`.

<div id="existing-project" className="scroll-mt-24" />
## Existing Project

Each framework guide includes an `Existing Project` section with the manual setup steps for that framework.

Pick your framework below and follow that path.

## Choose Your Framework

For Laravel, start with `laravel new` before using `shadcn/create` or `shadcn init`.

<div className="mt-8 grid gap-4 sm:grid-cols-2 sm:gap-6">
  <LinkedCard href="/docs/installation/next">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Next.js</title>
      <path d="M11.5725 0c-.1763 0-.3098.0013-.3584.0067-.0516.0053-.2159.021-.3636.0328-3.4088.3073-6.6017 2.1463-8.624 4.9728C1.1004 6.584.3802 8.3666.1082 10.255c-.0962.659-.108.8537-.108 1.7474s.012 1.0884.108 1.7476c.652 4.506 3.8591 8.2919 8.2087 9.6945.7789.2511 1.6.4223 2.5337.5255.3636.04 1.9354.04 2.299 0 1.6117-.1783 2.9772-.577 4.3237-1.2643.2065-.1056.2464-.1337.2183-.1573-.0188-.0139-.8987-1.1938-1.9543-2.62l-1.919-2.592-2.4047-3.5583c-1.3231-1.9564-2.4117-3.556-2.4211-3.556-.0094-.0026-.0187 1.5787-.0235 3.509-.0067 3.3802-.0093 3.5162-.0516 3.596-.061.115-.108.1618-.2064.2134-.075.0374-.1408.0445-.495.0445h-.406l-.1078-.068a.4383.4383 0 01-.1572-.1712l-.0493-.1056.0053-4.703.0067-4.7054.0726-.0915c.0376-.0493.1174-.1125.1736-.143.0962-.047.1338-.0517.5396-.0517.4787 0 .5584.0187.6827.1547.0353.0377 1.3373 1.9987 2.895 4.3608a10760.433 10760.433 0 004.7344 7.1706l1.9002 2.8782.096-.0633c.8518-.5536 1.7525-1.3418 2.4657-2.1627 1.5179-1.7429 2.4963-3.868 2.8247-6.134.0961-.6591.1078-.854.1078-1.7475 0-.8937-.012-1.0884-.1078-1.7476-.6522-4.506-3.8592-8.2919-8.2087-9.6945-.7672-.2487-1.5836-.42-2.4985-.5232-.169-.0176-1.0835-.0366-1.6123-.037zm4.0685 7.217c.3473 0 .4082.0053.4857.047.1127.0562.204.1642.237.2767.0186.061.0234 1.3653.0186 4.3044l-.0067 4.2175-.7436-1.14-.7461-1.14v-3.066c0-1.982.0093-3.0963.0234-3.1502.0375-.1313.1196-.2346.2323-.2955.0961-.0494.1313-.054.4997-.054z" />
    </svg>
    <p className="mt-2 font-medium">Next.js</p>
  </LinkedCard>
  <LinkedCard href="/docs/installation/vite">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Vite</title>
      <path d="m8.286 10.578.512-8.657a.306.306 0 0 1 .247-.282L17.377.006a.306.306 0 0 1 .353.385l-1.558 5.403a.306.306 0 0 0 .352.385l2.388-.46a.306.306 0 0 1 .332.438l-6.79 13.55-.123.19a.294.294 0 0 1-.252.14c-.177 0-.35-.152-.305-.369l1.095-5.301a.306.306 0 0 0-.388-.355l-1.433.435a.306.306 0 0 1-.389-.354l.69-3.375a.306.306 0 0 0-.37-.36l-2.32.536a.306.306 0 0 1-.374-.316zm14.976-7.926L17.284 3.74l-.544 1.887 2.077-.4a.8.8 0 0 1 .84.369.8.8 0 0 1 .034.783L12.9 19.93l-.013.025-.015.023-.122.19a.801.801 0 0 1-.672.37.826.826 0 0 1-.634-.302.8.8 0 0 1-.16-.67l1.029-4.981-1.12.34a.81.81 0 0 1-.86-.262.802.802 0 0 1-.165-.67l.63-3.08-2.027.468a.808.808 0 0 1-.768-.233.81.81 0 0 1-.217-.6l.389-6.57-7.44-1.33a.612.612 0 0 0-.64.906L11.58 23.691a.612.612 0 0 0 1.066-.004l11.26-20.135a.612.612 0 0 0-.644-.9z" />
    </svg>
    <p className="mt-2 font-medium">Vite</p>
  </LinkedCard>

<LinkedCard href="/docs/installation/tanstack">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    className="h-10 w-10"
    fill="currentColor"
  >
    <path d="M6.93 13.688a.343.343 0 0 1 .468.132l.063.106c.48.851.98 1.66 1.5 2.426a35.65 35.65 0 0 0 2.074 2.742.345.345 0 0 1-.039.484l-.074.066c-2.543 2.223-4.191 2.665-4.953 1.333-.746-1.305-.477-3.672.808-7.11a.344.344 0 0 1 .153-.18ZM17.75 16.3a.34.34 0 0 1 .395.27l.02.1c.628 3.286.187 4.93-1.325 4.93-1.48 0-3.36-1.402-5.649-4.203a.327.327 0 0 1-.074-.222c0-.188.156-.34.344-.34h.121a32.984 32.984 0 0 0 2.809-.098c1.07-.086 2.191-.23 3.359-.437zm.871-6.977a.353.353 0 0 1 .445-.21l.102.034c3.262 1.11 4.504 2.332 3.719 3.664-.766 1.305-2.993 2.254-6.684 2.848a.362.362 0 0 1-.238-.047.343.343 0 0 1-.125-.476l.062-.106a34.07 34.07 0 0 0 1.367-2.523c.477-.989.93-2.051 1.352-3.184zM7.797 8.34a.362.362 0 0 1 .238.047.343.343 0 0 1 .125.476l-.062.106a34.088 34.088 0 0 0-1.367 2.523c-.477.988-.93 2.051-1.352 3.184a.353.353 0 0 1-.445.21l-.102-.034C1.57 13.742.328 12.52 1.113 11.188 1.88 9.883 4.106 8.934 7.797 8.34Zm5.281-3.984c2.543-2.223 4.192-2.664 4.953-1.332.746 1.304.477 3.671-.808 7.109a.344.344 0 0 1-.153.18.343.343 0 0 1-.468-.133l-.063-.106a34.64 34.64 0 0 0-1.5-2.426 35.65 35.65 0 0 0-2.074-2.742.345.345 0 0 1 .039-.484ZM7.285 2.274c1.48 0 3.364 1.402 5.649 4.203a.349.349 0 0 1 .078.218.348.348 0 0 1-.348.344l-.117-.004a34.584 34.584 0 0 0-2.809.102 35.54 35.54 0 0 0-3.363.437.343.343 0 0 1-.394-.273l-.02-.098c-.629-3.285-.188-4.93 1.324-4.93Zm2.871 5.812h3.688a.638.638 0 0 1 .55.316l1.848 3.22a.644.644 0 0 1 0 .628l-1.847 3.223a.638.638 0 0 1-.551.316h-3.688a.627.627 0 0 1-.547-.316L7.758 12.25a.644.644 0 0 1 0-.629L9.61 8.402a.627.627 0 0 1 .546-.316Zm3.23.793a.638.638 0 0 1 .552.316l1.39 2.426a.644.644 0 0 1 0 .629l-1.39 2.43a.638.638 0 0 1-.551.316h-2.774a.627.627 0 0 1-.546-.316l-1.395-2.43a.644.644 0 0 1 0-.629l1.395-2.426a.627.627 0 0 1 .546-.316Zm-.491.867h-1.79a.624.624 0 0 0-.546.316l-.899 1.56a.644.644 0 0 0 0 .628l.899 1.563a.632.632 0 0 0 .547.316h1.789a.632.632 0 0 0 .547-.316l.898-1.563a.644.644 0 0 0 0-.629l-.898-1.558a.624.624 0 0 0-.547-.317Zm-.477.828c.227 0 .438.121.547.317l.422.73a.625.625 0 0 1 0 .629l-.422.734a.627.627 0 0 1-.547.317h-.836a.632.632 0 0 1-.547-.317l-.422-.734a.625.625 0 0 1 0-.629l.422-.73a.632.632 0 0 1 .547-.317zm-.418.817a.548.548 0 0 0-.473.273.547.547 0 0 0 0 .547.544.544 0 0 0 .473.27.544.544 0 0 0 .473-.27.547.547 0 0 0 0-.547.548.548 0 0 0-.473-.273Zm-4.422.546h.98M18.98 7.75c.391-1.895.477-3.344.223-4.398-.148-.63-.422-1.137-.84-1.508-.441-.39-1-.582-1.625-.582-1.035 0-2.12.472-3.281 1.367a14.9 14.9 0 0 0-1.473 1.316 1.206 1.206 0 0 0-.136-.144c-1.446-1.285-2.66-2.082-3.7-2.39-.617-.184-1.195-.2-1.722-.024-.559.187-1.004.574-1.317 1.117-.515.894-.652 2.074-.46 3.527.078.59.214 1.235.402 1.934a1.119 1.119 0 0 0-.215.047C3.008 8.62 1.71 9.269.926 10.015c-.465.442-.77.938-.883 1.481-.113.578 0 1.156.312 1.7.516.894 1.465 1.597 2.817 2.155.543.223 1.156.426 1.844.61a1.023 1.023 0 0 0-.07.226c-.391 1.891-.477 3.344-.223 4.395.148.629.425 1.14.84 1.508.44.39 1 .582 1.625.582 1.035 0 2.12-.473 3.28-1.364.477-.37.973-.816 1.489-1.336a1.2 1.2 0 0 0 .195.227c1.446 1.285 2.66 2.082 3.7 2.39.617.184 1.195.2 1.722.024.559-.187 1.004-.574 1.317-1.117.515-.894.652-2.074.46-3.527a14.941 14.941 0 0 0-.425-2.012 1.225 1.225 0 0 0 .238-.047c1.828-.61 3.125-1.258 3.91-2.004.465-.441.77-.937.883-1.48.113-.578 0-1.157-.313-1.7-.515-.894-1.464-1.597-2.816-2.156a14.576 14.576 0 0 0-1.906-.625.865.865 0 0 0 .059-.195z" />
  </svg>
  <p className="mt-2 font-medium">TanStack Start</p>
</LinkedCard>
<LinkedCard href="/docs/installation/laravel">
  <svg
    role="img"
    viewBox="0 0 62 65"
    fill="currentColor"
    xmlns="http://www.w3.org/2000/svg"
    className="h-10 w-10"
  >
    <path d="M61.8548 14.6253C61.8778 14.7102 61.8895 14.7978 61.8897 14.8858V28.5615C61.8898 28.737 61.8434 28.9095 61.7554 29.0614C61.6675 29.2132 61.5409 29.3392 61.3887 29.4265L49.9104 36.0351V49.1337C49.9104 49.4902 49.7209 49.8192 49.4118 49.9987L25.4519 63.7916C25.3971 63.8227 25.3372 63.8427 25.2774 63.8639C25.255 63.8714 25.2338 63.8851 25.2101 63.8913C25.0426 63.9354 24.8666 63.9354 24.6991 63.8913C24.6716 63.8838 24.6467 63.8689 24.6205 63.8589C24.5657 63.8389 24.5084 63.8215 24.456 63.7916L0.501061 49.9987C0.348882 49.9113 0.222437 49.7853 0.134469 49.6334C0.0465019 49.4816 0.000120578 49.3092 0 49.1337L0 8.10652C0 8.01678 0.0124642 7.92953 0.0348998 7.84477C0.0423783 7.8161 0.0598282 7.78993 0.0697995 7.76126C0.0884958 7.70891 0.105946 7.65531 0.133367 7.6067C0.152063 7.5743 0.179485 7.54812 0.20192 7.51821C0.230588 7.47832 0.256763 7.43719 0.290416 7.40229C0.319084 7.37362 0.356476 7.35243 0.388883 7.32751C0.425029 7.29759 0.457436 7.26518 0.498568 7.2415L12.4779 0.345059C12.6296 0.257786 12.8015 0.211853 12.9765 0.211853C13.1515 0.211853 13.3234 0.257786 13.475 0.345059L25.4531 7.2415H25.4556C25.4955 7.26643 25.5292 7.29759 25.5653 7.32626C25.5977 7.35119 25.6339 7.37362 25.6625 7.40104C25.6974 7.43719 25.7224 7.47832 25.7523 7.51821C25.7735 7.54812 25.8021 7.5743 25.8196 7.6067C25.8483 7.65656 25.8645 7.70891 25.8844 7.76126C25.8944 7.78993 25.9118 7.8161 25.9193 7.84602C25.9423 7.93096 25.954 8.01853 25.9542 8.10652V33.7317L35.9355 27.9844V14.8846C35.9355 14.7973 35.948 14.7088 35.9704 14.6253C35.9792 14.5954 35.9954 14.5692 36.0053 14.5405C36.0253 14.4882 36.0427 14.4346 36.0702 14.386C36.0888 14.3536 36.1163 14.3274 36.1375 14.2975C36.1674 14.2576 36.1923 14.2165 36.2272 14.1816C36.2559 14.1529 36.292 14.1317 36.3244 14.1068C36.3618 14.0769 36.3942 14.0445 36.4341 14.0208L48.4147 7.12434C48.5663 7.03694 48.7383 6.99094 48.9133 6.99094C49.0883 6.99094 49.2602 7.03694 49.4118 7.12434L61.3899 14.0208C61.4323 14.0457 61.4647 14.0769 61.5021 14.1055C61.5333 14.1305 61.5694 14.1529 61.5981 14.1803C61.633 14.2165 61.6579 14.2576 61.6878 14.2975C61.7103 14.3274 61.7377 14.3536 61.7551 14.386C61.7838 14.4346 61.8 14.4882 61.8199 14.5405C61.8312 14.5692 61.8474 14.5954 61.8548 14.6253ZM59.893 27.9844V16.6121L55.7013 19.0252L49.9104 22.3593V33.7317L59.8942 27.9844H59.893ZM47.9149 48.5566V37.1768L42.2187 40.4299L25.953 49.7133V61.2003L47.9149 48.5566ZM1.99677 9.83281V48.5566L23.9562 61.199V49.7145L12.4841 43.2219L12.4804 43.2194L12.4754 43.2169C12.4368 43.1945 12.4044 43.1621 12.3682 43.1347C12.3371 43.1097 12.3009 43.0898 12.2735 43.0624L12.271 43.0586C12.2386 43.0275 12.2162 42.9888 12.1887 42.9539C12.1638 42.9203 12.1339 42.8916 12.114 42.8567L12.1127 42.853C12.0903 42.8156 12.0766 42.7707 12.0604 42.7283C12.0442 42.6909 12.023 42.656 12.013 42.6161C12.0005 42.5688 11.998 42.5177 11.9931 42.4691C11.9881 42.4317 11.9781 42.3943 11.9781 42.3569V15.5801L6.18848 12.2446L1.99677 9.83281ZM12.9777 2.36177L2.99764 8.10652L12.9752 13.8513L22.9541 8.10527L12.9752 2.36177H12.9777ZM18.1678 38.2138L23.9574 34.8809V9.83281L19.7657 12.2459L13.9749 15.5801V40.6281L18.1678 38.2138ZM48.9133 9.14105L38.9344 14.8858L48.9133 20.6305L58.8909 14.8846L48.9133 9.14105ZM47.9149 22.3593L42.124 19.0252L37.9323 16.6121V27.9844L43.7219 31.3174L47.9149 33.7317V22.3593ZM24.9533 47.987L39.59 39.631L46.9065 35.4555L36.9352 29.7145L25.4544 36.3242L14.9907 42.3482L24.9533 47.987Z" />
  </svg>
  <p className="mt-2 font-medium">Laravel</p>
</LinkedCard>
<LinkedCard href="/docs/installation/react-router">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    className="h-10 w-10"
    fill="currentColor"
  >
    <path d="M12.118 5.466a2.306 2.306 0 0 0-.623.08c-.278.067-.702.332-.953.583-.41.423-.49.609-.662 1.469-.08.423.41 1.43.847 1.734.45.317 1.085.502 2.065.608 1.429.16 1.84.636 1.84 2.197 0 1.377-.385 1.747-1.96 1.906-1.707.172-2.58.834-2.765 2.117-.106.781.41 1.76 1.125 2.091 1.627.768 3.15-.198 3.467-2.196.211-1.284.622-1.642 1.998-1.747 1.588-.133 2.409-.675 2.713-1.787.278-1.02-.304-2.157-1.297-2.554-.264-.106-.873-.238-1.35-.291-1.495-.16-1.879-.424-2.038-1.39-.225-1.337-.317-1.562-.794-2.09a2.174 2.174 0 0 0-1.613-.73zm-4.785 4.36a2.145 2.145 0 0 0-.497.048c-1.469.318-2.17 2.051-1.35 3.295 1.178 1.774 3.944.953 3.97-1.177.012-1.193-.98-2.143-2.123-2.166zM2.089 14.19a2.22 2.22 0 0 0-.427.052c-2.158.476-2.237 3.626-.106 4.182.53.145.582.145 1.111.013 1.191-.318 1.866-1.456 1.549-2.607-.278-1.02-1.144-1.664-2.127-1.64zm19.824.008c-.233.002-.477.058-.784.162-1.39.477-1.866 2.092-.98 3.336.557.794 1.96 1.058 2.82.516 1.416-.874 1.363-3.057-.093-3.746-.38-.186-.663-.271-.963-.268z" />
  </svg>
  <p className="mt-2 font-medium">React Router</p>
</LinkedCard>
<LinkedCard href="/docs/installation/astro">
  <svg
    role="img"
    viewBox="0 0 24 24"
    xmlns="http://www.w3.org/2000/svg"
    className="h-10 w-10"
    fill="currentColor"
  >
    <title>Astro</title>
    <path
      d="M16.074 16.86C15.354 17.476 13.917 17.895 12.262 17.895C10.23 17.895 8.527 17.263 8.075 16.412C7.914 16.9 7.877 17.458 7.877 17.814C7.877 17.814 7.771 19.564 8.988 20.782C8.988 20.15 9.501 19.637 10.133 19.637C11.216 19.637 11.215 20.582 11.214 21.349V21.418C11.214 22.582 11.925 23.579 12.937 24C12.7812 23.6794 12.7005 23.3275 12.701 22.971C12.701 21.861 13.353 21.448 14.111 20.968C14.713 20.585 15.383 20.161 15.844 19.308C16.0926 18.8493 16.2225 18.3357 16.222 17.814C16.2221 17.4903 16.1722 17.1685 16.074 16.86ZM15.551 0.6C15.747 0.844 15.847 1.172 16.047 1.829L20.415 16.176C18.7743 15.3246 17.0134 14.7284 15.193 14.408L12.35 4.8C12.3273 4.72337 12.2803 4.65616 12.2162 4.60844C12.152 4.56072 12.0742 4.53505 11.9943 4.53528C11.9143 4.5355 11.8366 4.56161 11.7727 4.60969C11.7089 4.65777 11.6623 4.72524 11.64 4.802L8.83 14.405C7.00149 14.724 5.23264 15.3213 3.585 16.176L7.974 1.827C8.174 1.171 8.274 0.843 8.471 0.6C8.64406 0.385433 8.86922 0.218799 9.125 0.116C9.415 0 9.757 0 10.443 0H13.578C14.264 0 14.608 0 14.898 0.117C15.1529 0.219851 15.3783 0.386105 15.551 0.6Z"
      fill="currentColor"
    />
  </svg>
  <p className="mt-2 font-medium">Astro</p>
</LinkedCard>
  <LinkedCard href="/docs/installation/manual">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>React</title>
      <path d="M14.23 12.004a2.236 2.236 0 0 1-2.235 2.236 2.236 2.236 0 0 1-2.236-2.236 2.236 2.236 0 0 1 2.235-2.236 2.236 2.236 0 0 1 2.236 2.236zm2.648-10.69c-1.346 0-3.107.96-4.888 2.622-1.78-1.653-3.542-2.602-4.887-2.602-.41 0-.783.093-1.106.278-1.375.793-1.683 3.264-.973 6.365C1.98 8.917 0 10.42 0 12.004c0 1.59 1.99 3.097 5.043 4.03-.704 3.113-.39 5.588.988 6.38.32.187.69.275 1.102.275 1.345 0 3.107-.96 4.888-2.624 1.78 1.654 3.542 2.603 4.887 2.603.41 0 .783-.09 1.106-.275 1.374-.792 1.683-3.263.973-6.365C22.02 15.096 24 13.59 24 12.004c0-1.59-1.99-3.097-5.043-4.032.704-3.11.39-5.587-.988-6.38-.318-.184-.688-.277-1.092-.278zm-.005 1.09v.006c.225 0 .406.044.558.127.666.382.955 1.835.73 3.704-.054.46-.142.945-.25 1.44-.96-.236-2.006-.417-3.107-.534-.66-.905-1.345-1.727-2.035-2.447 1.592-1.48 3.087-2.292 4.105-2.295zm-9.77.02c1.012 0 2.514.808 4.11 2.28-.686.72-1.37 1.537-2.02 2.442-1.107.117-2.154.298-3.113.538-.112-.49-.195-.964-.254-1.42-.23-1.868.054-3.32.714-3.707.19-.09.4-.127.563-.132zm4.882 3.05c.455.468.91.992 1.36 1.564-.44-.02-.89-.034-1.345-.034-.46 0-.915.01-1.36.034.44-.572.895-1.096 1.345-1.565zM12 8.1c.74 0 1.477.034 2.202.093.406.582.802 1.203 1.183 1.86.372.64.71 1.29 1.018 1.946-.308.655-.646 1.31-1.013 1.95-.38.66-.773 1.288-1.18 1.87-.728.063-1.466.098-2.21.098-.74 0-1.477-.035-2.202-.093-.406-.582-.802-1.204-1.183-1.86-.372-.64-.71-1.29-1.018-1.946.303-.657.646-1.313 1.013-1.954.38-.66.773-1.286 1.18-1.868.728-.064 1.466-.098 2.21-.098zm-3.635.254c-.24.377-.48.763-.704 1.16-.225.39-.435.782-.635 1.174-.265-.656-.49-1.31-.676-1.947.64-.15 1.315-.283 2.015-.386zm7.26 0c.695.103 1.365.23 2.006.387-.18.632-.405 1.282-.66 1.933-.2-.39-.41-.783-.64-1.174-.225-.392-.465-.774-.705-1.146zm3.063.675c.484.15.944.317 1.375.498 1.732.74 2.852 1.708 2.852 2.476-.005.768-1.125 1.74-2.857 2.475-.42.18-.88.342-1.355.493-.28-.958-.646-1.956-1.1-2.98.45-1.017.81-2.01 1.085-2.964zm-13.395.004c.278.96.645 1.957 1.1 2.98-.45 1.017-.812 2.01-1.086 2.964-.484-.15-.944-.318-1.37-.5-1.732-.737-2.852-1.706-2.852-2.474 0-.768 1.12-1.742 2.852-2.476.42-.18.88-.342 1.356-.494zm11.678 4.28c.265.657.49 1.312.676 1.948-.64.157-1.316.29-2.016.39.24-.375.48-.762.705-1.158.225-.39.435-.788.636-1.18zm-9.945.02c.2.392.41.783.64 1.175.23.39.465.772.705 1.143-.695-.102-1.365-.23-2.006-.386.18-.63.406-1.282.66-1.933zM17.92 16.32c.112.493.2.968.254 1.423.23 1.868-.054 3.32-.714 3.708-.147.09-.338.128-.563.128-1.012 0-2.514-.807-4.11-2.28.686-.72 1.37-1.536 2.02-2.44 1.107-.118 2.154-.3 3.113-.54zm-11.83.01c.96.234 2.006.415 3.107.532.66.905 1.345 1.727 2.035 2.446-1.595 1.483-3.092 2.295-4.11 2.295-.22-.005-.406-.05-.553-.132-.666-.38-.955-1.834-.73-3.703.054-.46.142-.944.25-1.438zm4.56.64c.44.02.89.034 1.345.034.46 0 .915-.01 1.36-.034-.44.572-.895 1.095-1.345 1.565-.455-.47-.91-.993-1.36-1.565z" />
    </svg>
    <p className="mt-2 font-medium">Manual</p>
  </LinkedCard>
</div>


---

<!-- SOURCE: apps/v4/content/docs/installation/laravel.mdx -->

## apps/v4/content/docs/installation/laravel.mdx

---
title: Laravel
description: Install and configure shadcn/ui for Laravel.
---

The shadcn CLI does not scaffold a new Laravel app. Start by creating a Laravel app with the React starter kit, then choose how you want to configure shadcn/ui.

<Steps>

### Create Project

Create a new Laravel app using the Laravel installer:

```bash
laravel new my-app
```

If you already have a Laravel app with React and Inertia configured, skip this step.

Choose the **React** starter kit when prompted. For more information, see the official [Laravel frontend documentation](https://laravel.com/docs/12.x/frontend).

Then move into your project directory:

```bash
cd my-app
```

</Steps>

<div className="mt-10 grid gap-4 sm:grid-cols-2 sm:gap-6">
  <LinkedCard
    href="#configure-with-create"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use shadcn/create</div>
    <div className="leading-relaxed text-muted-foreground">
      Build your preset visually and generate a Laravel init command.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#configure-with-cli"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use the CLI</div>
    <div className="leading-relaxed text-muted-foreground">
      Configure shadcn/ui in your Laravel app directly from the terminal.
    </div>
  </LinkedCard>
</div>

<div id="configure-with-create" className="scroll-mt-24" />
## Use shadcn/create

<Steps>

### Build Your Preset

Open [shadcn/create](/create?template=laravel) and build your preset visually. Choose your style, colors, fonts, icons, and more.

<Button asChild size="sm">
  <Link
    href="/create?template=laravel"
    target="_blank"
    rel="noopener noreferrer"
    className="mt-6 no-underline!"
  >
    Open shadcn/create
  </Link>
</Button>

### Run the Command

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```bash
npx shadcn@latest init --preset [CODE] --template laravel
```

Run the command from the root of your Laravel app.

When asked to overwrite `components.json` and components, choose `Yes`.

### Add Components

Add the `Switch` component to your project:

```bash
npx shadcn@latest add switch
```

The command above will add the `Switch` component to `resources/js/components/ui/switch.tsx`. You can then import it like this:

```tsx title="resources/js/pages/index.tsx" showLineNumbers {1,6}
import { Switch } from "@/components/ui/switch"

const MyPage = () => {
  return (
    <div>
      <Switch />
    </div>
  )
}

export default MyPage
```

</Steps>

<div id="configure-with-cli" className="scroll-mt-24" />
## Use the CLI

<Steps>

### Run the CLI

Run the `shadcn` init command from the root of your Laravel app:

```bash
npx shadcn@latest init
```

When asked to overwrite `components.json` and components, choose `Yes`.

### Add Components

Add the `Switch` component to your project:

```bash
npx shadcn@latest add switch
```

The command above will add the `Switch` component to `resources/js/components/ui/switch.tsx`. You can then import it like this:

```tsx title="resources/js/pages/index.tsx" showLineNumbers {1,6}
import { Switch } from "@/components/ui/switch"

const MyPage = () => {
  return (
    <div>
      <Switch />
    </div>
  )
}

export default MyPage
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/manual.mdx -->

## apps/v4/content/docs/installation/manual.mdx

---
title: Manual Installation
description: Add dependencies to your project manually.
---

<Steps>

### Add Tailwind CSS

Components are styled using Tailwind CSS. You need to install Tailwind CSS in your project.

[Follow the Tailwind CSS installation instructions to get started.](https://tailwindcss.com/docs/installation)

### Add dependencies

Add the following dependencies to your project:

```bash
npm install shadcn class-variance-authority clsx tailwind-merge lucide-react tw-animate-css
```

### Configure path aliases

Configure the path aliases in your `tsconfig.json` file.

```json {3-6} title="tsconfig.json" showLineNumbers
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

The `@` alias is a preference. You can use other aliases if you want.

### Configure styles

Add the following to your styles/globals.css file. You can learn more about using CSS variables for theming in the [theming section](/docs/theming).

<CodeCollapsibleWrapper>

```css showLineNumbers title="src/styles/globals.css"
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";

@custom-variant dark (&:is(.dark *));

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --radius-sm: calc(var(--radius) * 0.6);
  --radius-md: calc(var(--radius) * 0.8);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) * 1.4);
  --radius-2xl: calc(var(--radius) * 1.8);
  --radius-3xl: calc(var(--radius) * 2.2);
  --radius-4xl: calc(var(--radius) * 2.6);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
}

:root {
  --radius: 0.625rem;
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.145 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.145 0 0);
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
  --secondary: oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --accent: oklch(0.97 0 0);
  --accent-foreground: oklch(0.205 0 0);
  --destructive: oklch(0.577 0.245 27.325);
  --border: oklch(0.922 0 0);
  --input: oklch(0.922 0 0);
  --ring: oklch(0.708 0 0);
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-accent-foreground: oklch(0.205 0 0);
  --sidebar-border: oklch(0.922 0 0);
  --sidebar-ring: oklch(0.708 0 0);
}

.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  --card: oklch(0.205 0 0);
  --card-foreground: oklch(0.985 0 0);
  --popover: oklch(0.205 0 0);
  --popover-foreground: oklch(0.985 0 0);
  --primary: oklch(0.922 0 0);
  --primary-foreground: oklch(0.205 0 0);
  --secondary: oklch(0.269 0 0);
  --secondary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --accent: oklch(0.269 0 0);
  --accent-foreground: oklch(0.985 0 0);
  --destructive: oklch(0.704 0.191 22.216);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.556 0 0);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.556 0 0);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}
```

</CodeCollapsibleWrapper>

### Add a cn helper

```ts showLineNumbers title="lib/utils.ts"
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### Create a `components.json` file

Create a `components.json` file in the root of your project.

```json title="components.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "radix-nova",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/styles/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
```

### That's it

You can now start adding components to your project.

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/next.mdx -->

## apps/v4/content/docs/installation/next.mdx

---
title: Next.js
description: Install and configure shadcn/ui for Next.js.
---

Choose the setup that matches your starting point.

<div className="mt-6 grid gap-4 sm:grid-cols-3 sm:gap-6">
  <LinkedCard
    href="#scaffold-with-create"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use shadcn/create</div>
    <div className="leading-relaxed text-muted-foreground">
      Build your preset and generate a Next.js project command.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#scaffold-with-cli"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use the CLI</div>
    <div className="leading-relaxed text-muted-foreground">
      Scaffold a new Next.js project directly from the terminal.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#existing-next-project"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Existing Project</div>
    <div className="leading-relaxed text-muted-foreground">
      Configure shadcn/ui manually in an existing Next.js project.
    </div>
  </LinkedCard>
</div>

<div id="scaffold-with-create" className="scroll-mt-24" />
## Use shadcn/create

<Steps>

### Build Your Preset

Open [shadcn/create](/create?template=next) and build your preset visually. Choose your style, colors, fonts, icons, and more.

<Button asChild size="sm">
  <Link
    href="/create?template=next"
    target="_blank"
    rel="noopener noreferrer"
    className="mt-6 no-underline!"
  >
    Open shadcn/create
  </Link>
</Button>

### Create Project

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```bash
npx shadcn@latest init --preset [CODE] --template next
```

The exact command will include your selected options such as `--base`, `--monorepo`, or `--rtl`.

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="app/page.tsx"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export default function Home() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your Next.js app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/app/page.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="scaffold-with-cli" className="scroll-mt-24" />
## Use the CLI

<Steps>

### Create Project

Run the `init` command to scaffold a new Next.js project. Follow the prompts to configure your project: base, preset, monorepo, and more.

```bash
npx shadcn@latest init -t next
```

**For a monorepo project, use `--monorepo` flag:**

```bash
npx shadcn@latest init -t next --monorepo
```

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="app/page.tsx"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export default function Home() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your Next.js app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/app/page.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="existing-next-project" className="scroll-mt-24" />
## Existing Project

<Steps>

### Create Project

If you need a new Next.js project, create one with `create-next-app`. Otherwise, skip this step.

```bash
npx create-next-app@latest
```

Choose the recommended defaults so Tailwind CSS, the App Router, and the default `@/*` import alias are configured for you.

If you prefer a `src/` directory, use `--src-dir` or choose `Yes` when prompted:

```bash
npx create-next-app@latest --src-dir
```

With `--src-dir`, Next.js places your app in `src/app` and configures the `@/*` alias to point to `./src/*`.

### Configure Tailwind CSS and Import Aliases

If you created your project with the recommended `create-next-app` defaults, you can skip this step.

If you're adding shadcn/ui to an older or custom Next.js app, make sure Tailwind CSS is installed first. You can follow the official [Next.js installation guide](https://nextjs.org/docs/app/getting-started).

Then make sure your `tsconfig.json` includes the `@/*` import alias:

```json title="tsconfig.json" showLineNumbers
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

If you used `--src-dir`, point the alias to `./src/*` instead.

### Run the CLI

Run the `shadcn` init command to set up shadcn/ui in your project.

```bash
npx shadcn@latest init
```

### Add Components

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx showLineNumbers title="app/page.tsx"
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
    <div className="flex min-h-svh items-center justify-center">
      <Button>Click me</Button>
    </div>
  )
}
```

If you used `--src-dir`, add the component to `src/app/page.tsx` instead.

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/react-router.mdx -->

## apps/v4/content/docs/installation/react-router.mdx

---
title: React Router
description: Install and configure shadcn/ui for React Router.
---

Choose the setup that matches your starting point.

<div className="mt-6 grid gap-4 sm:grid-cols-3 sm:gap-6">
  <LinkedCard
    href="#scaffold-with-create"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use shadcn/create</div>
    <div className="leading-relaxed text-muted-foreground">
      Build your preset and generate a React Router project.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#scaffold-with-cli"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use the CLI</div>
    <div className="leading-relaxed text-muted-foreground">
      Scaffold a new React Router project directly from the terminal.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#existing-react-router-project"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Existing Project</div>
    <div className="leading-relaxed text-muted-foreground">
      Configure shadcn/ui manually in an existing React Router project.
    </div>
  </LinkedCard>
</div>

<div id="scaffold-with-create" className="scroll-mt-24" />
## Use shadcn/create

<Steps>

### Build Your Preset

Open [shadcn/create](/create?template=react-router) and build your preset visually. Choose your style, colors, fonts, icons, and more.

<Button asChild size="sm">
  <Link
    href="/create?template=react-router"
    target="_blank"
    rel="noopener noreferrer"
    className="mt-6 no-underline!"
  >
    Open shadcn/create
  </Link>
</Button>

### Create Project

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```bash
npx shadcn@latest init --preset [CODE] --template react-router
```

The exact command will include your selected options such as `--base`, `--monorepo`, or `--rtl`.

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="app/routes/home.tsx"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card"

export default function Home() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your React Router app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/app/routes/home.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="scaffold-with-cli" className="scroll-mt-24" />
## Use the CLI

<Steps>

### Create Project

Run the `init` command to scaffold a new React Router project. Follow the prompts to configure your project: base, preset, monorepo, and more.

```bash
npx shadcn@latest init -t react-router
```

**For a monorepo project, use `--monorepo` flag:**

```bash
npx shadcn@latest init -t react-router --monorepo
```

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="app/routes/home.tsx"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card"

export default function Home() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your React Router app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/app/routes/home.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="existing-react-router-project" className="scroll-mt-24" />
## Existing Project

<Steps>

### Create Project

If you need a new React Router project, create one first. Otherwise, skip this step.

```bash
npm create react-router@latest
```

`create-react-router` already configures Tailwind CSS and the default `~/*` import alias for you. If you're adding shadcn/ui to an older or custom React Router app, make sure both are configured before continuing.

### Run the CLI

Run the `shadcn` init command to set up shadcn/ui in your project.

```bash
npx shadcn@latest init
```

### Add Components

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx showLineNumbers title="app/routes/home.tsx"
import { Button } from "~/components/ui/button"

export default function Home() {
  return (
    <div className="flex min-h-svh flex-col items-center justify-center">
      <Button>Click me</Button>
    </div>
  )
}
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/remix.mdx -->

## apps/v4/content/docs/installation/remix.mdx

---
title: Remix
description: Install and configure shadcn/ui for Remix.
---

<Callout>

**Note:** This guide is for Remix. For React Router, see the [React Router](/docs/installation/react-router) guide.

</Callout>

<Steps>

### Create project

Start by creating a new Remix project using `create-remix`:

```bash
npx create-remix@latest my-app
```

### Run the CLI

Run the `shadcn` init command to set up your project:

```bash
npx shadcn@latest init
```

### That's it

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx {1,6} showLineNumbers title="app/routes/index.tsx"
import { Button } from "~/components/ui/button"

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/tanstack-router.mdx -->

## apps/v4/content/docs/installation/tanstack-router.mdx

---
title: TanStack Router
description: Install and configure shadcn/ui for TanStack Router.
---

<Steps>

### Create project

Start by creating a new TanStack Router project:

```bash
npx create-tsrouter-app@latest my-app --template file-router --tailwind --add-ons shadcn
```

### Add Components

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx title="src/routes/index.tsx" showLineNumbers {3,12}
import { createFileRoute } from "@tanstack/react-router"

import { Button } from "@/components/ui/button"

export const Route = createFileRoute("/")({
  component: App,
})

function App() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/tanstack.mdx -->

## apps/v4/content/docs/installation/tanstack.mdx

---
title: TanStack Start
description: Install and configure shadcn/ui for TanStack Start.
---

Choose the setup that matches your starting point.

<div className="mt-6 grid gap-4 sm:grid-cols-3 sm:gap-6">
  <LinkedCard
    href="#scaffold-with-create"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use shadcn/create</div>
    <div className="leading-relaxed text-muted-foreground">
      Build your preset and generate a TanStack project command.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#scaffold-with-cli"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use the CLI</div>
    <div className="leading-relaxed text-muted-foreground">
      Scaffold a new TanStack project from the terminal.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#existing-start-project"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Existing Project</div>
    <div className="leading-relaxed text-muted-foreground">
      Configure shadcn/ui manually in an existing TanStack project.
    </div>
  </LinkedCard>
</div>

<div id="scaffold-with-create" className="scroll-mt-24" />
## Use shadcn/create

<Steps>

### Build Your Preset

Open [shadcn/create](/create?template=start) and build your preset visually. Choose your style, colors, fonts, icons, and more.

<Button asChild size="sm">
  <Link
    href="/create?template=start"
    target="_blank"
    rel="noopener noreferrer"
    className="mt-6 no-underline!"
  >
    Open shadcn/create
  </Link>
</Button>

### Create Project

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```bash
npx shadcn@latest init --preset [CODE] --template start
```

The exact command will include your selected options such as `--base`, `--monorepo`, or `--rtl`.

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="src/routes/index.tsx"
import { createFileRoute } from "@tanstack/react-router"

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export const Route = createFileRoute("/")({
  component: App,
})

function App() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your TanStack Start app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/src/routes/index.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="scaffold-with-cli" className="scroll-mt-24" />
## Use the CLI

<Steps>

### Create Project

Run the `init` command to scaffold a new TanStack Start project. Follow the prompts to configure your project: base, preset, monorepo, and more.

```bash
npx shadcn@latest init -t start
```

**For a monorepo project, use `--monorepo` flag:**

```bash
npx shadcn@latest init -t start --monorepo
```

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="src/routes/index.tsx"
import { createFileRoute } from "@tanstack/react-router"

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export const Route = createFileRoute("/")({
  component: App,
})

function App() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your TanStack Start app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}
```

If you created a monorepo, update `apps/web/src/routes/index.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="existing-start-project" className="scroll-mt-24" />
## Existing Project

<Steps>

### Create Project

If you need a new TanStack Start project, create one first. Otherwise, skip this step.

```bash
npx @tanstack/cli@latest create
```

Choose TanStack Start, the React framework, and the recommended defaults so Tailwind CSS and the `@/*` import alias are configured for you.

<Callout className="mt-6">

Do not add the `shadcn` add-on when prompted. The `shadcn` CLI will configure shadcn/ui later in this guide.

</Callout>

The TanStack CLI already configures Tailwind CSS and the default `@/*` import alias for you. If you're adding shadcn/ui to an older or custom TanStack Start app, make sure both are configured before continuing.

### Run the CLI

Run the `shadcn` init command to set up shadcn/ui in your project.

```bash
npx shadcn@latest init
```

### Add Components

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx showLineNumbers title="src/routes/index.tsx"
import { createFileRoute } from "@tanstack/react-router"

import { Button } from "@/components/ui/button"

export const Route = createFileRoute("/")({
  component: App,
})

function App() {
  return (
    <div className="flex min-h-svh items-center justify-center p-6">
      <Button>Click me</Button>
    </div>
  )
}
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/installation/vite.mdx -->

## apps/v4/content/docs/installation/vite.mdx

---
title: Vite
description: Install and configure shadcn/ui for Vite.
---

Choose the setup that matches your starting point.

<div className="mt-6 grid gap-4 sm:grid-cols-3 sm:gap-6">
  <LinkedCard
    href="#scaffold-with-create"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use shadcn/create</div>
    <div className="leading-relaxed text-muted-foreground">
      Build your preset and generate a Vite project command.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#scaffold-with-cli"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Use the CLI</div>
    <div className="leading-relaxed text-muted-foreground">
      Scaffold a new Vite project directly from the terminal.
    </div>
  </LinkedCard>
  <LinkedCard
    href="#existing-vite-project"
    className="items-start gap-1 p-6 text-sm md:p-6"
  >
    <div className="font-medium">Existing Project</div>
    <div className="leading-relaxed text-muted-foreground">
      Configure shadcn/ui manually in an existing Vite project.
    </div>
  </LinkedCard>
</div>

<div id="scaffold-with-create" className="scroll-mt-24" />
## Use shadcn/create

<Steps>

### Build Your Preset

Open [shadcn/create](/create?template=vite) and build your preset visually. Choose your style, colors, fonts, icons, and more.

<Button asChild size="sm">
  <Link
    href="/create?template=vite"
    target="_blank"
    rel="noopener noreferrer"
    className="mt-6 no-underline!"
  >
    Open shadcn/create
  </Link>
</Button>

### Create Project

Click `Create Project`, choose your package manager, and copy the generated command.

The generated command will look similar to this:

```bash
npx shadcn@latest init --preset [CODE] --template vite
```

The exact command will include your selected options such as `--base`, `--monorepo`, or `--rtl`.

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="src/App.tsx"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

function App() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your Vite app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}

export default App
```

If you created a monorepo, update `apps/web/src/App.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="scaffold-with-cli" className="scroll-mt-24" />
## Use the CLI

<Steps>

### Create Project

Run the `init` command to scaffold a new Vite project. Follow the prompts to configure your project: base, preset, monorepo, and more.

```bash
npx shadcn@latest init -t vite
```

**For a monorepo project, use `--monorepo` flag:**

```bash
npx shadcn@latest init -t vite --monorepo
```

### Add Components

Add the `Card` component to your project:

```bash
npx shadcn@latest add card
```

If you created a monorepo, run the command from `apps/web` or specify the workspace from the repo root:

```bash
npx shadcn@latest add card -c apps/web
```

The command above will add the `Card` component to your project. You can then import it like this:

```tsx showLineNumbers title="src/App.tsx"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

function App() {
  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>Project Overview</CardTitle>
        <CardDescription>
          Track progress and recent activity for your Vite app.
        </CardDescription>
      </CardHeader>
      <CardContent>
        Your design system is ready. Start building your next component.
      </CardContent>
    </Card>
  )
}

export default App
```

If you created a monorepo, update `apps/web/src/App.tsx` and import from `@workspace/ui/components/card` instead.

</Steps>

<div id="existing-vite-project" className="scroll-mt-24" />
## Existing Project

<Steps>

### Create Project

If you need a new Vite project, create one first and select the **React + TypeScript** template. Otherwise, skip this step.

```bash
npm create vite@latest
```

### Add Tailwind CSS

If your project already has Tailwind CSS configured, skip this step.

```bash
npm install tailwindcss @tailwindcss/vite
```

Replace everything in `src/index.css` with the following:

```css title="src/index.css"
@import "tailwindcss";
```

### Edit tsconfig.json file

If your project already has the `@/*` alias configured, skip this step.

Vite splits TypeScript configuration across multiple files. Add the `baseUrl` and `paths` properties to the `compilerOptions` section of `tsconfig.json` and `tsconfig.app.json`:

```ts title="tsconfig.json" {11-16} showLineNumbers
{
  "files": [],
  "references": [
    {
      "path": "./tsconfig.app.json"
    },
    {
      "path": "./tsconfig.node.json"
    }
  ],
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

### Edit tsconfig.app.json file

Add the same alias to `tsconfig.app.json` so your editor can resolve imports:

```ts title="tsconfig.app.json" {4-9} showLineNumbers
{
  "compilerOptions": {
    // ...
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
    // ...
  }
}
```

### Update vite.config.ts

Install `@types/node` and update `vite.config.ts` so Vite can resolve the `@` alias:

```bash
npm install -D @types/node
```

```typescript title="vite.config.ts" showLineNumbers {1,2,8-13}
import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})
```

### Run the CLI

Run the `shadcn` init command to set up shadcn/ui in your project:

```bash
npx shadcn@latest init
```

### Add Components

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx showLineNumbers title="src/App.tsx"
import { Button } from "@/components/ui/button"

function App() {
  return (
    <div className="flex min-h-svh flex-col items-center justify-center">
      <Button>Click me</Button>
    </div>
  )
}

export default App
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/registry/authentication.mdx -->

## apps/v4/content/docs/registry/authentication.mdx

---
title: Authentication
description: Secure your registry with authentication for private and personalized components.
---

Authentication lets you run private registries, control who can access your components, and give different teams or users different content. This guide shows common authentication patterns and how to set them up.

Authentication enables these use cases:

- **Private Components**: Keep your business logic and internal components secure
- **Team-Specific Resources**: Give different teams different components
- **Access Control**: Limit who can see sensitive or experimental components
- **Usage Analytics**: See who's using which components in your organization
- **Licensing**: Control who gets premium or licensed components

## Common Authentication Patterns

### Token-Based Authentication

The most common approach uses Bearer tokens or API keys:

```json title="components.json"
{
  "registries": {
    "@private": {
      "url": "https://registry.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

Set your token in environment variables:

```bash title=".env.local"
REGISTRY_TOKEN=your_secret_token_here
```

### API Key Authentication

Some registries use API keys in headers:

```json title="components.json"
{
  "registries": {
    "@company": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "X-API-Key": "${API_KEY}",
        "X-Workspace-Id": "${WORKSPACE_ID}"
      }
    }
  }
}
```

### Query Parameter Authentication

For simpler setups, use query parameters:

```json title="components.json"
{
  "registries": {
    "@internal": {
      "url": "https://registry.company.com/{name}.json",
      "params": {
        "token": "${ACCESS_TOKEN}"
      }
    }
  }
}
```

This creates: `https://registry.company.com/button.json?token=your_token`

## Server-Side Implementation

Here's how to add authentication to your registry server:

### Next.js API Route Example

```typescript title="app/api/registry/[name]/route.ts"
import { NextRequest, NextResponse } from "next/server"

export async function GET(
  request: NextRequest,
  { params }: { params: { name: string } }
) {
  // Get token from Authorization header.
  const authHeader = request.headers.get("authorization")
  const token = authHeader?.replace("Bearer ", "")

  // Or from query parameters.
  const queryToken = request.nextUrl.searchParams.get("token")

  // Check if token is valid.
  if (!isValidToken(token || queryToken)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  // Check if token can access this component.
  if (!hasAccessToComponent(token, params.name)) {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 })
  }

  // Return the component.
  const component = await getComponent(params.name)
  return NextResponse.json(component)
}

function isValidToken(token: string | null) {
  // Add your token validation logic here.
  // Check against database, JWT validation, etc.
  return token === process.env.VALID_TOKEN
}

function hasAccessToComponent(token: string, componentName: string) {
  // Add role-based access control here.
  // Check if token can access specific component.
  return true // Your logic here.
}
```

### Express.js Example

```javascript title="server.js"
app.get("/registry/:name.json", (req, res) => {
  const token = req.headers.authorization?.replace("Bearer ", "")

  if (!isValidToken(token)) {
    return res.status(401).json({ error: "Unauthorized" })
  }

  const component = getComponent(req.params.name)
  if (!component) {
    return res.status(404).json({ error: "Component not found" })
  }

  res.json(component)
})
```

## Advanced Authentication Patterns

### Team-Based Access

Give different teams different components:

```typescript title="api/registry/route.ts"
async function GET(request: NextRequest) {
  const token = extractToken(request)
  const team = await getTeamFromToken(token)

  // Get components for this team.
  const components = await getComponentsForTeam(team)
  return NextResponse.json(components)
}
```

### User-Personalized Registries

Give users components based on their preferences:

```typescript
async function GET(request: NextRequest) {
  const user = await authenticateUser(request)

  // Get user's style and framework preferences.
  const preferences = await getUserPreferences(user.id)

  // Get personalized component version.
  const component = await getPersonalizedComponent(params.name, preferences)

  return NextResponse.json(component)
}
```

### Temporary Access Tokens

Use expiring tokens for better security:

```typescript
interface TemporaryToken {
  token: string
  expiresAt: Date
  scope: string[]
}

async function validateTemporaryToken(token: string) {
  const tokenData = await getTokenData(token)

  if (!tokenData) return false
  if (new Date() > tokenData.expiresAt) return false

  return true
}
```

## Multi-Registry Authentication

With [namespaced registries](/docs/registry/namespace), you can set up multiple registries with different authentication:

```json title="components.json"
{
  "registries": {
    "@public": "https://public.company.com/{name}.json",
    "@internal": {
      "url": "https://internal.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${INTERNAL_TOKEN}"
      }
    },
    "@premium": {
      "url": "https://premium.company.com/{name}.json",
      "headers": {
        "X-License-Key": "${LICENSE_KEY}"
      }
    }
  }
}
```

This lets you:

- Mix public and private registries
- Use different authentication per registry
- Organize components by access level

## Security Best Practices

### Use Environment Variables

Never commit tokens to version control. Always use environment variables:

```bash title=".env.local"
REGISTRY_TOKEN=your_secret_token_here
API_KEY=your_api_key_here
```

Then reference them in `components.json`:

```json
{
  "registries": {
    "@private": {
      "url": "https://registry.company.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

### Use HTTPS

Always use HTTPS URLs for registries to protect your tokens in transit:

```json
{
  "@secure": "https://registry.company.com/{name}.json" // ✅
  "@insecure": "http://registry.company.com/{name}.json" // ❌
}
```

### Add Rate Limiting

Protect your registry from abuse:

```typescript
import rateLimit from "express-rate-limit"

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
})

app.use("/registry", limiter)
```

### Rotate Tokens

Change access tokens regularly:

```typescript
// Create new token with expiration.
function generateToken() {
  const token = crypto.randomBytes(32).toString("hex")
  const expiresAt = new Date(Date.now() + 30 * 24 * 60 * 60 * 1000) // 30 days.

  return { token, expiresAt }
}
```

### Log Access

Track registry access for security and analytics:

```typescript
async function logAccess(request: Request, component: string, userId: string) {
  await db.accessLog.create({
    timestamp: new Date(),
    userId,
    component,
    ip: request.ip,
    userAgent: request.headers["user-agent"],
  })
}
```

## Testing Authentication

Test your authenticated registry locally:

```bash
# Test with curl.
curl -H "Authorization: Bearer your_token" \
  https://registry.company.com/button.json

# Test with the CLI.
REGISTRY_TOKEN=your_token npx shadcn@latest add @private/button
```

## Error Handling

The shadcn CLI handles authentication errors gracefully:

- **401 Unauthorized**: Token is invalid or missing
- **403 Forbidden**: Token lacks permission for this resource
- **429 Too Many Requests**: Rate limit exceeded

### Custom Error Messages

Your registry server can return custom error messages in the response body, and the CLI will display them to users:

```typescript
// Registry server returns custom error
return NextResponse.json(
  {
    error: "Unauthorized",
    message:
      "Your subscription has expired. Please renew at company.com/billing",
  },
  { status: 403 }
)
```

The user will see:

```txt
Your subscription has expired. Please renew at company.com/billing
```

This helps provide context-specific guidance:

```typescript
// Different error messages for different scenarios
if (!token) {
  return NextResponse.json(
    {
      error: "Unauthorized",
      message:
        "Authentication required. Set REGISTRY_TOKEN in your .env.local file",
    },
    { status: 401 }
  )
}

if (isExpiredToken(token)) {
  return NextResponse.json(
    {
      error: "Unauthorized",
      message: "Token expired. Request a new token at company.com/tokens",
    },
    { status: 401 }
  )
}

if (!hasTeamAccess(token, component)) {
  return NextResponse.json(
    {
      error: "Forbidden",
      message: `Component '${component}' is restricted to the Design team`,
    },
    { status: 403 }
  )
}
```

## Next Steps

To set up authentication with multiple registries and advanced patterns, see the [Namespaced Registries](/docs/registry/namespace) documentation. It covers:

- Setting up multiple authenticated registries
- Using different authentication per namespace
- Cross-registry dependency resolution
- Advanced authentication patterns


---

<!-- SOURCE: apps/v4/content/docs/registry/examples.mdx -->

## apps/v4/content/docs/registry/examples.mdx

---
title: Examples
description: "Examples of registry items: styles, components, css vars, etc."
---

## registry:style

### Custom style that extends shadcn/ui

The following registry item is a custom style that extends shadcn/ui. On `npx shadcn init`, it will:

- Install `@tabler/icons-react` as a dependency.
- Add the `login-01` block and `calendar` component to the project.
- Add the `editor` from a remote registry.
- Set the `font-sans` variable to `Inter, sans-serif`.
- Install a `brand` color in light and dark mode.

```json title="example-style.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "example-style",
  "type": "registry:style",
  "dependencies": ["@tabler/icons-react"],
  "registryDependencies": [
    "login-01",
    "calendar",
    "https://example.com/r/editor.json"
  ],
  "cssVars": {
    "theme": {
      "font-sans": "Inter, sans-serif"
    },
    "light": {
      "brand": "20 14.3% 4.1%"
    },
    "dark": {
      "brand": "20 14.3% 4.1%"
    }
  }
}
```

### Custom style from scratch

The following registry item is a custom style that doesn't extend shadcn/ui. See the `extends: none` field.

It can be used to create a new style from scratch, i.e. custom components, css vars, dependencies, etc.

On `npx shadcn add`, the following will:

- Install `tailwind-merge` and `clsx` as dependencies.
- Add the `utils` registry item from the shadcn/ui registry.
- Add the `button`, `input`, `label`, and `select` components from a remote registry.
- Install new css vars: `main`, `bg`, `border`, `text`, `ring`.

```json title="example-style.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "extends": "none",
  "name": "new-style",
  "type": "registry:style",
  "dependencies": ["tailwind-merge", "clsx"],
  "registryDependencies": [
    "utils",
    "https://example.com/r/button.json",
    "https://example.com/r/input.json",
    "https://example.com/r/label.json",
    "https://example.com/r/select.json"
  ],
  "cssVars": {
    "theme": {
      "font-sans": "Inter, sans-serif"
    },
    "light": {
      "main": "#88aaee",
      "bg": "#dfe5f2",
      "border": "#000",
      "text": "#000",
      "ring": "#000"
    },
    "dark": {
      "main": "#88aaee",
      "bg": "#272933",
      "border": "#000",
      "text": "#e6e6e6",
      "ring": "#fff"
    }
  }
}
```

## registry:theme

### Custom theme

```json title="example-theme.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "light": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.546 0.245 262.881)",
      "primary-foreground": "oklch(0.97 0.014 254.604)",
      "ring": "oklch(0.746 0.16 232.661)",
      "sidebar-primary": "oklch(0.546 0.245 262.881)",
      "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
      "sidebar-ring": "oklch(0.746 0.16 232.661)"
    },
    "dark": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.707 0.165 254.624)",
      "primary-foreground": "oklch(0.97 0.014 254.604)",
      "ring": "oklch(0.707 0.165 254.624)",
      "sidebar-primary": "oklch(0.707 0.165 254.624)",
      "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
      "sidebar-ring": "oklch(0.707 0.165 254.624)"
    }
  }
}
```

### Custom colors

The following style will init using shadcn/ui defaults and then add a custom `brand` color.

```json title="example-style.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-style",
  "type": "registry:style",
  "cssVars": {
    "light": {
      "brand": "oklch(0.99 0.00 0)"
    },
    "dark": {
      "brand": "oklch(0.14 0.00 286)"
    }
  }
}
```

## registry:block

### Custom block

This block installs the `login-01` block from the shadcn/ui registry.

```json title="login-01.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "login-01",
  "type": "registry:block",
  "description": "A simple login form.",
  "registryDependencies": ["button", "card", "input", "label"],
  "files": [
    {
      "path": "blocks/login-01/page.tsx",
      "content": "import { LoginForm } ...",
      "type": "registry:page",
      "target": "app/login/page.tsx"
    },
    {
      "path": "blocks/login-01/components/login-form.tsx",
      "content": "...",
      "type": "registry:component"
    }
  ]
}
```

### Install a block and override primitives

You can install a block from the shadcn/ui registry and override the primitives using your custom ones.

On `npx shadcn add`, the following will:

- Add the `login-01` block from the shadcn/ui registry.
- Override the `button`, `input`, and `label` primitives with the ones from the remote registry.

```json title="example-style.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-login",
  "type": "registry:block",
  "registryDependencies": [
    "login-01",
    "https://example.com/r/button.json",
    "https://example.com/r/input.json",
    "https://example.com/r/label.json"
  ]
}
```

## registry:ui

### UI component

A `registry:ui` item is a reusable UI component. It can have dependencies, registry dependencies, and CSS variables.

```json title="button.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "button",
  "type": "registry:ui",
  "dependencies": ["radix-ui"],
  "files": [
    {
      "path": "ui/button.tsx",
      "content": "...",
      "type": "registry:ui"
    }
  ]
}
```

### UI component with CSS variables

```json title="sidebar.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "sidebar",
  "type": "registry:ui",
  "dependencies": ["radix-ui"],
  "registryDependencies": ["button", "separator", "sheet", "tooltip"],
  "files": [
    {
      "path": "ui/sidebar.tsx",
      "content": "...",
      "type": "registry:ui"
    }
  ],
  "cssVars": {
    "light": {
      "sidebar-background": "oklch(0.985 0 0)",
      "sidebar-foreground": "oklch(0.141 0.005 285.823)",
      "sidebar-border": "oklch(0.92 0.004 286.32)"
    },
    "dark": {
      "sidebar-background": "oklch(0.141 0.005 285.823)",
      "sidebar-foreground": "oklch(0.985 0 0)",
      "sidebar-border": "oklch(0.274 0.006 286.033)"
    }
  }
}
```

## registry:lib

### Utility library

A `registry:lib` item is a utility library. Use it to share helper functions, constants, or other non-component code.

```json title="utils.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "utils",
  "type": "registry:lib",
  "dependencies": ["clsx", "tailwind-merge"],
  "files": [
    {
      "path": "lib/utils.ts",
      "content": "import { clsx, type ClassValue } from \"clsx\"\nimport { twMerge } from \"tailwind-merge\"\n\nexport function cn(...inputs: ClassValue[]) {\n  return twMerge(clsx(inputs))\n}",
      "type": "registry:lib"
    }
  ]
}
```

## registry:hook

### Custom hook

A `registry:hook` item is a custom React hook.

```json title="use-mobile.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "use-mobile",
  "type": "registry:hook",
  "files": [
    {
      "path": "hooks/use-mobile.ts",
      "content": "...",
      "type": "registry:hook"
    }
  ]
}
```

### Hook with dependencies

```json title="use-debounce.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "use-debounce",
  "type": "registry:hook",
  "dependencies": ["react"],
  "files": [
    {
      "path": "hooks/use-debounce.ts",
      "content": "...",
      "type": "registry:hook"
    }
  ]
}
```

## registry:font

### Custom font

A `registry:font` item installs a Google Font. The `font` field is required and configures the font family, provider, import name, and CSS variable.

```json title="font-inter.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "font-inter",
  "type": "registry:font",
  "font": {
    "family": "'Inter Variable', sans-serif",
    "provider": "google",
    "import": "Inter",
    "variable": "--font-sans",
    "subsets": ["latin"],
    "dependency": "@fontsource-variable/inter"
  }
}
```

### Monospace font

```json title="font-jetbrains-mono.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "font-jetbrains-mono",
  "type": "registry:font",
  "font": {
    "family": "'JetBrains Mono Variable', monospace",
    "provider": "google",
    "import": "JetBrains_Mono",
    "variable": "--font-mono",
    "weight": ["400", "500", "600", "700"],
    "subsets": ["latin"],
    "dependency": "@fontsource-variable/jetbrains-mono"
  }
}
```

### Serif font

```json title="font-lora.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "font-lora",
  "type": "registry:font",
  "font": {
    "family": "'Lora Variable', serif",
    "provider": "google",
    "import": "Lora",
    "variable": "--font-serif",
    "subsets": ["latin"],
    "dependency": "@fontsource-variable/lora"
  }
}
```

### Font with custom selector

Use the `selector` field to apply a font to specific CSS selectors instead of globally on `html`. This is useful for heading fonts or other targeted font applications.

```json title="font-playfair-display.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "font-playfair-display",
  "type": "registry:font",
  "font": {
    "family": "'Playfair Display Variable', serif",
    "provider": "google",
    "import": "Playfair_Display",
    "variable": "--font-heading",
    "subsets": ["latin"],
    "selector": "h1, h2, h3, h4, h5, h6",
    "dependency": "@fontsource-variable/playfair-display"
  }
}
```

When `selector` is set, the font utility class (e.g. `font-heading`) is applied via CSS `@apply` on the specified selector within `@layer base`, instead of being added to the `<html>` element. The CSS variable is still injected on `<html>` so it's available globally.

## registry:base

### Custom base

A `registry:base` item is a complete design system base. It defines the full set of dependencies, CSS variables, and configuration for a project. The `config` field is unique to `registry:base` items.

The `config` field accepts the following properties (all optional):

| Property             | Type                                                                         | Description                                                     |
| -------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `style`              | `string`                                                                     | The style name for the base.                                    |
| `iconLibrary`        | `string`                                                                     | The icon library to use (e.g. `lucide`).                        |
| `rsc`                | `boolean`                                                                    | Whether to enable React Server Components. Defaults to `false`. |
| `tsx`                | `boolean`                                                                    | Whether to use TypeScript. Defaults to `true`.                  |
| `rtl`                | `boolean`                                                                    | Whether to enable right-to-left support. Defaults to `false`.   |
| `menuColor`          | `"default" \| "inverted" \| "default-translucent" \| "inverted-translucent"` | The menu color scheme. Defaults to `"default"`.                 |
| `menuAccent`         | `"subtle" \| "bold"`                                                         | The menu accent style. Defaults to `"subtle"`.                  |
| `tailwind.baseColor` | `string`                                                                     | The base color name (e.g. `neutral`, `slate`, `zinc`).          |
| `tailwind.css`       | `string`                                                                     | Path to the Tailwind CSS file.                                  |
| `tailwind.prefix`    | `string`                                                                     | A prefix to add to all Tailwind classes.                        |
| `aliases.components` | `string`                                                                     | Import alias for components.                                    |
| `aliases.utils`      | `string`                                                                     | Import alias for utilities.                                     |
| `aliases.ui`         | `string`                                                                     | Import alias for UI components.                                 |
| `aliases.lib`        | `string`                                                                     | Import alias for lib.                                           |
| `aliases.hooks`      | `string`                                                                     | Import alias for hooks.                                         |
| `registries`         | `Record<string, string \| object>`                                           | Custom registry URLs. Keys must start with `@`.                 |

```json title="custom-base.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-base",
  "type": "registry:base",
  "config": {
    "style": "custom-base",
    "iconLibrary": "lucide",
    "tailwind": {
      "baseColor": "neutral"
    }
  },
  "dependencies": [
    "class-variance-authority",
    "tw-animate-css",
    "lucide-react"
  ],
  "registryDependencies": ["utils", "font-inter"],
  "cssVars": {
    "light": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.21 0.006 285.885)",
      "primary-foreground": "oklch(0.985 0 0)"
    },
    "dark": {
      "background": "oklch(0.141 0.005 285.823)",
      "foreground": "oklch(0.985 0 0)",
      "primary": "oklch(0.985 0 0)",
      "primary-foreground": "oklch(0.21 0.006 285.885)"
    }
  },
  "css": {
    "@import \"tw-animate-css\"": {},
    "@layer base": {
      "*": {
        "@apply border-border outline-ring/50": {}
      },
      "body": {
        "@apply bg-background text-foreground": {}
      }
    }
  }
}
```

### Base from scratch

Use `extends: none` to create a base that doesn't extend shadcn/ui defaults.

```json title="custom-base.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "my-design-system",
  "extends": "none",
  "type": "registry:base",
  "config": {
    "style": "my-design-system",
    "iconLibrary": "lucide",
    "tailwind": {
      "baseColor": "slate"
    }
  },
  "dependencies": ["tailwind-merge", "clsx", "tw-animate-css", "lucide-react"],
  "registryDependencies": ["utils", "font-geist"],
  "cssVars": {
    "light": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)"
    },
    "dark": {
      "background": "oklch(0.141 0.005 285.823)",
      "foreground": "oklch(0.985 0 0)"
    }
  }
}
```

## Common Fields

### Author

Use the `author` field to add attribution to your registry items.

```json title="example-item.json" showLineNumbers {5}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:ui",
  "author": "shadcn",
  "files": [
    {
      "path": "ui/custom-component.tsx",
      "content": "...",
      "type": "registry:ui"
    }
  ]
}
```

### Dev dependencies

Use the `devDependencies` field to install packages as dev dependencies.

```json title="example-item.json" showLineNumbers {5}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-item",
  "type": "registry:item",
  "devDependencies": ["@types/mdx"],
  "files": [
    {
      "path": "lib/mdx.ts",
      "content": "...",
      "type": "registry:lib"
    }
  ]
}
```

### Metadata

Use the `meta` field to attach arbitrary metadata to your registry items. This can be used to store custom data that your tools or scripts can use.

```json title="example-item.json" showLineNumbers {5-8}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:ui",
  "meta": {
    "category": "forms",
    "version": "2.0.0"
  },
  "files": [
    {
      "path": "ui/custom-component.tsx",
      "content": "...",
      "type": "registry:ui"
    }
  ]
}
```

## CSS Variables

### Custom Theme Variables

Add custom theme variables to the `theme` object.

```json title="example-theme.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "theme": {
      "font-heading": "Inter, sans-serif",
      "shadow-card": "0 0 0 1px rgba(0, 0, 0, 0.1)"
    }
  }
}
```

### Override Tailwind CSS variables

```json title="example-theme.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "theme": {
      "spacing": "0.2rem",
      "breakpoint-sm": "640px",
      "breakpoint-md": "768px",
      "breakpoint-lg": "1024px",
      "breakpoint-xl": "1280px",
      "breakpoint-2xl": "1536px"
    }
  }
}
```

## Add custom CSS

### Base styles

```json title="example-base.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-style",
  "type": "registry:style",
  "css": {
    "@layer base": {
      "h1": {
        "font-size": "var(--text-2xl)"
      },
      "h2": {
        "font-size": "var(--text-xl)"
      }
    }
  }
}
```

### Components

```json title="example-card.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-card",
  "type": "registry:component",
  "css": {
    "@layer components": {
      "card": {
        "background-color": "var(--color-white)",
        "border-radius": "var(--rounded-lg)",
        "padding": "var(--spacing-6)",
        "box-shadow": "var(--shadow-xl)"
      }
    }
  }
}
```

## Add custom utilities

### Simple utility

```json title="example-component.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "css": {
    "@utility content-auto": {
      "content-visibility": "auto"
    }
  }
}
```

### Complex utility

```json title="example-utility.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "css": {
    "@utility scrollbar-hidden": {
      "scrollbar-hidden": {
        "&::-webkit-scrollbar": {
          "display": "none"
        }
      }
    }
  }
}
```

### Functional utilities

```json title="example-functional.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "css": {
    "@utility tab-*": {
      "tab-size": "var(--tab-size-*)"
    }
  }
}
```

## Add CSS imports

Use `@import` to add CSS imports to your registry item. The imports will be placed at the top of the CSS file.

### Basic import

```json title="example-import.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-import",
  "type": "registry:component",
  "css": {
    "@import \"tailwindcss\"": {},
    "@import \"./styles/base.css\"": {}
  }
}
```

### Import with url() syntax

```json title="example-url-import.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "font-import",
  "type": "registry:item",
  "css": {
    "@import url(\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap\")": {},
    "@import url('./local-styles.css')": {}
  }
}
```

### Import with media queries

```json title="example-media-import.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "responsive-import",
  "type": "registry:item",
  "css": {
    "@import \"print-styles.css\" print": {},
    "@import url(\"mobile.css\") screen and (max-width: 768px)": {}
  }
}
```

## Add custom plugins

Use `@plugin` to add Tailwind plugins to your registry item. Plugins will be automatically placed after imports and before other content.

**Important:** When using plugins from npm packages, you must also add them to the `dependencies` array.

### Basic plugin usage

```json title="example-plugin.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-plugin",
  "type": "registry:item",
  "css": {
    "@plugin \"@tailwindcss/typography\"": {},
    "@plugin \"foo\"": {}
  }
}
```

### Plugin with npm dependency

When using plugins from npm packages like `@tailwindcss/typography`, include them in the dependencies.

```json title="example-typography.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "typography-component",
  "type": "registry:item",
  "dependencies": ["@tailwindcss/typography"],
  "css": {
    "@plugin \"@tailwindcss/typography\"": {},
    "@layer components": {
      ".prose": {
        "max-width": "65ch"
      }
    }
  }
}
```

### Scoped and file-based plugins

```json title="example-scoped-plugin.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "scoped-plugins",
  "type": "registry:component",
  "css": {
    "@plugin \"@headlessui/tailwindcss\"": {},
    "@plugin \"tailwindcss/plugin\"": {},
    "@plugin \"./custom-plugin.js\"": {}
  }
}
```

### Multiple plugins with automatic ordering

When you add multiple plugins, they are automatically grouped together and deduplicated.

```json title="example-multiple-plugins.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "multiple-plugins",
  "type": "registry:item",
  "dependencies": [
    "@tailwindcss/typography",
    "@tailwindcss/forms",
    "tw-animate-css"
  ],
  "css": {
    "@plugin \"@tailwindcss/typography\"": {},
    "@plugin \"@tailwindcss/forms\"": {},
    "@plugin \"tw-animate-css\"": {}
  }
}
```

## Combined imports and plugins

When using both `@import` and `@plugin` directives, imports are placed first, followed by plugins, then other CSS content.

```json title="example-combined.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "combined-example",
  "type": "registry:item",
  "dependencies": ["@tailwindcss/typography", "tw-animate-css"],
  "css": {
    "@import \"tailwindcss\"": {},
    "@import url(\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap\")": {},
    "@plugin \"@tailwindcss/typography\"": {},
    "@plugin \"tw-animate-css\"": {},
    "@layer base": {
      "body": {
        "font-family": "Inter, sans-serif"
      }
    },
    "@utility content-auto": {
      "content-visibility": "auto"
    }
  }
}
```

## Add custom animations

Note: you need to define both `@keyframes` in css and `theme` in cssVars to use animations.

```json title="example-component.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "cssVars": {
    "theme": {
      "--animate-wiggle": "wiggle 1s ease-in-out infinite"
    }
  },
  "css": {
    "@keyframes wiggle": {
      "0%, 100%": {
        "transform": "rotate(-3deg)"
      },
      "50%": {
        "transform": "rotate(3deg)"
      }
    }
  }
}
```

## Add environment variables

You can add environment variables using the `envVars` field.

```json title="example-item.json" showLineNumbers {5-9}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-item",
  "type": "registry:item",
  "envVars": {
    "NEXT_PUBLIC_APP_URL": "http://localhost:4000",
    "DATABASE_URL": "postgresql://postgres:postgres@localhost:5432/postgres",
    "OPENAI_API_KEY": ""
  }
}
```

Environment variables are added to the `.env.local` or `.env` file. Existing variables are not overwritten.

<Callout>

**IMPORTANT:** Use `envVars` to add development or example variables. Do NOT use it to add production variables.

</Callout>

## Universal Items

As of `2.9.0`, you can create universal items that can be installed without framework detection or components.json.

To make an item universal i.e framework agnostic, all the files in the item must have an explicit target.

Here's an example of a registry item that installs custom Cursor rules for _python_:

```json title=".cursor/rules/custom-python.mdc" showLineNumbers {9}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "python-rules",
  "type": "registry:item",
  "files": [
    {
      "path": "/path/to/your/registry/default/custom-python.mdc",
      "type": "registry:file",
      "target": "~/.cursor/rules/custom-python.mdc",
      "content": "..."
    }
  ]
}
```

Here's another example for installing a custom ESLint config:

```json title=".eslintrc.json" showLineNumbers {9}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "my-eslint-config",
  "type": "registry:item",
  "files": [
    {
      "path": "/path/to/your/registry/default/custom-eslint.json",
      "type": "registry:file",
      "target": "~/.eslintrc.json",
      "content": "..."
    }
  ]
}
```

You can also have a universal item that installs multiple files:

```json title="my-custom-starter-template.json" showLineNumbers {9}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "my-custom-starter-template",
  "type": "registry:item",
  "dependencies": ["better-auth"],
  "files": [
    {
      "path": "/path/to/file-01.json",
      "type": "registry:file",
      "target": "~/file-01.json",
      "content": "..."
    },
    {
      "path": "/path/to/file-02.vue",
      "type": "registry:file",
      "target": "~/pages/file-02.vue",
      "content": "..."
    }
  ]
}
```


---

<!-- SOURCE: apps/v4/content/docs/registry/faq.mdx -->

## apps/v4/content/docs/registry/faq.mdx

---
title: FAQ
description: Frequently asked questions about running a registry.
---

## Frequently asked questions

### What does a complex component look like?

Here's an example of a complex component that installs a page, two components, a hook, a format-date utils and a config file.

```json showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "title": "Hello World",
  "type": "registry:block",
  "description": "A complex hello world component",
  "files": [
    {
      "path": "registry/new-york/hello-world/page.tsx",
      "type": "registry:page",
      "target": "app/hello/page.tsx"
    },
    {
      "path": "registry/new-york/hello-world/components/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/components/formatted-message.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/hooks/use-hello.ts",
      "type": "registry:hook"
    },
    {
      "path": "registry/new-york/hello-world/lib/format-date.ts",
      "type": "registry:lib"
    },
    {
      "path": "registry/new-york/hello-world/hello.config.ts",
      "type": "registry:file",
      "target": "~/hello.config.ts"
    }
  ]
}
```

### How do I add a new Tailwind color?

To add a new color you need to add it to `cssVars` under `light` and `dark` keys.

```json showLineNumbers {10-18}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "title": "Hello World",
  "type": "registry:block",
  "description": "A complex hello world component",
  "files": [
    // ...
  ],
  "cssVars": {
    "light": {
      "brand-background": "oklch(0.205 0.015 18)",
      "brand-accent": "oklch(0.205 0.015 18)"
    },
    "dark": {
      "brand-background": "oklch(0.205 0.015 18)",
      "brand-accent": "oklch(0.205 0.015 18)"
    }
  }
}
```

The CLI will update the project CSS file. Once updated, the new colors will be available to be used as utility classes: `bg-brand` and `text-brand-accent`.

### How do I add or override a Tailwind theme variable?

To add or override a theme variable you add it to `cssVars.theme` under the key you want to add or override.

```json showLineNumbers {10-15}
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "title": "Hello World",
  "type": "registry:block",
  "description": "A complex hello world component",
  "files": [
    // ...
  ],
  "cssVars": {
    "theme": {
      "text-base": "3rem",
      "ease-in-out": "cubic-bezier(0.4, 0, 0.2, 1)",
      "font-heading": "Poppins, sans-serif"
    }
  }
}
```


---

<!-- SOURCE: apps/v4/content/docs/registry/getting-started.mdx -->

## apps/v4/content/docs/registry/getting-started.mdx

---
title: Getting Started
description: Learn how to get setup and run your own component registry.
---

This guide will walk you through the process of setting up your own component registry. It assumes you already have a project with components and would like to turn it into a registry.

If you're starting a new registry project, you can use the [registry template](https://github.com/shadcn-ui/registry-template) as a starting point. We have already configured it for you.

## Requirements

You are free to design and host your custom registry as you see fit. The only requirement is that your registry items must be valid JSON files that conform to the [registry-item schema specification](/docs/registry/registry-item-json).

If you'd like to see an example of a registry, we have a [template project](https://github.com/shadcn-ui/registry-template) for you to use as a starting point.

## registry.json

The `registry.json` is the entry point for the registry. It contains the registry's name, homepage, and defines all the items present in the registry.

Your registry must have this file (or JSON payload) present at the root of the registry endpoint. The registry endpoint is the URL where your registry is hosted.

The `shadcn` CLI will automatically generate this file for you when you run the `build` command.

## Add a registry.json file

Create a `registry.json` file in the root of your project. Your project can be a Next.js, Vite, Vue, Svelte, PHP or any other framework as long as it supports serving JSON over HTTP.

```json title="registry.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    // ...
  ]
}
```

This `registry.json` file must conform to the [registry schema specification](/docs/registry/registry-json).

## Add a registry item

### Create your component

Add your first component. Here's an example of a simple `<HelloWorld />` component:

```tsx title="registry/new-york/hello-world/hello-world.tsx" showLineNumbers
import { Button } from "@/components/ui/button"

export function HelloWorld() {
  return <Button>Hello World</Button>
}
```

<Callout className="mt-6">
  **Note:** This example places the component in the `registry/new-york`
  directory. You can place it anywhere in your project as long as you set the
  correct path in the `registry.json` file and you follow the `registry/[NAME]`
  directory structure.
</Callout>

```txt
registry
└── new-york
    └── hello-world
        └── hello-world.tsx
```

### Add your component to the registry

To add your component to the registry, you need to add your component definition to `registry.json`.

```json title="registry.json" showLineNumbers {6-17}
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "files": [
        {
          "path": "registry/new-york/hello-world/hello-world.tsx",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

You define your registry item by adding a `name`, `type`, `title`, `description` and `files`.

For every file you add, you must specify the `path` and `type` of the file. The `path` is the relative path to the file from the root of your project. The `type` is the type of the file.

You can read more about the registry item schema and file types in the [registry item schema docs](/docs/registry/registry-item-json).

## Build your registry

### Install the shadcn CLI

```bash
npm install shadcn@latest
```

### Add a build script

Add a `registry:build` script to your `package.json` file.

```json title="package.json" showLineNumbers
{
  "scripts": {
    "registry:build": "shadcn build"
  }
}
```

### Run the build script

Run the build script to generate the registry JSON files.

```bash
npm run registry:build
```

<Callout className="mt-6">
  **Note:** By default, the build script will generate the registry JSON files
  in `public/r` e.g `public/r/hello-world.json`.

You can change the output directory by passing the `--output` option. See the [shadcn build command](/docs/cli#build) for more information.

</Callout>

## Serve your registry

If you're running your registry on Next.js, you can now serve your registry by running the `next` server. The command might differ for other frameworks.

```bash
npm run dev
```

Your files will now be served at `http://localhost:3000/r/[NAME].json` eg. `http://localhost:3000/r/hello-world.json`.

## Publish your registry

To make your registry available to other developers, you can publish it by deploying your project to a public URL.

## Guidelines

Here are some guidelines to follow when building components for a registry.

- Place your registry item in the `registry/[STYLE]/[NAME]` directory. I'm using `new-york` as an example. It can be anything you want as long as it's nested under the `registry` directory.
- The following properties are required for the block definition: `name`, `description`, `type` and `files`.
- It is recommended to add a proper name and description to your registry item. This helps LLMs understand the component and its purpose.
- Make sure to list all registry dependencies in `registryDependencies`. A registry dependency is the name of the component in the registry eg. `input`, `button`, `card`, etc or a URL to a registry item eg. `http://localhost:3000/r/editor.json`.
- Make sure to list all dependencies in `dependencies`. A dependency is the name of the package in the registry eg. `zod`, `sonner`, etc. To set a version, you can use the `name@version` format eg. `zod@^3.20.0`.
- **Imports should always use the `@/registry` path.** eg. `import { HelloWorld } from "@/registry/new-york/hello-world/hello-world"`
- Ideally, place your files within a registry item in `components`, `hooks`, `lib` directories.

## Install using the CLI

To install a registry item using the `shadcn` CLI, use the `add` command followed by the URL of the registry item.

```bash
npx shadcn@latest add http://localhost:3000/r/hello-world.json
```

See the [Namespaced
Registries](/docs/registry/namespace) docs for more information on
how to install registry items from a namespaced registry.


---

<!-- SOURCE: apps/v4/content/docs/registry/index.mdx -->

## apps/v4/content/docs/registry/index.mdx

---
title: Introduction
description: Run your own code registry.
---

You can use the `shadcn` CLI to run your own code registry. Running your own registry allows you to distribute your custom components, hooks, pages, config, rules and other files to any project.

<Callout>
  **Note:** The registry works with any project type and any framework, and is
  not limited to React.
</Callout>

<figure className="flex flex-col gap-4">
  <Image
    src="/images/registry-light.png"
    width="1432"
    height="960"
    alt="Registry"
    className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
  />
  <Image
    src="/images/registry-dark.png"
    width="1432"
    height="960"
    alt="Registry"
    className="mt-6 hidden w-full overflow-hidden rounded-lg border shadow-sm dark:block"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A distribution system for code
  </figcaption>
</figure>

Ready to create your own registry? In the next section, we'll walk you through setting up your own custom registry step-by-step, from creating your first component to publishing it for others to use.

<div className="mt-6 grid gap-4 sm:grid-cols-2">
  <LinkedCard href="/docs/registry/getting-started" className="items-start text-sm md:p-6">
    <div className="font-medium">Getting Started</div>
    <div className="text-muted-foreground">
      Set up and build your own registry
    </div>
  </LinkedCard>

<LinkedCard
  href="/docs/registry/authentication"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Authentication</div>
  <div className="text-muted-foreground">
    Secure your registry with authentication
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/namespace"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Namespaces</div>
  <div className="text-muted-foreground">
    Configure registries with namespaces
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/examples"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Examples</div>
  <div className="text-muted-foreground">
    Registry item examples and configurations
  </div>
</LinkedCard>
  <LinkedCard
    href="/docs/registry/registry-json"
    className="items-start text-sm md:p-6"
  >
    <div className="font-medium">Schema</div>
    <div className="text-muted-foreground">
      Schema specification for registry.json
    </div>
  </LinkedCard>
</div>


---

<!-- SOURCE: apps/v4/content/docs/registry/mcp.mdx -->

## apps/v4/content/docs/registry/mcp.mdx

---
title: MCP Server
description: MCP support for registry developers
---

The [shadcn MCP server](/docs/mcp) works out of the box with any shadcn-compatible registry. You do not need to do anything special to enable MCP support for your registry.

---

## Prerequisites

The MCP server works by requesting your registry index. Make sure you have a registry item file at the root of your registry named `registry`.

For example, if your registry is hosted at `https://acme.com/r/[name].json`, you should have a file at `https://acme.com/r/registry.json` or `https://acme.com/r/registry` if you're using a JSON file extension.

This file must be a valid JSON file that conforms to the [registry schema](/docs/registry/registry-json).

---

## Configuring MCP

Ask your registry consumers to configure your registry in their `components.json` file and install the shadcn MCP server:

<Tabs defaultValue="claude">
  <TabsList>
    <TabsTrigger value="claude">Claude Code</TabsTrigger>
    <TabsTrigger value="cursor">Cursor</TabsTrigger>
    <TabsTrigger value="vscode">VS Code</TabsTrigger>
    <TabsTrigger value="codex">Codex</TabsTrigger>
    <TabsTrigger value="opencode">OpenCode</TabsTrigger>
  </TabsList>
  <TabsContent value="claude" className="mt-4">
    **Configure your registry** in your `components.json` file:

    ```json title="components.json" showLineNumbers
    {
      "registries": {
        "@acme": "https://acme.com/r/{name}.json"
      }
    }
    ```

    **Run the following command** in your project:

    ```bash
    npx shadcn@latest mcp init --client claude
    ```

    **Restart Claude Code** and try the following prompts:
       - Show me the components in the acme registry
       - Create a landing page using items from the acme registry

    **Note:** You can use `/mcp` command in Claude Code to debug the MCP server.

  </TabsContent>

  <TabsContent value="cursor" className="mt-4">
    **Configure your registry** in your `components.json` file:

    ```json title="components.json" showLineNumbers
    {
      "registries": {
        "@acme": "https://acme.com/r/{name}.json"
      }
    }
    ```
    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client cursor
       ```

    Open **Cursor Settings** and **Enable the MCP server** for shadcn. Then try the following prompts:
       - Show me the components in the acme registry
       - Create a landing page using items from the acme registry

  </TabsContent>

  <TabsContent value="vscode" className="mt-4">
    **Configure your registry** in your `components.json` file:

    ```json title="components.json" showLineNumbers
    {
      "registries": {
        "@acme": "https://acme.com/r/{name}.json"
      }
    }
    ```
    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client vscode
       ```

    Open `.vscode/mcp.json` and click **Start** next to the shadcn server. Then try the following prompts with GitHub Copilot:
       - Show me the components in the acme registry
       - Create a landing page using items from the acme registry

  </TabsContent>

  <TabsContent value="codex" className="mt-4">
    **Configure your registry** in your `components.json` file:

    ```json title="components.json" showLineNumbers
    {
      "registries": {
        "@acme": "https://acme.com/r/{name}.json"
      }
    }
    ```

    **Add the following configuration** to `~/.codex/config.toml`:
       ```toml
       [mcp_servers.shadcn]
       command = "npx"
       args = ["shadcn@latest", "mcp"]
       ```

    **Restart Codex** and try the following prompts:
       - Show me the components in the acme registry
       - Create a landing page using items from the acme registry

  </TabsContent>

  <TabsContent value="opencode" className="mt-4">
    **Configure your registry** in your `components.json` file:

    ```json title="components.json" showLineNumbers
    {
      "registries": {
        "@acme": "https://acme.com/r/{name}.json"
      }
    }
    ```

    **Run the following command** in your project:
       ```bash
       npx shadcn@latest mcp init --client opencode
       ```

    **Restart OpenCode** and try the following prompts:
       - Show me the components in the acme registry
       - Create a landing page using items from the acme registry

  </TabsContent>
</Tabs>

You can read more about the MCP server in the [MCP documentation](/docs/mcp).

---

## Best Practices

Here are some best practices for MCP-compatible registries:

1. **Clear Descriptions**: Add concise, informative descriptions that help AI assistants understand what a registry item is for and how to use it.
2. **Proper Dependencies**: List all `dependencies` accurately so MCP can install them automatically.
3. **Registry Dependencies**: Use `registryDependencies` to indicate relationships between items.
4. **Consistent Naming**: Use kebab-case for component names and maintain consistency across your registry.


---

<!-- SOURCE: apps/v4/content/docs/registry/namespace.mdx -->

## apps/v4/content/docs/registry/namespace.mdx

---
title: Namespaces
description: Configure and use multiple resource registries with namespace support.
---

Namespaced registries let you configure multiple resource sources in one project. This means you can install components, libraries, utilities, AI prompts, configuration files, and other resources from various registries, whether they're public, third-party, or your own custom private libraries.

## Table of Contents

- [Overview](#overview)
- [Decentralized Namespace System](#decentralized-namespace-system)
- [Getting Started](#getting-started)
- [Registry Naming Convention](#registry-naming-convention)
- [Configuration](#configuration)
- [Authentication & Security](#authentication--security)
- [Versioning](#versioning)
- [Dependency Resolution](#dependency-resolution)
- [Built-in Registries](#built-in-registries)
- [CLI Commands](#cli-commands)
- [Error Handling](#error-handling)
- [Creating Your Own Registry](#creating-your-own-registry)
- [Example Configurations](#example-configurations)
- [Technical Details](#technical-details)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Overview

Registry namespaces are prefixed with `@` and provide a way to organize and reference resources from different sources. Resources can be any type of content: components, libraries, utilities, hooks, AI prompts, configuration files, themes, and more. For example:

- `@shadcn/button` - UI component from the shadcn registry
- `@v0/dashboard` - Dashboard component from the v0 registry
- `@ai-elements/input` - AI prompt input from an AI elements registry
- `@acme/auth-utils` - Authentication utilities from your company's private registry
- `@ai/chatbot-rules` - AI prompt rules from an AI resources registry
- `@themes/dark-mode` - Theme configuration from a themes registry

---

## Decentralized Namespace System

We intentionally designed the namespace system to be decentralized. There is a [central open source registry index](/docs/registry/registry-index) for open source namespaces but you are free to create and use any namespace you want.

This decentralized approach gives you complete flexibility to organize your resources however makes sense for your organization.

You can create multiple registries for different purposes:

```json title="components.json" showLineNumbers
{
  "registries": {
    "@acme-ui": "https://registry.acme.com/ui/{name}.json",
    "@acme-docs": "https://registry.acme.com/docs/{name}.json",
    "@acme-ai": "https://registry.acme.com/ai/{name}.json",
    "@acme-themes": "https://registry.acme.com/themes/{name}.json",
    "@acme-internal": {
      "url": "https://internal.acme.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${INTERNAL_TOKEN}"
      }
    }
  }
}
```

This allows you to:

- **Organize by type**: Separate UI components, documentation, AI resources, etc.
- **Organize by team**: Different teams can maintain their own registries
- **Organize by visibility**: Public vs. private resources
- **Organize by version**: Stable vs. experimental registries
- **No naming conflicts**: Since there's no central authority, you don't need to worry about namespace collisions

### Examples of Multi-Registry Setups

#### By Resource Type

```json title="components.json" showLineNumbers
{
  "@components": "https://cdn.company.com/components/{name}.json",
  "@hooks": "https://cdn.company.com/hooks/{name}.json",
  "@utils": "https://cdn.company.com/utils/{name}.json",
  "@prompts": "https://cdn.company.com/ai-prompts/{name}.json"
}
```

#### By Team or Department

```json title="components.json" showLineNumbers
{
  "@design": "https://create.company.com/registry/{name}.json",
  "@engineering": "https://eng.company.com/registry/{name}.json",
  "@marketing": "https://marketing.company.com/registry/{name}.json"
}
```

#### By Stability

```json title="components.json" showLineNumbers
{
  "@stable": "https://registry.company.com/stable/{name}.json",
  "@latest": "https://registry.company.com/beta/{name}.json",
  "@experimental": "https://registry.company.com/experimental/{name}.json"
}
```

---

## Getting Started

### Installing Resources

Once configured, you can install resources using the namespace syntax:

```bash
npx shadcn@latest add @v0/dashboard
```

or multiple resources at once:

```bash
npx shadcn@latest add @acme/header @lib/auth-utils @ai/chatbot-rules
```

### Quick Configuration

Add registries to your `components.json`:

```json title="components.json"
{
  "registries": {
    "@v0": "https://v0.dev/chat/b/{name}",
    "@acme": "https://registry.acme.com/resources/{name}.json"
  }
}
```

Then start installing:

```bash
npx shadcn@latest add @acme/button
```

---

## Registry Naming Convention

Registry names must follow these rules:

- Start with `@` symbol
- Contain only alphanumeric characters, hyphens, and underscores
- Examples of valid names: `@v0`, `@acme-ui`, `@my_company`

The pattern for referencing resources is: `@namespace/resource-name`

---

## Configuration

Namespaced registries are configured in your `components.json` file under the `registries` field.

### Basic Configuration

The simplest way to configure a registry is with a URL template string:

```json title="components.json"
{
  "registries": {
    "@v0": "https://v0.dev/chat/b/{name}",
    "@acme": "https://registry.acme.com/resources/{name}.json",
    "@lib": "https://lib.company.com/utilities/{name}",
    "@ai": "https://ai-resources.com/r/{name}.json"
  }
}
```

> **Note:** The `{name}` placeholder in the URL is automatically parsed and replaced with the resource name when you run `npx shadcn@latest add @namespace/resource-name`. For example, `@acme/button` becomes `https://registry.acme.com/resources/button.json`. See [URL Pattern System](#url-pattern-system) for more details.

### Advanced Configuration

For registries that require authentication or additional parameters, use the object format:

```json title="components.json"
{
  "registries": {
    "@private": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}",
        "X-API-Key": "${API_KEY}"
      },
      "params": {
        "version": "latest",
        "format": "json"
      }
    }
  }
}
```

> **Note:** Environment variables in the format `${VAR_NAME}` are automatically expanded from your environment (process.env). This works in URLs, headers, and params. For example, `${REGISTRY_TOKEN}` will be replaced with the value of `process.env.REGISTRY_TOKEN`. See [Authentication & Security](#authentication--security) for more details on using environment variables.

---

### URL Pattern System

Registry URLs support the following placeholders:

### `{name}` Placeholder (required)

The `{name}` placeholder is replaced with the resource name:

```json title="components.json" showLineNumbers
{
  "@acme": "https://registry.acme.com/{name}.json"
}
```

When installing `@acme/button`, the URL becomes: `https://registry.acme.com/button.json`
When installing `@acme/auth-utils`, the URL becomes: `https://registry.acme.com/auth-utils.json`

### `{style}` Placeholder (optional)

The `{style}` placeholder is replaced with the current style configuration:

```json
{
  "@themes": "https://registry.example.com/{style}/{name}.json"
}
```

With style set to `new-york`, installing `@themes/card` resolves to: `https://registry.example.com/new-york/card.json`

The style placeholder is optional. Use this when you want to serve different versions of the same resource. For example, you can serve a different version of a component for each style.

---

## Authentication & Security

### Environment Variables

Use environment variables to securely store credentials:

```json title="components.json"
{
  "registries": {
    "@private": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      }
    }
  }
}
```

Then set the environment variable:

```bash title=".env.local"
REGISTRY_TOKEN=your_secret_token_here
```

### Authentication Methods

#### Bearer Token (OAuth 2.0)

```json
{
  "@github": {
    "url": "https://api.github.com/repos/org/registry/contents/{name}.json",
    "headers": {
      "Authorization": "Bearer ${GITHUB_TOKEN}"
    }
  }
}
```

#### API Key in Headers

```json title="components.json" showLineNumbers
{
  "@private": {
    "url": "https://api.company.com/registry/{name}",
    "headers": {
      "X-API-Key": "${API_KEY}"
    }
  }
}
```

#### Basic Authentication

```json title="components.json" showLineNumbers
{
  "@internal": {
    "url": "https://registry.company.com/{name}.json",
    "headers": {
      "Authorization": "Basic ${BASE64_CREDENTIALS}"
    }
  }
}
```

#### Query Parameter Authentication

```json title="components.json" showLineNumbers
{
  "@secure": {
    "url": "https://registry.example.com/{name}.json",
    "params": {
      "api_key": "${API_KEY}",
      "client_id": "${CLIENT_ID}",
      "signature": "${REQUEST_SIGNATURE}"
    }
  }
}
```

#### Multiple Authentication Methods

Some registries require multiple authentication methods:

```json title="components.json" showLineNumbers
{
  "@enterprise": {
    "url": "https://api.enterprise.com/v2/registry/{name}",
    "headers": {
      "Authorization": "Bearer ${ACCESS_TOKEN}",
      "X-API-Key": "${API_KEY}",
      "X-Workspace-Id": "${WORKSPACE_ID}"
    },
    "params": {
      "version": "latest"
    }
  }
}
```

### Security Considerations

When working with namespaced registries, especially third-party or public ones, security is paramount. Here's how we handle security:

### Resource Validation

All resources fetched from registries are validated against our registry item schema before installation. This ensures:

- **Structure validation**: Resources must conform to the expected JSON schema
- **Type safety**: Resource types are validated (`registry:ui`, `registry:lib`, etc.)
- **No arbitrary code execution**: Resources are data files, not executable scripts

### Environment Variable Security

Environment variables used for authentication are:

- **Never logged**: The CLI never logs or displays environment variable values
- **Expanded at runtime**: Variables are only expanded when needed, not stored
- **Isolated per registry**: Each registry maintains its own authentication context

Example of secure configuration:

```json title="components.json" showLineNumbers
{
  "registries": {
    "@private": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${PRIVATE_REGISTRY_TOKEN}"
      }
    }
  }
}
```

Never commit actual tokens to version control. Use `.env.local`:

```bash title=".env.local"
PRIVATE_REGISTRY_TOKEN=actual_token_here
```

### HTTPS Enforcement

We strongly recommend using HTTPS for all registry URLs:

- **Encrypted transport**: Prevents man-in-the-middle attacks
- **Certificate validation**: Ensures you're connecting to the legitimate registry
- **Credential protection**: Headers and tokens are encrypted in transit

```json title="components.json" showLineNumbers
{
  "registries": {
    "@secure": "https://registry.example.com/{name}.json", // ✅ Good
    "@insecure": "http://registry.example.com/{name}.json" // ❌ Avoid
  }
}
```

### Content Security

Resources from registries are treated as data, not code:

1. **JSON parsing only**: Resources must be valid JSON
2. **Schema validation**: Must match the registry item schema
3. **File path restrictions**: Files can only be written to configured paths
4. **No script execution**: The CLI doesn't execute any code from registry resources

### Registry Trust Model

The namespace system operates on a trust model:

- **You trust what you install**: Only add registries you trust to your configuration
- **Explicit configuration**: Registries must be explicitly configured in `components.json`
- **No automatic registry discovery**: The CLI never automatically adds registries
- **Dependency transparency**: All dependencies are clearly listed in registry items

### Best Practices for Registry Operators

If you're running your own registry:

1. **Use HTTPS always**: Never serve registry content over HTTP
2. **Implement authentication**: Require API keys or tokens for private registries
3. **Rate limiting**: Protect your registry from abuse
4. **Content validation**: Validate resources before serving them

Example secure registry setup:

```json title="components.json" showLineNumbers
{
  "@company": {
    "url": "https://registry.company.com/v1/{name}.json",
    "headers": {
      "Authorization": "Bearer ${COMPANY_TOKEN}",
      "X-Registry-Version": "1.0"
    }
  }
}
```

### Inspecting Resources Before Installation

The CLI provides transparency about what's being installed. You can see the payload of a registry item using the following command:

```bash
npx shadcn@latest view @acme/button
```

This will output the payload of the registry item to the console.

---

## Dependency Resolution

### Basic Dependency Resolution

Resources can have dependencies across different registries:

```json title="registry-item.json" showLineNumbers
{
  "name": "dashboard",
  "type": "registry:block",
  "registryDependencies": [
    "@shadcn/card", // From default registry
    "@v0/chart", // From v0 registry
    "@acme/data-table", // From acme registry
    "@lib/data-fetcher", // Utility library
    "@ai/analytics-prompt" // AI prompt resource
  ]
}
```

The CLI automatically resolves and installs all dependencies from their respective registries.

### Advanced Dependency Resolution

Understanding how dependencies are resolved internally is important if you're developing registries or need to customize third-party resources.

### How Resolution Works

When you run `npx shadcn@latest add @namespace/resource`, the CLI does the following:

1. **Clears registry context** to start fresh
2. **Fetches the main resource** from the specified registry
3. **Recursively resolves dependencies** from their respective registries
4. **Applies topological sorting** to ensure proper installation order
5. **Deduplicates files** based on target paths (last one wins)
6. **Deep merges configurations** (tailwind, cssVars, css, envVars)

This means that if you run the following command:

```bash
npx shadcn@latest add @acme/auth @custom/login-form
```

The `login-form.ts` from `@custom/login-form` will override the `login-form.ts` from `@acme/auth` because it's resolved last.

### Overriding Third-Party Resources

You can leverage the dependency resolution process to override any third-party resource by adding them to your custom resource under `registryDependencies` and overriding with your own custom values.

#### Example: Customizing a Third-Party Button

Let's say you want to customize a button from a vendor registry:

**1. Original vendor button** (`@vendor/button`):

```json title="button.json" showLineNumbers
{
  "name": "button",
  "type": "registry:ui",
  "files": [
    {
      "path": "components/ui/button.tsx",
      "type": "registry:ui",
      "content": "// Vendor's button implementation\nexport function Button() { ... }"
    }
  ],
  "cssVars": {
    "light": {
      "--button-bg": "blue"
    }
  }
}
```

**2. Create your custom override** (`@my-company/custom-button`):

```json title="custom-button.json" showLineNumbers
{
  "name": "custom-button",
  "type": "registry:ui",
  "registryDependencies": [
    "@vendor/button" // Import original first
  ],
  "cssVars": {
    "light": {
      "--button-bg": "purple" // Override the color
    }
  }
}
```

**3. Install your custom version**:

```bash
npx shadcn@latest add @my-company/custom-button
```

This installs the original button from `@vendor/button` and then overrides the `cssVars` with your own custom values.

### Advanced Override Patterns

#### Extending Without Replacing

Keep the original and add extensions:

```json title="extended-table.json" showLineNumbers
{
  "name": "extended-table",
  "registryDependencies": ["@vendor/table"],
  "files": [
    {
      "path": "components/ui/table-extended.tsx",
      "content": "import { Table } from '@vendor/table'\n// Add your extensions\nexport function ExtendedTable() { ... }"
    }
  ]
}
```

This will install the original table from `@vendor/table` and then add your extensions to `components/ui/table-extended.tsx`.

#### Partial Override (Multi-file Resources)

Override only specific files from a complex component:

```json title="custom-auth.json" showLineNumbers
{
  "name": "custom-auth",
  "registryDependencies": [
    "@vendor/auth" // Has multiple files
  ],
  "files": [
    {
      "path": "lib/auth-server.ts",
      "type": "registry:lib",
      "content": "// Your custom auth server"
    }
  ]
}
```

### Resolution Order Example

When you install `@custom/dashboard` that depends on multiple resources:

```json title="dashboard.json" showLineNumbers
{
  "name": "dashboard",
  "registryDependencies": [
    "@shadcn/card", // 1. Resolved first
    "@vendor/chart", // 2. Resolved second
    "@custom/card" // 3. Resolved last (overrides @shadcn/card)
  ]
}
```

Resolution order:

1. `@shadcn/card` - installs to `components/ui/card.tsx`
2. `@vendor/chart` - installs to `components/ui/chart.tsx`
3. `@custom/card` - overwrites `components/ui/card.tsx` (if same target)

### Key Resolution Features

1. **Source Tracking**: Each resource knows which registry it came from, avoiding naming conflicts
2. **Circular Dependency Prevention**: Automatically detects and prevents circular dependencies
3. **Smart Installation Order**: Dependencies are installed first, then the resources that use them

---

## Versioning

You can implement versioning for your registry resources using query parameters. This allows users to pin specific versions or use different release channels.

### Basic Version Parameter

```json title="components.json" showLineNumbers
{
  "@versioned": {
    "url": "https://registry.example.com/{name}",
    "params": {
      "version": "v2"
    }
  }
}
```

This resolves `@versioned/button` to: `https://registry.example.com/button?version=v2`

### Dynamic Version Selection

Use environment variables to control versions across your project:

```json title="components.json" showLineNumbers
{
  "@stable": {
    "url": "https://registry.company.com/{name}",
    "params": {
      "version": "${REGISTRY_VERSION}"
    }
  }
}
```

This allows you to:

- Set `REGISTRY_VERSION=v1.2.3` in production
- Override per environment (dev, staging, prod)

### Semantic Versioning

Implement semantic versioning with range support:

```json title="components.json" showLineNumbers
{
  "@npm-style": {
    "url": "https://registry.example.com/{name}",
    "params": {
      "semver": "^2.0.0",
      "prerelease": "${ALLOW_PRERELEASE}"
    }
  }
}
```

### Version Resolution Best Practices

1. **Use environment variables** for version control across environments
2. **Provide sensible defaults** using the `${VAR:-default}` syntax
3. **Document version schemes** clearly for registry users
4. **Support version pinning** for reproducible builds
5. **Implement version discovery** endpoints (e.g., `/versions/{name}`)
6. **Cache versioned resources** appropriately with proper cache headers

---

## CLI Commands

The shadcn CLI provides several commands for working with namespaced registries:

### Adding Resources

Install resources from any configured registry:

```bash
# Install from a specific registry
npx shadcn@latest add @v0/dashboard

# Install multiple resources
npx shadcn@latest add @acme/button @lib/utils @ai/prompt

# Install from URL directly
npx shadcn@latest add https://registry.example.com/button.json

# Install from local file
npx shadcn@latest add ./local-registry/button.json
```

### Viewing Resources

Inspect registry items before installation:

```bash
# View a resource from a registry
npx shadcn@latest view @acme/button

# View multiple resources
npx shadcn@latest view @v0/dashboard @shadcn/card

# View from URL
npx shadcn@latest view https://registry.example.com/button.json
```

The `view` command displays:

- Resource metadata (name, type, description)
- Dependencies and registry dependencies
- File contents that will be installed
- CSS variables and Tailwind configuration
- Required environment variables

### Searching Registries

Search for available resources in registries:

```bash
# Search a specific registry
npx shadcn@latest search @v0

# Search with query
npx shadcn@latest search @acme --query "auth"

# Search multiple registries
npx shadcn@latest search @v0 @acme @lib

# Limit results
npx shadcn@latest search @v0 --limit 10 --offset 20

# List all items (alias for search)
npx shadcn@latest list @acme
```

Search results include:

- Resource name and type
- Description
- Registry source

---

## Error Handling

### Registry Not Configured

If you reference a registry that isn't configured:

```bash
npx shadcn@latest add @non-existent/component
```

Error:

```txt
Unknown registry "@non-existent". Make sure it is defined in components.json as follows:
{
  "registries": {
    "@non-existent": "[URL_TO_REGISTRY]"
  }
}
```

### Missing Environment Variables

If required environment variables are not set:

```txt
Registry "@private" requires the following environment variables:

  • REGISTRY_TOKEN

Set the required environment variables to your .env or .env.local file.
```

### Resource Not Found

404 Not Found:

```txt
The item at https://registry.company.com/button.json was not found. It may not exist at the registry.
```

This usually means:

- The resource name is misspelled
- The resource doesn't exist in the registry
- The registry URL pattern is incorrect

### Authentication Failures

401 Unauthorized:

```txt
You are not authorized to access the item at https://api.company.com/button.json
Check your authentication credentials and environment variables.
```

403 Forbidden:

```txt
Access forbidden for https://api.company.com/button.json
Verify your API key has the necessary permissions.
```

---

## Creating Your Own Registry

To make your registry compatible with the namespace system, you can serve any type of resource - components, libraries, utilities, AI prompts, themes, configurations, or any other shareable code/content:

1. **Implement the registry item schema**: Your registry must return JSON that conforms to the [registry item schema](/docs/registry/registry-item-json).

2. **Support the URL pattern**: Include `{name}` in your URL template where the resource name will be inserted.

3. **Define resource types**: Use appropriate `type` fields to identify your resources (e.g., `registry:ui`, `registry:lib`, `registry:ai`, `registry:theme`, etc.).

4. **Handle authentication** (if needed): Accept authentication via headers or query parameters.

5. **Document your namespace**: Provide clear instructions for users to configure your registry:

```json title="components.json" showLineNumbers
{
  "registries": {
    "@your-registry": "https://your-domain.com/r/{name}.json"
  }
}
```

---

## Technical Details

### Parser Pattern

The namespace parser uses the following regex pattern:

```regex title="namespace-parser.js"
/^(@[a-zA-Z0-9](?:[a-zA-Z0-9-_]*[a-zA-Z0-9])?)\/(.+)$/
```

This ensures valid namespace formatting and proper component name extraction.

### Resolution Process

1. **Parse**: Extract namespace and component name from `@namespace/component`
2. **Lookup**: Find registry configuration for `@namespace`
3. **Build URL**: Replace placeholders with actual values
4. **Set Headers**: Apply authentication headers if configured
5. **Fetch**: Retrieve component from the resolved URL
6. **Validate**: Ensure response matches registry item schema
7. **Resolve Dependencies**: Recursively fetch any registry dependencies

### Cross-Registry Dependencies

When a component has dependencies from different registries, the resolver:

1. Maintains separate authentication contexts for each registry
2. Resolves each dependency from its respective source
3. Deduplicates files based on target paths
4. Merges configurations (tailwind, cssVars, etc.) from all sources

---

## Best Practices

1. **Use environment variables** for sensitive data like API keys and tokens
2. **Namespace your registry** with a unique, descriptive name
3. **Document authentication requirements** clearly for users
4. **Implement proper error responses** with helpful messages
5. **Cache registry responses** when possible to improve performance
6. **Support style variants** if your components have multiple themes

---

## Troubleshooting

### Resources not found

- Verify the registry URL is correct and accessible
- Check that the `{name}` placeholder is included in the URL
- Ensure the resource exists in the registry
- Confirm the resource type matches what the registry provides

### Authentication issues

- Confirm environment variables are set correctly
- Verify API keys/tokens are valid and not expired
- Check that headers are being sent in the correct format

### Dependency conflicts

- Review resources with the same name from different registries
- Use fully qualified names (`@namespace/resource`) to avoid ambiguity
- Check for circular dependencies between registries
- Ensure resource types are compatible when mixing registries


---

<!-- SOURCE: apps/v4/content/docs/registry/open-in-v0.mdx -->

## apps/v4/content/docs/registry/open-in-v0.mdx

---
title: Open in v0
description: Integrate your registry with Open in v0.
---

If your registry is hosted and publicly accessible via a URL, you can open a registry item in v0 by using the `https://v0.dev/chat/api/open?url=[URL]` endpoint.

eg. [https://v0.dev/chat/api/open?url=https://ui.shadcn.com/r/styles/new-york/login-01.json](https://v0.dev/chat/api/open?url=https://ui.shadcn.com/r/styles/new-york/login-01.json)

<Callout className="mt-6">
  **Important:** `Open in v0` does not support `cssVars`, `css`, `envVars`,
  namespaced registries, or advanced authentication methods.
</Callout>

## Button

See [Build your Open in v0 button](https://v0.dev/chat/button) for more information on how to build your own `Open in v0` button.

Here's a simple example of how to add a `Open in v0` button to your site.

```tsx showLineNumbers
import { Button } from "@/components/ui/button"

export function OpenInV0Button({ url }: { url: string }) {
  return (
    <Button
      aria-label="Open in v0"
      className="h-8 gap-1 rounded-[6px] bg-black px-3 text-xs text-white hover:bg-black hover:text-white dark:bg-white dark:text-black"
      asChild
    >
      <a
        href={`https://v0.dev/chat/api/open?url=${url}`}
        target="_blank"
        rel="noreferrer"
      >
        Open in{" "}
        <svg
          viewBox="0 0 40 20"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="h-5 w-5 text-current"
        >
          <path
            d="M23.3919 0H32.9188C36.7819 0 39.9136 3.13165 39.9136 6.99475V16.0805H36.0006V6.99475C36.0006 6.90167 35.9969 6.80925 35.9898 6.71766L26.4628 16.079C26.4949 16.08 26.5272 16.0805 26.5595 16.0805H36.0006V19.7762H26.5595C22.6964 19.7762 19.4788 16.6139 19.4788 12.7508V3.68923H23.3919V12.7508C23.3919 12.9253 23.4054 13.0977 23.4316 13.2668L33.1682 3.6995C33.0861 3.6927 33.003 3.68923 32.9188 3.68923H23.3919V0Z"
            fill="currentColor"
          ></path>
          <path
            d="M13.7688 19.0956L0 3.68759H5.53933L13.6231 12.7337V3.68759H17.7535V17.5746C17.7535 19.6705 15.1654 20.6584 13.7688 19.0956Z"
            fill="currentColor"
          ></path>
        </svg>
      </a>
    </Button>
  )
}
```

```jsx
<OpenInV0Button url="https://example.com/r/hello-world.json" />
```

## Authentication

Open in v0 only supports query parameter authentication. It does not support namespaced registries or advanced authentication methods like Bearer tokens or API keys in headers.

### Using Query Parameter Authentication

To add authentication to your registry for Open in v0, use a `token` query parameter:

```
https://registry.company.com/r/hello-world.json?token=your_secure_token_here
```

When implementing this on your registry server:

1. Check for the `token` query parameter
2. Validate the token against your authentication system
3. Return a `401 Unauthorized` response if the token is invalid or missing
4. Both the shadcn CLI and Open in v0 will handle the 401 response and display an appropriate message to users

### Example Implementation

```typescript
// Next.js API route example
export async function GET(request: NextRequest) {
  const token = request.nextUrl.searchParams.get("token")

  if (!isValidToken(token)) {
    return NextResponse.json(
      {
        error: "Unauthorized",
        message: "Invalid or missing token",
      },
      { status: 401 }
    )
  }

  // Return the registry item
  return NextResponse.json(registryItem)
}
```

<Callout className="mt-6">
  **Security Note:** Make sure to encrypt and expire tokens. Never expose
  production tokens in documentation or examples.
</Callout>


---

<!-- SOURCE: apps/v4/content/docs/registry/registry-index.mdx -->

## apps/v4/content/docs/registry/registry-index.mdx

---
title: Add a Registry
description: Open Source Registry Index
---

The open source registry index is a list of all the open source registries that are available to use out of the box.

When you run `shadcn add` or `shadcn search`, the CLI will automatically check the registry index for the registry you are looking for and add it to your `components.json` file.

You can see the full list at [https://ui.shadcn.com/r/registries.json](https://ui.shadcn.com/r/registries.json).

## Adding a Registry

1. Add your registry to [`apps/v4/registry/directory.json`](https://github.com/shadcn-ui/ui/blob/main/apps/v4/registry/directory.json)
2. Run `pnpm registry:build` to update `registries.json` file.
3. Create a pull request to https://github.com/shadcn-ui/ui

Once you have submitted your request, it will be validated and reviewed by the team.

### Requirements

1. The registry must be open source and publicly accessible.
2. The registry must be a valid JSON file that conforms to the [registry schema specification](/docs/registry/registry-json).
3. The registry is expected to be a flat registry with no nested items i.e `/registry.json` and `/component-name.json` files are expected to be in the root of the registry.
4. The `files` array, if present, must NOT include a `content` property.

Here's an example of a valid registry:

```json title="registry.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "login-form",
      "type": "registry:component",
      "title": "Login Form",
      "description": "A login form component.",
      "files": [
        {
          "path": "registry/new-york/auth/login-form.tsx",
          "type": "registry:component"
        }
      ]
    },
    {
      "name": "example-login-form",
      "type": "registry:component",
      "title": "Example Login Form",
      "description": "An example showing how to use the login form component.",
      "files": [
        {
          "path": "registry/new-york/examples/example-login-form.tsx",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```


---

<!-- SOURCE: apps/v4/content/docs/registry/registry-item-json.mdx -->

## apps/v4/content/docs/registry/registry-item-json.mdx

---
title: registry-item.json
description: Specification for registry items.
---

The `registry-item.json` schema is used to define your custom registry items.

```json title="registry-item.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "type": "registry:block",
  "title": "Hello World",
  "description": "A simple hello world component.",
  "registryDependencies": [
    "button",
    "@acme/input-form",
    "https://example.com/r/foo"
  ],
  "dependencies": ["is-even@3.0.0", "motion"],
  "devDependencies": ["tw-animate-css"],
  "files": [
    {
      "path": "registry/new-york/hello-world/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/use-hello-world.ts",
      "type": "registry:hook"
    }
  ],
  "cssVars": {
    "theme": {
      "font-heading": "Poppins, sans-serif"
    },
    "light": {
      "brand": "oklch(0.205 0.015 18)"
    },
    "dark": {
      "brand": "oklch(0.205 0.015 18)"
    }
  }
}
```

<div className="mt-6 flex items-center gap-2">
  <Link href="/docs/registry/examples">See more examples</Link>
</div>

## Definitions

You can see the JSON Schema for `registry-item.json` [here](https://ui.shadcn.com/schema/registry-item.json).

### $schema

The `$schema` property is used to specify the schema for the `registry-item.json` file.

```json title="registry-item.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json"
}
```

### name

The name of the item. This is used to identify the item in the registry. It should be unique for your registry.

```json title="registry-item.json" showLineNumbers
{
  "name": "hello-world"
}
```

### title

A human-readable title for your registry item. Keep it short and descriptive.

```json title="registry-item.json" showLineNumbers
{
  "title": "Hello World"
}
```

### description

A description of your registry item. This can be longer and more detailed than the `title`.

```json title="registry-item.json" showLineNumbers
{
  "description": "A simple hello world component."
}
```

### type

The `type` property is used to specify the type of your registry item. This is used to determine the type and target path of the item when resolved for a project.

```json title="registry-item.json" showLineNumbers
{
  "type": "registry:block"
}
```

The following types are supported:

| Type                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| `registry:base`      | Use for entire design systems.                    |
| `registry:block`     | Use for complex components with multiple files.   |
| `registry:component` | Use for simple components.                        |
| `registry:font`      | Use for fonts.                                    |
| `registry:lib`       | Use for lib and utils.                            |
| `registry:hook`      | Use for hooks.                                    |
| `registry:ui`        | Use for UI components and single-file primitives. |
| `registry:page`      | Use for page or file-based routes.                |
| `registry:file`      | Use for miscellaneous files.                      |
| `registry:style`     | Use for registry styles. eg. `new-york`.          |
| `registry:theme`     | Use for themes.                                   |
| `registry:item`      | Use for universal registry items.                 |

### author

The `author` property is used to specify the author of the registry item.

It can be unique to the registry item or the same as the author of the registry.

```json title="registry-item.json" showLineNumbers
{
  "author": "John Doe <john@doe.com>"
}
```

### dependencies

The `dependencies` property is used to specify the dependencies of your registry item. This is for `npm` packages.

Use `@version` to specify the version of your registry item.

```json title="registry-item.json" showLineNumbers
{
  "dependencies": [
    "@radix-ui/react-accordion",
    "zod",
    "lucide-react",
    "name@1.0.2"
  ]
}
```

### devDependencies

The `devDependencies` property is used to specify the dev dependencies of your registry item. These are `npm` packages that are only needed during development.

Use `@version` to specify the version of the package.

```json title="registry-item.json" showLineNumbers
{
  "devDependencies": ["tw-animate-css", "name@1.2.0"]
}
```

### registryDependencies

Used for registry dependencies. Can be names, namespaced or URLs.

- For `shadcn/ui` registry items such as `button`, `input`, `select`, etc use the name eg. `['button', 'input', 'select']`.
- For namespaced registry items such as `@acme` use the name eg. `['@acme/input-form']`.
- For custom registry items use the URL of the registry item eg. `['https://example.com/r/hello-world.json']`.

```json title="registry-item.json" showLineNumbers
{
  "registryDependencies": [
    "button",
    "@acme/input-form",
    "https://example.com/r/editor.json"
  ]
}
```

Note: The CLI will automatically resolve remote registry dependencies.

### files

The `files` property is used to specify the files of your registry item. Each file has a `path`, `type` and `target` (optional) property.

**The `target` property is required for `registry:page` and `registry:file` types.**

```json title="registry-item.json" showLineNumbers
{
  "files": [
    {
      "path": "registry/new-york/hello-world/page.tsx",
      "type": "registry:page",
      "target": "app/hello/page.tsx"
    },
    {
      "path": "registry/new-york/hello-world/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/use-hello-world.ts",
      "type": "registry:hook"
    },
    {
      "path": "registry/new-york/hello-world/.env",
      "type": "registry:file",
      "target": "~/.env"
    }
  ]
}
```

#### path

The `path` property is used to specify the path to the file in your registry. This path is used by the build script to parse, transform and build the registry JSON payload.

#### type

The `type` property is used to specify the type of the file. See the [type](#type) section for more information.

#### target

The `target` property is used to indicate where the file should be placed in a project. This is optional and only required for `registry:page` and `registry:file` types.

By default, the `shadcn` cli will read a project's `components.json` file to determine the target path. For some files, such as routes or config you can specify the target path manually.

Use `~` to refer to the root of the project e.g `~/foo.config.js`.

### tailwind

**DEPRECATED:** Use `cssVars.theme` instead for Tailwind v4 projects.

The `tailwind` property is used for tailwind configuration such as `theme`, `plugins` and `content`.

You can use the `tailwind.config` property to add colors, animations and plugins to your registry item.

```json title="registry-item.json" showLineNumbers
{
  "tailwind": {
    "config": {
      "theme": {
        "extend": {
          "colors": {
            "brand": "hsl(var(--brand))"
          },
          "keyframes": {
            "wiggle": {
              "0%, 100%": { "transform": "rotate(-3deg)" },
              "50%": { "transform": "rotate(3deg)" }
            }
          },
          "animation": {
            "wiggle": "wiggle 1s ease-in-out infinite"
          }
        }
      }
    }
  }
}
```

### cssVars

Use to define CSS variables for your registry item.

```json title="registry-item.json" showLineNumbers
{
  "cssVars": {
    "theme": {
      "font-heading": "Poppins, sans-serif"
    },
    "light": {
      "brand": "20 14.3% 4.1%",
      "radius": "0.5rem"
    },
    "dark": {
      "brand": "20 14.3% 4.1%"
    }
  }
}
```

### css

Use `css` to add new rules to the project's CSS file eg. `@layer base`, `@layer components`, `@utility`, `@keyframes`, `@plugin`, etc.

```json title="registry-item.json" showLineNumbers
{
  "css": {
    "@plugin @tailwindcss/typography": {},
    "@plugin foo": {},
    "@layer base": {
      "body": {
        "font-size": "var(--text-base)",
        "line-height": "1.5"
      }
    },
    "@layer components": {
      "button": {
        "background-color": "var(--color-primary)",
        "color": "var(--color-white)"
      }
    },
    "@utility text-magic": {
      "font-size": "var(--text-base)",
      "line-height": "1.5"
    },
    "@keyframes wiggle": {
      "0%, 100%": {
        "transform": "rotate(-3deg)"
      },
      "50%": {
        "transform": "rotate(3deg)"
      }
    }
  }
}
```

### envVars

Use `envVars` to add environment variables to your registry item.

```json title="registry-item.json" showLineNumbers
{
  "envVars": {
    "NEXT_PUBLIC_APP_URL": "http://localhost:4000",
    "DATABASE_URL": "postgresql://postgres:postgres@localhost:5432/postgres",
    "OPENAI_API_KEY": ""
  }
}
```

Environment variables are added to the `.env.local` or `.env` file. Existing variables are not overwritten.

<Callout>

**IMPORTANT:** Use `envVars` to add development or example variables. Do NOT use it to add production variables.

</Callout>

### font

The `font` property is required for `registry:font` items. It configures the font family, provider, import name, CSS variable, and the npm package to install for non-Next.js projects.

```json title="registry-item.json" showLineNumbers
{
  "font": {
    "family": "'Inter Variable', sans-serif",
    "provider": "google",
    "import": "Inter",
    "variable": "--font-sans",
    "subsets": ["latin"],
    "dependency": "@fontsource-variable/inter"
  }
}
```

| Property     | Type       | Required | Description                                                                               |
| ------------ | ---------- | -------- | ----------------------------------------------------------------------------------------- |
| `family`     | `string`   | Yes      | The CSS font-family value.                                                                |
| `provider`   | `string`   | Yes      | The font provider. Currently only `google` is supported.                                  |
| `import`     | `string`   | Yes      | The import name for the font from `next/font/google`.                                     |
| `variable`   | `string`   | Yes      | The CSS variable name for the font (e.g., `--font-sans`, `--font-mono`).                  |
| `weight`     | `string[]` | No       | Array of font weights to include.                                                         |
| `subsets`    | `string[]` | No       | Array of font subsets to include.                                                         |
| `selector`   | `string`   | No       | CSS selector to apply the font to. Defaults to `html`.                                    |
| `dependency` | `string`   | No       | The npm package to install for non-Next.js projects (e.g., `@fontsource-variable/inter`). |

### docs

Use `docs` to show custom documentation or message when installing your registry item via the CLI.

```json title="registry-item.json" showLineNumbers
{
  "docs": "To get an OPENAI_API_KEY, sign up for an account at https://platform.openai.com."
}
```

### categories

Use `categories` to organize your registry item.

```json title="registry-item.json" showLineNumbers
{
  "categories": ["sidebar", "dashboard"]
}
```

### meta

Use `meta` to add additional metadata to your registry item. You can add any key/value pair that you want to be available to the registry item.

```json title="registry-item.json" showLineNumbers
{
  "meta": { "foo": "bar" }
}
```


---

<!-- SOURCE: apps/v4/content/docs/registry/registry-json.mdx -->

## apps/v4/content/docs/registry/registry-json.mdx

---
title: registry.json
description: Schema for running your own component registry.
---

The `registry.json` schema is used to define your custom component registry.

```json title="registry.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "shadcn",
  "homepage": "https://ui.shadcn.com",
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "registryDependencies": [
        "button",
        "@acme/input-form",
        "https://example.com/r/foo"
      ],
      "dependencies": ["is-even@3.0.0", "motion"],
      "files": [
        {
          "path": "registry/new-york/hello-world/hello-world.tsx",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

## Definitions

You can see the JSON Schema for `registry.json` [here](https://ui.shadcn.com/schema/registry.json).

### $schema

The `$schema` property is used to specify the schema for the `registry.json` file.

```json title="registry.json" showLineNumbers
{
  "$schema": "https://ui.shadcn.com/schema/registry.json"
}
```

### name

The `name` property is used to specify the name of your registry. This is used for data attributes and other metadata.

```json title="registry.json" showLineNumbers
{
  "name": "acme"
}
```

### homepage

The homepage of your registry. This is used for data attributes and other metadata.

```json title="registry.json" showLineNumbers
{
  "homepage": "https://acme.com"
}
```

### items

The `items` in your registry. Each item must implement the [registry-item schema specification](https://ui.shadcn.com/schema/registry-item.json).

```json title="registry.json" showLineNumbers
{
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "registryDependencies": [
        "button",
        "@acme/input-form",
        "https://example.com/r/foo"
      ],
      "dependencies": ["is-even@3.0.0", "motion"],
      "files": [
        {
          "path": "registry/new-york/hello-world/hello-world.tsx",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

See the [registry-item schema documentation](/docs/registry/registry-item-json) for more information.


---

<!-- SOURCE: apps/v4/content/docs/rtl/index.mdx -->

## apps/v4/content/docs/rtl/index.mdx

---
title: "RTL"
description: "Right-to-left support for shadcn/ui components."
---

shadcn/ui components have first-class support for right-to-left (RTL) layouts. Text alignment, positioning, and directional styles automatically adapt for languages like Arabic, Hebrew, and Persian.

<ComponentPreview
  styleName="base-nova"
  name="card-rtl"
  direction="rtl"
  previewClassName="h-auto"
  hideCode
  caption="A card component in RTL mode."
  className="mb-8"
/>

When you install components, the CLI automatically transforms physical positioning classes to logical equivalents, so your components work seamlessly in both LTR and RTL contexts.

## Get Started

Select your framework to get started with RTL support.

<div className="mt-6 grid gap-4 sm:grid-cols-2 sm:gap-6">
  <LinkedCard href="/docs/rtl/next">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Next.js</title>
      <path d="M11.5725 0c-.1763 0-.3098.0013-.3584.0067-.0516.0053-.2159.021-.3636.0328-3.4088.3073-6.6017 2.1463-8.624 4.9728C1.1004 6.584.3802 8.3666.1082 10.255c-.0962.659-.108.8537-.108 1.7474s.012 1.0884.108 1.7476c.652 4.506 3.8591 8.2919 8.2087 9.6945.7789.2511 1.6.4223 2.5337.5255.3636.04 1.9354.04 2.299 0 1.6117-.1783 2.9772-.577 4.3237-1.2643.2065-.1056.2464-.1337.2183-.1573-.0188-.0139-.8987-1.1938-1.9543-2.62l-1.919-2.592-2.4047-3.5583c-1.3231-1.9564-2.4117-3.556-2.4211-3.556-.0094-.0026-.0187 1.5787-.0235 3.509-.0067 3.3802-.0093 3.5162-.0516 3.596-.061.115-.108.1618-.2064.2134-.075.0374-.1408.0445-.495.0445h-.406l-.1078-.068a.4383.4383 0 01-.1572-.1712l-.0493-.1056.0053-4.703.0067-4.7054.0726-.0915c.0376-.0493.1174-.1125.1736-.143.0962-.047.1338-.0517.5396-.0517.4787 0 .5584.0187.6827.1547.0353.0377 1.3373 1.9987 2.895 4.3608a10760.433 10760.433 0 004.7344 7.1706l1.9002 2.8782.096-.0633c.8518-.5536 1.7525-1.3418 2.4657-2.1627 1.5179-1.7429 2.4963-3.868 2.8247-6.134.0961-.6591.1078-.854.1078-1.7475 0-.8937-.012-1.0884-.1078-1.7476-.6522-4.506-3.8592-8.2919-8.2087-9.6945-.7672-.2487-1.5836-.42-2.4985-.5232-.169-.0176-1.0835-.0366-1.6123-.037zm4.0685 7.217c.3473 0 .4082.0053.4857.047.1127.0562.204.1642.237.2767.0186.061.0234 1.3653.0186 4.3044l-.0067 4.2175-.7436-1.14-.7461-1.14v-3.066c0-1.982.0093-3.0963.0234-3.1502.0375-.1313.1196-.2346.2323-.2955.0961-.0494.1313-.054.4997-.054z" />
    </svg>
    <p className="mt-2 font-medium">Next.js</p>
  </LinkedCard>
  <LinkedCard href="/docs/rtl/vite">
    <svg
      role="img"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      className="h-10 w-10"
      fill="currentColor"
    >
      <title>Vite</title>
      <path d="m8.286 10.578.512-8.657a.306.306 0 0 1 .247-.282L17.377.006a.306.306 0 0 1 .353.385l-1.558 5.403a.306.306 0 0 0 .352.385l2.388-.46a.306.306 0 0 1 .332.438l-6.79 13.55-.123.19a.294.294 0 0 1-.252.14c-.177 0-.35-.152-.305-.369l1.095-5.301a.306.306 0 0 0-.388-.355l-1.433.435a.306.306 0 0 1-.389-.354l.69-3.375a.306.306 0 0 0-.37-.36l-2.32.536a.306.306 0 0 1-.374-.316zm14.976-7.926L17.284 3.74l-.544 1.887 2.077-.4a.8.8 0 0 1 .84.369.8.8 0 0 1 .034.783L12.9 19.93l-.013.025-.015.023-.122.19a.801.801 0 0 1-.672.37.826.826 0 0 1-.634-.302.8.8 0 0 1-.16-.67l1.029-4.981-1.12.34a.81.81 0 0 1-.86-.262.802.802 0 0 1-.165-.67l.63-3.08-2.027.468a.808.808 0 0 1-.768-.233.81.81 0 0 1-.217-.6l.389-6.57-7.44-1.33a.612.612 0 0 0-.64.906L11.58 23.691a.612.612 0 0 0 1.066-.004l11.26-20.135a.612.612 0 0 0-.644-.9z" />
    </svg>
    <p className="mt-2 font-medium">Vite</p>
  </LinkedCard>
  <LinkedCard href="/docs/rtl/start">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      className="h-10 w-10"
      fill="currentColor"
    >
      <path d="M6.93 13.688a.343.343 0 0 1 .468.132l.063.106c.48.851.98 1.66 1.5 2.426a35.65 35.65 0 0 0 2.074 2.742.345.345 0 0 1-.039.484l-.074.066c-2.543 2.223-4.191 2.665-4.953 1.333-.746-1.305-.477-3.672.808-7.11a.344.344 0 0 1 .153-.18ZM17.75 16.3a.34.34 0 0 1 .395.27l.02.1c.628 3.286.187 4.93-1.325 4.93-1.48 0-3.36-1.402-5.649-4.203a.327.327 0 0 1-.074-.222c0-.188.156-.34.344-.34h.121a32.984 32.984 0 0 0 2.809-.098c1.07-.086 2.191-.23 3.359-.437zm.871-6.977a.353.353 0 0 1 .445-.21l.102.034c3.262 1.11 4.504 2.332 3.719 3.664-.766 1.305-2.993 2.254-6.684 2.848a.362.362 0 0 1-.238-.047.343.343 0 0 1-.125-.476l.062-.106a34.07 34.07 0 0 0 1.367-2.523c.477-.989.93-2.051 1.352-3.184zM7.797 8.34a.362.362 0 0 1 .238.047.343.343 0 0 1 .125.476l-.062.106a34.088 34.088 0 0 0-1.367 2.523c-.477.988-.93 2.051-1.352 3.184a.353.353 0 0 1-.445.21l-.102-.034C1.57 13.742.328 12.52 1.113 11.188 1.88 9.883 4.106 8.934 7.797 8.34Zm5.281-3.984c2.543-2.223 4.192-2.664 4.953-1.332.746 1.304.477 3.671-.808 7.109a.344.344 0 0 1-.153.18.343.343 0 0 1-.468-.133l-.063-.106a34.64 34.64 0 0 0-1.5-2.426 35.65 35.65 0 0 0-2.074-2.742.345.345 0 0 1 .039-.484ZM7.285 2.274c1.48 0 3.364 1.402 5.649 4.203a.349.349 0 0 1 .078.218.348.348 0 0 1-.348.344l-.117-.004a34.584 34.584 0 0 0-2.809.102 35.54 35.54 0 0 0-3.363.437.343.343 0 0 1-.394-.273l-.02-.098c-.629-3.285-.188-4.93 1.324-4.93Zm2.871 5.812h3.688a.638.638 0 0 1 .55.316l1.848 3.22a.644.644 0 0 1 0 .628l-1.847 3.223a.638.638 0 0 1-.551.316h-3.688a.627.627 0 0 1-.547-.316L7.758 12.25a.644.644 0 0 1 0-.629L9.61 8.402a.627.627 0 0 1 .546-.316Zm3.23.793a.638.638 0 0 1 .552.316l1.39 2.426a.644.644 0 0 1 0 .629l-1.39 2.43a.638.638 0 0 1-.551.316h-2.774a.627.627 0 0 1-.546-.316l-1.395-2.43a.644.644 0 0 1 0-.629l1.395-2.426a.627.627 0 0 1 .546-.316Zm-.491.867h-1.79a.624.624 0 0 0-.546.316l-.899 1.56a.644.644 0 0 0 0 .628l.899 1.563a.632.632 0 0 0 .547.316h1.789a.632.632 0 0 0 .547-.316l.898-1.563a.644.644 0 0 0 0-.629l-.898-1.558a.624.624 0 0 0-.547-.317Zm-.477.828c.227 0 .438.121.547.317l.422.73a.625.625 0 0 1 0 .629l-.422.734a.627.627 0 0 1-.547.317h-.836a.632.632 0 0 1-.547-.317l-.422-.734a.625.625 0 0 1 0-.629l.422-.73a.632.632 0 0 1 .547-.317zm-.418.817a.548.548 0 0 0-.473.273.547.547 0 0 0 0 .547.544.544 0 0 0 .473.27.544.544 0 0 0 .473-.27.547.547 0 0 0 0-.547.548.548 0 0 0-.473-.273Zm-4.422.546h.98M18.98 7.75c.391-1.895.477-3.344.223-4.398-.148-.63-.422-1.137-.84-1.508-.441-.39-1-.582-1.625-.582-1.035 0-2.12.472-3.281 1.367a14.9 14.9 0 0 0-1.473 1.316 1.206 1.206 0 0 0-.136-.144c-1.446-1.285-2.66-2.082-3.7-2.39-.617-.184-1.195-.2-1.722-.024-.559.187-1.004.574-1.317 1.117-.515.894-.652 2.074-.46 3.527.078.59.214 1.235.402 1.934a1.119 1.119 0 0 0-.215.047C3.008 8.62 1.71 9.269.926 10.015c-.465.442-.77.938-.883 1.481-.113.578 0 1.156.312 1.7.516.894 1.465 1.597 2.817 2.155.543.223 1.156.426 1.844.61a1.023 1.023 0 0 0-.07.226c-.391 1.891-.477 3.344-.223 4.395.148.629.425 1.14.84 1.508.44.39 1 .582 1.625.582 1.035 0 2.12-.473 3.28-1.364.477-.37.973-.816 1.489-1.336a1.2 1.2 0 0 0 .195.227c1.446 1.285 2.66 2.082 3.7 2.39.617.184 1.195.2 1.722.024.559-.187 1.004-.574 1.317-1.117.515-.894.652-2.074.46-3.527a14.941 14.941 0 0 0-.425-2.012 1.225 1.225 0 0 0 .238-.047c1.828-.61 3.125-1.258 3.91-2.004.465-.441.77-.937.883-1.48.113-.578 0-1.157-.313-1.7-.515-.894-1.464-1.597-2.816-2.156a14.576 14.576 0 0 0-1.906-.625.865.865 0 0 0 .059-.195z" />
    </svg>
    <p className="mt-2 font-medium">TanStack Start</p>
  </LinkedCard>
</div>

## How it works

When you add components with `rtl: true` set in your `components.json`, the shadcn CLI automatically transforms classes and props to be RTL compatible:

- Physical positioning classes like `left-*` and `right-*` are converted to logical equivalents like `start-*` and `end-*`.
- Directional props are updated to use logical values.
- Text alignment and spacing classes are adjusted accordingly.
- Supported icons are automatically flipped using `rtl:rotate-180`.

## Try it out

Click the link below to open a Next.js project with RTL support in v0.

[![Open in v0](https://v0.app/chat-static/button.svg)](https://v0.app/chat/api/open?url=https://github.com/shadcn-ui/next-template-rtl)

## Supported Styles

Automatic RTL transformation via the CLI is only available for projects created using `shadcn create` with the new styles (`base-nova`, `radix-nova`, etc.).

For other styles, see the [Migration Guide](#migrating-existing-components).

## Font Recommendations

For the best RTL experience, we recommend using fonts that have proper support for your target language. [Noto](https://fonts.google.com/noto) is a great font family for this and it pairs well with Inter and Geist.

See your framework's RTL guide under [Get Started](#get-started) for details on installing and configuring RTL fonts.

## Animations

The CLI also handles animation classes, automatically transforming physical directional animations to their logical equivalents. For example, `slide-in-from-right` becomes `slide-in-from-end`.

This ensures animations like dropdowns, popovers, and tooltips animate in the correct direction based on the document's text direction.

**A note on tw-animate-css:**

There is a [known issue](https://github.com/Wombosvideo/tw-animate-css/issues/67) with the `tw-animate-css` library where the logical slide utilities are not working as expected. For now, make sure you pass in the `dir` prop to portal elements.

```tsx showLineNumbers /dir="rtl"/
<Popover>
  <PopoverTrigger>Open</PopoverTrigger>
  <PopoverContent dir="rtl">
    <div>Content</div>
  </PopoverContent>
</Popover>
```

```tsx showLineNumbers /dir="rtl"/
<Tooltip>
  <TooltipTrigger>Open</TooltipTrigger>
  <TooltipContent dir="rtl">
    <div>Content</div>
  </TooltipContent>
</Tooltip>
```

## Migrating existing components

If you have existing components installed before enabling RTL, you can migrate them using the CLI as follows:

<Steps>

<Step>Run the migrate command</Step>

```bash
npx shadcn@latest migrate rtl [path]
```

`[path]` accepts a path or glob pattern to migrate. If you don't provide a path, it will migrate all the files in the `ui` directory.

### Manual Migration (Optional)

The following components are not automatically migrated by the CLI. Follow the RTL support section for each component to manually migrate them.

- [Calendar](/docs/components/radix/calendar#rtl-support)
- [Pagination](/docs/components/radix/pagination#rtl-support)
- [Sidebar](/docs/components/radix/sidebar#rtl-support)

### Migrate Icons

Some icons like `ArrowRightIcon` or `ChevronLeftIcon` might need the `rtl:rotate-180` class to be flipped correctly. Add the `rtl:rotate-180` class to the icon component to flip it correctly.

```tsx showLineNumbers /rtl:rotate-180/
<ArrowRightIcon className="rtl:rotate-180" />
```

### Add direction component

Add the direction component to your project.

```bash
npx shadcn@latest add direction
```

### Add DirectionProvider

Follow your framework's documentation for details on how to add the `DirectionProvider` component to your project.

See the [Get Started](#get-started) section for details on how to add the `DirectionProvider` component to your project.

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/rtl/next.mdx -->

## apps/v4/content/docs/rtl/next.mdx

---
title: Next.js
description: Create a new Next.js project with RTL support.
---

<Callout className="mb-6 border-emerald-600 bg-emerald-100 dark:border-emerald-400 dark:bg-emerald-900">

**Starting a new project?** Use [shadcn/create](/create?template=next&base=base&rtl=true) for a fully configured Next.js app with custom themes, Base UI or Radix, and icon libraries.

</Callout>

<Steps>

### Create Project

Create a new project using the `--rtl` flag and the `next` template.

**You can skip this step if you have already created a project using [shadcn/create](/create?template=next&base=base&rtl=true).**

```bash
npx shadcn@latest create --template next --rtl
```

This will create a `components.json` file with the `rtl: true` flag.

```json title="components.json" showLineNumbers {4}
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "base-nova",
  "rtl": true
}
```

### Add DirectionProvider

Wrap your application with the `DirectionProvider` component with the `direction="rtl"` prop.

Then add the `dir="rtl"` and `lang="ar"` attributes to the `html` tag. Update `lang="ar"` to your target language.

```tsx title="app/layout.tsx" showLineNumbers {1,9-13}
import { DirectionProvider } from "@/components/ui/direction"

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ar" dir="rtl">
      <body>
        <DirectionProvider direction="rtl">{children}</DirectionProvider>
      </body>
    </html>
  )
}
```

### Add Font

For the best RTL experience, we recommend using fonts that have proper support for your target language. [Noto](https://fonts.google.com/noto) is a great font family for this and it pairs well with Inter and Geist.

```tsx title="app/layout.tsx" showLineNumbers {1,5-8,16}
import { Noto_Sans_Arabic } from "next/font/google"

import { DirectionProvider } from "@/components/ui/direction"

const fontSans = Noto_Sans_Arabic({
  subsets: ["arabic"],
  variable: "--font-sans",
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ar" dir="rtl" className={fontSans.variable}>
      <body>
        <DirectionProvider direction="rtl">{children}</DirectionProvider>
      </body>
    </html>
  )
}
```

For other languages, eg. Hebrew, you can use the `Noto_Sans_Hebrew` font.

### Add Components

You are now ready to add components to your project. The CLI will take care of handling RTL support for you.

```bash
npx shadcn@latest add item
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/rtl/start.mdx -->

## apps/v4/content/docs/rtl/start.mdx

---
title: TanStack Start
description: Create a new TanStack Start project with RTL support.
---

<Callout className="mb-6 border-emerald-600 bg-emerald-100 dark:border-emerald-400 dark:bg-emerald-900">

**Starting a new project?** Use [shadcn/create](/create?template=start&base=base&rtl=true) for a fully configured TanStack Start app with custom themes, Base UI or Radix, and icon libraries.

</Callout>

<Steps>

### Create Project

Create a new project using the `--rtl` flag and the `start` template.

**You can skip this step if you have already created a project using [shadcn/create](/create?template=start&base=base&rtl=true).**

```bash
npx shadcn@latest create --template start --rtl
```

This will create a `components.json` file with the `rtl: true` flag.

```json title="components.json" showLineNumbers {4}
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "base-nova",
  "rtl": true
}
```

### Add DirectionProvider

Add the `dir="rtl"` and `lang="ar"` attributes to the `html` tag. Update `lang="ar"` to your target language.

Then wrap your app with the `DirectionProvider` component with the `direction="rtl"` prop in your `__root.tsx`:

```tsx title="src/routes/__root.tsx" showLineNumbers {1,9,14-16}
import { DirectionProvider } from "@/components/ui/direction"

export const Route = createRootRoute({
  component: RootComponent,
})

function RootComponent() {
  return (
    <html lang="ar" dir="rtl">
      <head>
        <Meta />
      </head>
      <body>
        <DirectionProvider direction="rtl">{children}</DirectionProvider>
        <Scripts />
      </body>
    </html>
  )
}
```

### Add Font

For the best RTL experience, we recommend using fonts that have proper support for your target language. [Noto](https://fonts.google.com/noto) is a great font family for this and it pairs well with Inter and Geist.

Install the font using [Fontsource](https://fontsource.org/fonts/noto-sans-arabic):

```bash
npm install @fontsource-variable/noto-sans-arabic
```

Import the font in your `styles.css`:

```css title="src/styles.css" showLineNumbers {4,7}
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
@import "@fontsource-variable/noto-sans-arabic";

@theme inline {
  --font-sans: "Noto Sans Arabic Variable", sans-serif;
}
```

For other languages, eg. Hebrew, you can use `@fontsource-variable/noto-sans-hebrew`.

### Add Components

You are now ready to add components to your project. The CLI will take care of handling RTL support for you.

```bash
npx shadcn@latest add item
```

</Steps>


---

<!-- SOURCE: apps/v4/content/docs/rtl/vite.mdx -->

## apps/v4/content/docs/rtl/vite.mdx

---
title: Vite
description: Create a new Vite project with RTL support.
---

<Callout className="mb-6 border-emerald-600 bg-emerald-100 dark:border-emerald-400 dark:bg-emerald-900">

**Starting a new project?** Use [shadcn/create](/create?template=vite&base=base&rtl=true) for a fully configured Vite app with custom themes, Base UI or Radix, and icon libraries.

</Callout>

<Steps>

### Create Project

Create a new project using the `--rtl` flag and the `vite` template.

**You can skip this step if you have already created a project using [shadcn/create](/create?template=vite&base=base&rtl=true).**

```bash
npx shadcn@latest create --template vite --rtl
```

This will create a `components.json` file with the `rtl: true` flag.

```json title="components.json" showLineNumbers {4}
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "base-nova",
  "rtl": true
}
```

### Add DirectionProvider

Add the `dir="rtl"` and `lang="ar"` attributes to the `html` tag in your `index.html`. Update `lang="ar"` to your target language.

```html title="index.html" showLineNumbers {2}
<!doctype html>
<html lang="ar" dir="rtl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

Then wrap your app with the `DirectionProvider` component with the `direction="rtl"` prop in your `main.tsx`:

```tsx title="src/main.tsx" showLineNumbers {4,12-13}
import { StrictMode } from "react"
import { createRoot } from "react-dom/client"

import { DirectionProvider } from "@/components/ui/direction"

import App from "./App"

import "./index.css"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <DirectionProvider direction="rtl">
      <App />
    </DirectionProvider>
  </StrictMode>
)
```

### Add Font

For the best RTL experience, we recommend using fonts that have proper support for your target language. [Noto](https://fonts.google.com/noto) is a great font family for this and it pairs well with Inter and Geist.

Install the font using [Fontsource](https://fontsource.org/fonts/noto-sans-arabic):

```bash
npm install @fontsource-variable/noto-sans-arabic
```

Import the font in your `index.css`:

```css title="src/index.css" showLineNumbers {4,7}
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
@import "@fontsource-variable/noto-sans-arabic";

@theme inline {
  --font-sans: "Noto Sans Arabic Variable", sans-serif;
}
```

For other languages, eg. Hebrew, you can use `@fontsource-variable/noto-sans-hebrew`.

### Add Components

You are now ready to add components to your project. The CLI will take care of handling RTL support for you.

```bash
npx shadcn@latest add item
```

</Steps>
