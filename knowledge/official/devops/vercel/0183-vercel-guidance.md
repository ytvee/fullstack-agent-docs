--------------------------------------------------------------------------------
title: "vercel guidance"
description: "Enable or disable guidance messages in the Vercel CLI using the vercel guidance command."
last_updated: "2026-04-03T23:47:17.346Z"
source: "https://vercel.com/docs/cli/guidance"
--------------------------------------------------------------------------------

# vercel guidance

The `vercel guidance` command allows you to enable or disable guidance messages. Guidance messages are helpful suggestions shown after certain CLI commands complete, such as recommended next steps after a deployment.

## Usage

```bash filename="terminal"
vercel guidance <subcommand>
```

*Using the \`vercel guidance\` command to manage guidance
message settings.*

## Subcommands

### enable

Enable guidance messages to receive command suggestions after operations complete.

```bash filename="terminal"
vercel guidance enable
```

*Using \`vercel guidance enable\` to turn on guidance
messages.*

### disable

Disable guidance messages if you prefer a quieter CLI experience.

```bash filename="terminal"
vercel guidance disable
```

*Using \`vercel guidance disable\` to turn off guidance
messages.*

### status

Check whether guidance messages are currently enabled or disabled.

```bash filename="terminal"
vercel guidance status
```

*Using \`vercel guidance status\` to see the current
guidance setting.*

## Examples

### Enable guidance after deployment

```bash filename="terminal"
vercel guidance enable
vercel deploy
```

*After enabling guidance, deployments will show suggested next steps.*

### Check current status

```bash filename="terminal"
vercel guidance status
```

*Shows whether guidance messages are enabled or disabled.*

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


