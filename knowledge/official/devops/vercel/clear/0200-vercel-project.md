---
id: "vercel-0200"
title: "vercel project"
description: "Learn how to list, add, remove, and manage your Vercel Projects using the vercel project CLI command."
category: "vercel-cli"
subcategory: "cli"
type: "api-reference"
source: "https://vercel.com/docs/cli/project"
tags: ["project", "usage", "global-options", "api-reference", "cli-command"]
related: ["0212-vercel-teams.md", "0188-vercel-install.md", "0193-vercel-login.md"]
last_updated: "2026-04-03T23:47:17.548Z"
---

# vercel project

The `vercel project` command is used to manage your Vercel Projects, providing functionality to list, add, inspect, and remove.

## Usage

```bash filename="terminal"
vercel project ls

# Output as JSON
vercel project ls --json
```

*Using the \`vercel project\` command to list all Vercel
Project.*

```bash filename="terminal"
vercel project ls --update-required

# Output as JSON
vercel project ls --update-required --json
```

*Using the \`vercel project\` command to list all Vercel
Project that are affected by an upcoming Node.js runtime deprecation.*

```bash filename="terminal"
vercel project add
```

*Using the \`vercel project\` command to create a new
Vercel Project.*

```bash filename="terminal"
vercel project inspect
```

*Using the \`vercel project inspect\` command to display
information about the linked project.*

```bash filename="terminal"
vercel project inspect my-project
```

*Using the \`vercel project inspect\` command to display
information about a specific project by name.*

```bash filename="terminal"
vercel project rm
```

*Using the \`vercel project\` command to remove a Vercel
Project.*

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

