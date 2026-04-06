---
id: "vercel-0212"
title: "vercel teams"
description: "Learn how to list, add, remove, and manage your teams using the vercel teams CLI command."
category: "vercel-cli"
subcategory: "cli"
type: "api-reference"
source: "https://vercel.com/docs/cli/teams"
tags: ["cli-command", "team-management", "members", "invitations"]
related: ["0210-vercel-switch.md", "0001-account-management.md", "0199-vercel-cli-overview.md"]
last_updated: "2026-04-03T23:47:17.687Z"
---

# vercel teams

The `vercel teams` command is used to manage [Teams](/docs/accounts/create-a-team), providing functionality to list, add, and invite new [Team Members](/docs/rbac/managing-team-members).

> **💡 Note:** You can manage Teams with further options and greater control from the Vercel
> Dashboard.

## Usage

```bash filename="terminal"
vercel teams list
```

*Using the \`vercel teams\` command to list all teams
you’re a member of.*

## Extended Usage

```bash filename="terminal"
vercel teams add
```

*Using the \`vercel teams\` command to create a new team.*

```bash filename="terminal"
vercel teams invite [email]
```

*Using the \`vercel teams\` command to invite a new Team
Member.*

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


