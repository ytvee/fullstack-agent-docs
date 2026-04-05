--------------------------------------------------------------------------------
title: "vercel git"
description: "Learn how to manage your Git provider connections using the vercel git CLI command."
last_updated: "2026-04-03T23:47:17.340Z"
source: "https://vercel.com/docs/cli/git"
--------------------------------------------------------------------------------

# vercel git

The `vercel git` command is used to manage a Git provider repository for a Vercel Project,
enabling deployments to Vercel through Git.

When run, Vercel CLI searches for a local `.git` config file containing at least one remote URL.
If found, you can connect it to the Vercel Project linked to your directory.

[Learn more about using Git with Vercel](/docs/git).

## Usage

```bash filename="terminal"
vercel git connect
```

*Using the \`vercel git\` command to connect a Git
provider repository from your local Git config to a Vercel Project.*

```bash filename="terminal"
vercel git disconnect
```

*Using the \`vercel git\` command to disconnect a
connected Git provider repository from a Vercel Project.*

## Unique Options

These are options that only apply to the `vercel git` command.

### Yes

The `--yes` option can be used to skip connect confirmation.

```bash filename="terminal"
vercel git connect --yes
```

*Using the \`vercel git connect\` command with the
\`--yes\` option.*

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


