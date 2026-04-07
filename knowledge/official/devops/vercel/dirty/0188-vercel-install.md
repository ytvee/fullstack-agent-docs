---
id: "vercel-0188"
title: "vercel install"
description: "Learn how to install marketplace native integrations and provision resources with the vercel install CLI command."
category: "vercel-cli"
subcategory: "cli"
type: "api-reference"
source: "https://vercel.com/docs/cli/install"
tags: ["install", "usage", "examples", "global-options", "api-reference", "cli-command"]
related: ["0189-vercel-integration.md", "0193-vercel-login.md", "0194-vercel-logout.md"]
last_updated: "2026-04-03T23:47:17.418Z"
---

# vercel install

`vercel install` (alias: `vercel i`) is an alias for [`vercel integration add`](/docs/cli/integration#vercel-integration-add). Both commands are fully interchangeable with same flags and same behavior.

See the [`vercel integration add` reference](/docs/cli/integration#vercel-integration-add) for all options and examples.

## Usage

```bash filename="terminal"
vercel install <integration-name>
```

*Install a marketplace integration and provision a resource.*

For the `<integration-name>` in commands below, use the integration's [URL slug](/docs/integrations/create-integration/submit-integration#url-slug). You can find the slug in the Marketplace URL. For example, for `https://vercel.com/marketplace/neon`, the slug is `neon`. You can also browse available integrations with the [`integration discover`](/docs/cli/integration#vercel-integration-discover) command.

## Examples

```bash filename="terminal"
# Install an integration and provision a resource
vercel install neon
```

## Global Options

The following [global options](/docs/cli/global-options) can be passed when using the  command:

- [`--cwd`](/docs/cli/global-options#current-working-directory)
- [`--debug`](/docs/cli/global-options#debug)
- [`--global-config`](/docs/cli/global-options#global-config)
- [`--help`](/docs/cli/global-options#help)
- [`--local-config`](/docs/cli/global-options#local-config)
- [`--no-color`](/docs/cli/global-options#no-color)
- [`--scope`](/docs/cli/global-options#scope)
- [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).


