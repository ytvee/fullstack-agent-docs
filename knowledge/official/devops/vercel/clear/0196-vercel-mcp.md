---
id: "vercel-0196"
title: "vercel mcp"
description: "Set up Model Context Protocol (MCP) usage with a Vercel project using the vercel mcp CLI command."
category: "vercel-cli"
subcategory: "cli"
type: "api-reference"
source: "https://vercel.com/docs/cli/mcp"
tags: ["mcp", "usage", "examples", "unique-options", "project", "global-options"]
related: ["0186-vercel-init.md", "0172-vercel-contract.md", "0177-vercel-dns.md"]
last_updated: "2026-04-03T23:47:17.479Z"
---

# vercel mcp

The `vercel mcp` command helps you set up an MCP client to talk to MCP servers you deploy on Vercel. It links your local MCP client configuration to a Vercel Project and generates the connection details so agents and tools can call your MCP endpoints securely.

## Usage

```bash filename="terminal"
vercel mcp [options]
```

*Using the \`vercel mcp\` command to initialize local MCP
configuration for the currently linked Project.*

## Examples

### Initialize global MCP configuration

```bash filename="terminal"
vercel mcp
```

*Initializes global MCP client configuration for your Vercel account.*

### Initialize project-specific MCP access

```bash filename="terminal"
vercel mcp --project
```

*Sets up project-specific MCP access for the currently linked Vercel Project.*

## Unique options

These are options that only apply to the `vercel mcp` command.

### Project

The `--project` option sets up project-specific MCP access for the currently linked project instead of global configuration.

```bash filename="terminal"
vercel mcp --project
```

*Use the \`--project\` flag to configure MCP access scoped to your linked project.*

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

